#!/usr/bin/env bash
set -eo pipefail
source /tmp/lab4_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11314 ROS_HOSTNAME=localhost
roscore -p 11314 > /tmp/lab4-integration-master.log 2>&1 & LAB4_MASTER_PID=$!
trap 'kill -INT "$LAB4_MASTER_PID" 2>/dev/null || true; wait "$LAB4_MASTER_PID" 2>/dev/null || true' EXIT
sleep 2
rosparam set /use_sim_time true
python3 /workspace/lab4/scripts/test_trajectory.py
