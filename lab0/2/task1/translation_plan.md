# 《A compact algorithm for rectification of stereo pairs》结构与翻译计划

## 1. 文献识别与完整性核对

- 原文文件：`2000！Acompactalgorithmforrectificationofstereopairs.pdf`。
- 题名：*A compact algorithm for rectification of stereo pairs*。
- 作者：Andrea Fusiello、Emanuele Trucco、Alessandro Verri。
- 期刊信息：*Machine Vision and Applications* (2000) 12: 16–22。
- PDF 核对结果：共 7 个 PDF 页面，对应期刊印刷页 16–22；页面尺寸 595 × 786 pt；未加密；版式为双栏。
- 首页元数据中的 `Title` 是排版/制作信息，不是论文题名；翻译时以首页正文题名为准。
- PDF 文本可选择，但双栏抽取会把左右栏交错；翻译时须按“每页左栏从上到下，再右栏从上到下，随后进入下一页”的自然阅读顺序恢复正文。
- 正式编号公式共 13 条（(1)–(13)）；图共 8 幅（Fig. 1–Fig. 8）；表共 0 个。
- 参考文献共 14 条，全部集中在印刷页 22；正文引用均可在文末找到对应条目。页 19 的脚注是在线 `rectification kit` 地址，不是独立参考文献。
- 原文含致谢和作者简介；不含附录。作者简介是期刊末页的 back matter，不应误并入结论。

### 1.1 首页元数据

| 项目 | 原文信息 | 翻译处理 |
|---|---|---|
| 题名 | A compact algorithm for rectification of stereo pairs | 建议译为“用于双目图像对校正的紧凑算法”；正文统一用“立体校正”指 rectification |
| 作者 | Andrea Fusiello; Emanuele Trucco; Alessandro Verri | 保留英文姓名；作者顺序不变 |
| 第一作者单位 | Dipartimento Scientifico e Tecnologico, Università di Verona, Ca’ Vignal 2, Strada Le Grazie, 37134 Verona, Italy; e-mail: fusiello@sci.univr.it | 地址和邮箱保留；不要臆译专名 |
| 第二作者单位 | Heriot-Watt University, Department of Computing and Electrical Engineering, Edinburgh, UK | 保留机构英文名或给出中文释名并保留英文 |
| 第三作者单位 | INFM, Dipartimento di Informatica e Scienze dell’Informazione, Università di Genova, Genova, Italy | 保留 INFM 缩写和机构英文名 |
| 日期 | Received: 25 February 1999 / Accepted: 2 March 2000 | 译为“收稿：1999 年 2 月 25 日；录用：2000 年 3 月 2 日” |
| 通信作者 | Correspondence to: A. Fusiello | 译为“通信作者：A. Fusiello” |

## 2. 原文结构（自然阅读顺序）

