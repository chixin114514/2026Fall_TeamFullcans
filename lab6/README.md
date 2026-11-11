# VNAV Lab 6 — Two-view geometry and motion estimation

| Deliverable | 交付文件 |
| --- | --- |
| 报告（D1–D5 全部答案、图、表） | [report/lab6_report.pdf](report/lab6_report.pdf) |
| D1 Nister 5 点算法：步骤、退化、RANSAC 迭代次数（个人） | 报告 §1.1（表 1） |
| D2 已知旋转的 2 点最小求解器 + RANSAC 伪代码（个人，含选做） | 报告 §1.2（算法 1） |
| D3 关键点标定（`calibrateKeypoints`） | 报告 §2.1；代码 `lab_6/src/pose_estimation.cpp` |
| D4 5 点 / 8 点 / 2 点 + RANSAC，RPE 曲线，位姿发布（含选做：无 RANSAC 的 5 点） | 报告 §2.2（图 1、2，表 2）；选做无 RANSAC 对比 §2.4（图 4） |
| D5 Arun 3 点 + RANSAC（3D–3D） | 报告 §2.3（图 3，表 2）；与其他方法对比见 §2.4（图 4） |

代码：`lab_6/`（官方包 `lab_6`，所有 TODO 已实现）。

## 复现

环境：Ubuntu 20.04 + ROS Noetic，lab5 工作空间已编译（`lab5/scripts/build_workspace.sh`）。
数据：课程更新后的数据集 `vnav-lab6-office`（ROS2），用 rosbags 转成 ROS1，放在
`~/datasets/vnav/lab6/office.bag`：

```bash
rosbags-convert vnav-lab6-office --dst ~/datasets/vnav/lab6/office.bag \
  --include-topic /tesse/odom --include-topic /tesse/left_cam/rgb/image_raw \
  --include-topic /tesse/depth_cam/mono/image_raw
```

```bash
bash scripts/build_workspace.sh                  # OpenGV（打补丁）+ eigen_catkin 桩包 + lab_6，约 2 分钟
source ~/vnav-builds/lab6_ws/devel/setup.bash

# 交互：RViz 里看 /gt_camera_pose 与 /camera_pose
roslaunch lab_6 video_tracking.launch path_to_dataset:=$HOME/datasets/vnav/lab6/office.bag

# 全部实验（每个方法一个 csv，写到 results/rpe/）与阈值扫描（results/sweep/）
python3 scripts/run_experiments.py --rate 0.5
python3 scripts/run_experiments.py --sweep --rate 0.5
python3 scripts/make_figures.py                  # → report/figures/*.pdf, results/summary.json
bash scripts/build_report.sh                     # → report/lab6_report.pdf
```

`pose_estimator`：0 = 5 点 Nister，1 = 8 点，2 = 2 点（旋转取自真值），3 = Arun。

## 目录

- `lab_6/` 官方包；`dependencies/eigen_catkin` 是导出系统 Eigen 的桩包，
  `dependencies/opengv_sturm_terminate.patch` 修复 OpenGV 求根偶发死循环
- `results/rpe/*.csv` 每帧 RPE；`results/sweep/` 阈值扫描；`notes/` 过程记录
