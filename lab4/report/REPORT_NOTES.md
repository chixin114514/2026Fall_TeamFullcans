# Lab 4 报告与材料索引

## 2026-10-20 重写

报告 Team work 部分已改用 2026-10-20 重新跑的 Unity + RViz 同步录制（`runs/unity-gpu-rviz-20261020/`，1,489 行遥测，参考轨迹 18.91 s）。正文图：`system_overview`、`gate_headings`、`race_overview`（主图）、`tracking_accuracy`、`attitude_smoothness`、`race_video`，附录 `gate_local_00_05/06_11`；数学部分图不变。`attitude_smoothness` 用 `runs/unity-gpu-fast-20261019/` 作为定时器采样参考的对照。旧的 `unity_trajectory`、`unity_errors`、`unity_3d` 等图文件仍在 `figures/` 中，但正文不再引用。下面各节描述的是旧版本。

运行图脚本需要 numpy、matplotlib、imageio-ffmpeg（用于从视频解帧）。


正文为英文，采用提供的 ReportTemplate 的 A4、12 pt、25 mm 页边距、页眉页脚和章节结构。署名、学号、组号、实验日期、成员分工暂缓填写；正文中的 report date 是报告日期。云端链接由作者自行处理。

## 文件

| 文件 | 用途 |
|---|---|
| `output/pdf/lab4_report.pdf` | 完整英文实验报告 |
| `lab4_report.tex` | 可编辑 LaTeX 源码，含全部数学答案、结果与参考文献 |
| `make_report_figures.py` | 从原始 CSV 和解析多项式生成报告配图 |
| `figures/` | 19 幅绘制/组版图的 PDF、SVG、600 dpi PNG；12 张原视频截图、绘图数据及核对后的指标 |
| `unity_final_gate.png` | 原有 Unity 截图，在报告中完整引用 |

## 要求与证据对应

| 报告内容 | 现有证据 | 核对方式 |
|---|---|---|
| Deliverable 1，全部四题 | `deliverables_1_2.tex`；`../scripts/check_math.py` | 复核 Q、A、b、系数、边界条件、精确有理数代价和 KKT 条件 |
| Deliverable 2，最小 snap 及一般 r | `deliverables_1_2.tex` | 区分显式可行性约束与自然最优性条件，给出分部积分推导 |
| Part 0 | `../planner_pkg/src/simple_traj_planner.cpp`；`unity_hover.txt` | 源码核对持续发布、零导数、首门姿态；原记录只提供单帧位置 |
| Parts 1.1–1.3 | `../trajectory_generation_pkg/src/trajectory_generation_node.cpp` | 核对初始状态、yaw 展开、分段时间、N=10、端点条件和终点保持 |
| 参数与运行环境 | `../trajectory_generation_pkg/config/gains_arm64.yaml`；对应 launch；`runtime_versions.txt` | 按保存的配置与日志描述，不把请求频率当成实际运行频率 |
| 构建及集成检查 | `build_noetic.txt`；`integration_checks.txt` | 引用既有记录，本次未重新构建 ROS 或运行仿真 |
| Unity 轨迹、误差及门距离 | `unity_flight.csv`；`unity_summary.json`；课程门位置 CSV | 对全部 6,064 行检查有限值、时间递增；重算误差及逐门指标并断言与原汇总一致 |
| 截图、录像和 bag | `unity_final_gate.png`；`unity_race_submission.mp4`；`unity_race.bag`；`media_checks.txt` | 截图目视检查；bag 和视频统计引用保存的媒体检查记录；本次未重新解析 bag；已从视频提取并检查 12 张均匀时间采样的完整画面，未逐帧审阅全片 |

## 写作与绘图约定

