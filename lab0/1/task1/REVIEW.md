# Task 1 Review Worker 检查报告

检查日期：2026-09-15

检查范围：用户提供的原始论文 `张正友标定99FlexibleCameraCalibrationByViewingaPlaneFromUnknownOrientations.pdf`（`pdfinfo`：8 页）与当前 `task1/` 源文件、构建产物。除本报告外未修改 Task 1 或 Task 2 文件。

## 总体验收结论

当前章节源文件已经覆盖原论文摘要、1--6 节、附录 A--C、Figure 1--7、Table 1--2 和 24 条参考文献；逐节对照未发现会改变算法含义的明显漏译、重复或逻辑断裂。公式 (1)--(14) 的主体内容、变量和正文交叉引用已核对，7 个图文件及 2 个表标签均能解析。

当前不能直接提交：项目根路径下的 `task1/task1.pdf` 仍是 3 页骨架占位 PDF；最新构建结果位于 `task1/build/task1.pdf`，为 12 页。完成下面的阻塞项和重要项后，应由 Integration Worker 重新构建并更新提交路径。

## 阻塞

### 1. 提交路径 `task1/task1.pdf` 仍为骨架占位文件

- 证据：`pdfinfo task1/task1.pdf` 显示 `Pages: 3`；`pdftotext -layout task1/task1.pdf -` 仍包含“本节为 LaTeX 项目骨架占位内容，待翻译 worker 按用户提供的原始论文补充。”，摘要、1--6 节及附录均未包含实际译文。
- 对照：当前章节文件（例如 `task1/sections/abstract.tex:1-4`、`task1/sections/motivations.tex:1-17`）已有实际译文；`task1/build/task1.pdf` 及本次临时目录独立构建的 PDF 均为 12 页，且包含实际译文、图表和附录。
- 建议交回：Integration Worker。完成编号/术语修正后，按 `task1/build/BUILD.md:14-18` 的完整 XeLaTeX + BibTeX 流程构建，并将最新 PDF 写入 `task1/task1.pdf`；不要把现有 3 页骨架作为提交文件。

## 重要

### 1. 参考文献编号没有保持原论文的 24 条编号关系

- 文件证据：`task1/main.tex:57-59` 使用 `\nocite{*}`、`IEEEtran`；这会按当前正文首次引用顺序生成编号，而不是按用户原 PDF 的参考文献顺序。
- 已核对的错位示例：原论文 `[1]` Bougnoux 在当前 PDF 中为 `[15]`；原论文 `[2]` Brown 为 `[1]`；原论文 `[3]` Caprile 为 `[16]`；原论文 `[24]` Zhang 技术报告为 `[23]`。当前 citation key 指向的文献实体本身是正确的，问题是正文显示的数字与原论文编号不一致。
- 影响：若要求“保持原论文引用关系/编号”，读者按原论文编号核对时会得到错误对应关系，尤其影响引言、畸变模型和致谢中的引用。
- 建议交回：Integration Worker，保留 `references.bib` 的单一来源，并通过固定原论文顺序的 bibliography 方案（例如在任何正文引用前按原顺序显式 `\nocite{...}`，或使用等价的固定顺序方案）重新构建；重新构建后抽查正文与参考文献编号。

### 2. 正文额外生成了不属于原论文公式序列的 `(15)`

- 文件证据：`task1/sections/experiments.tex:14-24` 将三组仿真姿态写入带编号的 `equation`，并设置了 `eq:simulation-poses`。
- 构建证据：本次独立构建的 `main.aux:81` 将该标签记为 `15`；渲染后的临时构建 PDF 第 5 页在姿态矩阵右侧显示 `(15)`。用户要求核对原论文公式 (1)--(14)，而原 PDF 的该姿态块没有公式编号。
- 影响：产生一个未在正文引用的额外公式编号，破坏与原论文 (1)--(14) 的一一对应，也使后续按论文公式编号核对时产生歧义。
- 建议交回：`experiments.tex` 翻译 Worker 或 Integration Worker，将该姿态块改为不编号的环境并移除该标签；不要修改公式数值或姿态内容。

### 3. 术语表中的 `skew` 与正文有一处不一致

- 文件证据：`task1/terminology.md:14` 规定 `skew -> 倾斜参数`；`task1/sections/basic_equations.tex:24` 和 `task1/sections/calibration_solution.tex:74` 也使用“倾斜参数”，但 `task1/sections/experiments.tex:137` 写成“偏斜参数 c”。
- 影响：同一参数 `c` 在译文中出现两种译法，违反术语统一要求，但不改变数值或算法含义。
- 建议交回：`experiments.tex` 翻译 Worker（必要时由 Terminology Worker 做一次全局检索），将该处统一为“倾斜参数”。

## 可忽略

### 1. 浮动体造成的留白与页眉所示节名滞后

独立构建 PDF 共 12 页，Figure 7 单独位于第 9 页下部，第 9 页上方留白较多；第 2 页页眉显示“3 相机标定求解”但正文仍在第 2 节，第 4 页页眉显示“4 退化配置”但正文仍是第 3.3 节的续页。这些是分页/页眉美观问题，未发现裁切、正文/公式重叠、缺字、黑块或空白页，不影响阅读和提交，不建议为此反复调版式。

## 验证记录

### 内容、公式、图表和引用

- 原 PDF 章节结构核对：摘要、1. Motivations、2. Basic Equations（2.1--2.3）、3. Solving Camera Calibration（3.1--3.4）、4. Degenerate Configurations、5. Experimental Results（5.1--5.2）、6. Conclusion、附录 A--C 均在 `main.tex:48-55` 中按顺序输入。
- 公式标签核对：`eq:pinhole` 至 `eq:complete-maximum-likelihood` 在临时构建 `main.aux` 中依次为 1--14，内容与原 PDF 的公式 (1)--(14) 对照一致；额外的仿真姿态编号见“重要 2”。
- 图表：`task1/figures/` 中 Figure 1--7 文件均存在且可读；`task1/sections/experiments.tex:27-155` 的 7 个 `includegraphics`、7 个 figure label、2 个 table label 均解析成功，图题/表题与原文含义一致。
- 参考文献：`task1/references.bib` 有 24 个条目，临时构建 `main.bbl` 有 24 个 `\\bibitem`；所有正文 citation key 均有对应条目且无未定义 citation。只有编号顺序相对原论文错位，见“重要 1”。

### XeLaTeX + BibTeX 构建

在不覆盖项目文件的临时目录执行完整流程：

```text
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/private/tmp/task1-review-build-20260915 main.tex
BibTeX（在同一临时目录执行，BIBINPUTS 指向 task1/references.bib）
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/private/tmp/task1-review-build-20260915 main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=/private/tmp/task1-review-build-20260915 main.tex
```

结果：`BUILD_OK`，无致命错误；最终 XeLaTeX 日志无 undefined citation/reference、multiply-defined label 或 overfull/underfull 输出；`pdfinfo` 显示独立构建 PDF 为 12 页、A4、1,951,818 bytes。

### PDF 文本与视觉检查

- 已对独立构建 PDF 执行 `pdfinfo`、`pdftotext -layout`、`pdffonts`；未发现替换字符、占位正文、缺失 citation 或缺失图题。
- 已用 Poppler `pdftoppm -png -r 120` 渲染全部 12 页并逐页检查：公式、图、表、参考文献均显示；未发现裁切、重叠、缺字、黑色遮挡或空白页。仅保留上面的分页留白/页眉滞后记录。

