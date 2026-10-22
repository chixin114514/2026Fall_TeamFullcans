# 双目立体校正论文术语锁定表

来源论文：*A compact algorithm for rectification of stereo pairs*（Fusiello, Trucco, Verri, 2000）。本表用于任务 1 全文翻译，先定义的译法优先级最高；后续章节不得在“立体/双目”“投影/重投影”“光心/相机中心”等近义词之间随意切换。

## 1. 统一规则

- `rectification` 统一译为“立体校正”；根据语法可写“校正”，不再交替使用“整流”“校准”。“calibration”另译为“标定”，二者不能混用。
- `stereo` 在 `stereo pair` 中统一译为“双目图像对”，在泛指领域时可译为“双目/立体视觉”；不要把 `stereo` 误译为“立体（3D）模型”。
- `stereo rig` 统一译为“双目系统”；首次出现写“双目系统（stereo rig）”，`calibrated stereo rig` 写“已标定双目系统”，`unconstrained stereo geometry` 写“无约束双目几何”。
- `image plane` 和原文括号同义的 `retinal plane` 统一写“成像平面（图像平面）”；后文简称“成像平面”。原文符号 `\mathcal R` 保持不改。
- `projection` 统一译为“投影”；只有在原文明确出现 `reprojection` 时才译为“重投影”。本论文正文没有 `reprojection`，不要把所有 projection 改成重投影。
- `reconstruction` 统一译为“三维重建”；`triangulation` 统一译为“三角测量”，不要写成“三角剖分”。
- `camera` 统一译为“相机”；`camera matrix` 写“相机矩阵”；不在同一篇译文中混用“摄像机/照相机”。
- 专有名称 `MATLAB`、`QR`、`INRIA-Syntim`、`IEEE`、`CVPR`、`ICCV`、`PPM` 保留英文或原缩写；MATLAB 代码中的标识符不翻译、不改名。
- 本表中的“原文状态”用于防止凭空补充：`fundamental matrix`、`essential matrix`、`disparity`、`reprojection` 不在论文正文中作为术语出现；只能在术语表中备案，不应擅自加入译文内容或公式。

## 2. 核心术语表