- 写作路由：manuscript / research / 全文 / zh-to-en（最终正文英文）/ generic。读者是课程阅卷者，主线为数学约束、ROS 实现与真实 Unity 记录的对应关系。
- 使用 nature-writing 组织论证，anti-defensive-writing 控制主张范围，humanizer 清理空泛措辞；课程题目覆盖优先于期刊式新颖性包装。
- 术语统一：minimum snap（位置四阶导数）；reference trajectory（计划参考）；position tracking error（实际位置与记录参考的欧氏距离）；gate-centre distance（到门中心的欧氏距离）；RMS（root mean square）。
- 图 1：系统接口示意；图 2–3：精确解析轨迹及约束消元后的目标函数；图 4：三段最小 snap 的条件分布；图 5：门中心与朝向。
- 图 6–8：平面/高度、三维轨迹及 X/Y/Z 跟踪；图 9–11：整体误差、各轴残差与误差分布；图 12–13：姿态和终点响应。
- 图 14：原有完整截图；图 15–16：原视频的 12 张等间隔截图，按播放时间编排。未裁剪、调色或生成场景。
- 图 17–18：12 个门的完整距离时序；图 19–20：12 个门的局部参考/实际轨迹，统一使用最近时刻前后 2 s 的 201 个样本。
- 绘图后端：沿用已保存的 Python 偏好；所有新图用 Matplotlib 绘制，宽 160 mm 以适配模板；文字为 Arial/sans-serif，最小 8 pt。
- 输出为可编辑文字的 PDF/SVG 和 600 dpi PNG。未生成 TIFF：报告使用矢量 PDF，不存在期刊 TIFF 提交需求。静态验证器无法识别宽度变量，但代码明确设置 `160 / 25.4` 英寸。
- 全部 Unity 行保留。RMS/最大值遵循已有分析的活动区间 `trajectory_time < max(trajectory_time) - 0.01`，使用 4,556 行；终点保持有 1,508 行。没有删除异常值、平滑或重采样。扩展版局部轨迹图按明确标注的 ±2 s 窗口展示，每门 201 行；姿态图使用完整 quaternion 列，原 CSV 完整保留。
- 只有一段飞行记录，不进行跨次试验显著性检验，也不把时间样本当独立重复试验。

## 结果口径

1. 91.0797 s 是参考轨迹时长；121.30 s 是配对遥测记录时长；125 s 是保存的 bag 元数据所记时长。
2. 门 0–11 的全记录最近距离对应时间严格递增；最后一门最近时刻为 100.18 s，发生在终点参考保持期间。最近时刻不是穿越门平面的事件时间。
3. 活动段 RMS 为 0.31912956 m，最大值为 0.57817581 m。终点最后位置偏差为 0.16928689 m；保持期间误差范围为 0.15098272–0.58537230 m。
4. 原监测日志保留失败状态，既有说明将当时阈值记为 0.08 m；离线检查采用 0.20 m。报告没有把单帧达标写成整个保持区间达标。
5. 数学题使用每段至多七次多项式及端点至 jerk 的条件；代码使用 N=10，并固定端点至 snap。报告明确区分两者。
6. 未将独立刚体模型的更小误差混入 Unity 结果。

## 复现本地报告

从 `lab4` 目录运行（依赖 Python 的 NumPy/Matplotlib 和已安装的 TeX Live）：

```bash
MPLCONFIGDIR=/tmp/lab4-matplotlib python3 report/make_report_figures.py
python3 scripts/check_math.py
cd report
mkdir -p tmp/pdfs output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs lab4_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs lab4_report.tex
cp tmp/pdfs/lab4_report.pdf output/pdf/lab4_report.pdf
```

原模板的 `cleveref` 包在本机缺失，报告使用标准 `\ref`；Latin Modern 提供可嵌入的可缩放字体。原始模板和实验记录未覆盖。

## PDF 检查方式

`detect-pdf ReportTemplate/template.pdf --json` 返回 `command not found`。本机同名 `pdf2md` 要求 `<file.pdf> <projectname>`，并非所指定的 pdf-inspector CLI。源文档已有 LaTeX，因此以 `.tex` 为文字依据，使用 Poppler 的 `pdfinfo`、`pdffonts`、`pdftotext`、`pdftoppm` 检查生成 PDF。原模板 PDF 的元数据与源码不一致，因此新报告以模板源码的布局和章节为准。

