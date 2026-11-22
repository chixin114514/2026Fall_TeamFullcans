#!/usr/bin/env bash
# Deliverable 7: run LDSO (monocular, cam0 only) on the full EuRoC MH_01_easy sequence.
# Output: results/d7/results.txt (with loop closing) and results.txt.noloop (without).
#   env: DISPLAY (default :0); NOGUI=1 runs without the Pangolin window.
set -euo pipefail
LAB=$(cd "$(dirname "$0")/.." && pwd)
LDSO=${LDSO_DIR:-$HOME/vnav-builds/ldso}
CAM0=${CAM0:-$HOME/datasets/vnav/MH_01_easy/mav0/cam0}
OUT=$LAB/results/d7
mkdir -p "$OUT"
export DISPLAY=${DISPLAY:-:0}
export LD_LIBRARY_PATH=$HOME/vnav-builds/pangolin/lib:${LD_LIBRARY_PATH:-}
cd "$LDSO"   # LDSO loads ./vocab/orbvoc.dbow3 and ./examples/EUROC/EUROC.txt relative to here
rm -f "$OUT/results.txt" "$OUT/results.txt.noloop"
./bin/run_dso_euroc preset=0 files="$CAM0" output="$OUT/results.txt" \
    nogui="${NOGUI:-0}" >"$OUT/ldso_run.log" 2>&1 &
PID=$!
# The trajectory is written after the final pose-graph optimisation; afterwards the program
# only waits for the Pangolin window to be closed by hand, so stop it once both files exist.
while kill -0 $PID 2>/dev/null; do
  if [[ -s $OUT/results.txt.noloop ]]; then sleep 5; kill $PID 2>/dev/null || true; break; fi
  sleep 5
done
wait $PID 2>/dev/null || true
echo "loops accepted: $(grep -c 'Loop detected' "$OUT/ldso_run.log")"
echo "→ $OUT/results.txt ($(wc -l <"$OUT/results.txt") keyframe poses)"
