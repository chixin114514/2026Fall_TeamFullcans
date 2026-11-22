#!/usr/bin/env bash
# Run ORB-SLAM3 and then Kimera-VIO on the full EuRoC MH_01_easy sequence (never in parallel:
# the machine has 15 GB RAM), then copy the raw trajectories into results/d6/.
#   usage: scripts/run_slam.sh [orbslam|kimera|both]   (default: both)
set -euo pipefail
LAB=$(cd "$(dirname "$0")/.." && pwd)
cd "$LAB"
OUT=results/d6
mkdir -p "$OUT"
which=${1:-both}

DS=$HOME/datasets/vnav
# Kimera reads state_groundtruth_estimate0/sensor.yaml with cv::FileStorage, which needs a
# "%YAML:1.0" first line that the EuRoC files lack ("Cannot open file ... sensor.yaml").
# Build a hard-linked copy (no extra disk space) where only the yaml files get the header,
# so the original dataset stays untouched.
prepare_kimera_dataset() {
  local dst=$DS/MH_01_easy_kimera
  [[ -f $dst/mav0/state_groundtruth_estimate0/sensor.yaml ]] && \
    head -1 "$dst/mav0/state_groundtruth_estimate0/sensor.yaml" | grep -q '^%YAML' && return
  rm -rf "$dst"
  cp -al "$DS/MH_01_easy" "$dst"
  for f in "$dst"/mav0/*/sensor.yaml "$dst"/mav0/body.yaml; do
    { echo '%YAML:1.0'; cat "$f"; } >"$f.tmp" && rm "$f" && mv "$f.tmp" "$f"
  done
}

run() {  # $1 = orbslam|kimera
  echo "== $1: started $(date -Is)" | tee "$OUT/$1_run.log"
  if [[ $1 == kimera ]]; then
    prepare_kimera_dataset
    ./run_docker_vnav.sh kimera:latest bash run_kimera.sh -p /datasets/MH_01_easy_kimera \
      >>"$OUT/$1_run.log" 2>&1
  else
    ./run_docker_vnav.sh "$1:latest" >>"$OUT/$1_run.log" 2>&1
  fi
  echo "== $1: finished $(date -Is)" | tee -a "$OUT/$1_run.log"
}

if [[ $which == orbslam || $which == both ]]; then
  run orbslam
  mkdir -p "$OUT/orbslam" && cp output/orbslam/CameraTrajectory.txt "$OUT/orbslam/"
fi
if [[ $which == kimera || $which == both ]]; then
  run kimera
  mkdir -p "$OUT/kimera" && cp output/kimera/traj_vio.csv output/kimera/StatisticsVIO.csv "$OUT/kimera/"
fi
