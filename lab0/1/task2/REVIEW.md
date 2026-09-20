# Task 2 快速独立复验

复验日期：2026-09-19

本次只更新本文件，未修改程序、README、NPZ、报告源文件或 PDF。

## 结论

当前版本的配置、结果文件和报告已统一为真实棋盘格边长 `3.0 cm`。程序默认配置为 `8x5`、`square_size=3.0`，README 明确为 iPhone 15 Pro 后置摄像头和 3 cm 方格，官方 NPZ 和报告均已同步。

没有发现新的阻塞项；Task 2 可提交。报告中的课程标题、姓名、学号和班级仍需提交者自行填写。

## 配置与官方 NPZ

- `task2/calibrate_camera.py:4-5,21-25,77-81`：默认棋盘格为 `8x5`，默认 `square_size=3.0`，单位为 cm，输出 `tvec` 单位为 cm。
- `task2/README.md:8-15,22-28,49-50`：明确记录 18 张 iPhone 15 Pro 后置摄像头 JPEG、8x5 内角点、3 cm 方格和 `--square-size 3.0`。
- `task2/output/camera_params.npz` 是 `task2` 下唯一 NPZ 文件；回读得到 `square_size=3.0`、`checkerboard=[8,5]`、`image_size=[5712,4284]`、18 张候选/18 张有效/0 张失败，平移向量形状为 `18x3x1`。
- 官方 NPZ SHA-256：

```text
7415ebecd6df926e770caaf92e909a47b40b0bf18f50f38e22224e5546ab012f
```

本次未发现旧的 `square_size=1.0`、相对单位或旧 NPZ 输出契约。

## 最小运行复验

使用 `/Users/jiaqiaosu/miniconda3/bin/python`：

| 检查 | 结果 |
| --- | --- |
| `PYTHONPYCACHEPREFIX=/tmp/... python -m py_compile task2/calibrate_camera.py` | 退出码 0 |
| `python task2/calibrate_camera.py --help` | 退出码 0；帮助显示默认 `3.0`，单位 cm |
| 前一轮中文版 XeLaTeX 第一遍/第二遍 | 均退出码 0；第二遍无错误或未定义引用，输出 7 页；当前英文版复验见下 |

前一轮中文版编译临时产物的 `pdfinfo` 为 7 页 A4；`pdftotext` 语义扫描确认没有以下陈旧文本：`square_size=1.0`、`相对单位`、`待确认`、`待实际测量`、`待人工确认`。当前英文版的独立 8 页验收见下文。数字畸变系数中的 `1.045...` 不属于旧尺度文本。

## 报告内容核对

`task2/report/report.pdf` 与最新源文件一致，且包含：

- iPhone 15 Pro 后置摄像头；
- `8×5` 内角点；
- 方格边长 `3 cm`；
- `square_size=3.0`；
- 相机矩阵、五参数畸变系数、OpenCV RMS、逐角点平均误差、逐图 RMS 平均；
- 外参平移向量单位为 cm。

对应源文件位置：`main.tex:43`、`environment.tex:5-6,21-34`、`data_collection.tex:7,13-15,30-42`、`results.tex:3-65`、`analysis.tex:3-4,29-38,54-59`、`conclusion.tex:3-5`。

报告仍说明具体后置镜头焦段和姿态覆盖记录未进一步细分；这不是旧的“前/后置待确认”或 1.0 相对尺度陈述，也不影响本次官方 NPZ 与像素级标定结果验收。

## 提交前剩余动作

只需填写 `task2/report/main.tex:28-35` 的课程作业标题、姓名、学号和课程/班级；其余 Task 2 核心成果可提交。

## English Report Review (2026-09-19)

本次独立检查只读核对英文版 `main.tex`、`sections/*.tex`、`terminology_en.md` 和编译后 PDF；未修改报告、程序或数据。

### Language and structure

- `main.tex`、9 个 `sections/*.tex` 和 `terminology_en.md` 的 CJK 扫描结果为 0；编译后 `pdftotext` 的 CJK 扫描结果也为 0。
- 九章均存在且标题为英文：Objectives、Principles、Experimental Environment、Data Acquisition、Experimental Procedure、Program Design、Experimental Results、Analysis、Conclusion。
- 表格标题/表头、图题、公式相关文字和代码清单标题均为英文；公式、交叉引用和 `Listing 1` 均正常。
- 未发现会改变技术含义的明显误译或语法错误。结果与分析使用了谨慎表述：明确说明后置镜头焦段和详细姿态记录未知，没有把 18/18 检测成功夸大为完整姿态覆盖或通用精度保证。

