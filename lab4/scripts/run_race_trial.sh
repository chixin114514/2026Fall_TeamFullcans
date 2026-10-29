#!/usr/bin/env bash
# One timed race attempt in a running start_unity_gpu.sh session.
#   run_race_trial.sh TRAJECTORY.json OUTPUT_DIR [race_node params as name:=value ...]
# The drone is respawned at the start; gates already passed in this Unity
# session stay green (the timer does not depend on their colour).
set -eo pipefail
LAB4_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
source /tmp/lab4_ws/devel/setup.bash
export ROS_MASTER_URI=${LAB4_ROS_MASTER:-http://localhost:11316} ROS_HOSTNAME=localhost
TRAJ=$(readlink -f "$1"); OUT=$2; shift 2
mkdir -p "$OUT"
pids=()
cleanup() {
  for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
  for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
}
trap cleanup EXIT
python3 -u "$LAB4_DIR/scripts/race_timer.py" --output "$OUT/result.jsonl" \
  --unity-log "${LAB4_UNITY_LOG:-/tmp/lab4-unity-gpu/unity.log}" > "$OUT/timer.log" 2>&1 & pids+=("$!")
rosbag record -O "$OUT/race.bag" /current_state /desired_state /rotor_speed_cmds /tesse/collision \
  > "$OUT/bag.log" 2>&1 & pids+=("$!")
rosparam delete /race_node 2>/dev/null || true
params=()
for arg in "$@"; do params+=("_$arg"); done
python3 -u "$LAB4_DIR/scripts/race_node.py" _trajectory:="$TRAJ" "${params[@]}" \
  > "$OUT/race_node.log" 2>&1 & pids+=("$!")
sleep 2
window=$(DISPLAY=${LAB4_DISPLAY:-:98} xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
DISPLAY=${LAB4_DISPLAY:-:98} xdotool windowfocus "$window" key r
duration=$(python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(int(sum(d['durations']))+1)" "$TRAJ")
for _ in $(seq $((duration * 2 + 30))); do
  if [[ -s "$OUT/result.jsonl" ]] && grep -q 'RACE TIME\|DNF' "$OUT/timer.log"; then break; fi
  sleep 0.5
done
sleep "${LAB4_SETTLE:-3}"
cat "$OUT/timer.log" | grep -v '^\s*$' | tail -20
