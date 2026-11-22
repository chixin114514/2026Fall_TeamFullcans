#!/bin/bash
# Launch the lab9 SLAM images (orbslam:latest / kimera:latest) from inside the
# vnav-xby container. vnav-xby talks to the WSL host's docker daemon through
# /var/run/docker.sock, so every bind-mount source must be a HOST path:
#   container /root  ==  host $VNAV_HOST_HOME (/srv/vnav2023/homes/xby)
#
# usage: ./run_docker_vnav.sh orbslam:latest|kimera:latest [cmd ...]
#   env: DISPLAY (default :0), LAB9_NET (default robot-exp1_default, same
#        network as vnav-xby so the container is reachable by name)
set -e
IMAGE=${1:?usage: $0 orbslam:latest|kimera:latest [cmd ...]}
shift

HOST_HOME=${VNAV_HOST_HOME:-/srv/vnav2023/homes/xby}
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)
case "$SCRIPT_DIR" in
  /root|/root/*) HOST_LAB_DIR="${HOST_HOME}${SCRIPT_DIR#/root}" ;;
  *)             HOST_LAB_DIR="$SCRIPT_DIR" ;;
esac
HOST_DATASETS="${HOST_HOME}/datasets/vnav"

export DISPLAY=${DISPLAY:-:0}
DISPLAY_NUM=$(echo "$DISPLAY" | sed -E 's/^[^:]*:([0-9]+).*/\1/')
NET=${LAB9_NET:-robot-exp1_default}
NAME="lab9-${IMAGE%%:*}"

mkdir -p "$SCRIPT_DIR/output/orbslam" "$SCRIPT_DIR/output/kimera"
[ -d "$HOME/datasets/vnav/MH_01_easy" ] || [ -d "$HOST_DATASETS/MH_01_easy" ] || \
  echo "WARNING: MH_01_easy not found under ${HOST_DATASETS}" >&2

xhost +si:localuser:root >/dev/null 2>&1 || true
docker rm -f "$NAME" >/dev/null 2>&1 || true

TTY=(); [ -t 0 ] && TTY=(-it)
docker run "${TTY[@]}" \
    --name "$NAME" \
    --network "$NET" \
    -v /tmp/.X11-unix/X${DISPLAY_NUM}:/tmp/.X11-unix/X${DISPLAY_NUM} \
    -v "${HOST_DATASETS}":/datasets:ro \
    -v "${HOST_LAB_DIR}/output":/output:rw \
    -v "${HOST_LAB_DIR}/params":/kimera_params:ro \
    -e DISPLAY \
    "$IMAGE" "$@"
