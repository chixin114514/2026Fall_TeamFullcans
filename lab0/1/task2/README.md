# 任务 2：手机相机内参标定

`calibrate_camera.py` 使用 OpenCV 的棋盘格角点检测、亚像素优化和
`cv2.calibrateCamera` 完成相机标定。程序会逐张报告 `[OK]` 或 `[FAILED]`，并
计算每幅图像及全部有效图像的重投影误差。

## 运行

在仓库根目录执行：

```bash
python3 task2/calibrate_camera.py --help
python3 task2/calibrate_camera.py \
  --checkerboard 9x6 \
  --square-size 25.0 \
  --images "task2/images/*" \
  --output-dir task2/output
```

如果尚未安装依赖，可在实际标定环境中执行：

```bash
python3 -m pip install numpy opencv-python
```

也可以先进入 `task2/` 后使用相对路径：

```bash
cd task2
python3 calibrate_camera.py --checkerboard 9x6 --square-size 25.0 \
  --images "images/*" --output-dir output
```

## 参数

| 参数 | 含义 |
| --- | --- |
| `--checkerboard COLSxROWS` | 棋盘格的内角点列数和行数，例如 `9x6`，不是方格数 |
| `--square-size UNITS` | 一个方格的实际边长；单位可为 mm 或 cm，但必须前后一致 |
| `--images GLOB` | 图片路径或 glob，例如 `"images/*"` |
| `--output-dir DIR` | 输出目录，默认 `output` |
| `--min-images N` | 至少需要的有效视图数，默认 `3` |
| `--save-corners` | 可选，保存角点检测可视化到 `DIR/corners/` |
| `--undistort` | 可选，保存有效图片的畸变校正结果到 `DIR/undistorted/` |

图片读取失败、角点检测失败和尺寸不一致的图片会单独打印失败原因，程序会
继续处理其余图片。有效图片少于 `--min-images` 时会明确报错并且不会生成
不完整的标定参数。

## 输出

成功标定后，`output/camera_params.npz` 至少包含：

* `camera_matrix`：相机内参矩阵 `K`，其中 `fx`、`fy` 为焦距，`cx`、`cy` 为主点；
* `distortion_coefficients`：畸变系数，通常为 `k1,k2,p1,p2,k3`；
* `rotation_vectors` 和 `translation_vectors`：每个有效视图对应的外参数；
* `rms_error`：OpenCV 返回的 RMS 标定误差；
* `per_image_reprojection_error` 和 `mean_reprojection_error`：逐图及平均像素误差；
* `image_size`、`checkerboard`、`square_size`、有效/失败图像数及有效图片路径。

## 拍摄建议

建议使用同一分辨率拍摄 10--20 张清晰图片，让棋盘格覆盖图像中央、左/右侧、
上/下方，并包含不同距离和倾角。避免所有图片都正对标定板；避免运动模糊、
强反光和棋盘格被遮挡。拍摄后不要改变图片分辨率或裁剪方式。

## 当前数据状态

当前项目的 `task2/images/` 尚未提供真实手机棋盘格照片，因此目前没有真实的
相机矩阵、畸变系数、RMS 或重投影误差，也不会伪造 `camera_params.npz`。把真实
照片放入该目录后，按上面的命令运行程序，再将终端输出和生成的 NPZ 结果用于
实验报告。
