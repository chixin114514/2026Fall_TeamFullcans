#!/usr/bin/env bash
# Deliverable 8: run the Farneback node on a bag and dump every visualization frame.
#   bash scripts/run_flow.sh [30fps|smooth]
# Needs a running roscore. Frames go to ~/vnav-builds/lab5_frames/<bag>/flow
# (outside the repo); one frame is kept in results/d8_flow/<bag>/frames for the report.
set -eo pipefail
source "${LAB5_WS:-$HOME/vnav-builds/lab5_ws}/devel/setup.bash"
LAB5=$(cd "$(dirname "$0")/.." && pwd)
DATA=${LAB5_DATASETS:-$HOME/datasets/vnav/lab5}
BAG=${1:-30fps}
case "$BAG" in
  30fps)  FILE=30fps_424x240_2018-10-01-18-35-06.bag; TOPIC=/camera/color/image_raw ;;
  smooth) FILE=vnav-lab5-smooth-trajectory.bag;       TOPIC=/tesse/left_cam/rgb/image_raw ;;
  *) echo "unknown bag $BAG"; exit 1 ;;
esac
FRAMES=${LAB5_FRAMES:-$HOME/vnav-builds/lab5_frames}/$BAG/flow
rm -rf "$FRAMES"; mkdir -p "$FRAMES"
rosparam delete /self_flow >/dev/null 2>&1 || true
rosrun lab_5 self_flow _frames_dir:="$FRAMES" _show:=false /images_topic:="$TOPIC" &
NODE=$!
sleep 2
rosbag play -q "$DATA/$FILE" --topics "$TOPIC"
# let the node drain its queue
prev=-1; while n=$(ls "$FRAMES" | wc -l); [ "$n" != "$prev" ]; do prev=$n; sleep 2; done
kill -INT $NODE; wait $NODE || true
OUT="$LAB5/results/d8_flow/$BAG/frames"
rm -rf "$OUT"; mkdir -p "$OUT"
mid=$(ls "$FRAMES" | sort | sed -n "$(( prev / 2 ))p")
cp "$FRAMES/$mid" "$OUT/"
echo "$prev frames → $FRAMES (kept $mid)"
