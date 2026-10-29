#!/usr/bin/env bash
# Encode the dumped frames (run_experiments.py --frames-for SIFT LK, run_flow.sh) into video/.
set -euo pipefail
LAB5=$(cd "$(dirname "$0")/.." && pwd)
FRAMES=${LAB5_FRAMES:-$HOME/vnav-builds/lab5_frames}
mkdir -p "$LAB5/video"
enc() {  # <frames dir> <output mp4>
  ffmpeg -y -loglevel error -framerate 30 -pattern_type glob -i "$1/frame_*.png" \
    -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -c:v libx264 -pix_fmt yuv420p -crf 26 "$2"
  echo "→ $2 ($(du -h "$2" | cut -f1))"
}
enc "$FRAMES/30fps/SIFT"  "$LAB5/video/d6_sift_tracking_30fps.mp4"
enc "$FRAMES/smooth/SIFT" "$LAB5/video/d6_sift_tracking_smooth.mp4"
enc "$FRAMES/30fps/LK"    "$LAB5/video/d7_lk_tracking_30fps.mp4"
enc "$FRAMES/smooth/LK"   "$LAB5/video/d7_lk_tracking_smooth.mp4"
enc "$FRAMES/30fps/flow"  "$LAB5/video/d8_farneback_flow_30fps.mp4"
enc "$FRAMES/smooth/flow" "$LAB5/video/d8_farneback_flow_smooth.mp4"
