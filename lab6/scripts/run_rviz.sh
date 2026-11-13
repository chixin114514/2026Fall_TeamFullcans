#!/usr/bin/env bash
# Live RViz demo: pose estimator + trajectories (GT, anchored estimate, chained visual odometry).
#   bash scripts/run_rviz.sh [pose_estimator 0|1|2|3] [bag]
#   bash scripts/run_rviz.sh 0 results/race/race.bag     # bonus race bag (flight segment)
#   RANSAC=false bash scripts/run_rviz.sh 0               # optional: no RANSAC
#   bash scripts/run_rviz.sh stop                         # stop the demo
# Real time by default (RATE=1): the node skips stale frames (--latest_only) and uses a
# 0.3 px RANSAC threshold (PX=...) so the 5-point solver keeps a usable update rate.
# The report's evaluation uses every frame at 0.1 px (scripts/run_experiments.py).
# Runs on its own ROS master (port 11320) so it does not disturb other experiments.
set -e
if [[ ${1:-} == stop ]]; then STOP_ONLY=1; fi
LAB6=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
EST=${1:-0}; [[ $EST == stop ]] && EST=0
BAG=${2:-$HOME/datasets/vnav/lab6/office.bag}
source ~/vnav-builds/lab6_ws/devel/setup.bash
# Ground truth: /tesse/odom in the office bag, /current_state in the race bag.
if [[ -z ${STOP_ONLY:-} ]] && rosbag info "$BAG" | grep -q "/current_state"; then
  GT=/current_state; PLAY=(-r "${RATE:-1.0}" -s 1.5 -u 21)
else
  GT=/tesse/odom; PLAY=(-r "${RATE:-1.0}")
fi
# Stop any previous demo first: every process bound to master 11320, including the
# bag player (its process is named "play", not "rosbag").
stop_demo() {
  for p in $(pgrep -u "$(id -u)" .); do
    [[ $p == $$ || $p == $PPID ]] && continue
    # an older copy of this script: its ROS_MASTER_URI is exported inside, not in environ
    if [[ $(tr '\0' ' ' < /proc/$p/cmdline 2>/dev/null) == "bash "*run_rviz.sh* ]]; then
      kill "$p" 2>/dev/null; continue
    fi
    tr '\0' '\n' < /proc/$p/environ 2>/dev/null | grep -qx "ROS_MASTER_URI=http://localhost:11320" && kill "$p" 2>/dev/null
  done
  sleep 2
}
stop_demo
[[ -n ${STOP_ONLY:-} ]] && exit 0
export ROS_MASTER_URI=http://localhost:11320 ROS_HOSTNAME=localhost DISPLAY=${DISPLAY:-:0}
pids=()
trap 'kill "${pids[@]}" 2>/dev/null' EXIT
roscore -p 11320 > /dev/null 2>&1 & pids+=("$!"); sleep 3
rosparam set use_sim_time true
rosrun tf2_ros static_transform_publisher 0 0 0 0 0 0 world world_anchor & pids+=("$!")
rosrun lab_6 pose_estimation --use_ransac="${RANSAC:-true}" --pose_estimator="$EST" --scale_translation=true \
  --latest_only=true --ransac_px="${PX:-0.3}" --ransac_max_iter="${MAXIT:-1000}" \
  /ground_truth_pose:="$GT" /rgb_images_topic:=/tesse/left_cam/rgb/image_raw \
  /depth_images_topic:=/tesse/depth_cam/mono/image_raw & pids+=("$!")
python3 -u "$LAB6/scripts/rviz_paths.py" /rgb_images_topic:=/tesse/left_cam/rgb/image_raw \
  /depth_images_topic:=/tesse/depth_cam/mono/image_raw & pids+=("$!")
rviz -d "$LAB6/lab_6/rviz/office_paths.rviz" & pids+=("$!")
sleep 8
# Only the needed topics: the race bag also holds a recorded /clock that would fight --clock.
rosbag play --clock -l "${PLAY[@]}" "$BAG" \
  --topics "$GT" /tesse/left_cam/rgb/image_raw /tesse/depth_cam/mono/image_raw
