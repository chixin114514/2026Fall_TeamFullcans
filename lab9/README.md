# VNAV 2023 Lab 9 — Visual SLAM: ORB-SLAM3, Kimera-VIO, LDSO

| Deliverable | 交付文件 |
| --- | --- |
| 报告（D1–D7 全部答案、图、表） | [report/lab9_report.pdf](report/lab9_report.pdf) |
| D1 Spy game（个人） | 报告 §1.1（表 1、图 1） |
| D2 位姿图初始化（个人） | 报告 §1.2 |
| D3 ORB-SLAM 模块与错误回环（个人） | 报告 §1.3 |
| D4（选做）LSD-SLAM / 直接法（个人） | 报告 §1.4 |
| D5（选做）路标 SLAM → 纯旋转问题（个人） | 报告 §1.5 |
| D6 不对齐的轨迹对比（团队） | 报告 §2.2（图 2） |
| D6 与真值对齐后的对比 + ATE（团队） | 报告 §2.3（图 3、表 2） |
| D7（选做）LDSO + 三者 Sim(3) 对齐对比 | 报告 §2.4（图 4、表 3） |

结果（`MH_01_easy` 全序列，`evo_ape --align`，SE(3)）：ORB-SLAM3 ATE RMSE **0.039 m**，
Kimera-VIO **0.176 m**；仅对齐首帧时 Kimera 终点漂移 0.62 m（路程的 0.8 %），ORB-SLAM3 为 0.018 m。
D7：LDSO（单目）原始尺度只有真值的 1/1.52；Sim(3) 对齐后 ATE RMSE 为 **0.043 m**（不闭环时 0.049 m，
接受了 16 个闭环）。同样用 Sim(3) 对齐，ORB-SLAM3 为 0.021 m，Kimera 为 0.170 m。

## 复现

前提：镜像 `orbslam:latest`、`kimera:latest` 已构建；数据集在 `~/datasets/vnav/MH_01_easy/mav0`；
已安装 `evo`、`latexmk`/`xelatex`。

一键演示（现场展示画面用，不做评估）：依次弹出 ORB-SLAM3、Kimera-VIO、LDSO 的可视化窗口，
再显示 D6、D7 的 evo 轨迹图（用 `results/` 里已有的轨迹）。每一项开始前暂停，Enter 开始，s 跳过，q 退出；
运行中按 Enter 立即结束当前项、进入下一项，不用等它跑完。演示不会改动 `results/` 和 `output/`。

```bash
scripts/run_demo.sh
```

分步执行：

```bash
cd ~/2026Fall_TeamFullcans/lab9
scripts/run_slam.sh            # 依次跑 ORB-SLAM3、Kimera-VIO（各几分钟，不要并行），
                               # 原始轨迹 -> output/，拷贝到 results/d6/{orbslam,kimera}/
scripts/evaluate.sh            # fix_timestamps.py、真值 data.tum、evo_traj 两张图、evo_ape
python3 scripts/make_figures.py  # results/ -> report/figures/，并写 results/d6/metrics.json
scripts/build_report.sh        # -> report/lab9_report.pdf（中间文件在 .build/）

# D7（选做）：LDSO 编译在仓库外的 ~/vnav-builds/{pangolin,ldso}
scripts/build_ldso.sh          # Pangolin v0.6 装到本地前缀，LDSO master 9b0c48c，源码未改
scripts/run_ldso.sh            # 单目 cam0，整条序列约 16 分钟 -> results/d7/results.txt(.noloop)
scripts/evaluate_d7.sh         # fix_ldso.py 清洗 + evo_traj --align --correct_scale --plot_mode xy + evo_ape
python3 scripts/make_figures.py && scripts/build_report.sh
```

注意事项：

- 容器用 `run_docker_vnav.sh` 启动（会把本容器路径换成 docker 宿主机路径，DISPLAY 默认 `:0`），
  不要用官方的 `run_docker.sh`。
- Kimera 用 `cv::FileStorage` 读 `state_groundtruth_estimate0/sensor.yaml`，要求首行是 `%YAML:1.0`，
  EuRoC 原文件没有这一行，会报 `Cannot open file ... sensor.yaml` 并崩溃。`run_slam.sh` 会用硬链接
  建一份 `~/datasets/vnav/MH_01_easy_kimera`（不额外占空间），只给其中的 yaml 补上这一行，再用
  `run_kimera.sh -p /datasets/MH_01_easy_kimera` 运行。原始数据集和 SLAM 源码都没有改。
- 本容器没有可交互的显示，所以 `evo_traj` 用 `--save_plot` 代替 `--plot`（加 `--plot` 时会卡在
  `plt.show()`）。原始 evo 图在 `results/d6/evo/` 和 `results/d7/evo/`。
- LDSO 写完轨迹后会一直等人手动关闭 Pangolin 窗口，`run_ldso.sh` 会在两个结果文件都写出后自动结束它。
  `NOGUI=1 scripts/run_ldso.sh` 可以不开窗口运行。

## 目录

- `report/`：`lab9_report.tex`（主文件）、`sec_individual.tex`（D1–D5）、`references.bib`、`figures/`、PDF
- `scripts/`：`run_demo.sh`（一键演示）、`run_slam.sh`、`evaluate.sh`、`build_ldso.sh`、`run_ldso.sh`、`fix_ldso.py`、`evaluate_d7.sh`、`make_figures.py`、`build_report.sh`
- `results/d1/`：从题目 spy 图读出的块稀疏模式，以及脚本校验过的答案
- `results/d6/`：两个系统的原始轨迹、TUM 格式轨迹、真值 `data.tum`、evo 输出、`metrics.json`、运行日志
- `results/d7/`：LDSO 原始输出 `results.txt(.noloop)`、清洗后的 `ldso*.txt`、evo 输出、`metrics.json`、运行日志
- `notes/`：过程记录
- 官方文件：`lab9_exercises.md`、`Dockerfile_*`、`run_docker.sh`、`.run_*.sh`、`orb_slam.patch`、
  `fix_timestamps.py`、`params/`；`output/` 是 SLAM 容器的挂载输出目录（已在 gitignore 中忽略）