| English | 锁定中文 | 缩写/符号 | 首次使用方式与原文位置 |
|---|---|---|---|
| rectification | 立体校正 | — | 标题、摘要和 §1 首次写“立体校正（rectification）”，后文可简称“校正”。 |
| rectifying transformation | 校正变换 | `T_1,T_2` | §4 首次写“校正变换（rectifying transformation）”；左/右图分别用 T1/T2。 |
| stereo pair | 双目图像对 | `I_1,I_2` | 摘要/§5 首次写“双目图像对（stereo pair）”；不要误写为“立体模型”。 |
| stereo rig | 双目系统 | — | 摘要和 §1 首次写“双目系统（stereo rig）”；`calibrated stereo rig` 为“已标定双目系统”。 |
| general, unconstrained stereo rig/geometry | 一般、几何无约束的双目系统/几何 | — | 摘要和 §1；“unconstrained”表示没有额外的相机安装几何约束，不是“无约束优化”。 |
| stereo vision | 双目视觉（或立体视觉） | — | 领域泛称时优先“双目视觉”；关键词 `Stereo` 译为“双目视觉”。 |
| perspective projection | 透视投影 | `\tilde P` | §2.1 首次写“透视投影（perspective projection）”。 |
| perspective projection matrix | 透视投影矩阵 | PPM，`\tilde P` | §2.1 首次写“透视投影矩阵（perspective projection matrix, PPM）”；之后保留 PPM。 |
| rectifying projection matrix | 校正投影矩阵 | `\tilde P_{n1},\tilde P_{n2}` | 摘要和 §3；与原始 PPM `\tilde P_{o1},\tilde P_{o2}` 对照。 |
| camera model | 相机模型 | — | §2 标题/§2.1；“pinhole camera”译为“针孔相机”。 |
| calibrated / calibration | 已标定 / 标定 | — | §1、§3、§6；不要译为“校正”。 |
| intrinsic parameters | 内参数（内参） | `A` | §2.1 首次写“内参数（intrinsic parameters）”；`A` 称“内参矩阵”。 |
| extrinsic parameters | 外参数（外参） | `R,t` | §2.1 首次写“外参数（extrinsic parameters）”；R 为旋转，t 为平移。 |
| camera reference frame | 相机参考系 | — | §2.1；`X/Y/Z axes of the camera reference frame` 译为“相机参考系的 X/Y/Z 轴”。 |
| world reference frame | 世界参考系 | — | §2.1；`w` 的坐标属于任意固定的世界参考系。 |
| optical center | 光心 | `C,C_1,C_2` | §2.1 首次写“光心（optical center）”；不要与“主点”混淆。 |
| retinal plane / image plane | 成像平面（图像平面） | `\mathcal R` | §2.1 首次写“成像平面（retinal plane/image plane）”；后文统一“成像平面”。 |
| optical axis | 光轴 | — | §2.1；光轴与成像平面的交点是主点。 |
| principal point | 主点 | `(u_0,v_0)` | §2.1；是光轴与成像平面的交点，不是光心。 |
| focal length | 焦距 | `f,\alpha_u,\alpha_v` | §2.1；`f` 是毫米单位焦距，`\alpha_u/\alpha_v` 是像素方向焦距。 |
| focal plane | 焦平面 | — | §2.2/§3；是与成像平面平行且经过光心的平面。 |
| baseline | 基线 | `C_1C_2` 或方向 `c_1-c_2` | §2.2 首次写“基线（baseline）”；不要译成“基准线”。 |
| epipolar geometry | 对极几何 | — | 摘要关键词和 §2 标题首次写“对极几何（epipolar geometry）”。 |
| epipolar line | 对极线 | — | §2.2 首次写“对极线（epipolar line）”；不要写成“极线”后再切换。 |
| epipole | 极点 | `E_1,E_2` | §2.2 首次写“极点（epipole）”；图 1 的 E1/E2 是极点，不是 essential matrix 的 E。 |
| epipolar ray / optical ray | 对极射线 / 光线 | `MC`、`Q^{-1}\tilde m` | §2.2 可译“光线”；§2.1 的 `optical ray` 统一为“光线”。 |
| conjugate point / conjugate pair | 共轭点 / 共轭点对 | `M_1,M_2` | §2.2 首次写“共轭点对（conjugate pair）”；指同一 3D 点在两图的投影。 |
| homogeneous coordinates | 齐次坐标 | `\tilde m,\tilde w` | §2.1 首次写“齐次坐标（homogeneous coordinates）”；波浪号必须保留。 |
| Cartesian coordinates | 笛卡尔坐标 | `u,v,w` | §2.1；与“齐次坐标”区分。 |
| QR factorization | QR 分解 | `QR` | §2.1；保留英文大写，不译为“QR 因式分解”以外的算法名称。 |
| rotation matrix | 旋转矩阵 | `R` | §2.1/§3；新相机两者共享同一个 R。 |
| translation vector | 平移向量 | `t` | §2.1；是 PPM 分解中的外参，不能和图像平移操作混淆。 |
| collinearity | 共线性 | `T_1=Q_{n1}Q_{o1}^{-1}` | §4；校正变换是图像平面间的共线变换。 |
| triangulation | 三角测量 | — | §4；`3D reconstruction by triangulation` 译为“通过三角测量进行三维重建”。 |
| bilinear interpolation | 双线性插值 | — | §4；用于校正图像非整数采样位置的灰度计算。 |
| rectified image | 校正图像 | — | 摘要、§4、实验部分；与 `unrectified image` 的“未校正图像”对应。 |
| unrectified image | 未校正图像 | — | Fig. 7/8 图注；不要译成“非校正图像”。 |
| weakly calibrated | 弱标定 | — | §1 相关工作；表示只给出图像点对应关系，不能译成“弱校正”。 |
| image distortion | 图像畸变 | — | §1 相关工作；与校正变换本身区分。 |

## 3. 用户指定但原文正文未使用的术语

这些词需要纳入锁定表以防后续 Worker 自由发挥，但不能因为课程主题相关就把它们加入原文译文。

