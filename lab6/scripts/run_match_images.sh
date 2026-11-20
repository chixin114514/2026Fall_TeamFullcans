#!/usr/bin/env bash
# SIFT-match and RANSAC inlier/outlier images from the actual pipeline (5-point Nister), as
# optical-flow arrows on the current frame, at the usual 1 px threshold and at the report's
# 0.1 px, for a few frame pairs of each bag.
#   bash scripts/run_match_images.sh  ->  results/screenshots/match_<bag>_<px>px_frameNNNN.png
if [ -z "${BASH_VERSION:-}" ]; then exec bash "$0" "$@"; fi
set -eo pipefail
LAB6=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$LAB6"
OUT=$LAB6/results/screenshots
OFFICE=${OFFICE_BAG:-$HOME/datasets/vnav/lab6/office.bag}
RACE=$LAB6/results/race/race.bag
PORT=11340
mkdir -p "$OUT"
source ~/vnav-builds/lab6_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:$PORT ROS_HOSTNAME=localhost
roscore -p $PORT > /dev/null 2>&1 & CORE=$!
trap 'kill $CORE 2>/dev/null || true' EXIT
sleep 3

# dump <label> <bag> <gt topic> <ransac px> <frames> <play args...>
dump() {
  local label=$1 bag=$2 gt=$3 px=$4 frames=$5; shift 5
  [[ -f $bag ]] || { echo "skip $label: no $bag"; return; }
  local tmp; tmp=$(mktemp -d)
  rosrun lab_6 pose_estimation --pose_estimator=0 --use_ransac=true --scale_translation=true \
    --ransac_px="$px" --ransac_max_iter=5000 --mask_self_depth=$([[ $gt == /current_state ]] && echo true || echo false) \
    --match_dump_dir="$tmp" --match_dump_frames="$frames" \
    /ground_truth_pose:="$gt" /rgb_images_topic:=/tesse/left_cam/rgb/image_raw \
    /depth_images_topic:=/tesse/depth_cam/mono/image_raw > "$OUT/.match_$label.log" 2>&1 & local node=$!
  sleep 2
  rosbag play -q "$@" "$bag" --topics "$gt" /tesse/left_cam/rgb/image_raw /tesse/depth_cam/mono/image_raw
  local last=${frames##*,}
  for _ in $(seq 600); do [[ -f $tmp/frame$(printf %04d "$last")_matches_ransac.png ]] && break; sleep 1; done
  kill -INT $node 2>/dev/null || true; wait $node 2>/dev/null || true
  for f in "$tmp"/*.png; do [[ -f $f ]] && mv "$f" "$OUT/match_${label}_${px}px_$(basename "$f" _matches_ransac.png).png"; done
  rm -rf "$tmp"
  ls "$OUT"/match_"$label"_"$px"px_*.png
}

rm -f "$OUT"/match_*.png
dump office "$OFFICE" /tesse/odom 1 150,600 -r 0.5 -u 45
dump office "$OFFICE" /tesse/odom 0.1 150,600 -r 0.5 -u 45
if [[ -f $RACE ]]; then
  read -r START DUR < <(python3 scripts/race_window.py "$RACE")
  dump race "$RACE" /current_state 1 120 -r 0.5 -s "$START" -u 15
fi
