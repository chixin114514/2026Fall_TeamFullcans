#!/usr/bin/env bash
# One-command Lab5 demo. Data and workspace paths follow README.md.
set -eo pipefail

LAB5_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
LAB5_WS=${LAB5_WS:-$HOME/vnav-builds/lab5_ws}
LAB5_DATASETS=${LAB5_DATASETS:-$HOME/datasets/vnav/lab5}
export LAB5_WS
DATASET=30fps
SECONDS_PER_VIDEO=0
SECONDS_PER_IMAGE=0
WINDOW_WIDTH=1600
WINDOW_HEIGHT=900
# Use most of the desktop when its dimensions are available.
if command -v xdotool >/dev/null &&
   read -r desktop_width desktop_height < <(xdotool getdisplaygeometry 2>/dev/null); then
  WINDOW_WIDTH=$((desktop_width * 85 / 100))
  WINDOW_HEIGHT=$((desktop_height * 80 / 100))
fi
SKIP_FLOW=false
FORCE_BUILD=false
DRY_RUN=false
ACTIVE_LAUNCH=

usage() {
  cat <<'EOF'
用法：bash scripts/demo_lab5.sh [选项]

依次展示：SIFT 图像匹配 → ORB 图像匹配 → SIFT 视频 → Harris+LK → Farneback。
每种图像匹配各展示 5 张过程图，按回车关闭当前图片并显示下一张。
视频播放中按回车关闭当前视频并播放下一段，不必等待播完。
可在展示窗口或启动终端按回车；Ctrl+C 结束整个演示。
首次使用会自动编译，需要 Ubuntu 20.04、ROS Noetic 和图形桌面。

选项：
  --dataset 30fps|smooth  选择数据集（默认 30fps）
  --width N              窗口宽度（默认桌面宽度的 85%，无法检测时为 1600）
  --height N             窗口高度（默认桌面高度的 80%，无法检测时为 900）
  --seconds N            可选的视频自动切换秒数；默认 0，仅回车或播放结束时切换
  --image-seconds N      可选的图片自动切换秒数；默认 0，仅回车切换
  --skip-flow            跳过选做 D8
  --build                演示前重新编译
  --dry-run              只打印执行命令，不编译、不启动 ROS
  -h, --help             显示帮助

路径可通过 LAB5_WS、LAB5_DATASETS 环境变量覆盖，参见 README.md。
EOF
}

die() { echo "错误：$*" >&2; exit 1; }

