#!/usr/bin/env python3
"""Print the flight segment of a race bag as "<start offset> <duration>" in seconds.

The drone hovers before take-off and after the last gate; only the segment where the
ground-truth speed exceeds 0.3 m/s (plus a margin) is used for evaluation and display.
    python3 scripts/race_window.py results/race/race.bag   ->   2.0 44.4
"""
import sys

import numpy as np
import rosbag

MARGIN = 0.5  # s before take-off and after landing


def flight_window(path, topic="/current_state", v_min=0.3):
    with rosbag.Bag(path) as bag:
        t0 = bag.get_start_time()
        P = np.array([(m.header.stamp.to_sec(), m.pose.pose.position.x, m.pose.pose.position.y,
                       m.pose.pose.position.z) for _, m, _ in bag.read_messages([topic])])
    v = np.linalg.norm(np.diff(P[:, 1:], axis=0), axis=1) / np.maximum(np.diff(P[:, 0]), 1e-3)
    moving = P[1:][v > v_min, 0]
    start = max(0.0, moving.min() - MARGIN - t0)
    return start, moving.max() + MARGIN - t0 - start


if __name__ == "__main__":
    print("%.1f %.1f" % flight_window(sys.argv[1]))
