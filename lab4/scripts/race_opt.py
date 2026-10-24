#!/usr/bin/env python3
"""Offline minimum-time trajectory for the Lab4 Unity course.

The trajectory is a minimum-snap spline (degree 7, continuous to jerk) that
starts from hover at the spawn point, passes one knot per gate and one free
via point between gates, and stops in the last room. Knot positions, via
points and segment durations are optimised with L-BFGS-B to minimise the
time from the gate 0 knot to the gate 11 knot, with penalties for

  * clearance to walls, floor and ceiling (distance field of the scene colliders),
  * mass-normalised thrust |a + g| and reference body rate |omega|,

while each gate knot is bounded to the region where the drone's collider
box still overlaps the gate trigger box (minus a tracking margin).

Writes the spline as JSON for race_node.py.
"""
import argparse
import json
import os
import sys
import time

# Small dense solves: multithreaded BLAS only adds contention here.
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np  # noqa: E402
from scipy import ndimage, optimize  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import race_timer  # noqa: E402

LAB4_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE = os.path.join(LAB4_DIR, 'race', 'course_occupancy.npz')
G = 9.81
START = np.array([0.4, 8.0, 2.0])
DRONE_HALF = np.array([0.534, 0.534, 0.095])

# ---------------------------------------------------------------- polynomials
DEG = 7
N_COEF = DEG + 1


def basis(tau, k):
    """Row vector of the k-th derivative of [1, tau, ..., tau^7]."""
    row = np.zeros(N_COEF)
    for i in range(k, N_COEF):
        row[i] = np.prod(range(i - k + 1, i + 1)) * tau ** (i - k)
    return row


A_BOUND = np.array([basis(0.0, k) for k in range(4)] + [basis(1.0, k) for k in range(4)])
A_INV = np.linalg.inv(A_BOUND)
Q_SNAP = np.zeros((N_COEF, N_COEF))
for _i in range(4, N_COEF):
    for _j in range(4, N_COEF):
        ci = np.prod(range(_i - 3, _i + 1))
        cj = np.prod(range(_j - 3, _j + 1))
        Q_SNAP[_i, _j] = ci * cj / (_i + _j - 7)
H_NORM = A_INV.T @ Q_SNAP @ A_INV


_SAMPLE_CACHE = {}


def sample_basis(per_segment):
    if per_segment not in _SAMPLE_CACHE:
        taus = (np.arange(per_segment) + 0.5) / per_segment
        _SAMPLE_CACHE[per_segment] = (taus, [np.array([basis(t, k) for t in taus]) for k in range(4)])
    return _SAMPLE_CACHE[per_segment]


class Spline:
    """Knot positions are fixed; velocity, acceleration and jerk at interior
    knots minimise total snap. The first and last knot are at rest."""

    def __init__(self, knots, durations):
        self.knots = np.asarray(knots, float)
        self.T = np.asarray(durations, float)
        k = len(self.knots)
        n = 4 * k
        H = np.zeros((n, n))
        for s, T in enumerate(self.T):
            scale = np.array([1, T, T*T, T**3] * 2)
            idx = np.r_[4*s:4*s+4, 4*s+4:4*s+8]
            H[np.ix_(idx, idx)] += (scale[:, None] * H_NORM * scale[None, :]) / T**7
        fixed = np.zeros(n, bool)
        fixed[0::4] = True
        fixed[1:4] = True
        fixed[n-3:n] = True
        values = np.zeros((n, 3))
        values[0::4] = self.knots
        free = ~fixed
        Hff = H[np.ix_(free, free)] + 1e-12 * np.eye(free.sum())
        values[free] = -np.linalg.solve(Hff, H[np.ix_(free, fixed)] @ values[fixed])
        self.derivs = values.reshape(k, 4, 3)
        self.coef = []
        for s, T in enumerate(self.T):
            scale = np.array([1, T, T*T, T**3])
            b = np.vstack([self.derivs[s] * scale[:, None], self.derivs[s+1] * scale[:, None]])
            self.coef.append(A_INV @ b)
        self.coef = np.array(self.coef)
        self.t_knot = np.r_[0.0, np.cumsum(self.T)]

    def sample(self, per_segment):
        taus, B = sample_basis(per_segment)
        out = []
        for k in range(4):
            vals = np.einsum('ij,sjd->sid', B[k], self.coef) / (self.T ** k)[:, None, None]
            out.append(vals.reshape(-1, 3))
        times = (self.t_knot[:-1, None] + taus[None, :] * self.T[:, None]).ravel()
        return times, out

    def evaluate(self, t):
        s = int(np.clip(np.searchsorted(self.t_knot, t, side='right') - 1, 0, len(self.T) - 1))
        T = self.T[s]
        tau = np.clip((t - self.t_knot[s]) / T, 0.0, 1.0)
        return [basis(tau, k) @ self.coef[s] / T**k for k in range(5)]


