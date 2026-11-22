#!/usr/bin/env bash
# Live demo of lab 9: shows each system's GUI on $DISPLAY, one at a time.
# Before each item it waits: Enter = start, s = skip, q = quit.
# While an item is running, Enter stops it and moves on (no need to wait for the end).
#
#   scripts/run_demo.sh
#
# Items: D1 answers -> ORB-SLAM3 (Pangolin) -> Kimera-VIO (OpenCV) -> LDSO (Pangolin)
#        -> D6 evo_traj plots -> D7 evo_traj plot (from the existing results/, nothing recomputed).
# Demo runs never touch results/: a stopped ORB-SLAM3/Kimera run would leave partial files in
# output/, so output/ is backed up before and restored after; LDSO writes into .build/demo/.
set -euo pipefail
LAB=$(cd "$(dirname "$0")/.." && pwd)
cd "$LAB"
export DISPLAY=${DISPLAY:-:0}
DEMO=$LAB/.build/demo
mkdir -p "$DEMO"
DS=$HOME/datasets/vnav

die() { printf '\033[1;31merror: %s\033[0m\n' "$*" >&2; exit 1; }
[[ -r /dev/tty ]] && { : </dev/tty; } 2>/dev/null || die "needs an interactive terminal"
[[ -S /tmp/.X11-unix/X${DISPLAY#:} ]] || die "X socket /tmp/.X11-unix/X${DISPLAY#:} missing (DISPLAY=$DISPLAY)"

N=0
# item TITLE DESCRIPTION... ; returns 0 = start, 1 = skip
item() {
  local title=$1; shift
  N=$((N + 1))
  printf '\n\033[1;36m━━━ [%d] %s ━━━\033[0m\n' "$N" "$title"
  local l; for l in "$@"; do echo "    $l"; done
  local ans
  read -r -p $'\033[1;33m    Enter 开始 / s 跳过 / q 退出 > \033[0m' ans </dev/tty || ans=q
  case $ans in
    q|Q) echo "退出。"; exit 0 ;;
    s|S) echo "    （跳过）"; return 1 ;;
  esac
}

# show LOG CLEANUP CMD... : run CMD in the background (own process group) and return when the
# user presses Enter or the program ends by itself; then run CLEANUP to stop it.
show() {
  local log=$1 cleanup=$2; shift 2
  setsid "$@" </dev/null >"$log" 2>&1 &
  local pid=$!
  CUR=$pid
  printf '\033[1;32m    运行中（日志 %s），按 Enter 结束并进入下一项\033[0m\n' "${log#$LAB/}"
  while kill -0 "$pid" 2>/dev/null; do
    if read -r -t 1 _ </dev/tty; then break; fi
  done
  if kill -0 "$pid" 2>/dev/null; then
    eval "$cleanup"
    kill -TERM -- "-$pid" 2>/dev/null || true
    sleep 1; kill -KILL -- "-$pid" 2>/dev/null || true
    echo "    已停止。"
  else
    echo "    程序已自行结束。"
  fi
  wait "$pid" 2>/dev/null || true
  CUR=
}

# output/ is the SLAM containers' mount; keep the full-run files safe from a stopped demo run
backup_output()  { rm -rf "$DEMO/output.bak"; cp -a output "$DEMO/output.bak"; }
restore_output() { rm -rf output; mv "$DEMO/output.bak" output; }
need_free() {  # 15 GB RAM: never two SLAM systems at once
  local busy
  busy=$(docker ps --filter 'name=^lab9-' --format '{{.Names}}'; pgrep -x run_dso_euroc || true)
  [[ -z $busy ]] || die "another SLAM system is still running: $(echo $busy)"
}
need_image() { docker image inspect "$1" >/dev/null 2>&1 || die "docker image $1 missing (do not rebuild, ask)"; }
# on exit (also Ctrl-C): stop whatever is still running and put output/ back
CUR=
cleanup_all() {
  [[ -n $CUR ]] && kill -KILL -- "-$CUR" 2>/dev/null
  docker rm -f lab9-orbslam lab9-kimera >/dev/null 2>&1
  [[ -d $DEMO/output.bak ]] && restore_output
  return 0
}
trap cleanup_all EXIT
trap 'exit 130' INT TERM HUP

printf '\033[1mLab 9 演示\033[0m  DISPLAY=%s  数据集 EuRoC MH_01_easy\n' "$DISPLAY"
echo "每一项开始前暂停（Enter 开始，s 跳过，q 退出）；运行中按 Enter 直接结束当前项。"

# ---------------------------------------------------------------- D1
if item "D1 Spy game（个人）" "从题目 spy 图读出的块稀疏模式，脚本做符号消元得到的答案（报告 §1.1）。"; then
  python3 - <<'EOF'
import json
a = json.load(open("results/d1/answers.json"))
print(f"    位姿数 {a['poses']}，路标数 {a['landmarks']}")
print("    每个位姿看到的路标数：", ", ".join(f"{k}={v}" for k, v in a["landmarks_per_pose"].items()))
print("    观测到 l2 的位姿：", ", ".join(a["observers_of_l2"]))
print("    边缘化后不产生 fill-in 的变量：", ", ".join(a["no_fill_in_variables"]))
EOF
fi

# ---------------------------------------------------------------- SLAM GUIs
if item "D6 ORB-SLAM3（双目 + IMU）" "docker orbslam:latest，Pangolin 窗口显示特征点、关键帧和地图点。"; then
  need_image orbslam:latest; need_free; backup_output
  show "$DEMO/orbslam.log" "docker rm -f lab9-orbslam >/dev/null 2>&1" ./run_docker_vnav.sh orbslam:latest
  restore_output
fi
if item "D6 Kimera-VIO（双目 + IMU）" "docker kimera:latest，OpenCV 窗口显示特征跟踪和 3D 轨迹。"; then
  need_image kimera:latest; need_free
  [[ -d $DS/MH_01_easy_kimera ]] || die "missing $DS/MH_01_easy_kimera: run scripts/run_slam.sh kimera once"
  backup_output
  show "$DEMO/kimera.log" "docker rm -f lab9-kimera >/dev/null 2>&1" \
    ./run_docker_vnav.sh kimera:latest bash run_kimera.sh -p /datasets/MH_01_easy_kimera
  restore_output
fi
if item "D7 LDSO（单目 cam0，带闭环）" "Pangolin 窗口显示直接法的点云和关键帧，检测到闭环时轨迹会被拉回。"; then
  LDSO=$HOME/vnav-builds/ldso
  [[ -x $LDSO/bin/run_dso_euroc ]] || die "LDSO not built: run scripts/build_ldso.sh"
  need_free
  # LDSO loads ./vocab and ./examples relative to its directory
  show "$DEMO/ldso.log" : env LD_LIBRARY_PATH="$HOME/vnav-builds/pangolin/lib:${LD_LIBRARY_PATH:-}" \
    bash -c "cd '$LDSO' && exec ./bin/run_dso_euroc preset=0 files='$DS/MH_01_easy/mav0/cam0' output='$DEMO/ldso_results.txt'"
fi

# ---------------------------------------------------------------- trajectory plots (existing results)
export MPLBACKEND=QtAgg
D6=results/d6; D7=results/d7
if item "D6 轨迹对比图（evo_traj）" "用 results/d6 里已有的轨迹，先显示不对齐的，再显示与真值 SE(3) 对齐的。"; then
  show "$DEMO/evo_d6_unaligned.log" : \
    evo_traj tum $D6/kimera/kimera.txt $D6/orbslam/orb_slam3.txt --plot --plot_mode xyz
  show "$DEMO/evo_d6_aligned.log" : \
    evo_traj tum $D6/kimera/kimera.txt $D6/orbslam/orb_slam3.txt --ref $D6/data.tum --align --plot --plot_mode xyz
fi
if item "D7 三系统 Sim(3) 对齐图（evo_traj）" "Kimera、ORB-SLAM3、LDSO 与真值做 Sim(3) 对齐（修正尺度），x-y 平面。"; then
  show "$DEMO/evo_d7.log" : \
    evo_traj tum $D6/kimera/kimera.txt $D6/orbslam/orb_slam3.txt $D7/ldso.txt --ref $D6/data.tum \
      --align --correct_scale --plot --plot_mode xy
fi
echo; echo "演示结束。"
