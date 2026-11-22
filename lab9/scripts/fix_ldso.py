#!/usr/bin/env python3
"""Clean LDSO's results.txt into a TUM trajectory (handout: "output might be formatted
incorrectly, e.g. spurious backspaces"). Drops control characters, keeps only lines with
8 finite numbers (t x y z qx qy qz qw; LDSO already writes seconds), sorts by time and removes
duplicate stamps.  usage: fix_ldso.py IN OUT"""
import math
import re
import sys

src, dst = sys.argv[1], sys.argv[2]
rows, bad = {}, 0
for line in open(src, "rb").read().decode("latin-1").splitlines():
    line = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", line).strip()
    if not line or line.startswith("#"):
        continue
    try:
        v = [float(x) for x in line.split()]
    except ValueError:
        bad += 1
        continue
    if len(v) != 8 or not all(math.isfinite(x) for x in v):
        bad += 1
        continue
    rows[round(v[0], 6)] = v
with open(dst, "w") as f:
    for t in sorted(rows):
        v = rows[t]
        f.write(f"{v[0]:.6f} " + " ".join(f"{x:.9f}" for x in v[1:]) + "\n")
print(f"{dst}: {len(rows)} poses, {bad} malformed lines dropped")
