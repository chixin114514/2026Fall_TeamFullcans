#!/usr/bin/env bash
# Lab 6 demo: walks through the deliverables in RViz, one step at a time.
#
#   bash scripts/demo.sh            # all steps; press Enter to go to the next one
#   bash scripts/demo.sh 3          # only step 3
#   bash scripts/demo.sh list       # list the steps
#
# RViz opens on the Windows desktop (WSLg). Every step uses its own ROS master on port
# 11320 (scripts/run_rviz.sh), so it does not disturb other ROS work. Ctrl-C stops the demo.
set -eo pipefail
LAB6=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$LAB6"
OFFICE=${OFFICE_BAG:-$HOME/datasets/vnav/lab6/office.bag}
RACE=$LAB6/results/race/race.bag
WS=$HOME/vnav-builds/lab6_ws
LOG=$(mktemp -d /tmp/lab6-demo.XXXXXX)

bold() { printf '\n\033[1m%s\033[0m\n' "$*"; }
note() { printf '  %s\n' "$@"; }
stop_rviz() { bash scripts/run_rviz.sh stop > /dev/null 2>&1 || true; }
trap 'stop_rviz; echo; echo "demo stopped (logs: $LOG)"' EXIT INT TERM

# ----------------------------------------------------------------------------- checks
check() {
  local ok=1
  [[ -f $WS/devel/setup.bash ]] || { echo "missing $WS: run bash scripts/build_workspace.sh"; ok=0; }
  [[ -f $OFFICE ]] || { echo "missing office bag $OFFICE (set OFFICE_BAG=...)"; ok=0; }
  [[ -n ${DISPLAY:-} ]] || export DISPLAY=:0
  [[ $ok == 1 ]] || exit 1
  [[ -f $RACE ]] || echo "note: no race bag ($RACE); steps 5-6 are skipped." \
                         "Record it with: bash scripts/record_race_bag.sh"
}

# Launch one RViz configuration and wait for Enter.
#   show <estimator 0|1|2|3> <bag> [ENV=VALUE ...]
show() {
  local est=$1 bag=$2; shift 2
  stop_rviz
  env "$@" setsid bash scripts/run_rviz.sh "$est" "$bag" > "$LOG/step$STEP.log" 2>&1 < /dev/null &
  printf '  starting RViz'
  for _ in $(seq 60); do
    grep -q "RPE frame" "$LOG/step$STEP.log" 2>/dev/null && break
    printf '.'; sleep 1
  done
  echo
  if ! grep -q "RPE frame" "$LOG/step$STEP.log"; then
    echo "  the estimator did not start, see $LOG/step$STEP.log"; return
  fi
  echo "  RViz is running. Press Enter for the next step."
  read -r _
}

legend() {
  note "In RViz (right panel):" \
       "  green line/arrow   ground-truth camera trajectory and pose" \
       "  yellow line/arrow  per-frame estimate, anchored on the previous ground-truth pose" \
       "  red line           estimates chained frame to frame only (visual odometry, drifts)" \
       "  point cloud        scene from the depth images, placed with the ground-truth poses" \
       "Left panels: the RGB image that is tracked and the depth image."
}

# ----------------------------------------------------------------------------- steps
STEPS=(
  "Office bag: 5-point Nister + RANSAC (Deliverable 4)"
  "Office bag: 8-point and 2-point with known rotation (Deliverable 4)"
  "Office bag: Arun 3-point, 3D-3D with depth (Deliverable 5)"
  "Office bag: 5-point WITHOUT RANSAC (optional baseline)"
  "Race bag (bonus): Lab 4 race flown in the Lab 6 simulator, 5-point"
  "Race bag (bonus): 2-point and Arun at real time"
  "Results: summary table and the report"
)

