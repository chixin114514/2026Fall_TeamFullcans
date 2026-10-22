# T2-C 真实运行证据

状态：`DONE_WITH_CONCERNS`

本次运行使用 OpenCV 官方 `opencv/opencv` 仓库 `4.x/samples/data` 的 aloe
双目样例。程序只计算像素视差和无标定的相对深度代理
`depth_proxy = 1 / disparity`；由于该图像对没有随附且明确配套的焦距
`f`、基线 `B` 或 `Q` 矩阵，不能从本结果声称米制绝对深度。

## 输入来源与 SHA-256

| 文件 | 最终下载 URL | SHA-256 |
|---|---|---|
| `task2/data/aloeL.jpg` | <https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/aloeL.jpg> | `cce5736808efe80d9f04b118dbb978c344d4345672b332718c3e039a3eeb8eee` |
| `task2/data/aloeR.jpg` | <https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/aloeR.jpg> | `9b23100df31a846bc6e6a6545563b2b4120b948c9835c7d36cde00af77f4503e` |
| `task2/data/aloeGT.png`（视差参考，可选） | <https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/aloeGT.png> | `39ce4f3cb48d797d1091c5152f93361d8104298c337f8a1c134d87dda3442c04` |

下载得到的左右 JPG 原始尺寸均为 `1282 x 1110`，3 通道；`aloeGT.png`
为 `1282 x 1110` 的 8-bit 灰度图。`aloeGT.png` 只保留为官方视差参考，未作为深度标定或米制真值使用。

## 隔离环境与真实命令

环境创建于项目本地 `task2/.venv`，未修改系统 Python：

```text
Python 3.13.5
OpenCV runtime 5.0.0 (pip package opencv-python 5.0.0.93)
NumPy 2.5.3
```

安装命令：

```bash
python3.13 -m venv task2/.venv
task2/.venv/bin/python -m pip install -r task2/requirements.txt
```

默认 CLI 实际运行命令（未使用 `--no-pyrdown`，未做参数调整）：

```bash
task2/.venv/bin/python task2/src/stereo_depth.py \
  --left task2/data/aloeL.jpg \
  --right task2/data/aloeR.jpg \
  --out-dir task2/results
```

实际处理图像为官方样例式一次 `pyrDown` 后的 `641 x 555`，匹配器为
`StereoSGBM`，`minDisparity=16`、`numDisparities=96`、`blockSize=5`，
`P1=72`、`P2=288`、`disp12MaxDiff=1`、`uniquenessRatio=10`、
`speckleWindowSize=100`、`speckleRange=32`。完整参数也写入
[`params.json`](params.json)。

## 从真实数组得到的统计

统计对象为 `disparity_raw.npy` 与 `depth_proxy.npy`，不是手工读取图片的估计值。
有效视差规则为有限值且 `disparity > 15`；无效视差及相应深度为 `NaN`。

| 指标 | 实测值 |
|---|---:|
| 数组尺寸 | `555 x 641` |
| 总像素 | `355755` |
| 有效视差像素 | `261378` |
| 有效像素比例 | `73.4713496648%` |
| 有效视差范围 | `16.000 .. 105.875 px` |
| 有限相对深度范围 | `0.0094451001 .. 0.0625000000`（任意尺度） |
| 相对深度公式核验误差 | `max(abs(depth_proxy - 1/disparity)) = 0.0` |

近远关系可解释：视差较低的 0–5% 有效像素范围为 `16.000 .. 23.750 px`，
其相对深度代理中位数为 `0.043127`；视差较高的 95–100% 范围为
`65.750 .. 105.875 px`，其相对深度代理中位数为 `0.014172`。由于
`depth_proxy = 1 / disparity`，较大视差对应较小代理深度，前后关系方向一致；
这不是带米、厘米等物理单位的深度。

## 输出与图像完整性检查

程序实际生成并保留了以下文件：

```text
left.png
right.png
disparity_raw.npy
disparity.png
valid_mask.png
depth_proxy.npy
depth_proxy.png
params.json
```

使用 OpenCV 重新读取 5 个 PNG 均成功，尺寸均为 `555 x 641`；文件非空且
像素统计非全零：`left.png`/`right.png` 为彩色原图，`disparity.png`、
`valid_mask.png`、`depth_proxy.png` 均有有效的非零像素和正常的 8-bit 范围。
对结果图进行渲染检查可见植物、花盆与背景的结构；视差图和相对深度图均有
连续灰度区域，`valid_mask.png` 有对应的有效区域，不是空白或损坏文件。

## 限制

官方 aloe 图像对没有验证过的配套 `f`、`B`、`doffs` 或 `Q`。因此本次交付
不计算米制绝对深度，也不输出带物理尺度的三维点云；`depth_proxy` 只能用于
展示由视差反映的相对前后关系。
