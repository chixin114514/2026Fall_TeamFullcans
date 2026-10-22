# VNAV 2023 Lab4

题目：https://vnav.mit.edu/labs_2023/lab4/exercises.html

## 原生 Ubuntu 20.04 / ROS1 Noetic（2026-10-20 已验证）

如果系统本身就是 Ubuntu 20.04 并装有 ROS Noetic，就不需要 PRoot 和 `noetic.sh`，全部用原生命令即可。在 WSL2 上，较新的 WSL 已经自带 D3D12 图形库，20.04 自带的 Mesa 21.2.6 可以直接用 RTX 4060 渲染（OpenGL 3.3），也不需要运行 `setup_unity_gpu.sh`。

首次准备：

```bash
sudo apt-get install -y --no-install-recommends python3-scipy xvfb xdotool p7zip-full
python3 -m pip install --no-deps lab4/dependencies/tesse_interface
# 脚本使用固定路径 /workspace/lab4 和 /workspace/lab3，用软链接指向仓库
sudo mkdir -p /workspace
sudo ln -sfn "$PWD/lab4" /workspace/lab4
sudo ln -sfn "$PWD/lab3" /workspace/lab3
bash /workspace/lab4/scripts/build_workspace.sh       # 编译到 /tmp/lab4_ws
bash /workspace/lab4/scripts/run_integration_checks.sh # 三行 PASS
```

其他依赖（编译工具、Eigen、glog、yaml-cpp、NLopt、ROS 消息包、RViz、ffmpeg、mesa-utils）在已验证的环境里已经装好；完整清单见 `DOCKER_HANDOFF.md` 第 4 节。

录制（两个终端，都在 `/workspace/lab4` 下执行）：

```bash
# 终端 1：Xvfb、roscore、GPU Unity、bridge；首次运行会下载 Unity
./scripts/start_unity_gpu.sh
# 终端 2：出现 "GPU rendering verified" 后
LAB4_GPU_SESSION=/tmp/lab4-unity-gpu LAB4_RECORD_FPS=30 bash scripts/run_unity_race.sh
```

`start_unity_gpu.sh` 会自动判断：系统是 20.04 且装有 Noetic 时直接运行 ROS 命令，否则改用 PRoot；GPU 库依次从 `/usr/lib/wsl/lib` 和 `/opt/vnav-gpu/lib` 查找。`run_unity_race.sh` 会同时在 `:96` 上录制 RViz（`rviz/race_gpu.rviz`），设置 `LAB4_RVIZ=0` 可以关闭。原生环境的完整录像在 `report/runs/unity-gpu-native2004-20261020/`，结果与 PRoot 下的交付版本一致：轨迹 18.91 s，门中心最大距离 0.076 m，跟踪 RMS 0.063 m，终点误差 0.014 m。

## Ubuntu 22.04 / x86_64 的 ROS1 环境

宿主机保留 ROS2 Humble；Lab4 使用独立 Ubuntu 20.04 / ROS1 Noetic 文件系统，默认位于 `/opt/vnav-noetic/bundle/rootfs`。通过 PRoot 运行，不需要 Docker daemon 或特权挂载。首次安装：

```bash
sudo bash scripts/setup_noetic.sh
```

日常使用（从 `lab4` 目录执行）：

```bash
# 进入已加载 Noetic 和 Lab4 工作空间的终端
bash scripts/noetic.sh

# 或直接执行 ROS1 命令
bash scripts/noetic.sh rosversion -d
bash scripts/noetic.sh rospack find controller_pkg

# 修改 C++ 后重新编译；运行不依赖 Unity 的集成测试
bash scripts/noetic.sh bash scripts/build_workspace.sh
bash scripts/noetic.sh bash scripts/run_integration_checks.sh
```

启动器把当前 `lab4` 和相邻 `lab3` 映射到环境内的 `/workspace/lab4`、`/workspace/lab3`，修改源码无需复制；构建产物仍位于 `/tmp/lab4_ws`，重启或清理 `/tmp` 后需重新编译。每个需要 ROS1 的终端都使用此启动器，环境变量自动隔离。ROS1 安装本身不下载模拟器，下面的 x86_64 启动脚本会在首次启动时下载官方 Unity。

