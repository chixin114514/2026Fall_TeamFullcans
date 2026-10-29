#!/usr/bin/env python3
"""Iterative learning for race_node.py: shift the reference against the
tracking error of the last flight.

  race_ilc.py TRAJ.json RUN_DIR [--previous CORR.npz] --output CORR.npz

The error e(t) = x(t) - x_traj(t) is taken at every state of the run (t from
the GO stamp in race_node.log), smoothed, and the new offset is
dx = dx_previous - gain * e; its derivatives give the velocity and
acceleration offsets.
"""
import argparse
import os
import re
import sys

import numpy as np
import rosbag
from scipy.ndimage import gaussian_filter1d

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from race_node import Trajectory  # noqa: E402

DT = 0.01


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('trajectory')
    ap.add_argument('run')
    ap.add_argument('--previous')
    ap.add_argument('--output', required=True)
    ap.add_argument('--gain', type=float, default=0.8)
    ap.add_argument('--sigma', type=float, default=0.04, help='smoothing [s]')
    ap.add_argument('--time-scale', type=float, default=1.0)
    ap.add_argument('--shift', type=float, default=0.0,
                    help='learn from the error this much later (phase lead) [s]')
    ap.add_argument('--accel-gain', type=float, default=0.0,
                    help='weight of the (noisy) acceleration offset')
    args = ap.parse_args()
    traj = Trajectory(args.trajectory, args.time_scale)
    log = open(os.path.join(args.run, 'race_node.log')).read()
    t0 = float(re.findall(r'GO at t=([\d.]+)', log)[-1])
    ts, xs = [], []
    for _, msg, _ in rosbag.Bag(os.path.join(args.run, 'race.bag')).read_messages(topics=['/current_state']):
        t = msg.header.stamp.to_sec() - t0
        if 0.0 <= t <= traj.duration:
            p = msg.pose.pose.position
            ts.append(t)
            xs.append([p.x, p.y, p.z])
    ts, xs = np.array(ts), np.array(xs)
    grid = np.arange(0.0, traj.duration + DT / 2, DT)
    ref = np.array([traj(t)[0] for t in ts])
    err = np.column_stack([np.interp(grid + args.shift, ts, (xs - ref)[:, i]) for i in range(3)])
    err = gaussian_filter1d(err, args.sigma / DT, axis=0, mode='nearest')
    # Learn only up to just after the last gate, fading in and out; the
    # braking after the race does not count.
    end = min(traj.gate_times[-1] + 0.3, grid[-1])
    ramp = np.clip(np.minimum(grid, end - grid) / 0.3, 0.0, 1.0)[:, None]
    dx = -args.gain * err * ramp
    if args.previous:
        prev = np.load(args.previous)
        dx += np.column_stack([np.interp(grid, prev['t'], prev['dx'][:, i]) for i in range(3)])
    dv = np.gradient(dx, DT, axis=0)
    da = args.accel_gain * np.gradient(
        gaussian_filter1d(dv, args.sigma / DT, axis=0, mode='nearest'), DT, axis=0)
    np.savez(args.output, t=grid, dx=dx, dv=dv, da=da)
    e = np.linalg.norm(xs - ref, axis=1)
    print('run error rms %.3f max %.3f; offset max %.3f m, accel offset max %.1f m/s^2' % (
        np.sqrt(np.mean(e**2)), e.max(), np.linalg.norm(dx, axis=1).max(),
        np.linalg.norm(da, axis=1).max()))


if __name__ == '__main__':
    main()
