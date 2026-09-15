import cv2
import numpy as np
import glob
import os

# =========================
# 配置
# =========================

# 棋盘格内部角点数
CHECKERBOARD = (8, 5)

# 单个方格实际边长，单位 m
SQUARE_SIZE = 0.03

IMAGE_PATH = "images_jpg/*.jpg"

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =========================
# 构造棋盘格世界坐标
# =========================

# 例如：
# (0,0,0)
# (1,0,0)
# (2,0,0)
# ...
objp = np.zeros(
    (CHECKERBOARD[0] * CHECKERBOARD[1], 3),
    np.float32
)

objp[:, :2] = np.mgrid[
    0:CHECKERBOARD[0],
    0:CHECKERBOARD[1]
].T.reshape(-1, 2)

objp *= SQUARE_SIZE


# 保存所有图片中的三维点和二维角点
objpoints = []
imgpoints = []

images = glob.glob(IMAGE_PATH)

if len(images) == 0:
    raise RuntimeError("没有找到标定图片，请检查 images/ 目录")


print(f"找到 {len(images)} 张图片")


# 亚像素角点优化终止条件
criteria = (
    cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
    30,
    0.001
)


image_size = None
valid_images = []


# =========================
# 提取棋盘格角点
# =========================

for filename in images:

    img = cv2.imread(filename)

    if img is None:
        print(f"[跳过] 无法读取：{filename}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if image_size is None:
        image_size = gray.shape[::-1]

    # 检测棋盘格
    ret, corners = cv2.findChessboardCorners(
        gray,
        CHECKERBOARD,
        flags=(
            cv2.CALIB_CB_ADAPTIVE_THRESH
            + cv2.CALIB_CB_NORMALIZE_IMAGE
        )
    )

    if ret:

        # 亚像素级角点优化
        corners_subpix = cv2.cornerSubPix(
            gray,
            corners,
            (11, 11),
            (-1, -1),
            criteria
        )

        objpoints.append(objp)
        imgpoints.append(corners_subpix)
        valid_images.append(filename)

        # 可视化角点
        display = img.copy()

        cv2.drawChessboardCorners(
            display,
            CHECKERBOARD,
            corners_subpix,
            ret
        )

        print(f"[成功] {filename}")

        # 如果不想显示，可以删除下面三行
        cv2.imshow("Corners", display)
        cv2.waitKey(200)

    else:
        print(f"[失败] {filename}")


cv2.destroyAllWindows()


if len(objpoints) < 10:
    print(
        f"警告：只有 {len(objpoints)} 张有效图片，"
        "建议至少准备 15～20 张。"
    )


# =========================
# 相机标定
# =========================

rms, camera_matrix, dist_coeffs, rvecs, tvecs = \
    cv2.calibrateCamera(
        objpoints,
        imgpoints,
        image_size,
        None,
        None
    )

# =========================
# 计算每张图片的 RMS 重投影误差
# =========================

per_image_errors = []

print("\n========== 每张图片的重投影误差 ==========")

for i in range(len(objpoints)):
    projected, _ = cv2.projectPoints(
        objpoints[i],
        rvecs[i],
        tvecs[i],
        camera_matrix,
        dist_coeffs
    )

    diff = (
        imgpoints[i].reshape(-1, 2)
        - projected.reshape(-1, 2)
    )

    image_rms = np.sqrt(
        np.mean(
            np.sum(diff ** 2, axis=1)
        )
    )

    per_image_errors.append(image_rms)

    print(
        f"{valid_images[i]}: "
        f"{image_rms:.4f} px"
    )


# 这里一定已经退出 for 循环
mean_image_rms = np.mean(per_image_errors)

global_rms_check = np.sqrt(
    np.mean(
        np.square(per_image_errors)
    )
)

print(
    f"\n单图 RMS 算术平均："
    f"{mean_image_rms:.4f} px"
)

print(
    f"全局 RMS："
    f"{global_rms_check:.4f} px"
)

print(
    f"OpenCV RMS："
    f"{rms:.4f} px"
)
# =========================
# 输出结果
# =========================

print("\n========== 标定结果 ==========")

print(f"\n有效图片数量：{len(objpoints)}")

print(f"\nRMS 重投影误差：{rms:.6f}")

print("\n相机内参矩阵 K：")
print(camera_matrix)

print("\n畸变系数：")
print(dist_coeffs)


fx = camera_matrix[0, 0]
fy = camera_matrix[1, 1]
cx = camera_matrix[0, 2]
cy = camera_matrix[1, 2]

print("\n内参参数：")
print(f"fx = {fx:.6f}")
print(f"fy = {fy:.6f}")
print(f"cx = {cx:.6f}")
print(f"cy = {cy:.6f}")


# =========================
# 保存标定参数
# =========================

np.savez(
    os.path.join(
        OUTPUT_DIR,
        "camera_calibration.npz"
    ),
    camera_matrix=camera_matrix,
    dist_coeffs=dist_coeffs,
    rms=rms,
    mean_error=mean_image_rms,
    image_size=image_size
)


# 同时保存为文本，方便实验报告查看
with open(
    os.path.join(OUTPUT_DIR, "calibration_result.txt"),
    "w"
) as f:

    f.write("Camera Matrix K:\n")
    f.write(str(camera_matrix))

    f.write("\n\nDistortion Coefficients:\n")
    f.write(str(dist_coeffs))

    f.write(f"\n\nRMS Error: {rms}\n")
    f.write(
        f"Mean Reprojection Error: {mean_image_rms} pixel\n"
    )


print("\n标定参数已经保存到：")
print(
    os.path.join(
        OUTPUT_DIR,
        "camera_calibration.npz"
    )
)