2026-10-19 已在本机完成七个包的编译、ROS1 发布/订阅、轨迹集成测试、TESSE bridge 导入、已有 rosbag 读取和 RViz 启动验证。RViz 配置所需的 IMU 插件也已安装；验证记录见 `report/ros_noetic_22_04_checks.txt`。

## 轨迹调优：更平滑、更快（2026-10-19，GPU）

最新录像：`report/runs/unity-gpu-smooth-gates-20261019/unity_race.mp4`（30 fps，33.4 s，含起飞和 10 s 终点保持）。这次是全新启动的 Unity：每个门在飞机穿过之前都是红色，穿过后才变绿。同目录有 rosbag、CSV、`unity_summary.json`、使用的增益和 `unity_tracking.png`。`unity-gpu-smooth-20261019` 是同一配置在旧会话里的录像（开场时门已经是绿的），数据几乎一致。

**门的颜色：** Unity 在飞机穿过门时把门变绿，而且不会变回去。按 `r` 重生会保留颜色；用 `scene_change_request` 重新加载场景能让门变红，但会多生成一架无人机、两机相撞，所以不可用。因此每次正式录制都要先重启 `start_unity_gpu.sh`。`run_unity_race.sh` 会按 Unity 进程号记录已经飞过的会话，第二次录制会直接报错提示重启；试跑时可设置 `LAB4_ALLOW_GREEN_GATES=1` 跳过。

两次运行的 CSV 都按同一仿真时间重新对齐参考点后计算：

| 指标 | 原始 `unity-gpu-final` | 上一版 `unity-gpu-fast` | **当前 `unity-gpu-smooth`** |
|---|---|---|---|
| 参考轨迹时长 | 91.08 s | 25.52 s | **18.91 s** |
| 姿态高频抖动（RMS） | — | 0.48° | **0.10°** |
| 最大跟踪误差 | 0.59 m（撞到场景） | 0.17 m | **0.11 m** |
| 跟踪误差 RMS | 0.13 m | 0.076 m | **0.061 m** |
| 门中心最大距离 | 0.200 m | 0.041 m | 0.074 m |
| 终点误差 | 0.112 m | 0.013 m | **0.008 m** |
| 碰撞 | 天花板附近 `Collider_02/03` | 仅起飞时碰地面 | 仅起飞时碰地面 |

为了换取速度和平滑度，门中心精度略有下降，但所有门仍在 7.5 cm 以内。当前版的两次正式录像跟踪 RMS 都是 0.061 m，峰值都是 0.109 m。

当前版的 `unity_flight.csv` 是用 `scripts/rebuild_flight_csv.py` 从 rosbag 重建的：每个状态都和按它自己时间戳采样的参考点配对。在线监测的原始 CSV 另存为 `unity_flight_monitor.csv`，它的参考点对齐有偏差，此前报告的 0.093 m 就是这个偏差造成的。`monitor_unity.py` 已改用众数对齐。上一版和原始版的数值是另一种对齐方式的近似值。

### 抖动的原因与修复

1. **参考点与状态时间不同步（主因）。** Unity 的仿真时钟按 20–80 ms 不均匀跳变，而原先参考点由 100 Hz 定时器按"当前时间"采样，控制器拿到的参考点有约 40% 的时候比状态超前 20–40 ms。以 8 m/s 飞行时，这相当于 0.16–0.32 m 的位置跳变，再被 kx 放大成推力冲击。现在 `trajectory_generation_node` 收到每个状态后，按该状态的时间戳采样参考点（参数 `sync_to_state`，默认 true），然后把该状态转发到 `synced_state`。launch 文件把控制器的 `current_state` 重映射到这个话题，所以控制器拿到的状态和参考点总是一一对应。定时器只在状态中断时作为后备。相同速度、相同增益下，仅这一项就把高频姿态抖动从 0.35° 降到 0.02°。
2. **姿态增益留出裕量。** kr=22 精度略好，但 Unity 步长波动时，急转弯处偶尔会出现 5–12° 的姿态振荡，各次运行表现不一。kr=12、komega=2.2 在多次重复中从未出现这种情况。位置增益用 kx=14、kv=6。kx=18 反而使悬停和跟踪变差。见 `config/gains_gpu.yaml`。
3. **起飞翻转。** 新增竖直加速度上限 `a_z_max`（默认 5 m/s²）。此前起飞段在约 1.5 s 内爬升 2.5 m，并要求在门 0 处竖直速度为零。刹停所需的向下加速度接近 g，而旋翼无法提供，飞机因此倾斜到 84°。