# ----------------------------------------------------------------- the course
class Course:
    def __init__(self, path=COURSE):
        data = np.load(path)
        occupied = np.unpackbits(data['occupancy'])[:int(np.prod(data['shape']))]
        occupied = occupied.reshape(data['shape']).astype(bool)
        self.lo = data['lo']
        self.res = float(data['res'])
        self.dist = ndimage.distance_transform_edt(~occupied) * self.res
        self.gates = race_timer.load_gates()

    def distance(self, p):
        return ndimage.map_coordinates(self.dist, ((p - self.lo) / self.res).T,
                                       order=1, mode='nearest')


# -------------------------------------------------------------- optimisation
class Problem:
    def __init__(self, course, args):
        self.course = course
        self.args = args
        gates = course.gates
        self.n_gates = len(gates)
        # Gate knot: offsets (along gate width, height, normal) in the trigger
        # region grown by the drone's half size and shrunk by the margin.
        # Box bounds use the drone's largest possible reach; the penalty in
        # cost() uses its reach at the attitude the reference demands.
        self.gate_bounds = [half + np.linalg.norm(DRONE_HALF) for _, _, half in gates]
        # Gates the drone must fly through: knot on the gate plane, centre
        # inside the opening, so any attitude overlaps the trigger.
        for g in args.cross:
            half = gates[g][2]
            self.gate_bounds[g] = np.array([half[0] - args.margin, half[1] - args.margin, 1e-6])
        self.gate_margin = np.array([args.margin, args.margin, args.margin_normal])
        self.layout = []  # ('fixed', p) | ('gate', i) | ('via', lo, hi)
        self.layout.append(('fixed', START))
        # Run-up in the start room: the clock only starts at gate 0.
        for _ in range(args.runup_vias):
            self.layout.append(('via', np.array([-3.3, 3.8, 1.2]), np.array([3.8, 11.0, 4.4])))
        for i in range(self.n_gates):
            self.layout.append(('gate', i))
            if i + 1 < self.n_gates:
                a, b = gates[i][0], gates[i + 1][0]
                mid = 0.5 * (a + b)
                lo = np.minimum(a, b) - args.via_box
                hi = np.maximum(a, b) + args.via_box
                lo[2], hi[2] = 1.0, 4.4
                self.layout.append(('via', lo, hi))
        self.layout.append(('via', np.array([-38.0, 8.0, 1.2]), np.array([-31.0, 18.5, 4.4])))
        self.layout.append(('end', np.array([-37.0, 6.0, 1.5]), np.array([-31.5, 18.0, 3.5])))
        self.gate_knot = [k for k, item in enumerate(self.layout) if item[0] == 'gate']

    def initial(self):
        x, lo, hi, pts = [], [], [], []
        for item in self.layout:
            if item[0] == 'fixed':
                pts.append(item[1])
            elif item[0] == 'gate':
                x += [0.0, 0.0, 0.0]
                b = self.gate_bounds[item[1]]
                lo += list(-b)
                hi += list(b)
                pts.append(self.course.gates[item[1]][0])
            else:
                pts.append(None)
                x += [0.0, 0.0, 0.0]
                lo += list(item[1])
                hi += list(item[2])
        for k, item in enumerate(self.layout):
            if item[0] in ('via', 'end'):
                prev = next(p for p in reversed(pts[:k]) if p is not None)
                nxt = next((p for p in pts[k+1:] if p is not None), None)
                guess = 0.5 * (prev + nxt) if nxt is not None else prev + np.array([4.0, -1.0, -0.5])
                guess = np.clip(guess, item[1], item[2])
                pts[k] = guess
        # write via guesses into x
        j = 0
        for k, item in enumerate(self.layout):
            if item[0] == 'fixed':
                continue
            if item[0] in ('via', 'end'):
                x[j:j+3] = list(pts[k])
            j += 3
        n_seg = len(self.layout) - 1
        d = [np.linalg.norm(pts[k+1] - pts[k]) for k in range(n_seg)]
        T = [max(0.3, di / self.args.v_init) for di in d]
        x += list(np.log(T))
        lo += [np.log(0.08)] * n_seg
        hi += [np.log(6.0)] * n_seg
        return np.array(x), list(zip(lo, hi))

    def unpack(self, x):
        knots = []
        j = 0
        for item in self.layout:
            if item[0] == 'fixed':
                knots.append(item[1])
                continue
            v = x[j:j+3]
            j += 3
            if item[0] == 'gate':
                center, axes, _ = self.course.gates[item[1]]
                # columns of axes: width, height, normal
                knots.append(center + axes @ v)
            else:
                knots.append(v)
        T = np.exp(x[j:])
        return np.array(knots), T

    def race_time(self, T):
        return T[self.gate_knot[0]:self.gate_knot[-1]].sum()

    def cost(self, x, detail=False):
        a = self.args
        knots, T = self.unpack(x)
        spline = Spline(knots, T)
        t, (p, v, acc, jerk) = spline.sample(a.samples)
        dt = np.repeat(T / a.samples, a.samples)
        clearance = self.course.distance(p)
        f = acc + np.array([0.0, 0.0, G])
        fn = np.linalg.norm(f, axis=1)
        b3 = f / fn[:, None]
        jp = jerk - (jerk * b3).sum(1)[:, None] * b3
        omega = np.linalg.norm(jp, axis=1) / fn
        rate = np.cross(b3, jp / fn[:, None])
        alpha = np.linalg.norm(np.gradient(rate, t, axis=0), axis=1)
        pen_clear = np.maximum(0.0, a.clearance - clearance)
        pen_floor = np.maximum(0.0, a.z_min - p[:, 2]) + np.maximum(0.0, p[:, 2] - a.z_max)
        pen_thrust = np.maximum(0.0, fn - a.thrust) / a.thrust
        pen_low = np.maximum(0.0, a.thrust_min - fn) / G
        pen_omega = np.maximum(0.0, omega - a.omega) / a.omega
        pen_alpha = np.maximum(0.0, alpha - a.alpha) / a.alpha
        penalty = (a.w_clear * np.sum(dt * (pen_clear**2 + pen_floor**2))
                   + a.w_dyn * np.sum(dt * (pen_thrust**2 + pen_low**2 + pen_omega**2 + pen_alpha**2)))
        # Gate knots: the drone box, at the attitude of the reference
        # acceleration with zero yaw, must overlap the trigger box along the
        # gate's axes, with the tracking margin.
        pen_gate = 0.0
        for g, k in enumerate(self.gate_knot):
            center, axes, half = self.course.gates[g]
            b3 = spline.derivs[k][2] + np.array([0.0, 0.0, G])
            b3 /= np.linalg.norm(b3)
            b2 = np.cross(b3, [1.0, 0.0, 0.0])
            b2 /= np.linalg.norm(b2)
            body = np.column_stack([np.cross(b2, b3), b2, b3])
            reach = half + np.abs(axes.T @ body) @ DRONE_HALF - self.gate_margin
            offset = np.abs(axes.T @ (knots[k] - center))
            pen_gate += np.sum(np.maximum(0.0, offset - reach) ** 2)
        penalty += a.w_gate * pen_gate
        race = self.race_time(T)
        other = T.sum() - race
        total = race + a.w_other * other + self.weight * penalty
        if detail:
            return dict(race=race, total=T.sum(), penalty=penalty, gate_penalty=pen_gate,
                        min_clearance=float(clearance.min()), max_thrust=float(fn.max()),
                        min_thrust=float(fn.min()), max_omega=float(omega.max()), max_alpha=float(alpha.max()),
                        max_speed=float(np.linalg.norm(v, axis=1).max()),
                        z_range=(float(p[:, 2].min()), float(p[:, 2].max())))
        return total


