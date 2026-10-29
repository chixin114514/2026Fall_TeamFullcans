#!/usr/bin/env python3
"""Nudge the reference towards one gate the drone keeps missing.

  race_gate_pull.py TRAJ.json RUN_DIR GATE --output CORR.npz [--previous CORR.npz]

Finds where the flown path came closest to the gate's centre, and adds a
position offset towards the centre around that moment (Gaussian in time),
on top of an earlier correction file.
"""
import argparse
import os
import re
import sys

import numpy as np
import rosbag

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from race_node import Trajectory  # noqa: E402
from race_timer import load_gates  # noqa: E402

DT = 0.01


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('trajectory')
    ap.add_argument('run')
    ap.add_argument('gate', type=int)
    ap.add_argument('--previous')
    ap.add_argument('--output', required=True)
    ap.add_argument('--gain', type=float, default=0.6)
    ap.add_argument('--sigma', type=float, default=0.12, help='width of the nudge [s]')
    ap.add_argument('--time-scale', type=float, default=1.0)
    args = ap.parse_args()
    traj = Trajectory(args.trajectory, args.time_scale)
    t0 = float(re.findall(r'GO at t=([\d.]+)', open(os.path.join(args.run, 'race_node.log')).read())[-1])
    ts, xs = [], []
    for _, msg, _ in rosbag.Bag(os.path.join(args.run, 'race.bag')).read_messages(topics=['/current_state']):
        p = msg.pose.pose.position
        ts.append(msg.header.stamp.to_sec() - t0)
        xs.append([p.x, p.y, p.z])
    ts, xs = np.array(ts), np.array(xs)
    center = load_gates()[args.gate][0]
    window = np.abs(ts - traj.gate_times[args.gate]) < 0.3
    k = np.flatnonzero(window)[np.argmin(np.linalg.norm(xs[window] - center, axis=1))]
    pull = args.gain * (center - xs[k])
    grid = np.arange(0.0, traj.duration + DT / 2, DT)
    shape = np.exp(-0.5 * ((grid - ts[k]) / args.sigma) ** 2)[:, None]
    dx = shape * pull
    if args.previous:
        prev = np.load(args.previous)
        dx += np.column_stack([np.interp(grid, prev['t'], prev['dx'][:, i]) for i in range(3)])
    dv = np.gradient(dx, DT, axis=0)
    np.savez(args.output, t=grid, dx=dx, dv=dv, da=np.zeros_like(dx))
    print('closest to gate %d at t=%.2f, %.2f m from centre; pull %s' % (
        args.gate, ts[k], np.linalg.norm(center - xs[k]), np.round(pull, 2)))


if __name__ == '__main__':
    main()