### 提速

- **逐段时间分配**（`fit_limits`）：之前所有分段统一缩放时间，赛道中段只用到 3–4 m/s²，由起点和终点两段决定全局速度。现在每段迭代逼近各自的 |v|、|a|、|a_z| 上限。分段时间不均会改变路径形状，有一次试验在门 2→3 之间向外鼓出 3.8 m 并撞墙。因此加了走廊约束：任一分段偏离其两端连线的距离，比均匀分配时多出 `corridor`（默认 0.5 m）以上，该步就被拒绝并把步长减半。最终取所有合格方案中总时间最短的一个，因此不会比均匀分配更慢。
- **门处竖直速度为零**（`level_gates`）：z 轴单独求解，避免爬升惯性把轨迹带出门的高度。原始轨迹的 0.59 m 峰值误差就是这样撞到天花板附近造成的。

默认值（`run_unity_race.sh`、`traj_following.launch`）：`gains_gpu.yaml`，`v_max=8`、`a_max=6`、`a_z_max=5`、`corridor=0.5`。速度与平滑度的取舍（kx 14 / kr 12，各跑两次）：

| v_max / a_max | 时长 | 姿态高频抖动 | 门中心最大距离 |
|---|---|---|---|
| **8 / 6（默认）** | **18.9 s** | 0.06–0.07° | 0.074 m |
| 9 / 7 | 17.8 s | 0.11–0.12° | 0.089 m |

可以在 `noetic.sh env` 中设置 `LAB4_V_MAX`、`LAB4_A_MAX`、`LAB4_A_Z_MAX`、`LAB4_CORRIDOR`。离线规划耗时可用 `rosrun trajectory_generation trajectory_generation_node` 配合假的里程计查看，日志会打印时长和峰值。软件渲染或 Box64（2–6 fps）请改回 `LAB4_GAINS_FILE=.../gains_arm64.yaml LAB4_V_MAX=2 LAB4_A_MAX=1`。

## RTX 4060 GPU 渲染和新录像（2026-10-19）

最新 GPU 录像为 `report/runs/unity-gpu-final-20261019/unity_race_review.mp4`。Unity 已确认渲染器为 `D3D12 (NVIDIA GeForce RTX 4060)`，OpenGL 检查为 `Accelerated: yes`；画面实测约 90–120 fps，录屏按 30 fps 保存，分辨率 960×600。每次录制仍生成原始视频、rosbag、CSV 和独立日志；不覆盖旧录像。

最终视频 105.567 s，共 3,167 帧。12 个门中心按顺序访问，最近距离均小于 0.200 m；活动段跟踪 RMS 0.1344 m，终点偏差 0.1124 m，终点保持 10.18 s。在线监测及独立 CSV 检查均通过；完整数据见该目录的 `unity_summary.json`。控制器参数沿用原配置，未通过插帧或加速改变播放时序。

本环境虽然有 `/dev/dxg` 和可用的 CUDA，但缺少 Direct3D 及 NVIDIA 的 WSL 图形库。已从官方 WSL 所用的 `Microsoft.Direct3D.Linux` 包和 NVIDIA 591.74 官方包补齐缺项；没有更换宿主机驱动。安装脚本固定匹配本机的 591.74 版本，并对恢复的库作 SHA256 校验。

从 `lab4` 目录执行：

```bash
# 首次配置 GPU 图形库（当前机器已完成）
sudo bash scripts/setup_unity_gpu.sh

# 终端 1：直接在宿主机启动 GPU Unity，ROS1 服务由脚本启动
./scripts/start_unity_gpu.sh

# 终端 2：首个终端显示 GPU rendering verified 后录制
./scripts/noetic.sh env LAB4_GPU_SESSION=/tmp/lab4-unity-gpu \
  LAB4_RECORD_FPS=30 bash scripts/run_unity_race.sh
```

`start_unity_gpu.sh` 使用宿主机 Mesa/D3D12，ROS1 继续运行在独立 Noetic 环境内；启动时同时核验 OpenGL 和 Unity 日志中的硬件渲染器。`LAB4_GPU_SESSION` 会把这次渲染器证据一起保存到录像目录。环境与库来源记录见 `report/gpu_rendering_checks.txt`。

