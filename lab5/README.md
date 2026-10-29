# VNAV 2023 Lab 5 — Feature tracking and matching

| Deliverable | 交付文件 |
| --- | --- |
| 报告（D1–D8 全部答案、表格、图） | [report/lab5_report.pdf](report/lab5_report.pdf) |
| D1 球体透视投影（个人） | 报告 §1.1 |
| D2 消失点（个人） | 报告 §1.2 |
| D3 SIFT 关键点与描述子 | 报告 §2.2 |
| D4 FLANN 匹配 + ratio test | 报告 §2.3 |
| D5 内点/外点与 SIFT 统计表 | 报告 §2.4（表 1） |
| D6a 图像对：SIFT / SURF / ORB / FAST+BRIEF | 报告 §2.5（表 1、2） |
| D6b 两个数据集上的平均统计 + 结论 | 报告 §2.6（表 3–5）；[video/d6_sift_tracking_30fps.mp4](video/d6_sift_tracking_30fps.mp4)、[video/d6_sift_tracking_smooth.mp4](video/d6_sift_tracking_smooth.mp4) |
| D7 Harris + LK tracker | 报告 §2.7（表 3–4 最后一列）；[video/d7_lk_tracking_30fps.mp4](video/d7_lk_tracking_30fps.mp4)、[video/d7_lk_tracking_smooth.mp4](video/d7_lk_tracking_smooth.mp4) |
| D8（选做）Farneback 稠密光流 | 报告 §2.8；[video/d8_farneback_flow_30fps.mp4](video/d8_farneback_flow_30fps.mp4)、[video/d8_farneback_flow_smooth.mp4](video/d8_farneback_flow_smooth.mp4) |

代码：`feature_tracking/`（官方包 `lab_5`，所有 `FILL IN HERE` 都已实现）。
视频里 SIFT 用默认参数、LK 用 500 个角点；表格用的是内点最多的参数（报告表 5）。

## 复现

环境：Ubuntu 20.04 + ROS Noetic。数据集放在 `~/datasets/vnav/lab5/`
（`30fps_424x240_2018-10-01-18-35-06.bag`、`vnav-lab5-smooth-trajectory.bag`，
来自 [VNAV-lab-data](https://github.com/MIT-SPARK/VNAV-lab-data) 的 Dropbox，只能整包下载 7.2 GB zip）。

```bash
bash scripts/build_workspace.sh                 # 编译 opencv3_catkin（OpenCV 3.4.2+contrib，约 4 分钟）和 lab_5
source ~/vnav-builds/lab5_ws/devel/setup.bash
roscore &

# 交互查看（按任意键进入下一张图）
roslaunch lab_5 two_frames_tracking.launch descriptor:=SIFT     # SIFT / SURF / ORB / FAST
roslaunch lab_5 video_tracking.launch descriptor:=LK path_to_dataset:=$HOME/datasets/vnav/lab5/30fps_424x240_2018-10-01-18-35-06.bag
roslaunch lab_5 self_flow.launch path_to_dataset:=$HOME/datasets/vnav/lab5/30fps_424x240_2018-10-01-18-35-06.bag

# 生成报告里的全部数据、图、视频和 PDF（无窗口）
python3 scripts/run_experiments.py pair                          # D3–D6a → results/d6a_pair/
python3 scripts/run_experiments.py video --frames-for SIFT LK    # D6b/D7 → results/d6b_video/（约 35 分钟）
bash scripts/run_flow.sh 30fps && bash scripts/run_flow.sh smooth  # D8
python3 scripts/make_figures.py                                  # → report/figures/，并打印表格行
bash scripts/make_videos.sh                                      # → video/
bash scripts/build_report.sh                                     # → report/lab5_report.pdf
```

视频帧导出到仓库外的 `~/vnav-builds/lab5_frames/`，不提交。

## 目录

- `feature_tracking/` — `lab_5` 包：`src/*_feature_tracker.cpp`、`lk_feature_tracker.cpp`、`self_flow.cpp`、`track_features.cpp`
- `dependencies/` — `opencv3_catkin`（关掉了 python/viz/ffmpeg）、`catkin_simple`；glog/gflags 用系统库代替 `glog_catkin`
- `scripts/` — 编译、实验、出图、出视频、编译报告
- `results/` — 每个配置的 `stats.csv`（逐帧统计）、`params.json`、输出图片；`summary.json` 是汇总
- `notes/` — 过程记录（环境问题、踩坑）
