# VNAV 2023 Lab4

题目：https://vnav.mit.edu/labs_2023/lab4/exercises.html

## 已完成的交付物

- Deliverable 1–2：`report/deliverables_1_2.pdf`，含全部 QP 推导、最优系数/代价、多段最小 snap 与一般 r 阶条件计数；LaTeX 源码同目录。
- Deliverable 3：Part 0、1.1、1.2、1.3 全部实现，官方 Unity 赛道实际飞行录像 `report/unity_race_submission.mp4` 和 ROS1 数据 `report/unity_race.bag` 已生成。
- 上传链接：`rviz_drone_race.txt`。**两个 Drive 文件目前仅所有者可访问，需要在共享设置中改成“知道链接的任何人 / 查看者”才满足提交要求。**

官方 Unity 实测：12 个门中心按顺序到达，最近距离均小于 0.45 m；参考轨迹时长 91.0797 s，飞行段跟踪 RMS 误差 0.319 m，最大误差 0.578 m；终点继续记录约 30 s，最后位置偏差 0.169 m。详见 `report/unity_summary.json`、`report/unity_tracking.png` 和 `report/unity_final_gate.png`。

最初在线监测设置了 0.08 m 的终点阈值，该检查超时；视频和 bag 包含完整赛道及终点悬停。最终独立检查使用 0.20 m 终点容差，原始失败日志保留在 `report/unity_monitor.txt`，独立检查源码为 `scripts/analyze_unity.py`。门的绿色状态也可在官方录像中看到。未完成可选的最快前三名挑战。

当前工作目录是用户指定的 `Lab4`；课程手册约定提交目录名为小写 `lab4`，正式提交时应按课程要求命名。尚未执行 Git commit 或 push。

## 实现说明

`planner_pkg/src/simple_traj_planner.cpp` 取首门位置/姿态，持续发布零速度、零加速度悬停参考，并广播 `world → desired_pose`。

`trajectory_generation_pkg/src/trajectory_generation_node.cpp` 等待有效当前位置；建立三维位置与一维 yaw 顶点，逐段展开 yaw，使用相同分段时间独立求解两个最小 snap 轨迹；起终点导数固定为零；按经过的 ROS 时间采样并持续保持终点。空消息、非法数据、重复航点、零距离段及批量推进仿真时间均有处理。

旧模板的外部 Eigen/glog/yaml/nlopt 下载包装改为 Ubuntu 系统库，附带所需 `mav_msgs` 和优化库源码。桥接器修复 Python3 shebang、执行权限与 ARM64 上 OpenCV 导入顺序。Lab3 控制器从相邻 `../lab3/controller_pkg` 复用，未改动其源文件。

## 当前 Docker 中运行

已经在容器 `ros_noetic_lab3` 的 `/workspace/lab4` 配好，catkin 工作空间是 `/tmp/lab4_ws`。宿主机中的修改需要重新复制到容器：

```bash
# 宿主机，在 Lab4 内
./scripts/docker_build.sh
```

容器内的最终工作空间包含七个包，已全部编译通过。Docker 使用独立 ROS master 端口 11316 运行 Unity，11314 用于集成检查，11315 用于独立模型。

```bash
# 宿主机终端 1：启动官方模拟器和 bridge，保持此命令运行
docker exec -it ros_noetic_lab3 bash /workspace/lab4/scripts/start_unity_arm64.sh

# 宿主机终端 2：完整赛道，自动录制视频和 bag
docker exec -it ros_noetic_lab3 bash /workspace/lab4/scripts/run_unity_race.sh
```

运行赛道脚本会覆盖容器中的 `report/unity_race.mp4`、`report/unity_race.bag`、`report/unity_flight.csv`，先备份要保留的试验。输出留在容器中，复制回宿主机：

```bash
docker cp ros_noetic_lab3:/workspace/lab4/report/. ./report/
```

Part 0 可在模拟器和 bridge 已运行时单独启动：

```bash
docker exec -it ros_noetic_lab3 bash -lc '
  source /tmp/lab4_ws/devel/setup.bash
  export ROS_MASTER_URI=http://localhost:11316 ROS_HOSTNAME=localhost
  roslaunch planner_pkg static_point_test.launch simulator_data_directory:=/workspace/lab4/simulator_data
'
```

Unity 窗口在虚拟显示器 `:98`，原始分辨率 960×600。要手动重生，先聚焦窗口再按 `r`；`run_unity_race.sh` 会自动处理。默认使用已验证的低增益 `trajectory_generation_pkg/config/gains_arm64.yaml` 和 `v_max=2, a_max=1`。这些参数仅用于时间估计，不代表严格速度/加速度上界；提高它们需重新验证赛道。

## 新容器复现

```bash
# 宿主机，在 Lab4 内
docker build -t vnav-lab4:noetic .
docker run -it --name ros_noetic_lab4 \
  -v "$PWD":/workspace/lab4 \
  -v "$PWD/../lab3":/workspace/lab3:ro \
  vnav-lab4:noetic

# 容器内
bash /workspace/lab4/scripts/build_workspace.sh
bash /workspace/lab4/scripts/prepare_unity_arm64.sh
bash /workspace/lab4/scripts/start_unity_arm64.sh
```

宿主机 ARM64 上的 x86_64 Unity 无法通过 QEMU 正常启动（崩溃记录在 `report/qemu_runtime.txt`），已验证 Box64 0.3.6 可以运行官方 Unity 2019.3.9f1，包含真实渲染、碰撞和桥接通信。准备脚本下载官方模拟器及 Box64 源码；首次编译需几分钟。不要直接运行 x86_64 二进制，应使用提供的 Box64 启动脚本。

## 验证

```bash
python3 scripts/check_math.py
# 在已准备好的容器内：
bash /workspace/lab4/scripts/run_integration_checks.sh
python3 /workspace/lab4/scripts/analyze_unity.py
```

集成检查覆盖：无状态先收到航点、非法/空航点、重复发布不重启、跨 ±π 的短角度变化、参考速度/加速度与位置差分一致、单个重合航点、终点持续保持、首门持续悬停。构建结果为 `report/build_noetic.txt`，集成检查结果为 `report/integration_checks.txt`。

`report/rigid_body_*` 是另行生成的独立六自由度模型调试记录，明确不属于 Unity；正式交付使用 `unity_*` 文件。该模型结果使用 Lab3 的单位惯量假设与原始控制器增益，不能代替官方仿真结果。

## 源码来源

实验模板与优化库来自 MIT-SPARK/VNAV-labs 的 `VNAV2023` 标签（commit `7d234d8`）；保留优化库 Apache 2.0 许可证及源码版权声明。桥接器、TESSE Python 接口来自现有 Lab3 Docker 环境，保留原始版权/许可证；仅做上述 Noetic 兼容修改。Box64：https://github.com/ptitSeb/box64/tree/v0.3.6 。