## 此前的 CPU 软件渲染记录（2026-10-19）

此前的软件渲染赛道录像是 `report/runs/unity-native-20261019T0907/unity_race_review.mp4`，同目录保留原始录像、rosbag、CSV、ROS 参数和 `unity_summary.json`。参考轨迹为 91.0797 s，录像约 172.834 s（保留实际屏幕播放时序，未加速或插帧）。软件渲染画面约 2–3 fps，录像文件按 24 fps 采集。

12 个门中心按顺序接近，最近距离均小于 0.381 m。终点保持约 30 s，最后偏差 0.278 m，因此该次运行**没有通过**原监测脚本的 0.20 m 悬停判据；原始失败日志未修改。后续增益和宿主机渲染试跑没有改善稳定性，属于调试记录，不替代这段完整录像。旧的 ARM64 正式交付录像和数据保持不变。

在当前 x86_64 机器复现（两个终端，从 `lab4` 执行）：

```bash
# 终端 1：下载/启动官方 Unity、虚拟显示器和 ROS bridge
./scripts/noetic.sh bash scripts/start_unity_x86_64.sh

# 终端 2：首个终端显示 ready 后，启动轨迹并录制
./scripts/noetic.sh bash scripts/run_unity_race.sh
```

每次录制默认写入新的 `report/runs/unity-<UTC时间>/`，已有视频、bag 和 CSV 不会覆盖。可用 `LAB4_OUTPUT_DIR` 指定新目录、`LAB4_GAINS_FILE` 指定试验参数文件，需放在 `noetic.sh env ...` 的 `env` 参数中。完整实验记录和试跑状态见 `report/runs/README.md`。

## 已完成的交付物

- Deliverable 1–2：`report/deliverables_1_2.pdf`，含全部 QP 推导、最优系数/代价、多段最小 snap 与一般 r 阶条件计数；LaTeX 源码同目录。
- Deliverable 3：Part 0、1.1、1.2、1.3 全部实现。

| 交付项 | 文件 |
| --- | --- |
| Unity 模拟器赛道录像（GPU） | [unity_gpu_race.mp4](report/video/unity_gpu_race.mp4) |
| 同时录制的 RViz 录像（GPU） | [rviz_gpu_race.mp4](report/video/rviz_gpu_race.mp4) |
| 飞行数据、指标和增益 | [report/runs/unity-gpu-rviz-20261020/](report/runs/unity-gpu-rviz-20261020/)（`unity_race.bag`、`unity_flight.csv`、`unity_summary.json`、`gains_used.yaml`） |
| 题目要求的录像说明文件 | [rviz_drone_race.txt](rviz_drone_race.txt) |

两段录像都是 32.1 s、30 fps、正常速度，在同一次飞行中同时录制。Unity 960×600；RViz 1280×800，显示规划轨迹（橙）、实际路径（青）、飞机姿态和 12 个门的朝向（红色箭头）。这次飞行在原生 Ubuntu 20.04 / Noetic 上运行，使用全新启动的 Unity，所以门在穿过前是红色。轨迹 18.91 s；12 个门按顺序通过，门中心最大距离 0.077 m；跟踪 RMS 0.063 m；终点误差 0.017 m；起飞后没有碰撞。

以下为 ARM64 / Box64 环境的原始交付记录。官方 Unity 实测：12 个门中心按顺序到达，最近距离均小于 0.45 m；参考轨迹时长 91.0797 s，飞行段跟踪 RMS 误差 0.319 m，最大误差 0.578 m；终点继续记录约 30 s，最后位置偏差 0.169 m。详见 `report/unity_summary.json`、`report/unity_tracking.png` 和 `report/unity_final_gate.png`。

最初在线监测设置了 0.08 m 的终点阈值，该检查超时；视频和 bag 包含完整赛道及终点悬停。最终独立检查使用 0.20 m 终点容差，原始失败日志保留在 `report/unity_monitor.txt`，独立检查源码为 `scripts/analyze_unity.py`。门的绿色状态也可在官方录像中看到。未完成可选的最快前三名挑战。

当时的录像是 `report/unity_race_submission.mp4` 和 `report/unity_race.bag`。

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

运行赛道脚本默认在容器中的 `report/runs/unity-<UTC时间>/` 新建录像、bag 和 CSV，不再覆盖旧交付物。输出留在容器中，复制回宿主机：

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