| 顺序 | 原文标题/层级 | PDF 页 / 印刷页 | 内容边界与翻译要点 |
|---:|---|---|---|
| 0 | Abstract | PDF 1 / p.16 | 线性校正算法、一般无约束双目系统、两个原始相机 PPM、22 行 MATLAB 代码、可复现性、校正图像直接三维重建的精度变化。 |
| 0 | Key words | PDF 1 / p.16 | Rectification – Stereo – Epipolar geometry；对应“立体校正—双目/立体视觉—对极几何”。 |
| 1 | **1 Introduction and motivations** | PDF 1–2 / p.16–17 | 校正定义与水平对极线优势；标定假设；相关工作、弱标定对比；本文贡献和在线代码说明。该节跨页、跨栏。 |
| 2 | **2 Camera model and epipolar geometry** | PDF 1–2 / p.16–17 | 先给出透视投影数学背景。 |
| 2.1 | **2.1 Camera model** | PDF 1–2 / p.16–17 | 针孔相机、光心/成像平面/光轴/主点/焦距；齐次坐标；PPM 分解；内参矩阵 A；外参 R、t；相机中心和光线。 |
| 2.2 | **2.2 Epipolar geometry** | PDF 2 / p.17 | 两相机、共轭点、对极线和极点；基线与无穷远极点；校正使对极线平行且水平。 |
| 3 | **3 Rectification of camera matrices** | PDF 2–3 / p.17–18 | 由原始 PPM 构造新 PPM；保持光心、旋转相机使焦平面共面并包含基线；相同内参；新坐标轴 r1、r2、r3；纯前向运动失败条件。 |
| 4 | **4 The rectifying transformation** | PDF 3 / p.18 | 从原始左/右图像平面到新 PPM 的共线变换 T1/T2；光线推导；非整数像素的双线性插值；校正图像直接三角测量。 |
| 5 | **5 Summary of the rectification algorithm** | PDF 3–4 / p.18–19 | 22 行 MATLAB 算法的用途说明、输入 I1/I2 与 Po1/Po2、rectify 输出 T1/T2/Pn1/Pn2；随后给出完整 MATLAB 代码。代码注释可翻译，但 MATLAB 标识符、函数和变量必须保持。 |
| 6 | **6 Experimental results** | PDF 4–6 / p.19–21 | 验证正确性和三维重建精度。 |
| 6.1 | **Correctness.**（原文无编号小标题，段落级小标题） | PDF 4–6 / p.19–21 | 合成数据（近校正与一般几何，Fig. 3–4）；INRIA-Syntim 实拍数据（Sport、Color，Fig. 5–6）；相机矩阵与裁剪说明。 |
| 6.2 | **Accuracy.**（原文无编号小标题，段落级小标题） | PDF 6 / p.21 | 在带噪声图像/标定参数下比较原图与校正图的三维重建，Fig. 7–8；每个绘点为 100 次独立试验平均值。 |
| 7 | **7 Conclusion** | PDF 6–7 / p.21–22 | 总结密集立体匹配简化、算法易理解易使用、解析和实验正确性、校正后重建误差可忽略。 |
| — | **Acknowledgements.**（无编号） | PDF 7 / p.22 | 感谢 Bruno Caprile 和匿名审稿人；British Council-MURST/CRUI 与 EPSRC (GR/L18716) 资助；INRIA-Syntim 提供立体图像。 |
| — | **References** | PDF 7 / p.22 | 14 条完整书目，见本文档第 5 节；不得新增大规模文献。 |
| — | **Author biographies**（期刊 back matter，无标题编号） | PDF 7 / p.22 | Andrea Fusiello、Emanuele Trucco、Alessandro Verri 的作者简介和照片；课程译文可保留为“作者简介”附于文末，也可在正文 PDF 中作为非章节 back matter。 |

原文没有 `Related Work`、`Appendix` 或独立的 `Discussion` 章节。不要为了套模板新建这些章节；`Correctness` 和 `Accuracy` 属于第 6 节内部的原文段落级小标题。

## 3. 图、表与代码索引

### 3.1 图索引

| 编号 | PDF / 印刷页 | 原文图注要点 | 译文保留要求 |
|---:|---|---|---|
| Fig. 1 | PDF 2 / p.17 | *Epipolar geometry.* 第一相机的极点 E 是第二相机光心 C2 的投影，反之亦然。图示 W、M1/M2、C1/C2、E1/E2、R1/R2。 | 译为“对极几何”；保留两相机、光心、像点和极点标注。正文在 2.2 节引用。 |
| Fig. 2 | PDF 3 / p.18 | *Rectified cameras.* 成像平面共面且平行于基线。 | 译为“校正后的相机”；保留两成像平面、C1/C2、M1/M2 与基线关系。正文在第 3 节引用。 |
| Fig. 3 | PDF 4 / p.19 | *Nearly rectified synthetic stereo pair (top) and rectified pair (bottom).* 圆点标记点对应的两图对极线。 | 4 个子图（左/右原图，左/右校正图）及对极线、坐标轴、图注全部保留。 |
| Fig. 4 | PDF 4 / p.19 | *General synthetic stereo pair (top) and rectified pair (bottom).* 一般几何的合成双目图像及对极线。 | 4 个子图和完整图注保留；不要把它与 Fig. 3 合并。 |
| Fig. 5 | PDF 5 / p.20 | “Sport” stereo pair（上）及校正对（下）；右图绘制左图所标点的对极线。 | 4 个实拍子图、`Sport` 名称、右图对极线说明保留。 |
| Fig. 6 | PDF 5 / p.20 | “Color” stereo pair（上）及校正对（下）；右图绘制左图所标点的对极线。 | 4 个实拍子图、`Color` 名称、右图对极线说明保留。 |
| Fig. 7 | PDF 6 / p.21 | 一般合成双目系统中重建误差随图像坐标噪声（左）和标定参数噪声（右）变化；叉号=校正图重建，圆圈=未校正图重建。 | 4 个坐标图、坐标轴和图注保留；不要把“left/right”误译成左右相机，它指两个噪声变量图。 |
| Fig. 8 | PDF 6 / p.21 | 近校正合成双目系统中相同的两类重建误差图；符号含义同 Fig. 7。 | 4 个坐标图和完整图注保留。 |

