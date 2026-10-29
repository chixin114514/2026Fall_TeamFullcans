# 交接：为 VNAV Lab4 写 Ubuntu 20.04 / ROS1 Noetic 的 Dockerfile

读者是接手这项工作的 Claude Code，事先不了解本项目。以下内容截至 2026-10-19，均来自已经跑通的环境；文件路径相对于仓库根目录 `2026Fall_TeamFullcans/`。

## 1. 目标

用一个 Docker 容器替代现在的 PRoot 方案，在其中运行 MIT VNAV Lab4（无人机穿门竞速）的 ROS1 部分：

- 宿主机：Ubuntu 22.04，跑在 WSL2 上（x86_64，RTX 4060）。宿主机上装的是 ROS2 Humble，不能用。
- 课程官方环境：Ubuntu 20.04 + ROS1 Noetic。
- 现状：`/opt/vnav-noetic/bundle/rootfs` 下放着一个 20.04 的根文件系统，用 PRoot 运行（`lab4/scripts/noetic.sh`）。PRoot 靠 ptrace 拦截系统调用，速度慢。
- 目标：用真正的 20.04 容器跑 ROS1，同时保持现有脚本、参数和结果不变。

## 2. 推荐架构（已验证可行的分工）

- **容器里**：ROS1 Noetic、全部 catkin 包、控制器、轨迹节点、`tesse_ros_bridge`、Xvfb、roscore、rosbag、ffmpeg 录屏、xdotool。
- **宿主机上**：Unity 模拟器 `lab4.x86_64`，用 GPU 渲染。GPU 依赖 WSL 的 `/dev/dxg` 和宿主机的 Mesa 23.2.1 D3D12 驱动。这套组合只在宿主机上验证过；20.04 的 Mesa 较旧，没有验证过，所以不要把 Unity 放进容器，除非用户明确要求。
- 两边通过 `--network host` 共用 `localhost`，通过共享的 `/tmp/.X11-unix` 共用显示器 `:98`。

## 3. 起点：仓库里已有的 `lab4/Dockerfile`

它原本是给 ARM64 机器用的（Unity 当时跑在 Box64 下），内容如下：

```dockerfile
FROM ros:noetic-ros-base-focal
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake python3-catkin-tools python3-numpy python3-matplotlib python3-scipy python3-defusedxml python3-pil python3-pip \
    libeigen3-dev libgoogle-glog-dev libyaml-cpp-dev libnlopt-cxx-dev \
    ros-noetic-tf ros-noetic-tf2-eigen ros-noetic-tf2-geometry-msgs \
    ros-noetic-rosgraph-msgs ros-noetic-visualization-msgs ros-noetic-cmake-modules \
    ros-noetic-cv-bridge ros-noetic-ackermann-msgs xvfb xdotool curl unzip \
    libgl1-mesa-dri libxcursor1 libxrandr2 libxi6 libxinerama1 libasound2 \
    libpulse0 libudev1 libgtk2.0-0 libsdl2-2.0-0 libnss3 \
    ffmpeg texlive-latex-base texlive-latex-recommended \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /workspace/lab4
CMD ["bash"]
```

和已跑通的 PRoot 环境（`lab4/scripts/setup_noetic.sh`）相比，它**缺少**：

- `pkg-config`
- `ros-noetic-rviz`、`ros-noetic-rviz-plugin-tutorials`（`lab4/rviz/` 下的 RViz 配置要用 IMU 插件）
- `tesse_interface` Python 包（见第 5 节）
- 工作空间编译（见第 6 节）

`texlive-*` 是编译报告用的，和飞行无关，保留或删除都可以。

PRoot 环境用的镜像固定为 `docker.io/library/ros@sha256:72b8bc59035dc0a5b8e07aae28c16caa84192971d72d207c72ed734fb1d5e97d`（`ros:noetic`，amd64）。需要完全复现时用这个摘要。

## 4. 完整 apt 依赖（已验证）

