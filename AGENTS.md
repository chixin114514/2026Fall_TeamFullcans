# AGENTS.md — 仓库结构约定

本仓库是 MIT VNAV 课程各个 lab 的作业。从 **lab5** 开始，每个 `labN/` 都按下面的结构组织。
lab0–lab4 保持原样，不需要迁移。

## 核心要求

1. **只看 `report/` 就够**：tex 源文件、bib、图，以及**最终 PDF**，全部直接放在 `labN/report/` 下，一眼就能找到。
2. **编译产物不进 `report/`**：xelatex/latexmk 的 aux、log、xdv、fls、fdb_latexmk 等中间文件统一输出到 `labN/.build/`，由 gitignore 忽略。
3. **视频单独放一个目录**：`labN/video/` 只放最终交付的 mp4，文件名标明对应哪个 Deliverable。
4. **原始数据和过程记录不进 `report/`**：实验输出放 `results/`，过程笔记、session 记录放 `notes/`。

## 目录结构

```
labN/
├── README.md                  # 入口：第一屏是交付清单表 + 复现命令
├── report/                    # ★ 只放要交的东西，必须保持干净
│   ├── labN_report.tex        #   唯一的 tex 主文件
│   ├── labN_report.pdf        #   ★ 最终 PDF（由构建脚本复制过来）
│   ├── references.bib
│   └── figures/               #   报告引用的图，每张图只留一种格式
├── video/                     # ★ 只放最终交付视频，例如 d6_sift_tracking.mp4
├── bag/                       # ★ 只放作业要求提交的最终 rosbag（没有要求就不建这个目录）
├── <官方 ROS 包>/              # 代码本体，保持官方包名
├── scripts/
│   ├── build_report.sh        #   编译报告，并把 PDF 复制回 report/
│   ├── make_figures.py        #   从 results/ 生成图，写入 report/figures/
│   └── run_*.sh               #   跑实验、录屏
├── results/                   # 运行过程输出（csv/json/log/bag），按 deliverable 或时间戳分子目录；其中的 bag 不提交
├── notes/                     # 过程记录、AI session 记录、草稿
└── .build/                    # xelatex 中间产物（gitignore，不用打开）
```

## 规则

- **`report/` 白名单**：只能有 `*.tex`、`*.bib`、`figures/` 和**唯一一份** `labN_report.pdf`。
  不要在这里放 csv、json、txt 日志、编译记录、多个版本的 PDF 或嵌套的子报告目录。
  - 作业要求的纯文本答案（例如某个 deliverable 的终端输出）写进报告；如果必须单独交文件，
    放在 `report/` 下，命名为 `dN_<内容>.txt`。
- **`video/` 只放最终版**：截图、关键帧放 `report/figures/`（被报告引用的）或 `results/`（其他的）。
  旧版本直接删除，不要留 `_old`、`_full`、`_v2`。命名格式为 `dN_<内容>.mp4`。
- **图由脚本生成**：`scripts/make_figures.py` 从 `results/` 读数据，写入 `report/figures/`。
  不要手动拷贝图片，同一张图也不要同时留 svg、png、pdf 三份。
- **编译报告**只用脚本，不在 `report/` 目录里直接运行 `xelatex`：

  ```bash
  #!/usr/bin/env bash
  # scripts/build_report.sh
  set -euo pipefail
  cd "$(dirname "$0")/../report"
  latexmk -xelatex -interaction=nonstopmode -outdir=../.build/report labN_report.tex
  cp ../.build/report/labN_report.pdf ./labN_report.pdf
  echo "→ report/labN_report.pdf"
  ```

- **报告模板**：从仓库根目录的 `ReportTemplate/template.tex` 复制，作为 `labN_report.tex` 的起点。
  不要把整个 `ReportTemplate/` 拷进 lab 目录。
- **README 第一屏是交付清单表**：每行写 Deliverable 和对应的文件链接，只指向 `report/` 和 `video/` 下的文件。
- **rosbag 分两类**：
  - **运行过程中的 bag**（调参、试飞、中间版本）放在 `results/` 下，由 gitignore 忽略，不提交。
    只提交生成图表所需的 csv/json 摘要。
  - **最终版本的 bag**（作业要求提交的）复制到 `bag/`，命名为 `dN_<内容>.bag`，正常提交，并在 README 的交付清单里列出。
    每个 deliverable 只留一份最终 bag，不要留多个版本。
  - GitHub 单个文件上限 100 MB。最终 bag 超过这个大小时，先用 `rosbag filter` 只保留需要的 topic，
    或者用 `rosbag compress` 压缩；还是太大就改用 Git LFS。
- `*.bag.active` 是录制中断留下的不完整文件，任何情况下都不提交。
- **lab 根目录**只放 `README.md`、`Dockerfile`、官方作业说明，以及上面列出的目录，不要散放其他文件。