step1() {
  legend
  note "" "Every frame pair: SIFT matches (lab 5) -> calibrateKeypoints -> bearing vectors" \
       "-> OpenGV 5-point RANSAC. Yellow sits on green; red drifts only slowly."
  show 0 "$OFFICE"
}
step2() {
  note "8-point (Longuet-Higgins) first, then the 2-point solver, which takes the rotation" \
       "from ground truth and only solves the translation direction (Deliverable 2)."
  note "" "8-point:"
  show 1 "$OFFICE"
  note "2-point (rotation given): the red odometry line now drifts much less."
  show 2 "$OFFICE"
}
step3() {
  note "Matches are lifted to 3D with the depth image; Arun's SVD aligns the two point" \
       "clouds inside RANSAC. Depth gives metric scale, no ground-truth rescaling needed."
  show 3 "$OFFICE"
}
step4() {
  note "Same matches, but the 5-point solver is fed all of them, outliers included." \
       "Watch the yellow arrow jump and the red line leave the green one within seconds."
  show 0 "$OFFICE" RANSAC=false
}
step5() {
  [[ -f $RACE ]] || { note "skipped: no race bag"; return; }
  note "Recorded with scripts/record_race_bag.sh: the Lab 4 planner and controller fly the" \
       "gate course (about 96 m in 18 s, up to 7.3 m/s) in the Lab 6 simulator; the bag holds" \
       "stereo RGB, depth and odometry. The red frames in the cloud are the gates."
  note "" "Live settings: 0.5 px RANSAC, newest frame only (about 10 Hz pose updates)." \
       "The depth camera also renders the drone's own body; the map masks it out."
  show 0 "$RACE" PX=0.5
}
step6() {
  [[ -f $RACE ]] || { note "skipped: no race bag"; return; }
  note "2-point (rotation given), then Arun: both run in a few ms per frame."
  note "" "2-point:"
  show 2 "$RACE"
  note "Arun:"
  show 3 "$RACE"
}
step7() {
  stop_rviz
  python3 - <<'EOF'
import json
s = json.load(open("results/summary.json"))
names = {"5pt": "5-point Nister", "8pt": "8-point", "2pt": "2-point (known R)",
         "arun": "Arun 3D-3D", "5pt_noransac": "5-point, no RANSAC",
         "8pt_noransac": "8-point, no RANSAC", "arun_noransac": "Arun, no RANSAC"}
print("Office sequence, %d frame pairs per method (thresholds 0.1 px / 1 cm)\n" % s["5pt"]["frames"])
print("%-22s %10s %8s %10s %8s %10s" % ("method", "rot med", "<1 deg", "trans med", "<0.1", "time"))
for k, n in names.items():
    if k not in s:
        continue
    d = s[k]
    rot = "    --" if k == "2pt" else "%7.3f deg" % d["rot_med_deg"]
    print("%-22s %10s %7.1f%% %10.3f %7.1f%% %7.2f ms" % (n, rot, 100 * d["rot_lt1deg"],
          d["tu_med"], 100 * d["tu_lt01"], d["time_ms_med"]))
print("\nArun metric translation error: median %.1f mm" % s["arun"]["tm_med_mm"])
EOF
  echo
  if command -v wslview > /dev/null; then wslview report/lab6_report.pdf
  elif command -v explorer.exe > /dev/null; then explorer.exe "$(wslpath -w report/lab6_report.pdf)" || true
  else echo "report: $LAB6/report/lab6_report.pdf"; fi
}

# ----------------------------------------------------------------------------- main
if [[ ${1:-} == list ]]; then
  for i in "${!STEPS[@]}"; do printf '%d  %s\n' $((i + 1)) "${STEPS[$i]}"; done
  trap - EXIT; exit 0
fi
check
if [[ -n ${1:-} ]]; then sel=("$1"); else sel=($(seq ${#STEPS[@]})); fi
for STEP in "${sel[@]}"; do
  [[ $STEP =~ ^[1-7]$ ]] || { echo "unknown step $STEP (bash scripts/demo.sh list)"; exit 1; }
  bold "[$STEP/${#STEPS[@]}] ${STEPS[$((STEP - 1))]}"
  "step$STEP"
done
bold "Demo finished."
