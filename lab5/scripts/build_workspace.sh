#!/usr/bin/env bash
# 把 lab5 的包软链接进 catkin 工作空间并编译（首次会下载并编译 OpenCV 3.4.2 + contrib）。
set -eo pipefail
source /opt/ros/noetic/setup.bash
LAB5_DIR=$(cd "$(dirname "$0")/.." && pwd)
LAB5_WS=${LAB5_WS:-$HOME/vnav-builds/lab5_ws}
mkdir -p "$LAB5_WS/src"
ln -sfn "$LAB5_DIR/feature_tracking" "$LAB5_WS/src/feature_tracking"
for pkg in opencv3_catkin catkin_simple; do
  ln -sfn "$LAB5_DIR/dependencies/$pkg" "$LAB5_WS/src/$pkg"
done
cd "$LAB5_WS"
[ -f .catkin_tools/profiles/default/config.yaml ] || catkin init >/dev/null
catkin build -j"$(nproc)" --no-status --cmake-args -DCMAKE_BUILD_TYPE=Release -- "$@"
echo "→ source $LAB5_WS/devel/setup.bash"