编译日志、配图静态检查输出及页面预览位于 `tmp/pdfs/`，不属于提交正文。

扩展版最终检查见 `tmp/pdfs/final_checks.txt`：19 页、20 幅编号图、3 张表。新增定量图沿用同一次已有飞行，未补跑仿真。原始模板、实验 CSV、rosbag、录像及既有截图均未覆盖。

## 扩展版配图与分析记录

| 新图文件 | 图的职责与数据来源 |
|---|---|
| `reduced_objectives` | 展示解析消元后的一维目标函数和最优点，属于数学图示 |
| `continuity_map` | 用固定值/显式连续性/自然连续性区分理论约束，不生成虚构轨迹 |
| `gate_headings` | 用课程 CSV 的位置和转换后的四元数绘制 12 个门的位置、yaw 方向 |
| `unity_3d` | 三维观察完整记录；垂直显示比例加大，轴刻度保留真实米制数值 |
| `axis_tracking`、`signed_errors` | 所有行的各轴参考、实际位置及有符号差；按活动段计算轴向 RMS |
| `error_distribution` | 0.025 m 固定宽度的直方图和经验累计分布，分别按活动/保持区间样本数归一化 |
| `recorded_attitude` | 归一化四元数后按 ZYX 转换 roll/pitch/yaw；yaw 时间展开，未假定存在期望姿态数据 |
| `terminal_detail` | 全部 1,508 行保持期数据，时间归零到保持开始；与全记录曲线的关系在图注中说明 |
| `gate_distances_00_05`、`gate_distances_06_11` | 每门保留全程 6,064 个样本，标注各自全局最近距离和时刻 |
| `gate_local_00_05`、`gate_local_06_11` | 每门固定 ±2 s 局部窗口，每门 201 行；横坐标是沿门 yaw 方向的投影，纵坐标为高度偏移；所有显示样本均在坐标范围内 |
| `video_sequence_1`、`video_sequence_2` | 组版 12 张视频全幅截图，播放时间依次为 5、15、…、115 s；视频时间未与遥测对齐 |

所有新图继续使用 Python/Matplotlib，定量图为 quantitative grid 或单幅定量图，条件图为示意图，视频页为 image plate。图宽为 160 mm，最小字号 8 pt；所有图均具有明确的证据或解释职责。

新增指标保存于 `figures/expanded_metrics.json`。X/Y/Z 活动段 RMS 分别为 0.07682194、0.06473549、0.30290491 m，其平方和与三维 RMS 的平方一致，脚本已断言。活动段中位数为 0.28495224 m，95% 分位数为 0.50650694 m。四元数范数范围为 0.9999998863–1.0000001594。

视频帧及来源元数据保存在 `figures/video_frames/`。视频解码使用本机已安装的 FFmpeg，图片组版使用 Python。抽帧命令的形式为：

```bash
ffmpeg -hide_banner -loglevel error -ss 5 -i report/unity_race_submission.mp4 -frames:v 1 frame_01.png
```

其余帧按 `frames.json` 中的 requested playback time 提取。绘图脚本复用已交付的 PNG，不依赖重新安装视频解码库。视频抽帧属于读取已有素材，没有更改原视频速度、颜色或裁剪范围。

配图源检查为 12 PASS、2 WARN、0 FAIL；两项警告仍为未生成 TIFF 和验证器未识别宽度变量，理由见前文。扩展版保留原有数学结论，更新正文中的配图说明及数据解读。

## 紧凑排版修订

保持 20 幅编号图、3 张表及原始实验数据；PDF 从 26 页缩减为 19 页。取消强制分页与独占浮动页，曲线图缩短画布但保留字号，录像和逐门图改为两行三列。图宽仍为 160 mm，绘图字号下限为 8 pt；原始截图以正文宽度的 78% 显示。段间距由 0.5 em 改为 0.3 em，参考文献使用 small 字号。逐页检查完成，单图独占且大面积留白的页面已消除。压紧前的 PDF 留存于 tmp/pdfs/lab4_report_before_compaction.pdf。
