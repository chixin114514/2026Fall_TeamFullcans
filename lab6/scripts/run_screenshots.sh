#!/usr/bin/env bash
# Screenshots of the team-part demos (D4, D5, optional baselines, race bonus).
# RViz runs on a private Xvfb display (WSLg's own screen cannot be captured), GPU rendered,
# and is captured after each bag has played for a while so the trajectories are visible.
#
#   bash scripts/run_screenshots.sh            # all shots -> results/screenshots/*.png
if [ -z "${BASH_VERSION:-}" ]; then exec bash "$0" "$@"; fi
set -eo pipefail
LAB6=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$LAB6"
OUT=$LAB6/results/screenshots
OFFICE=${OFFICE_BAG:-$HOME/datasets/vnav/lab6/office.bag}
RACE=$LAB6/results/race/race.bag
SCREEN=1920x1080
XDISP=:97
mkdir -p "$OUT"

[[ ! -e /tmp/.X${XDISP#:}-lock ]] || { echo "display $XDISP is in use" >&2; exit 1; }
Xvfb $XDISP -screen 0 ${SCREEN}x24 > /dev/null 2>&1 &
XPID=$!
trap 'bash scripts/run_rviz.sh stop > /dev/null 2>&1 || true; kill $XPID 2>/dev/null || true; rm -rf "${CFG:-/nonexistent}"' EXIT
sleep 2
export DISPLAY=$XDISP GALLIUM_DRIVER=d3d12 MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
export DEMO_PORT=11330     # leaves an interactive demo on 11320 running

# Fixed overview of the whole trajectory (the interactive configs follow the camera).
CFG=$(mktemp -d)
python3 scripts/rviz_overview.py lab_6/rviz/office_paths.rviz "$OFFICE" /tesse/odom 0 0 "$CFG/office.rviz"
if [[ -f $RACE ]]; then
  read -r RSTART RDUR < <(python3 scripts/race_window.py "$RACE")
  python3 scripts/rviz_overview.py lab_6/rviz/race_paths.rviz "$RACE" /current_state "$RSTART" "$RDUR" "$CFG/race.rviz"
fi

# shot <file> <estimator> <bag> <seconds of playback> [ENV=VALUE ...]
shot() {
  local name=$1 est=$2 bag=$3 wait=$4; shift 4
  [[ -f $bag ]] || { echo "skip $name: no $bag"; return; }
  local cfg=$CFG/office.rviz; [[ $bag == "$RACE" ]] && cfg=$CFG/race.rviz
  echo "$name: estimator $est on $(basename "$bag"), ${wait} s of playback"
  env RVIZ_CONFIG="$cfg" "$@" setsid bash scripts/run_rviz.sh "$est" "$bag" > "$OUT/.$name.log" 2>&1 < /dev/null &
  local win=
  for _ in $(seq 60); do
    win=$(xdotool search --onlyvisible --name "RViz" 2>/dev/null | head -n1) || true
    [[ -n $win ]] && break; sleep 1
  done
  [[ -n $win ]] || { echo "  RViz did not open, see $OUT/.$name.log"; return; }
  xdotool windowmove "$win" 0 0 windowsize "$win" ${SCREEN/x/ }
  sleep "$wait"
  ffmpeg -loglevel error -y -f x11grab -video_size $SCREEN -i $XDISP -frames:v 1 "$OUT/$name.png"
  bash scripts/run_rviz.sh stop > /dev/null 2>&1 || true
  echo "  -> results/screenshots/$name.png"
}

# Office bag: 237 s at 2.5x -> about 95 s; shot just before it loops.
shot d4_5pt_ransac        0 "$OFFICE" 88 RATE=2.5
shot d4_8pt_ransac        1 "$OFFICE" 88 RATE=2.5
shot d4_2pt_ransac        2 "$OFFICE" 88 RATE=2.5
shot d5_arun_ransac       3 "$OFFICE" 88 RATE=2.5
shot d4_5pt_no_ransac     0 "$OFFICE" 88 RATE=2.5 RANSAC=false
# Race bag: the whole flight at real time.
shot bonus_race_5pt       0 "$RACE" "${RDUR%.*}" PX=0.5
