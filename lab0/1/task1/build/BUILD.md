# task1 骨架构建记录

## 原始材料

- 主来源：`../张正友标定99FlexibleCameraCalibrationByViewingaPlaneFromUnknownOrientations.pdf`
- `pdfinfo` 确认：8 页，Letter 页面，标题为 *Flexible Camera Calibration by Viewing a Plane from Unknown Orientations*，作者为 Zhengyou Zhang。
- 章节结构：1. Motivations；2. Basic Equations（2.1 Notation、2.2 Homography between the model plane and its image、2.3 Constraints on the intrinsic parameters）；3. Solving Camera Calibration（3.1 Closed-form solution、3.2 Maximum likelihood estimation、3.3 Dealing with radial distortion、3.4 Summary）；4. Degenerate Configurations；5. Experimental Results（5.1 Computer Simulations、5.2 Real Data）；6. Conclusion；Appendices A--C；References。

## 基础编译

在 `task1/` 目录执行：

```text
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -jobname=task1 -output-directory=build main.tex
bibtex build/task1
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -jobname=task1 -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -jobname=task1 -output-directory=build main.tex
cp build/task1.pdf task1.pdf
```

## 结果与依赖

- TeX Live：2026；引擎：XeLaTeX；编译结果：成功，骨架 PDF 为 3 页。
- 首次尝试使用 ctex 默认 macOS 字体集时失败，原因是环境中找不到 `STHeiti`。已在唯一全局配置文件 `main.tex` 使用 `fontset=fandol`，改用 TeX Live 自带 CJK 字体后成功。
- 初始的 `10.5pt` 不是 `ctexart` 的有效全局字号选项，已改为 `10pt`。
- 当前未发现缺失宏包；`ctexart`、`amsmath`、`graphicx`、`caption`、`IEEEtran.bst` 等均可用。
- `task1.pdf` 是当前骨架输出；章节占位文本被翻译 worker 替换后需按同一命令重新构建。