while (($#)); do
  case "$1" in
    --dataset)
      (($# >= 2)) || die "--dataset 缺少参数"
      DATASET=$2; shift 2 ;;
    --seconds)
      (($# >= 2)) || die "--seconds 缺少参数"
      SECONDS_PER_VIDEO=$2; shift 2 ;;
    --image-seconds)
      (($# >= 2)) || die "--image-seconds 缺少参数"
      SECONDS_PER_IMAGE=$2; shift 2 ;;
    --width)
      (($# >= 2)) || die "--width 缺少参数"
      WINDOW_WIDTH=$2; shift 2 ;;
    --height)
      (($# >= 2)) || die "--height 缺少参数"
      WINDOW_HEIGHT=$2; shift 2 ;;
    --skip-flow) SKIP_FLOW=true; shift ;;
    --build) FORCE_BUILD=true; shift ;;
    --dry-run) DRY_RUN=true; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "未知参数：$1（使用 --help 查看帮助）" ;;
  esac
done

[[ "$SECONDS_PER_VIDEO" =~ ^(0|[1-9][0-9]*)$ ]] || die "--seconds 必须为非负整数"
[[ "$SECONDS_PER_IMAGE" =~ ^(0|[1-9][0-9]*)$ ]] || die "--image-seconds 必须为非负整数"
# ROS parameters of type int are signed 32-bit values, in milliseconds.
[[ ${#SECONDS_PER_IMAGE} -le 7 && "$SECONDS_PER_IMAGE" -le 2147483 ]] ||
  die "--image-seconds 过大"
DISPLAY_DELAY_MS=$((SECONDS_PER_IMAGE * 1000))
for dimension in "$WINDOW_WIDTH" "$WINDOW_HEIGHT"; do
  [[ "$dimension" =~ ^[1-9][0-9]*$ && ${#dimension} -le 5 && "$dimension" -le 16384 ]] ||
    die "窗口宽高必须是 1–16384 的正整数"
done
case "$DATASET" in
  30fps)
    BAG="$LAB5_DATASETS/30fps_424x240_2018-10-01-18-35-06.bag"
    IMAGE_TOPIC=/camera/color/image_raw ;;
  smooth)
    BAG="$LAB5_DATASETS/vnav-lab5-smooth-trajectory.bag"
    IMAGE_TOPIC=/tesse/left_cam/rgb/image_raw ;;
  *) die "--dataset 只能是 30fps 或 smooth" ;;
esac

run() {
  printf '\n执行：'
  printf '%q ' "$@"
  printf '\n'
  if ! "$DRY_RUN"; then "$@"; fi
}

stop_video() {
  if [[ -n "$ACTIVE_LAUNCH" ]]; then
    # SIGTERM also works if Enter arrives before roslaunch installs its
    # handlers (background commands initially inherit ignored SIGINT).
    kill -TERM "$ACTIVE_LAUNCH" 2>/dev/null || true
    wait "$ACTIVE_LAUNCH" 2>/dev/null || true
    ACTIVE_LAUNCH=
  fi
}

# Shut down only the launch owned by this script; roslaunch cleans up its nodes.
trap stop_video EXIT
trap 'printf "\n演示已停止。\n"; exit 130' INT
trap 'exit 143' TERM

if ! "$DRY_RUN"; then
  [[ -n "${DISPLAY:-}" ]] || die "没有 DISPLAY，请在图形桌面的终端运行此脚本"
  [[ -f /opt/ros/noetic/setup.bash ]] || die "未找到 ROS Noetic：/opt/ros/noetic/setup.bash"
  [[ -f "$BAG" ]] || die "未找到数据集：$BAG；可设置 LAB5_DATASETS 指向数据目录"
  [[ -t 0 ]] || die "请直接在交互终端运行，以便按回车控制演示"
fi

NEEDS_BUILD=$FORCE_BUILD
if [[ -x "$LAB5_WS/devel/lib/lab_5/track_features" ]]; then
  # Rebuild when this checkout's source changed, including demo display options.
  while IFS= read -r -d '' source_file; do
    if [[ "$source_file" -nt "$LAB5_WS/devel/lib/lab_5/track_features" ]]; then
      NEEDS_BUILD=true
      break
    fi
  done < <(find "$LAB5_DIR/feature_tracking/src" "$LAB5_DIR/feature_tracking/include" \
    -type f \( -name '*.cpp' -o -name '*.h' \) -print0)
fi
if "$NEEDS_BUILD" || [[ ! -f "$LAB5_WS/devel/setup.bash" ]] ||
   [[ ! -x "$LAB5_WS/devel/lib/lab_5/track_features" ]] ||
   [[ ! -x "$LAB5_WS/devel/lib/lab_5/self_flow" ]]; then
  run bash "$LAB5_DIR/scripts/build_workspace.sh"
fi
run source "$LAB5_WS/devel/setup.bash"

if ! "$DRY_RUN"; then
  command -v roslaunch >/dev/null || die "加载工作空间后仍找不到 roslaunch"
  PACKAGE_DIR=$(rospack find lab_5) || die "工作空间中找不到 lab_5，请使用 --build 重试"
  [[ "$(readlink -f "$PACKAGE_DIR")" == "$(readlink -f "$LAB5_DIR/feature_tracking")" ]] ||
    die "lab_5 指向其他目录：$PACKAGE_DIR；请使用 --build 重试"
fi

video() {
  if "$DRY_RUN"; then
    run roslaunch lab_5 "$@" "${DISPLAY_ARGS[@]}"
    echo "（按回车关闭这一段，随后播放下一段）"
    return
  fi
  # Keep rosbag from competing with the script for terminal input.
  roslaunch lab_5 "$@" "${DISPLAY_ARGS[@]}" </dev/null &
  ACTIVE_LAUNCH=$!
  local started=$SECONDS line status=0
  echo ">>> 视频播放中：在视频窗口或本终端按回车，关闭当前视频并进入下一段。"
  while kill -0 "$ACTIVE_LAUNCH" 2>/dev/null; do
    if read -r -t 0.2 line; then
      stop_video
      return
    fi
    if [[ "$SECONDS_PER_VIDEO" != 0 ]] && ((SECONDS - started >= SECONDS_PER_VIDEO)); then
      stop_video
      return
    fi
  done
  wait "$ACTIVE_LAUNCH" || status=$?
  ACTIVE_LAUNCH=
  if [[ "$status" != 0 ]]; then
    die "视频演示启动或运行失败（退出码 $status）"
  fi
}

DISPLAY_ARGS=("window_width:=$WINDOW_WIDTH" "window_height:=$WINDOW_HEIGHT" enter_only:=true)
echo "Lab5 演示：数据集 $DATASET，窗口 ${WINDOW_WIDTH}×${WINDOW_HEIGHT}"
echo "先展示两组静态图，每组 5 张；之后播放三个连续视频。"
echo "在展示窗口或本终端按回车切换，前一个窗口会关闭；Ctrl+C 结束整个演示。"

echo "[1/5 静态图组] D3–D5：SIFT 关键点、匹配与内外点（共 5 张）"
run roslaunch lab_5 two_frames_tracking.launch descriptor:=SIFT "display_delay_ms:=$DISPLAY_DELAY_MS" \
  terminal_enter:=true "${DISPLAY_ARGS[@]}"

echo "[2/5 静态图组] D6a：ORB 图像匹配对比（共 5 张）"
run roslaunch lab_5 two_frames_tracking.launch descriptor:=ORB "display_delay_ms:=$DISPLAY_DELAY_MS" \
  terminal_enter:=true "${DISPLAY_ARGS[@]}"

echo "[3/5 连续视频] D6b：SIFT 视频跟踪"
video video_tracking.launch descriptor:=SIFT "path_to_dataset:=$BAG"

echo "[4/5 连续视频] D7：Harris + Lucas–Kanade 视频跟踪"
video video_tracking.launch descriptor:=LK "path_to_dataset:=$BAG"

if ! "$SKIP_FLOW"; then
  echo "[5/5 连续视频] D8（选做）：Farneback 稠密光流"
  video self_flow.launch "path_to_dataset:=$BAG" "image_topic:=$IMAGE_TOPIC"
fi

echo "演示结束。数学推导和算法统计表请查看 report/lab5_report.pdf。"
