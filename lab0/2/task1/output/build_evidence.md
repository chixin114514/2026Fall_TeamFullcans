# Task 1 集成与编译证据

日期：2026-09-15

## 构建命令

在 `task1/` 目录执行：

```text
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output main.tex
(cd output && BIBINPUTS='.:..:' bibtex main)
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output main.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=output main.tex
cp output/main.pdf final_paper.pdf
```

结果：

- 第 1 次 XeLaTeX：退出码 0
- BibTeX：退出码 0
- 第 2 次 XeLaTeX：退出码 0
- 第 3 次 XeLaTeX：退出码 0
- `task1/final_paper.pdf`：已生成
- `pdfinfo`：15 页，A4，文件大小约 2.3 MB

## 内容与资源检查

- `main.tex` 输入 9 个实际章节文件，且全部存在。
- 正式编号公式环境 13 个，标签连续为 (1)--(13)。
- 图环境 8 个，`figures/fig1.png`--`figures/fig8.png` 全部存在且已嵌入 PDF。
- `references.bib` 含 14 条条目；最终 PDF 中参考文献编号为 [1]--[14]。
- 最终日志无 `undefined control sequence`、未定义引用/交叉引用、缺图、`Float too large` 或 fatal error。

## 渲染检查

使用以下命令渲染全部页面：

```text
pdftoppm -png -r 120 final_paper.pdf output/render/page
```

退出码为 0，共渲染 15 页。逐页抽查渲染结果：中文、公式、代码、8 幅图和参考文献均可见，未发现明显裁切、重叠、黑块或空白异常。

## 集成修复

仅做了影响编译或阅读顺序的最小修复：

1. 在 `main.tex` 加载 `xcolor` 与 `listings`，并设置 MATLAB 代码的最小样式。
2. 将图 7、图 8 缩放至 `0.90\linewidth`，并在实验结果末尾加入 `\clearpage`，保证两幅图出现在结论和参考文献之前。