### Facts and numerical consistency

英文报告与 README、官方 NPZ 及现有采集记录一致：

- Apple iPhone 15 Pro rear camera；18 candidate / 18 valid / 0 failed；image size `5712x4284`；checkerboard `8x5`；square size `3 cm`；translation vectors in cm；
- 完整相机矩阵：
  `[[4082.15290893, 0, 2883.66417823], [0, 4083.58657686, 2107.20293734], [0, 0, 1]]`；
- 五项畸变：`[0.20245123, -0.29420837, -0.00326679, 0.00308671, -1.04554325]`；
- OpenCV RMS `2.06424401` px；mean pointwise reprojection error `1.65696931` px；mean per-image RMS `1.90750642` px。

数值与官方 `task2/output/camera_params.npz` 回读值一致；官方 NPZ SHA-256 为：

```text
7415ebecd6df926e770caaf92e909a47b40b0bf18f50f38e22224e5546ab012f
```

### Independent PDF verification

- 独立 XeLaTeX 第一遍和第二遍均退出码 0；第二遍无错误、未定义引用或致命警告。
- `pdfinfo`：8 页、A4、未加密；`pdftotext` 可读，CJK 数量为 0。
- 8 页 PNG 已全部渲染并目视检查；未发现文字截断、表格/公式越界、图片缺失、重叠或不可读关键内容。第 8 页结论页留白较多，但不影响阅读或提交。

### English review conclusion

英文正文本身未发现阻塞项或重要技术问题；此前发现的 Mermaid 流程图语义阻塞已在本次复验中关闭。剩余身份占位仍需提交前填写。

## Mermaid Workflow Re-review (2026-09-20)

### Source and integration checks

- `task2/report/figures/calibration_workflow.mmd:1-31` 使用标准 `flowchart TD`、节点、判定、带标签箭头和 `<br/>` 文本语法；静态语法检查未发现非法 Mermaid 构造。
- 本机没有 `mmdc`/Mermaid CLI，因此无法执行 Mermaid 原生解析器；`.mmd` 保留为可编辑源，语法结论来自标准语法静态检查。
- `task2/report/sections/procedure.tex:17-24` 的正文引用、英文 caption、`fig:calibration-workflow` label 和 `calibration_workflow.pdf` 路径均正确；独立 XeLaTeX 两遍通过。
- 当前报告最终为 8 页，流程图实际排在第 5 页；第 5 页渲染目视检查显示文字可读、节点和主要箭头未裁切或重叠。

### Previous blocking source/render mismatch (resolved)

`calibration_workflow.mmd:24-30` 的真实程序流程是两个连续判定：

1. `--save-corners?`：Yes 后保存角点覆盖图，再进入第二个 `--undistort?` 判定；No 直接进入第二个判定。
2. `--undistort?`：Yes 保存去畸变图，No 结束。因此两个选项可以同时为 Yes；报告中的实际命令 `program_design.tex:29-33` 也同时传入 `--save-corners --undistort`。

当前重新生成的 `calibration_workflow.pdf` 已显示两个独立菱形：先是 `--save-corners?`，其 Yes 分支进入角点覆盖图并继续进入 `--undistort?`，No 分支也进入第二个判定；第二个判定的 Yes 分支保存去畸变图、No 分支结束。因此 `--save-corners --undistort` 两项同时启用的路径已在图中保留。PDF 文本回读也同时包含两个判定，且 Abort 节点有明确箭头连接到 End。

此前 fallback 的语义阻塞已关闭。当前图件仍未单独画出 `cv2.calibrateCamera` 异常返回分支，但 `.mmd` 原始流程也未声明该异常分支；不影响本次与源文件的一致性验收。

### Facts and language after workflow integration

独立编译后的 PDF CJK 扫描仍为 0；报告关键事实和数值未漂移：iPhone 15 Pro rear camera、18/18、`5712x4284`、`8x5`、3 cm、tvec cm、完整 K、五项畸变、OpenCV RMS `2.06424401`、pointwise mean `1.65696931`、mean per-image RMS `1.90750642` 均保留。

流程图语义阻塞已关闭；除身份占位外，当前英文报告和 Mermaid 图件可提交。
