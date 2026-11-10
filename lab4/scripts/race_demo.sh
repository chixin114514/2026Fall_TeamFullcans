#!/usr/bin/env bash
# One command for the Lab4 race on the Windows desktop:
#   bash scripts/race_demo.sh            # Unity window with the race clock, then fly
#   bash scripts/race_demo.sh --rviz     # also open RViz
# Starts a fresh Unity (red gates) in a Xephyr window, roscore, the TESSE
# bridge, race_timer.py, the in-window clock (race_overlay.py) and
# race_node.py, then respawns the drone; it hovers for 2 s and races. Press
# Enter to fly again (the gates stay green), Ctrl+C to close everything.
# Ports default to 9100 (Unity) and 11316 (ROS) so a Lab3 session on 9000 /
# 11317 can keep running; override with LAB4_PORT, LAB4_ROS_PORT, LAB4_DISPLAY.
set -eo pipefail
LAB4_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
PORT=${LAB4_PORT:-9100}
ROS_PORT=${LAB4_ROS_PORT:-11316}
DISP=${LAB4_DISPLAY:-:97}
SESSION=${LAB4_SESSION:-/tmp/lab4-race-demo}
TRAJ=${LAB4_TRAJECTORY:-$LAB4_DIR/race/trajectories/x3.json}
# Most reliable on a freshly started Unity (about 2.49 s); see README.
RACE_PARAMS=(_lead:=0.03 _kr:=20 _komega:=3 "_inertia:=[0.11,0.21,0.11]"
             _yaw_free:=true _fb_tilt_thrust:=100 _time_scale:=${LAB4_TIME_SCALE:-1.0})
RVIZ=0
[[ ${1:-} == --rviz ]] && RVIZ=1

fail() { printf '%s\n' "$*" >&2; exit 1; }
[[ -f /tmp/lab4_ws/devel/setup.bash ]] || fail "No workspace: run bash scripts/build_workspace.sh first."
python3 -c 'import tkinter' 2>/dev/null || fail "Missing Tk: sudo apt-get install -y python3-tk"
command -v Xephyr >/dev/null || fail "Missing Xephyr: sudo apt-get install -y xserver-xephyr"
[[ -e /tmp/.X11-unix/X0 || -n ${LAB4_HOST_DISPLAY:-} ]] || fail "No Windows display (WSLg :0) found."
if ss -uln 2>/dev/null | grep -q ":$PORT "; then fail "UDP port $PORT is in use; set LAB4_PORT."; fi
if ss -tln 2>/dev/null | grep -q ":$ROS_PORT "; then fail "ROS port $ROS_PORT is in use; set LAB4_ROS_PORT."; fi

mkdir -p "$SESSION"
rm -f "$SESSION"/{start.log,result.jsonl}
pids=()
start_pid=
cleanup() {
  trap - EXIT INT TERM
  printf '\nShutting down...\n'
  for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
  for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
  [[ -n $start_pid ]] && kill -TERM "$start_pid" 2>/dev/null || true
  [[ -n $start_pid ]] && wait "$start_pid" 2>/dev/null || true
}
trap cleanup EXIT
trap 'exit 130' INT TERM

printf 'Starting Unity (GPU) in a window on the Windows desktop...\n'
LAB4_XEPHYR=1 LAB4_DISPLAY=$DISP LAB4_PORT=$PORT LAB4_ROS_PORT=$ROS_PORT LAB4_SESSION=$SESSION \
  bash "$LAB4_DIR/scripts/start_unity_gpu.sh" > "$SESSION/start.log" 2>&1 &
start_pid=$!
for _ in $(seq 120); do
  grep -q 'verified' "$SESSION/start.log" 2>/dev/null && break
  kill -0 "$start_pid" 2>/dev/null || { cat "$SESSION/start.log"; fail "Unity did not start."; }
  sleep 1
done
grep -q 'verified' "$SESSION/start.log" || { cat "$SESSION/start.log"; fail "Unity did not start in time."; }

source /tmp/lab4_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:$ROS_PORT ROS_HOSTNAME=localhost
python3 -u "$LAB4_DIR/scripts/race_timer.py" --unity-log "$SESSION/unity.log" \
  --output "$SESSION/result.jsonl" \
  > >(grep --line-buffered -E 'gate|GO|RACE|DNF|Collision|MISSED|referee|Attempt') 2>&1 &
pids+=("$!")
DISPLAY=$DISP python3 "$LAB4_DIR/scripts/race_overlay.py" > "$SESSION/overlay.log" 2>&1 & pids+=("$!")
if [[ $RVIZ == 1 ]]; then
  DISPLAY=${LAB4_HOST_DISPLAY:-:0} DISABLE_ROS1_EOL_WARNINGS=1 rosrun rviz rviz -d "$LAB4_DIR/rviz/race_gpu.rviz" \
    > "$SESSION/rviz.log" 2>&1 & pids+=("$!")
fi
rosparam delete /race_node 2>/dev/null || true
python3 -u "$LAB4_DIR/scripts/race_node.py" _trajectory:="$TRAJ" "${RACE_PARAMS[@]}" \
  > "$SESSION/race_node.log" 2>&1 & pids+=("$!")
sleep 2

respawn() {
  local window
  window=$(DISPLAY=$DISP xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
  DISPLAY=$DISP xdotool windowfocus "$window" key r
}
while true; do
  runs=$( [[ -f $SESSION/result.jsonl ]] && wc -l < "$SESSION/result.jsonl" || echo 0)
  printf 'Respawning the drone; it hovers for 2 s, then races.\n'
  respawn
  for _ in $(seq 60); do
    [[ -f $SESSION/result.jsonl && $(wc -l < "$SESSION/result.jsonl") -gt $runs ]] && break
    sleep 0.5
  done
  read -r -p $'\nEnter: fly again    Ctrl+C: quit ' _ || break
done
