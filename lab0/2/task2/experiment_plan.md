# 任务 2：OpenCV 双目深度估计实验方案

## 结论与状态

**状态：`DONE_WITH_CONCERNS`**

- **所选数据：** OpenCV 官方 `4.x` 仓库 `samples/data` 中的 `aloeL.jpg` 与 `aloeR.jpg`。
- **可以完成：** 左右图读取、StereoSGBM 视差估计、视差可视化，以及由有效视差计算的相对/代理深度图。
- **不能声称完成：** 米制绝对深度或带物理单位的三维点云。该立体对没有在官方样例代码中提供与它明确配套的物理 baseline、焦距、`doffs` 或 `Q` 矩阵。不得把其他样例的标定文件套用到 aloe 图像，也不得把猜测的 `Q` 当成真实标定。
- **依据：** OpenCV 官方 `stereo_match.py` 直接读取 `aloeL.jpg`/`aloeR.jpg` 并计算视差；该示例用 `f = 0.8*w` 作为“guess for focal length”，再构造示例 `Q`，这只能产生任意尺度的重建结果。官方深度教程给出的物理关系是 $d=Bf/Z$，因此没有已知 $B$ 和 $f$ 时不能恢复绝对 $Z$。

## 1. 官方数据与来源

| 内容 | 官方来源 | 本实验用途 |
|---|---|---|
| OpenCV 样例数据目录 | [opencv/opencv `4.x/samples/data`](https://github.com/opencv/opencv/tree/4.x/samples/data) | 数据来源总目录 |
| 左图 | [`aloeL.jpg`](https://github.com/opencv/opencv/blob/4.x/samples/data/aloeL.jpg) | 左相机输入 |
| 右图 | [`aloeR.jpg`](https://github.com/opencv/opencv/blob/4.x/samples/data/aloeR.jpg) | 右相机输入 |
| 可选视差参考 | [`aloeGT.png`](https://github.com/opencv/opencv/blob/4.x/samples/data/aloeGT.png) | 只作视差结果的可选参考，不用于深度标定 |
| 官方 Python 立体匹配样例 | [`samples/python/stereo_match.py`](https://github.com/opencv/opencv/blob/4.x/samples/python/stereo_match.py) | SGBM 参数和处理流程参考 |
| 官方深度教程 | [Depth Map from Stereo Images](https://docs.opencv.org/4.x/dd/d53/tutorial_py_depthmap.html) | 视差—深度关系与 StereoBM API 依据 |

`aloeGT.png` 不是必需输入；如果保存或比较它，报告中只能称为视差参考图，不能称为米制深度真值。

## 2. 标定信息核查

针对选定的 aloe 图像对，当前实验只接受以下信息结论：

| 参数 | 是否有与 aloe 图像明确配套的官方值 | 处理方式 |
|---|---:|---|
| baseline $B$ | 否 | 不计算米制绝对深度 |
| 焦距 $f$（像素） | 否 | 不把样例中的猜测值当真实标定 |
| `doffs` | 否 | 不补写或猜测 |
| `Q` 矩阵 | 否 | 不调用带猜测 `Q` 的绝对三维重投影 |
| `aloeGT.png` | 有同目录文件，但它是视差参考，不是相机标定 | 可选做视差图对照 |

同一官方目录中可能存在 `intrinsics.yml`、`left_intrinsics.yml` 等其他校准样例文件；官方 aloe 的 `stereo_match.py` 没有读取这些文件，且没有明确声明它们与 aloe 图像对属于同一相机/同一分辨率。没有这种配对证据时禁止混用。

如果课程教师明确要求绝对深度，必须另行取得与这对图像匹配的 $B,f,Q$，或者用同一双目相机、已知棋盘格尺寸和左右标定序列重新执行 `stereoCalibrate`/`stereoRectify`。这属于额外标定阶段，不应在本最简实验中伪造。

## 3. 最简实验流程

1. 将官方 `aloeL.jpg`、`aloeR.jpg` 放入 `task2/data/`；程序不得自动依赖系统安装目录中的隐式样例路径。
2. 用 `cv2.imread(..., cv2.IMREAD_COLOR)` 读入左右图，检查返回值非空且尺寸相同；随后转灰度用于匹配。
3. 为降低运行时间，可以像官方 Python 样例一样先对左右图各执行一次 `cv2.pyrDown`。左右图必须使用相同缩放。
4. 用 `cv2.StereoSGBM_create` 计算视差。首轮只使用一组固定参数，不进行无止境调参。
5. 将 OpenCV 返回的定点视差转换为浮点视差：
   
   ```python
   disparity = matcher.compute(gray_l, gray_r).astype(np.float32) / 16.0
   ```

6. 用有效掩码去除无效视差：
   
   ```python
   valid = np.isfinite(disparity) & (disparity > min_disparity - 1)
   ```

   无效区域在原始数组中置为 `NaN`（或另存 `valid_mask.png`），不得把无效值参与深度统计或拉伸显示。
7. 保存原始浮点视差和归一化视差图。归一化只用于显示，不能替代原始视差。
8. 在有效区域计算相对/代理深度：
   
   ```text
   depth_proxy = 1 / disparity
   ```

   视差越大表示相对越近；显示时可使用有效像素的百分位范围归一化，并在图注中注明“相对深度/任意尺度”。
9. 报告中同时写出物理公式 $Z=fB/d$，并明确本实验没有 $f$ 与 $B$，所以 `depth_proxy` 只表达前后关系，不是米、厘米等单位的深度。

## 4. 推荐匹配器与参数

优先使用 **StereoSGBM**，因为官方 `stereo_match.py` 就以 aloe 图像对为例，且相较最小化的 StereoBM 更适合得到连续的课程演示结果。

建议首轮参数如下；`numDisparities` 必须是 16 的倍数：

```python
window_size = 3
min_disparity = 16
num_disparities = 96
block_size = 5
matcher = cv2.StereoSGBM_create(
    minDisparity=min_disparity,
    numDisparities=num_disparities,
    blockSize=block_size,
    P1=8 * 1 * window_size ** 2,    # 灰度图，1 个通道
    P2=32 * 1 * window_size ** 2,
    disp12MaxDiff=1,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=32,
)
```

这组参数保留了官方样例的视差范围、左右一致性和 speckle 过滤思路；`blockSize=5` 是灰度实现的保守起点。如果实测有效区域明显过少，只允许在报告中记录一次小范围调整（例如 `numDisparities=112` 或 `blockSize=7`），并保存最终实际参数；不能凭图片观感反复调参。

StereoBM 可以作为简单对照，但不是主流程：若做对照，使用 `numDisparities=96`、`blockSize=15`，并同样执行定点缩放、无效掩码和相对深度处理。

## 5. 程序 CLI 约定

建议 T2-B 将程序入口固定为：

```bash
python3 task2/src/stereo_depth.py \
  --left task2/data/aloeL.jpg \
  --right task2/data/aloeR.jpg \
  --out-dir task2/results
```

至少支持以下参数：

```text
--left       左图路径，必填
--right      右图路径，必填
--out-dir    输出目录，必填
--no-pyrdown 可选，禁用官方样例式降采样
```

参数应集中在程序顶部或命令行默认值中，并在 `run_info.txt`/`params.json` 中记录实际输入、是否降采样、匹配器和所有 SGBM 参数。程序默认不接受伪造的 `--baseline`、`--focal-length` 或 `--q`；只有拿到配套标定文件后才增加绝对深度分支。

## 6. 必须保存的真实结果

`task2/results/` 至少保留：

- `left.png`、`right.png`：程序实际读入/处理后的左右图（如保留原始 JPG，也要在报告中说明）；
- `disparity_raw.npy`：除无效区域外保持浮点视差值，单位为像素；
- `disparity.png`：用于报告展示的视差可视化；
- `valid_mask.png`：有效视差区域；
- `depth_proxy.npy`：`1/disparity` 的相对深度数组，无效区域为 `NaN`；
- `depth_proxy.png`：标注为“相对深度/任意尺度”的可视化；
- `run_info.txt` 或 `params.json`：运行命令、输入文件、图像尺寸、OpenCV 参数和实测环境版本；
- 可选：`aloeGT.png` 及视差对照图，但必须标注为视差参考，不得标为绝对深度真值。

报告只引用这些由程序实际生成的图片和数组统计，不得使用手工绘制或虚构的结果。

## 7. 环境版本实测

提交前在实际运行程序的同一 Python 环境执行，不要预填版本号：

```bash
python3 -c "import sys, cv2; print('python=', sys.version); print('opencv=', cv2.__version__); print('cv2_path=', cv2.__file__)"
```

若 `import cv2` 失败，应记录完整错误并先修复环境；不能在报告中用记忆中的版本号替代实测值。

## 验收判定

- [x] 数据来自 OpenCV 官方 `opencv/opencv` 仓库，左右文件名明确。
- [x] 官方 Python 样例和官方深度教程已核对。
- [x] disparity 流程、SGBM 参数、定点缩放和无效值处理已规定。
- [x] depth 的含义已限定为相对/代理深度，未伪造绝对尺度。
- [x] CLI、结果清单、版本实测命令已规定。
- [ ] 米制绝对深度：**当前不具备，除非后续取得与 aloe 图像对配套的 $B,f,Q$**。