### 3.2 表索引

原文没有表格（0 个）。第 6 节中的 Po1、Po2、Pn1、Pn2 是显示出来的 3×4 数值矩阵，不是表格；翻译时应使用公式/矩阵环境，不要转换成表格。

### 3.3 MATLAB 代码块

第 5 节给出 `rectify(Po1,Po2)` 与 `art(P)` 两个函数的完整 MATLAB 代码，摘要明确称其为 22 行代码。代码位于 PDF 4 / 印刷页 19，跨左栏底部和右栏上部；须作为一个连续代码块保存。代码中的 `Po1`、`Po2`、`Pn1`、`Pn2`、`T1`、`T2`、`A`、`R`、`c1`、`c2` 等标识符不可汉化或改名。

## 4. 正式编号公式索引

以下是 PDF 中全部 13 条带编号公式；编号、变量、上下标和转置/逆矩阵必须保留。页码同时给出 PDF 页序和期刊印刷页。

| 编号 | PDF / 印刷页 | 公式内容（结构化摘要） | 翻译关注点 |
|---:|---|---|---|
| (1) | PDF 2 / p.17 | 齐次像点与齐次世界点的透视投影：`m̃ ≃ P̃ w̃`。 | `≃` 表示相差一个尺度因子，不能译成严格等号。 |
| (2) | PDF 2 / p.17 | PPM 的 QR 分解：`P̃ = A[R | t]`。 | 竖线表示矩阵拼接；A 为内参矩阵，R/t 为姿态和位移部分。 |
| (3) | PDF 2 / p.17 | 内参矩阵 `A = [[αu, γ, u0], [0, αv, v0], [0, 0, 1]]`。 | `αu, αv, γ, u0, v0` 的符号和矩阵位置不能变。 |
| (4) | PDF 2 / p.17 | PPM 按左侧 3×3 块和最后一列写为 `P̃ = [Q | q̃]`。 | `Q` 与 `q̃` 的维度/列结构要保持。 |
| (5) | PDF 2 / p.17 | 笛卡尔投影坐标：`u=(q1ᵀw+q14)/(q3ᵀw+q34)`，`v=(q2ᵀw+q24)/(q3ᵀw+q34)`。 | 两个分式的分母相同，转置符号和下标不能漏。 |
| (6) | PDF 2 / p.17 | 光心坐标：`c = −Q⁻¹ q̃`。 | 负号和逆矩阵都必须保留。 |
| (7) | PDF 2 / p.17 | PPM 以光心表示：`P̃ = [Q | −Qc]`。 | 不要误写成 `[Q | Qc]`。 |
| (8) | PDF 2 / p.17 | 图像点对应的光线参数式：`w = c + λQ⁻¹m̃, λ∈R`。 | `λ` 是实数参数；这是光线而不是深度视差公式。 |
| (9) | PDF 3 / p.18 | 新 PPM：`P̃n1=A[R | −Rc1]`，`P̃n2=A[R | −Rc2]`。 | 两个新相机共享 A、R，光心 c1/c2 不同。 |
| (10) | PDF 3 / p.18 | 新旋转矩阵按行向量写成 `R=[r1ᵀ; r2ᵀ; r3ᵀ]`。 | `r1,r2,r3` 是相机坐标系 X/Y/Z 轴在世界坐标中的表达。 |
| (11) | PDF 3 / p.18 | 同一 3D 点在原始/新左相机中的投影：`m̃o1≃P̃o1w̃`、`m̃n1≃P̃n1w̃`。 | 两行属于一个带大括号的公式组。 |
| (12) | PDF 3 / p.18 | 校正不移动光心时的两条光线：`w=c1+λoQo1⁻¹m̃o1`、`w=c1+λnQn1⁻¹m̃n1`。 | `λo` 与 `λn` 需区分，两个 Q 也要保留下标。 |
| (13) | PDF 3 / p.18 | 校正变换的齐次像点关系：`m̃n1=λQn1Qo1⁻¹m̃o1, λ∈R`。 | 这是 T1 的共线变换依据，不要改成欧氏坐标等式。 |