| English | 锁定中文 | 常用符号 | 原文状态与使用限制 |
|---|---|---|---|
| fundamental matrix | 基础矩阵 | `F` | 论文正文未出现；参考文献/方法中也未定义 F。不得凭空添加 F 公式或声称本文使用基础矩阵。 |
| essential matrix | 本质矩阵 | `E`（通用文献符号） | 论文正文未出现；本文 `E_1,E_2` 已用于极点，翻译时绝不能把极点 E 改称本质矩阵。 |
| disparity | 视差 | `d` | 论文正文没有以该术语展开视差公式；不得擅自加入 `Z=fB/d`，那不是本文给出的公式。 |
| reprojection | 重投影 | — | 论文正文没有 `reprojection`；`projection` 仍译为“投影”，`reconstruction` 译为“三维重建”。 |
| homography | 单应性；homography matrix 为单应矩阵 | `H` | 正文没有定义 H；只在参考文献 Loop & Zhang (1999) 的题名中出现 `rectifying homographies`，可在该书目中译作“校正单应矩阵”，不要为正文补 H 推导。 |

## 4. 符号和上下标锁定

| 符号 | 含义与统一称呼 | 注意事项 |
|---|---|---|
| `W,w,\tilde w` | 世界中的 3D 点、其笛卡尔/齐次坐标 | `W` 是几何点，`w` 是坐标向量；不要都译成“世界坐标”。 |
| `M,m,\tilde m` | 图像点、其二维/齐次坐标 | `M` 是图像点，`m` 是 `[u\ v]^T`；波浪号表示齐次形式。 |
| `C,c` | 光心及其坐标 | `C_1/C_2` 与 `c_1/c_2` 分别是几何点和坐标。 |
| `\tilde P` | 透视投影矩阵（PPM） | 原始/新相机分别使用下标 `o1,o2,n1,n2`。 |
| `A` | 内参矩阵 | `A_1/A_2` 是原相机分解得到的内参；新 PPM 中使用共同的 A。 |
| `R,t` | 旋转矩阵、平移向量 | 公式 (2) 的 `P̃=A[R\mid t]` 与公式 (9) 的新 R 要统一。 |
| `Q,\tilde q` | PPM 的左侧 3×3 块与最后一列 | 不要把 `q` 翻译成“点”；它是矩阵列向量。 |
| `T_1,T_2` | 左/右图像的校正变换 | 不要与相机平移向量 t 混淆。 |
| `r_1,r_2,r_3` | 新相机参考系的 X/Y/Z 轴（世界坐标表达） | 公式 (10) 中按行堆叠；`r_1` 沿基线。 |
| `k` | 任意单位向量 | 算法取旧左相机的 Z 轴单位向量；不要译成核函数或标定参数。 |
| `\lambda,\lambda_o,\lambda_n` | 光线参数 | 保留为希腊字母；不等同于深度 Z 或视差 d。 |
| `u,v` | 图像像素坐标 | `u` 水平，`v` 垂直；`u_0,v_0` 是主点坐标。 |
| `\alpha_u,\alpha_v` | 水平/垂直像素焦距 | 原文定义为 `−f k_u`、`−f k_v`，负号不可省略。 |
| `\gamma` | 斜切因子 | 描述非正交 u–v 轴；建议首次写“斜切因子（skew factor）”。 |
| `P_{o1},P_{o2}` / `P_{n1},P_{n2}` | 原始/校正后的相机矩阵 | 期刊页面公式中带波浪号；代码中无波浪号是 MATLAB 变量写法，语义相同。 |

## 5. 首次出现的建议写法（可直接交给翻译 Worker）

1. 摘要：`本文提出一种适用于一般、几何无约束双目系统的线性立体校正算法。`
2. §1：`给定一对双目图像，立体校正（rectification）为每个图像平面确定一个变换，使共轭对极线变为共线且彼此平行。`
3. §2.1：`相机由光心 C 和成像平面（图像平面）\mathcal R 构成；三维点 W 通过透视投影映射为图像点 M。`
4. §2.1：`相机由透视投影矩阵（perspective projection matrix, PPM）\tilde P 建模。`
5. §2.1：`矩阵 A 仅依赖于内参数（intrinsic parameters），而相机的位置和姿态由外参数（extrinsic parameters）R、t 表示。`
6. §2.2：`两相机形成对极几何（epipolar geometry）；给定左图点 M1，其右图共轭点必须位于对应的对极线（epipolar line）上，所有对极线交于极点（epipole）。`
7. §4：`所得校正变换是由 3×3 矩阵 T1 给出的共线性（collinearity）变换；校正图像的灰度通过双线性插值（bilinear interpolation）计算。`
8. §6：`我们比较从原始图像和校正图像进行三维重建（3D reconstruction）的误差。`

这些建议句只锁定术语和技术关系，不替代各 Worker 对原段落的完整翻译；公式、图注、代码和数字仍以原 PDF 为准。

