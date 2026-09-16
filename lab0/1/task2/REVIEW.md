# Task 2 Re-review

复验日期：2026-09-15

范围：仅复验当前 live 的 `task2`，并仅更新本文件。未修改程序、README、报告源文件、PDF、图片或 `task2/output/`；所有临时输出和合成测试图均放在 `/tmp`。

## 结论

上轮 B1--B5 及重要项均已修复，没有发现新的阻塞项或重要正确性问题。程序、README、唯一 NPZ 和报告结果目前相互一致，真实 18 图标定可复现，PDF 可编译且可读。

除提交身份字段和方格物理尺寸/镜头模式待用户确认外，可提交。

## 程序复验

使用 `/Users/jiaqiaosu/miniconda3/bin/python`，并将 pycache 和输出隔离到 `/tmp`：

| 检查 | 结果 | 证据 |
| --- | --- | --- |
| `py_compile` | 通过 | 退出码 0 |
| `--help` | 通过 | 退出码 0，显示 `--checkerboard`、`--square-size`、`--images`、`--output-dir`、`--min-images`、`--save-corners`、`--undistort` |
| 无图片 | 通过 | 退出码 1，输出 `[ERROR] 未找到可读取的图片`，未生成参数文件 |
| 仅 1 张图、`--min-images 3` | 通过 | 退出码 1，明确报告有效图像不足，未生成参数文件 |
| 混合分辨率 | 通过 | 退出码 1，报告期望 `5712x4284`、实际 `2856x2142`，未生成参数文件 |
| 读取失败/角点失败 | 通过 | `/tmp` 中 1 张真实图、1 张空 JPG、1 张空白 JPG：有效 1、失败 2，分别计入读取失败和角点失败 |
| README 目录命令 | 通过 | `--images "task2/images_jpg/*"` 的完整标定退出码 0，生成 1 个临时 NPZ |
| 18 图完整标定 | 通过 | `8x5`、`square-size 1.0`、18 张 JPEG 全部 `[OK]`，退出码 0 |

当前源代码关键位置：OpenCV 接口在 `task2/calibrate_camera.py:274-298,331-337,352-360`；数量/尺寸拒绝在 `249-324`；唯一 NPZ 写入在 `384-413`；无 GUI 调用。读取失败和角点失败会继续处理其他图片并汇总计数。

## 18 图结果与官方 NPZ

`find task2 -name '*.npz'` 只发现 `task2/output/camera_params.npz`；旧的
`camera_calibration.npz` 和 `calibration_result.txt` 已不存在。当前官方文件 SHA-256 为：

```text
60a0d3d657c0c155d80badc8f98745ce87c11bb239226e201e11bb18b4dcc295
```

官方 NPZ 回读得到 21 个字段。将 18 图完整重跑结果与官方文件比较，字段顺序、字段集合和全部 21 个字段均完全相等，关键值为：

- `camera_matrix`：
  `[[4082.152908930645, 0, 2883.66417822517], [0, 4083.586576856829, 2107.202937340385], [0, 0, 1]]`
- `distortion_coefficients`：
  `[0.202451229180696, -0.294208365368304, -0.003266786122390, 0.003086706055211, -1.045543248781]`
- `rms_error = 2.0642440068812222 px`
- `mean_reprojection_error = 1.6569693071302027 px`
- `mean_per_image_rms = 1.9075064228640661 px`
- `image_size = [5712, 4284]`，`checkerboard = [8, 5]`，`square_size = 1.0`
- `total_image_count = 18`，`valid_image_count = 18`，`failed_image_count = 0`；读取、角点、尺寸失败计数均为 0
- `rotation_vectors`、`translation_vectors` 形状均为 `18x3x1`，逐图误差数组长度为 18，路径数组为 18/18/0。

## 上轮问题逐条复验

| 上轮问题 | 当前状态 | 复验依据 |
| --- | --- | --- |
| B1：CLI 与 README/报告命令不一致 | 已修复 | `calibrate_camera.py:64-112,219-228` 已使用 `argparse`；README `:19-37` 命令实际运行成功 |
| B2：有效图像不足/混合分辨率仍标定 | 已修复 | `calibrate_camera.py:249-324` 先统计并拒绝；少图和混合尺寸测试均非零退出且无输出 |
| B3：NPZ 名称、字段和结果信息不一致 | 已修复 | `:384-413` 写入唯一 `camera_params.npz`，21 字段与 README `:61-104` 和重跑完全一致 |
| B4：报告没有真实结果 | 已修复 | `results.tex:3-78` 已写入 18/18、K、五参数畸变、三类误差、图像和图件；`environment.tex:16-27` 已写入软件和图像事实 |
| B5：平均重投影误差口径不一致 | 已修复 | `calibrate_camera.py:342-367` 分别计算点级平均、逐图 RMS 平均和 OpenCV RMS；`principle.tex:102-122` 明确三种定义 |
| 配置、输入格式和 GUI 不一致 | 已修复 | 程序/README/报告统一使用 `8x5`、JPEG glob、`square_size=1.0`；源码无 `imshow/waitKey`，HEIC 不可读限制已明确说明 |
| 失败状态和失败计数缺失 | 已修复 | 程序输出 `[FAILED]`、总计和分类计数，并将路径/原因写入 NPZ |

## 报告复验

报告内容已落地以下真实数据：

- `task2/report/sections/results.tex:36-52`：18 张候选、18 张有效、0 失败，分辨率 `5712x4284`，棋盘格 `8x5`；
- `results.tex:9-26`：相机矩阵和完整五参数畸变系数；
- `results.tex:49-65`：OpenCV RMS、逐角点全局平均和逐图 RMS 平均，以及 NPZ 字段说明；
- `environment.tex:16-27`：macOS/Python/OpenCV、Apple iPhone 15 Pro EXIF、图像和有效统计；
- `data_collection.tex:30-36`、`conclusion.tex:3-5`：明确保留尚未确认的方格物理边长、前/后置及具体镜头模式，并不伪造这些信息；
- `results.tex:67-78` 和 `report/figures/`：真实图像的角点可视化和去畸变图件。

报告仍有 `main.tex:28-35` 的课程作业标题、姓名、学号、班级待填写；方格物理边长在 `environment.tex:25`、镜头模式在 `environment.tex:22` 待人工确认。姿态覆盖记录的限制已在 `data_collection.tex:17,36` 和 `analysis.tex:34-36,53` 明确披露，报告没有把它夸大为已验证事实；不影响当前程序和像素级结果验收。

## PDF 验收

对 `task2/report/main.tex` 在临时目录执行完整 XeLaTeX 两遍：两遍退出码均为 0，第二遍无未定义引用或致命错误，输出 7 页。当前 `task2/report/report.pdf` 与 `task2/report/build/report.pdf` SHA-256 相同：

```text
5b8637372cd2bfa2c52a48cd40116fbb38a47433d5a39d4efa6934a963232287
```

`pdfinfo`：7 页、A4、未加密；`pdftotext` 可提取完整正文并核对 18/18、K、畸变、三类误差、`8x5`、`5712x4284`、`待确认` 字段。对最终 `report.pdf` 的 7 页 PNG 全页渲染检查未发现文字截断、表格越界、图片缺失、重叠或不可读关键内容；轻微留白不构成问题。

## 真实数据说明

当前不是“缺少真实手机照片”：`task2/images_jpg/` 有 18 张带 Apple iPhone 15 Pro EXIF 的真实 JPEG，且 18 图完整运行与官方 NPZ 完全一致。原始 HEIC 不能被当前 OpenCV 直接读取，README、程序和报告均已明确本次使用 JPEG 转换件；这不是当前阻塞项。
