#!/usr/bin/env bash
# Deliverable 6: timestamp fix, ground truth, evo_traj plots and evo_ape numbers.
# Runs the handout commands with --save_plot in place of --plot (no display here; with --plot
# evo blocks in plt.show()). evo writes one PNG per figure (_trajectories, _xyz, _rpy).
set -euo pipefail
LAB=$(cd "$(dirname "$0")/.." && pwd)
cd "$LAB"
OUT=results/d6
GT_CSV=${GT_CSV:-$HOME/datasets/vnav/MH_01_easy/mav0/state_groundtruth_estimate0/data.csv}
export MPLBACKEND=Agg

# 1. handout script: output/orbslam/orb_slam3.txt, output/kimera/kimera.txt
python3 fix_timestamps.py
cp output/orbslam/orb_slam3.txt "$OUT/orbslam/"
cp output/kimera/kimera.txt "$OUT/kimera/"

# 2. ground truth -> results/d6/data.tum
rm -f "$OUT/data.tum"   # evo asks before overwriting, which fails without a tty
(cd "$OUT" && evo_traj euroc "$GT_CSV" --save_as_tum)

K=output/kimera/kimera.txt
O=output/orbslam/orb_slam3.txt
rm -rf "$OUT/evo" && mkdir -p "$OUT/evo"
# 3a. not aligned
evo_traj tum $K $O --plot_mode xyz --save_plot "$OUT/evo/traj_unaligned.png" \
  | tee "$OUT/evo/traj_unaligned.txt"
# 3b. aligned (SE(3), Umeyama) to ground truth
evo_traj tum $K $O --ref "$OUT/data.tum" --align --plot_mode xyz \
  --save_plot "$OUT/evo/traj_aligned.png" | tee "$OUT/evo/traj_aligned.txt"

# 4. ATE (translation part), SE(3) alignment; Sim(3) as a scale check
for name in kimera orb_slam3; do
  f=$([[ $name == kimera ]] && echo $K || echo $O)
  rm -f "$OUT/evo/ape_${name}.zip" "$OUT/evo/ape_${name}_sim3.zip"
  evo_ape tum "$OUT/data.tum" "$f" --align -va \
    --save_results "$OUT/evo/ape_${name}.zip" | tee "$OUT/evo/ape_${name}.txt"
  evo_ape tum "$OUT/data.tum" "$f" --align --correct_scale -va \
    --save_results "$OUT/evo/ape_${name}_sim3.zip" | tee "$OUT/evo/ape_${name}_sim3.txt"
done
echo "→ $OUT/evo"
