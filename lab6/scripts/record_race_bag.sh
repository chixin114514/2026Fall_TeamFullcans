#!/usr/bin/env bash
# Bonus: fly the Lab 4 race in the Lab 6 simulator and record a rosbag with
# stereo RGB, depth and ground-truth odometry for the Lab 6 pose estimators.
#
#   bash scripts/record_race_bag.sh [output.bag]
#
# Needs: the Lab 6 simulator in ~/vnav-builds/lab6-sim/lab6 (https://vnav.mit.edu/material/lab6.zip),
# the Lab 4 workspace built in /tmp/lab4_ws (lab4/scripts/build_workspace.sh), Xvfb and the
# WSL D3D12 driver. Unity renders at 720x480 so the camera matches the hard-coded intrinsics.
set -eo pipefail
LAB6=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
LAB4=$(cd "$LAB6/../lab4" && pwd)
SIM=${LAB6_SIM:-$HOME/vnav-builds/lab6-sim/lab6}
OUT=${1:-$LAB6/results/race/race.bag}
SESSION=$(dirname "$OUT")/session
V_MAX=${LAB6_V_MAX:-8.0}
A_MAX=${LAB6_A_MAX:-6.0}
DURATION=${LAB6_RECORD_S:-45}
DISPLAY_NUM=:98
ROS_PORT=11316
PORT=9000
mkdir -p "$SESSION"
[[ ! -e $OUT ]] || { echo "Refusing to overwrite $OUT" >&2; exit 1; }
[[ ! -e /tmp/.X${DISPLAY_NUM#:}-lock ]] || { echo "Display $DISPLAY_NUM is in use" >&2; exit 1; }

source /tmp/lab4_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:$ROS_PORT ROS_HOSTNAME=localhost
pids=()
cleanup() {
  for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
  sleep 2
  for pid in "${pids[@]}"; do kill -TERM "$pid" 2>/dev/null || true; done
  wait 2>/dev/null || true
}
trap cleanup EXIT

Xvfb $DISPLAY_NUM -screen 0 960x600x24 > "$SESSION/xvfb.log" 2>&1 & pids+=("$!")
roscore -p $ROS_PORT > "$SESSION/roscore.log" 2>&1 & pids+=("$!")
sleep 3

# Unity on the NVIDIA GPU through D3D12; a fresh player shows unpassed gates.
( export DISPLAY=$DISPLAY_NUM GALLIUM_DRIVER=d3d12 MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA \
         LD_LIBRARY_PATH=/usr/lib/wsl/lib
  unset LIBGL_ALWAYS_SOFTWARE LIBGL_ALWAYS_INDIRECT
  cd "$SIM" && exec env -u PYTHONPATH ./lab6.x86_64 -screen-width 720 -screen-height 480 \
    -screen-fullscreen 0 -force-glcore -logFile "$SESSION/unity.log" \
    --listen_port $PORT --send_port $PORT ) > "$SESSION/player.log" 2>&1 & pids+=("$!")
for _ in {1..120}; do
  WIN=$(DISPLAY=$DISPLAY_NUM xdotool search --onlyvisible --name tesse_vnav_scenes 2>/dev/null | head -n1) || true
  [[ -n $WIN ]] && break; sleep 0.5
done
[[ -n $WIN ]] || { echo "Unity window did not appear" >&2; exit 1; }
sleep 5
grep -q 'Renderer: D3D12 (NVIDIA' "$SESSION/unity.log" || { echo "Unity is not on the NVIDIA renderer" >&2; exit 1; }

# Bridge with the extra streams the handout asks for.
roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true \
  publish_stereo_rgb:=true publish_depth:=true publish_odom:=true \
  position_port:=$PORT metadata_port:=$((PORT+1)) image_port:=$((PORT+2)) \
  udp_port:=$((PORT+4)) step_port:=$((PORT+5)) > "$SESSION/bridge.log" 2>&1 & pids+=("$!")
timeout 60 rostopic echo -n 1 /current_state > /dev/null
timeout 60 rostopic echo -n 1 --noarr /tesse/depth_cam/mono/image_raw > /dev/null

# Lab 4 race stack: trajectory follower + controller, then the gate planner.
roslaunch trajectory_generation traj_following.launch \
  gains_file:="$LAB4/trajectory_generation_pkg/config/gains_gpu.yaml" \
  v_max:="$V_MAX" a_max:="$A_MAX" a_z_max:=5.0 corridor:=0.5 > "$SESSION/follower.log" 2>&1 & pids+=("$!")
for _ in {1..40}; do rosnode ping -c 1 /controller_node > /dev/null 2>&1 && break; sleep 0.5; done
DISPLAY=$DISPLAY_NUM xdotool windowfocus "$WIN" key r
sleep 2

rosbag record -O "$OUT" /current_state /desired_state /clock \
  /tesse/left_cam/rgb/image_raw /tesse/left_cam/camera_info \
  /tesse/right_cam/rgb/image_raw /tesse/right_cam/camera_info \
  /tesse/depth_cam/mono/image_raw /tesse/depth_cam/camera_info \
  > "$SESSION/rosbag.log" 2>&1 & REC=$!; pids+=("$REC")
sleep 1
roslaunch planner_pkg traj_gen.launch simulator_data_directory:="$LAB4/simulator_data" \
  > "$SESSION/planner.log" 2>&1 & pids+=("$!")
echo "Recording $DURATION s -> $OUT"
sleep "$DURATION"
kill -INT "$REC"; wait "$REC" 2>/dev/null || true
rosbag info "$OUT" | sed -n '1,25p'