### 4.1 未编号但必须保留的数学对象

- PDF 1 / p.16–17：`w=[x y z]ᵀ`、`m=[u v]ᵀ`；齐次坐标 `m̃=[u v 1]ᵀ`、`w̃=[x y z 1]ᵀ`。
- PDF 2 / p.17：`αu=−fku`、`αv=−fkv`；`f` 为毫米焦距，`ku/kv` 为沿 u/v 轴的每毫米有效像素数。
- PDF 3 / p.18：`T1=Qn1Qo1⁻¹`（左图校正变换；右图同理）；新坐标轴约束 `r1=(c1−c2)/||c1−c2||`、`r2=k∧r1`、`r3=r1∧r2`；`k` 取旧左相机 Z 轴单位向量。
- PDF 6 / p.21：四组 3×4 数值矩阵 `Po1`、`Po2`、`Pn1`、`Pn2`；不要漏掉科学计数法和负号。另有 MATLAB 语句 `A(1,3)=A(1,3)+160`，用于把校正图移入 768×576 窗口中心。
- 第 5 节 MATLAB 代码中的 QR 分解、矩阵求逆、叉积和归一化是算法逻辑的一部分；不要把代码逻辑误译成新的数学结论。

## 5. 参考文献完整清单（14 条）

以下按原文出现顺序抄录，供 `references.bib` 使用。作者、年份、期刊/会议、卷期、页码、出版地和 URL 应保持；不需要额外检索或扩充。

1. Ayache N, Lustman F (1991) Trinocular stereo vision for robotics. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 13: 73–85.
2. Caprile B, Torre V (1990) Using vanishing points for camera calibration. *International Journal of Computer Vision* 4: 127–140.
3. Dhond UR, Aggarwal JK (1989) Structure from stereo – a review. *IEEE Transactions on Systems, Man, and Cybernetics* 19(6): 1489–1510.
4. Faugeras O (1993) *Three-Dimensional Computer Vision: A Geometric Viewpoint*. The MIT Press, Cambridge, Mass.
5. Fusiello A, Trucco E, Verri A (1998) Rectification with unconstrained stereo geometry. Research Memorandum RM/98/12, CEE Dept., Heriot-Watt University, Edinburgh, UK. `ftp://ftp.sci.univr.it/pub/Papers/Fusiello/RM-98-12.ps.gz`
6. Hartley R (1999) Theory and practice of projective rectification. *International Journal of Computer Vision* 35(2): 1–16.
7. Hartley R, Gupta R (1993) Computing matched-epipolar projections. In: *CVPR93*, New York, NJ, pp 549–555.
8. Hartley RI, Sturm P (1997) Triangulation. *Computer Vision and Image Understanding* 68(2): 146–157.
9. Isgrò F, Trucco E (1999) Projective rectification without epipolar geometry. In: *CVPR99*, Fort Collins, CO, pp I:94–99.
10. Loop C, Zhang Z (1999) Computing rectifying homographies for stereo vision. In: *CVPR99*, Fort Collins, CO, pp I:125–131.
11. Papadimitriou DV, Dennis TJ (1996) Epipolar line estimation and rectification for stereo images pairs. *IEEE Transactions on Image Processing* 3(4): 672–676.
12. Pollefeys M, Koch R, VanGool L (1999) A simple and efficient rectification method for general motion. In: *ICCV99*, Corfu, Greece, pp 496–501.
13. Robert L (1996) Camera calibration without feature extraction. *Computer Vision, Graphics and Image Processing* 63(2): 314–325.
14. Robert L, Zeller C, Faugeras O, Hébert M (1997) Applications of non-metric vision to some visually guided robotics tasks. In: Aloimonos Y (ed) *Visual Navigation: From Biological Systems to Unmanned Ground Vehicles*, Chap. 5. Lawrence Erlbaum Assoc., pp 89–134.

核对结论：正文中的 `Faugeras (1993)`、`Dhond and Aggarwal (1989)`、`Caprile and Torre (1990)`、`Robert (1996)`、`Ayache and Lustman (1991)`、`Papadimitriou and Dennis (1996)`、`Hartley and Gupta (1993)`、`Robert et al. (1997)`、`Hartley (1999)`、`Loop and Zhang (1999)`、`Isgrò and Trucco (1999)`、`Pollefeys et al. (1999)`、`Fusiello et al. (1998)`、`Hartley and Sturm (1997)` 均有对应条目。正文 p.18 有一次 `Hartey and Sturm (1997)` 的拼写误差，参考文献作者为 `Hartley RI, Sturm P`；翻译时按书目统一为 Hartley，不要复制该拼写错误。

