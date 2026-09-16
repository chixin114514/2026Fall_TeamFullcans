# 任务 2：手机相机内参标定

`calibrate_camera.py` 使用 OpenCV 完成棋盘格角点检测、亚像素优化、相机标定和
重投影误差计算。程序无 GUI 调用，逐图输出 `[OK]` 或 `[FAILED]` 及具体原因。

## 当前真实数据

项目中用于标定的是 `task2/images_jpg/*.jpg` 的 18 张 JPEG，图片尺寸为
`5712x4284`；JPEG 的 EXIF 显示设备为 `Apple iPhone 15 Pro`。原始
`task2/images/*.HEIC` 文件不能由当前 OpenCV 的 `cv2.imread` 直接读取，因此本次
标定使用已转换的 JPEG，不把 HEIC 当作可直接输入格式。

现有照片的棋盘格为 `8x5` 个内角点。方格的真实物理边长尚未由用户确认，真实运行
采用 `--square-size 1.0`，表示“每格一个单位”；该设置只影响平移向量的尺度，不
代表实测的米、厘米或毫米，不能写成 `0.03 m`。

## 运行

在仓库根目录执行帮助命令和本次真实标定：

```bash
python3 task2/calibrate_camera.py --help
python3 task2/calibrate_camera.py \
  --checkerboard 8x5 \
  --square-size 1.0 \
  --images "task2/images_jpg/*.jpg" \
  --output-dir task2/output \
  --min-images 3
```

也可以指定目录、单个图片或其他 glob：

```bash
python3 task2/calibrate_camera.py \
  --checkerboard 8x5 --square-size 1.0 \
  --images "task2/images_jpg/*" --output-dir task2/output
```

如果尚未安装依赖，可在实际标定环境中执行：

```bash
python3 -m pip install numpy opencv-python
```

## 参数

| 参数 | 含义 |
| --- | --- |
| `--checkerboard COLSxROWS` | 棋盘格内角点列数和行数，例如 `8x5`，不是方格数 |
| `--square-size UNITS` | 一个方格的边长；采用 `1.0` 时表示每格一个相对单位，只影响外参尺度 |
| `--images PATH_OR_GLOB` | 图片目录、单个图片或 glob；本项目使用 `task2/images_jpg/*.jpg` |
| `--output-dir DIR` | 输出目录，默认 `task2/output` |
| `--min-images N` | 至少需要的有效视图数，默认 `3` |
| `--save-corners` | 可选，保存角点可视化到 `DIR/corners/`，不打开窗口 |
| `--undistort` | 可选，保存有效图片的畸变校正结果到 `DIR/undistorted/` |

读取失败和角点检测失败的图片会被跳过并计入失败统计，其他图片继续处理。若检测到
混合分辨率，程序会拒绝本次标定并以非零退出码结束；有效图片少于 `--min-images`
时也会以非零退出码结束，且不会写入不完整的参数文件。

## 输出契约

成功运行只生成一个参数文件：`task2/output/camera_params.npz`。程序在新文件写入
成功后会移除同一目录中过时的 `camera_calibration.npz` 和
`calibration_result.txt`，避免出现两个互相矛盾的结果来源。

`camera_params.npz` 的字段如下，字段名与程序保持一致：

| 字段 | 内容 |
| --- | --- |
| `camera_matrix` | 相机内参矩阵 `K`，包含 `fx`、`fy`、`cx`、`cy` |
| `distortion_coefficients` | 畸变系数，通常为 `k1,k2,p1,p2,k3` |
| `rotation_vectors` | 每个有效视图的旋转向量 |
| `translation_vectors` | 每个有效视图的平移向量 |
| `rms_error` | `cv2.calibrateCamera` 返回的 OpenCV RMS，单位 px |
| `per_image_reprojection_error` | 每个有效视图的点距离 RMS，单位 px |
| `mean_reprojection_error` | 所有有效角点欧氏距离的全局平均值，单位 px |
| `mean_per_image_rms` | `per_image_reprojection_error` 的算术平均，单位 px |
| `image_size` | `[width, height]` |
| `checkerboard` | `[columns, rows]` 内角点配置 |
| `square_size` | 运行时方格边长数值；本次为相对单位 `1.0` |
| `image_paths` | 本次发现的全部图片路径 |
| `valid_image_paths` | 实际用于标定的图片路径 |
| `failed_image_paths` | 被跳过或拒绝的图片路径 |
| `failure_reasons` | 与 `failed_image_paths` 一一对应的失败原因 |
| `total_image_count` | 候选图片总数 |
| `valid_image_count` | 有效图片数 |
| `failed_image_count` | 失败图片数 |
| `read_failure_count` | 图片读取失败数 |
| `corner_detection_failure_count` | 棋盘格角点检测失败数 |
| `size_mismatch_count` | 分辨率不一致数 |

可用 NumPy 回读结果：

```python
import numpy as np

result = np.load("task2/output/camera_params.npz", allow_pickle=False)
print(result.files)
print(result["camera_matrix"])
print(result["distortion_coefficients"])
print(float(result["rms_error"]))
print(float(result["mean_reprojection_error"]))
```

## 采集建议

使用同一分辨率拍摄 10--20 张清晰图片，让棋盘格覆盖图像中央、左侧、右侧、上方和
下方，并包含不同距离和倾角。避免所有图片都正对标定板，也要避免运动模糊、强反光
和遮挡。拍摄后不要改变图片的分辨率或裁剪方式。若只有 HEIC，请先转换为 JPEG，
再把 JPEG 路径传给程序。
