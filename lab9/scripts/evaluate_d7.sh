#!/usr/bin/env bash
# Deliverable 7: LDSO + Kimera + ORB-SLAM3, Sim(3)-aligned (--correct_scale) to ground truth.
# Needs results/d6 from scripts/evaluate.sh and results/d7/results.txt from scripts/run_ldso.sh.
set -euo pipefail
LAB=$(cd "$(dirname "$0")/.." && pwd)
cd "$LAB"
D6=results/d6; D7=results/d7
export MPLBACKEND=Agg
python3 scripts/fix_ldso.py "$D7/results.txt" "$D7/ldso.txt"
python3 scripts/fix_ldso.py "$D7/results.txt.noloop" "$D7/ldso_noloop.txt"

K=$D6/kimera/kimera.txt; O=$D6/orbslam/orb_slam3.txt; L=$D7/ldso.txt
rm -rf "$D7/evo" && mkdir -p "$D7/evo"
# handout: all three, aligned and scale corrected, x-y plane (--save_plot instead of --plot)
evo_traj tum $K $O $L --ref $D6/data.tum --align --correct_scale --plot_mode xy \
  --save_plot "$D7/evo/traj_sim3_xy.png" | tee "$D7/evo/traj_sim3_xy.txt"
for f in $L $D7/ldso_noloop.txt; do
  n=$(basename "$f" .txt)
  evo_ape tum $D6/data.tum "$f" --align --correct_scale -va \
    --save_results "$D7/evo/ape_${n}_sim3.zip" | tee "$D7/evo/ape_${n}_sim3.txt"
done
echo "→ $D7/evo"