```
build-essential cmake pkg-config python3-catkin-tools
python3-numpy python3-matplotlib python3-scipy python3-defusedxml python3-pil python3-pip
libeigen3-dev libgoogle-glog-dev libyaml-cpp-dev libnlopt-cxx-dev
ros-noetic-tf ros-noetic-tf2-eigen ros-noetic-tf2-geometry-msgs
ros-noetic-rosgraph-msgs ros-noetic-visualization-msgs ros-noetic-cmake-modules
ros-noetic-cv-bridge ros-noetic-ackermann-msgs
ros-noetic-rviz ros-noetic-rviz-plugin-tutorials
xvfb xdotool curl unzip ffmpeg
```

只有把 Unity 也放进容器时才需要：

```
libgl1-mesa-dri libxcursor1 libxrandr2 libxi6 libxinerama1
libasound2 libpulse0 libudev1 libgtk2.0-0 libsdl2-2.0-0 libnss3
```

`libnlopt-cxx-dev` 是必需的：`mav_trajectory_generation` 的 CMake 里有 `find_library(NLOPT_LIBRARY nlopt REQUIRED)`。

## 5. Python 包

```
python3 -m pip install --no-deps /workspace/lab4/dependencies/tesse_interface
```

`tesse_ros_bridge` 需要导入这个包。它在仓库里，所以只能在源码进入容器之后安装：要么在 Dockerfile 里 `COPY` 源码再安装，要么在容器启动后安装。

## 6. 源码布局和编译

脚本把以下路径**写死**了，容器里必须一致：

| 容器内路径 | 宿主机来源 |
|---|---|
| `/workspace/lab4` | `lab4/` |
| `/workspace/lab3` | `lab3/`（Lab4 复用 `lab3/controller_pkg` 作为控制器） |
| `/tmp/lab4_ws` | catkin 工作空间，由 `lab4/scripts/build_workspace.sh` 创建 |

`build_workspace.sh` 的做法是：在 `/tmp/lab4_ws/src` 下为 7 个包建软链接，然后执行 `catkin build -j2 --no-status --cmake-args -DCMAKE_BUILD_TYPE=Release`。7 个包是：

- `lab4/planner_pkg`、`lab4/trajectory_generation_pkg`
- `lab4/dependencies/{mav_trajectory_generation, mav_msgs, catkin_simple, tesse_ros_bridge}`
- `lab3/controller_pkg`

有一个坑：`run_unity_race.sh`、`run_integration_checks.sh`、`start_unity_x86_64.sh`、`run_rigid_body_validation.sh` 都写死了 `source /tmp/lab4_ws/devel/setup.bash`。如果运行时把宿主机的 `/tmp` 挂进容器，镜像里编好的 `/tmp/lab4_ws` 就会被盖住。只需要挂 `/tmp/.X11-unix`，不要挂整个 `/tmp`；或者在容器启动后再运行 `build_workspace.sh`。另外，软链接指向 `/workspace/...`，所以源码必须先挂载或复制到位，才能编译。

## 7. 运行参数

```bash
docker run -it --name vnav-noetic --network host \
  -v <repo>/lab4:/workspace/lab4 -v <repo>/lab3:/workspace/lab3 \
  -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=:98 \
  <image>
```

固定端口和显示器：

- ROS master：`11316`（比赛和录制）；`11314`（集成测试，由测试脚本自己启动 roscore）。
- 显示器：`:98`，Xvfb `960x600x24`。Unity 窗口名为 `tesse_vnav_scenes`。xdotool 往这个窗口发 `r` 让飞机重生，并点击 (512,570) 关闭开发者控制台；ffmpeg 用 `x11grab` 录 `:98`。
- Unity 和 bridge 之间用 TCP 通信，所以需要 `--network host`。

## 8. 宿主机上的 Unity 和 GPU（容器之外，已就绪）

- 播放器来自 `https://vnav.mit.edu/material/lab4.zip`，解压到 `/tmp/lab4-runtime/lab4/lab4.x86_64`（Unity 2019.3.9f1）。
- GPU 设备：`/dev/dxg`。`lab4/scripts/setup_unity_gpu.sh` 补齐了 `/opt/vnav-gpu/lib/{libd3d12.so, libd3d12core.so}` 和 `/usr/lib/wsl/drivers/nvmdi.inf_amd64_*/libnvwgf2umx.so`（对应 NVIDIA 驱动 591.74，带 SHA256 校验）。
- 启动环境变量：`GALLIUM_DRIVER=d3d12`、`MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA`、`LD_LIBRARY_PATH=/opt/vnav-gpu/lib`；同时取消 `LIBGL_ALWAYS_SOFTWARE`。
- 启动参数：`-screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile <路径>`。
- 验证：`glxinfo -B` 显示 `OpenGL renderer string: D3D12 (NVIDIA GeForce RTX 4060)`，Unity 日志中有 `Renderer: D3D12 (NVIDIA`。