## 6. 推荐的精确 LaTeX 文件拆分

下面的拆分只映射原文已有结构；不得据此新增 `related_work`、`discussion` 或 `appendix`。

| 文件 | 负责内容 | 原文位置 | 备注 |
|---|---|---|---|
| `main.tex` | 文档类、中文/数学/图片/引用宏包、标题作者单位、全局命令、按顺序 `\input{}`、参考文献与 back matter 组织 | 全文 | 不放正文大段文字。建议输入顺序严格遵循下表。 |
| `sections/abstract.tex` | Abstract、Key words | p.16 | 摘要和关键词放在标题/作者信息之后。 |
| `sections/introduction.tex` | §1 Introduction and motivations | p.16–17 | 保留原文引用关系，不拆出虚构的 related work。 |
| `sections/camera_model.tex` | §2.1 Camera model | p.16–17 | 公式 (1)–(8) 和 Fig. 1 的前置定义在此/下一文件按原文位置组织。 |
| `sections/epipolar_geometry.tex` | §2.2 Epipolar geometry | p.17 | Fig. 1 在该小节后或首次引用处插入。 |
| `sections/rectification_camera_matrices.tex` | §3 Rectification of camera matrices | p.17–18 | Fig. 2、公式 (9)–(10)、r1/r2/r3 约束和纯前向运动限制。 |
| `sections/rectifying_transformation.tex` | §4 The rectifying transformation | p.18 | 公式 (11)–(13)、T1/T2、双线性插值和校正图直接三角测量。 |
| `sections/algorithm_summary.tex` | §5 Summary of the rectification algorithm、完整 MATLAB 代码 | p.18–19 | 算法三步摘要和 `rectify`/`art` 代码作为一个连续代码环境。 |
| `sections/experiments.tex` | §6 Experimental results；`Correctness.`；`Accuracy.` | p.19–21 | Fig. 3–8、Po/Pn 矩阵以及全部数值和噪声设置。 |
| `sections/conclusion.tex` | §7 Conclusion | p.21–22 | 只放原结论，不扩写新的讨论。 |
| `sections/acknowledgements.tex` | Acknowledgements | p.22 | 原文存在，作为无编号 back matter。 |
| `references.bib` | 14 条原始参考文献 | p.22 | 以原顺序保留；URL 可转义但不得丢失。 |

若为了减少文件数把 `camera_model.tex` 与 `epipolar_geometry.tex` 合并为 `method.tex`，只能作为等价的机械合并，必须保留 §2.1/§2.2 标题和原文顺序；推荐优先使用上表的精确拆分，便于 Worker T1-D 独立负责第 2–5 节而不与其他章节冲突。

### 6.1 `main.tex` 的推荐输入顺序

```latex
\input{sections/abstract}
\input{sections/introduction}
\input{sections/camera_model}
\input{sections/epipolar_geometry}
\input{sections/rectification_camera_matrices}
\input{sections/rectifying_transformation}
\input{sections/algorithm_summary}
\input{sections/experiments}
\input{sections/conclusion}
\input{sections/acknowledgements}
```

之后再加载 `references.bib`，最后按需要放作者简介。图文件应放入 `figures/`，图注使用中文，但图内标注可在无法低成本重绘时保留英文；正文引用编号必须与 Fig. 1–8 对齐。

## 7. 给后续 Worker 的硬性检查项

1. 不要漏译跨栏/跨页的段落，尤其是 p.16 左栏的 §1、p.17 左栏的 §2.1、p.18 左栏的 §3、p.19 的 MATLAB 代码和 p.21 左栏的相机矩阵。
2. 公式 (1)–(13) 必须全部出现且编号连续；未编号的 `r1/r2/r3` 约束和四组 Po/Pn 数值矩阵也必须保留。
3. 图必须是 8 幅，不要把多子图误计为多幅，也不要漏掉 Fig. 7/8 的“叉号/圆圈”含义。
4. 不要创建表格；四组相机矩阵是矩阵环境。
5. 参考文献必须是 14 条；不要把脚注 URL 当成第 15 条，也不要添加原文没有的文献。
6. 正文保留 `Acknowledgements`；不新增附录或虚构的 `Discussion`。

