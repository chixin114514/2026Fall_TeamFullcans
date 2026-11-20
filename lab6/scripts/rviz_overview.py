#!/usr/bin/env python3
"""Write an RViz config whose fixed oblique view frames a bag's whole camera trajectory.

    python3 scripts/rviz_overview.py <base.rviz> <bag> <gt topic> <start s> <duration s> <out.rviz>
Used for screenshots: the interactive configs follow the camera instead.
"""
import sys

import numpy as np
import rosbag
import yaml

base, bag, topic, start, dur, out = sys.argv[1], sys.argv[2], sys.argv[3], *map(float, sys.argv[4:6]), sys.argv[6]
with rosbag.Bag(bag) as b:
    t0 = b.get_start_time() + start
    P = np.array([(m.pose.pose.position.x, m.pose.pose.position.y, m.pose.pose.position.z)
                  for _, m, t in b.read_messages([topic]) if t0 <= t.to_sec() <= t0 + (dur or 1e9)])
lo, hi = P.min(0), P.max(0)
center, extent = (lo + hi) / 2, max(hi[0] - lo[0], hi[1] - lo[1], 4.0)
c = yaml.safe_load(open(base))
# Overview shots are taken from far away: thicker trajectories, larger pose arrows.
width = {"/gt_path": 0.25, "/est_path": 0.12, "/odom_path": 0.18}
for d in c["Visualization Manager"]["Displays"]:
    if d.get("Class") == "rviz/Path" and d.get("Topic") in width:
        d["Line Width"] = width[d["Topic"]]
    if d.get("Class") == "rviz/Pose":
        d.update({"Shaft Length": 2.0, "Shaft Radius": 0.15, "Head Length": 0.8, "Head Radius": 0.4})
c["Visualization Manager"]["Views"]["Current"] = {
    "Class": "rviz/Orbit", "Name": "Current View", "Target Frame": "<Fixed Frame>",
    "Focal Point": {"X": float(center[0]), "Y": float(center[1]), "Z": float(lo[2])},
    "Focal Shape Fixed Size": True, "Focal Shape Size": 0.05, "Invert Z Axis": False,
    "Distance": float(1.15 * extent), "Pitch": 0.95, "Yaw": 3.9, "Field of View": 0.785,
    "Near Clip Distance": 0.01, "Value": "Orbit (rviz)"}
yaml.safe_dump(c, open(out, "w"), sort_keys=False)
print("view centre %s, extent %.1f m" % (np.round(center, 1), extent))
