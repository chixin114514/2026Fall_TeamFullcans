#!/usr/bin/env bash
# 编译 lab6：工作空间 extend lab5 的工作空间（复用其中的 opencv3_catkin、catkin_simple、lab_5），
# 再加入 OpenGV（ethz-asl catkin 版本，固定 commit）、eigen_catkin 桩包和 lab_6。
set -eo pipefail
source /opt/ros/noetic/setup.bash
LAB6_DIR=$(cd "$(dirname "$0")/.." && pwd)
LAB5_WS=${LAB5_WS:-$HOME/vnav-builds/lab5_ws}
LAB6_WS=${LAB6_WS:-$HOME/vnav-builds/lab6_ws}
OPENGV_COMMIT=7542b89   # ethz-asl/opengv master，lab_6.rosinstall 指向的仓库

[ -f "$LAB5_WS/devel/setup.bash" ] || { echo "先运行 lab5/scripts/build_workspace.sh"; exit 1; }
mkdir -p "$LAB6_WS/src"
if [ ! -d "$LAB6_WS/src/opengv" ]; then
  git clone https://github.com/ethz-asl/opengv.git "$LAB6_WS/src/opengv"
fi
git -C "$LAB6_WS/src/opengv" checkout -q "$OPENGV_COMMIT"
# Sturm 二分法在重根/数值不一致时死循环（Nister 5 点偶发卡死），打补丁让它必然终止。
PATCH="$LAB6_DIR/dependencies/opengv_sturm_terminate.patch"
if git -C "$LAB6_WS/src/opengv" apply --check "$PATCH" 2>/dev/null; then
  git -C "$LAB6_WS/src/opengv" apply "$PATCH"
fi
ln -sfn "$LAB6_DIR/lab_6" "$LAB6_WS/src/lab_6"
ln -sfn "$LAB6_DIR/dependencies/eigen_catkin" "$LAB6_WS/src/eigen_catkin"

cd "$LAB6_WS"
if [ ! -f .catkin_tools/profiles/default/config.yaml ]; then
  catkin init >/dev/null
  catkin config --extend "$LAB5_WS/devel" >/dev/null
fi
catkin build -j"$(nproc)" --no-status --cmake-args -DCMAKE_BUILD_TYPE=Release -- "$@"
echo "→ source $LAB6_WS/devel/setup.bash"
