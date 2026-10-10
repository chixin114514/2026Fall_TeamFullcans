#!/usr/bin/env bash
# Requires Unity under Box64 on :98 and the bridge on ROS master 11316.
set -eo pipefail
source /tmp/lab4_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11316 ROS_HOSTNAME=localhost
LAB4_DIR=/workspace/lab4
rosnode kill /controller_node /simple_traj_planner /traj_vertices_publisher 2>/dev/null || true
pids=()
cleanup() {
  for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
  for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
}
trap cleanup EXIT
rosbag record -O "$LAB4_DIR/report/unity_race.bag" /current_state /desired_state > /tmp/lab4-unity-bag.log 2>&1 & pids+=("$!")
ffmpeg -y -loglevel error -f x11grab -framerate 6 -video_size 960x600 -i :98 \
  -c:v libx264 -preset ultrafast -crf 25 -pix_fmt yuv420p "$LAB4_DIR/report/unity_race.mp4" > /tmp/lab4-unity-video.log 2>&1 & pids+=("$!")
roslaunch trajectory_generation traj_following.launch \
  gains_file:="$LAB4_DIR/trajectory_generation_pkg/config/gains_arm64.yaml" \
  v_max:=2.0 a_max:=1.0 > /tmp/lab4-unity-follower.log 2>&1 & pids+=("$!")
sleep 2
LAB4_WINDOW_ID=$(DISPLAY=:98 xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
DISPLAY=:98 xdotool windowfocus "$LAB4_WINDOW_ID" key r
sleep 1
roslaunch planner_pkg traj_gen.launch simulator_data_directory:="$LAB4_DIR/simulator_data" > /tmp/lab4-unity-gates.log 2>&1 & pids+=("$!")
python3 "$LAB4_DIR/scripts/monitor_unity.py" > /tmp/lab4-unity-monitor.log 2>&1