def solve(problem, x0, bounds, args):
    x = x0.copy()
    for weight in args.weights:
        problem.weight = weight
        t0 = time.time()
        res = optimize.minimize(problem.cost, x, method='L-BFGS-B', bounds=bounds,
                                options=dict(maxiter=args.iters, maxfun=10**7, eps=1e-6))
        x = res.x
        d = problem.cost(x, detail=True)
        print('weight %8.0f  race %.3f s  total %.2f  pen %.2e  clear %.2f  thrust %.1f..%.1f  '
              'omega %.2f  vmax %.1f  (%.0f s, %s)' % (
                  weight, d['race'], d['total'], d['penalty'], d['min_clearance'], d['min_thrust'],
                  d['max_thrust'], d['max_omega'], d['max_speed'], time.time() - t0, res.message),
              flush=True)
    return x


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--output', required=True)
    ap.add_argument('--init', help='start from a previous JSON result')
    ap.add_argument('--thrust', type=float, default=30.0, help='max |a+g| [m/s^2]')
    ap.add_argument('--thrust-min', type=float, default=3.0, help='min |a+g| [m/s^2]')
    ap.add_argument('--omega', type=float, default=3.5, help='max reference body rate [rad/s]')
    ap.add_argument('--alpha', type=float, default=1e9, help='max reference angular acceleration [rad/s^2]')
    ap.add_argument('--clearance', type=float, default=0.9, help='min distance of the centre to obstacles [m]')
    ap.add_argument('--margin', type=float, default=0.4, help='gate tracking margin [m]')
    ap.add_argument('--margin-normal', type=float, default=0.3)
    ap.add_argument('--z-min', type=float, default=0.9)
    ap.add_argument('--z-max', type=float, default=4.6)
    ap.add_argument('--via-box', type=float, default=2.5)
    ap.add_argument('--v-init', type=float, default=6.0)
    ap.add_argument('--samples', type=int, default=24)
    ap.add_argument('--iters', type=int, default=400)
    ap.add_argument('--weights', type=float, nargs='+', default=[10, 100, 1000, 10000])
    ap.add_argument('--w-clear', type=float, default=30.0)
    ap.add_argument('--w-dyn', type=float, default=1.0)
    ap.add_argument('--w-other', type=float, default=0.05)
    ap.add_argument('--w-gate', type=float, default=100.0)
    ap.add_argument('--cross', type=int, nargs='*', default=[], help='gates to fly through')
    ap.add_argument('--runup-vias', type=int, default=1, help='free waypoints before gate 0')
    args = ap.parse_args()
    course = Course()
    problem = Problem(course, args)
    x0, bounds = problem.initial()
    if args.init:
        x0 = np.array(json.load(open(args.init))['x'])
    x = solve(problem, x0, bounds, args)
    knots, T = problem.unpack(x)
    spline = Spline(knots, T)
    detail = problem.cost(x, detail=True)
    gate_times = [float(spline.t_knot[k]) for k in problem.gate_knot]
    result = dict(args=vars(args), x=list(map(float, x)), knots=knots.tolist(), durations=T.tolist(),
                  coef=spline.coef.tolist(), gate_knot_times=gate_times, stats=detail)
    with open(args.output, 'w') as f:
        json.dump(result, f)
    print(json.dumps(detail))


if __name__ == '__main__':
    main()