## 9. 需要改的脚本

- `lab4/scripts/noetic.sh`、`noetic_env.bash`、`setup_noetic.sh`：PRoot 专用。容器方案里不用它们，可以保留，作为没有 Docker 时的备用方案。
- `lab4/scripts/start_unity_gpu.sh`：需要改造。它在宿主机上启动 Unity 并检查 GPU，这部分保留；但 Xvfb、`roscore -p 11316`、bridge（`roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true`），以及开始时的 xdotool 操作，都是通过 `noetic.sh` 在 PRoot 里启动的（函数 `guest_service` 和几处 `bash noetic.sh ...` 调用）。要把这些改成在容器里启动，例如 `docker exec -d vnav-noetic ...`，或者由容器的入口脚本负责启动。启动顺序：Xvfb 和 roscore → Unity 在宿主机上启动，等窗口出现 → bridge → 等到 `/current_state` 有数据。
- `lab4/scripts/start_unity_x86_64.sh`：另一种方案，把 Xvfb、roscore、Unity 和 bridge 全部放在同一个环境里，但用的是软件渲染（`LIBGL_ALWAYS_SOFTWARE=1`，只有 2–3 fps）。这个脚本在容器里可以直接使用（需要第 4 节里的 Unity 运行库），适合用来验证容器本身，不适合正式录像。
- 以下脚本不用改，直接在容器里运行：`run_unity_race.sh`、`monitor_unity.py`、`rebuild_flight_csv.py`、`run_integration_checks.sh`、`build_workspace.sh`。
- `run_unity_race.sh` 用 `pgrep -f 'lab4\.x86_64'` 查找 Unity 进程号，用来判断这个 Unity 会话是否已经飞过（飞过之后门已经变绿）。如果 Unity 在宿主机上，容器默认看不到宿主机进程，这个检查会报错 "Unity player is not running"。解决办法有两个：加 `--pid host`；或者把这个检查改成别的方式，例如由宿主机写入一个标记文件。

## 10. 验收步骤（都通过才算完成）

1. 在容器里运行 `bash /workspace/lab4/scripts/build_workspace.sh`，输出 `Failed: No packages failed.`。
2. 运行 `bash /workspace/lab4/scripts/run_integration_checks.sh`，输出三行 PASS（empty input…、invalid waypoint…、first-gate hover…）。不需要 Unity。
3. 在宿主机上启动 Unity，在容器里启动 Xvfb、roscore 和 bridge 后，`rostopic echo -n 1 /current_state` 能收到数据。
4. **全新启动的 Unity** 上运行 `bash scripts/run_unity_race.sh`，`monitor.log` 末行是 `complete=True`。和当前交付结果 `lab4/report/runs/unity-gpu-smooth-gates-20261019/unity_summary.json` 对比，应接近：轨迹时长 18.91 s，12 个门按顺序通过且门中心最大距离约 0.074 m，跟踪 RMS 约 0.061 m（先用 `scripts/rebuild_flight_csv.py <run 目录>` 从 bag 重建 CSV），终点误差 < 0.02 m，碰撞只有起飞时的 `Floor_01`。

## 11. 不要改动的东西

- 默认参数已经调好：`lab4/trajectory_generation_pkg/config/gains_gpu.yaml`（kx 14, kv 6, kr 12, komega 2.2），`v_max 8`、`a_max 6`、`a_z_max 5`、`corridor 0.5`。默认值写在 `traj_following.launch` 和 `run_unity_race.sh` 里。
- 轨迹节点通过 `synced_state` 话题与控制器同步，launch 文件里把控制器的 `current_state` 重映射到了这个话题。这是消除抖动的关键，不要去掉。
- 已有的录像和数据在 `lab4/report/runs/`，不要覆盖。`run_unity_race.sh` 每次都会新建一个输出目录。
- 不要修改 `lab3/controller_pkg` 的代码，它也是 Lab3 的交付物。
