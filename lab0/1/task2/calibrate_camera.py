#!/usr/bin/env python3
"""使用 OpenCV 棋盘格照片完成手机相机内参标定。

默认配置对应本项目已有的 18 张 JPEG：8x5 个内角点、每格 3.0 cm。
因此标定得到的外参平移向量 ``tvec`` 以 cm 计。
"""

from __future__ import annotations

import argparse
import glob
import os
import re
from pathlib import Path
from typing import Iterable, Sequence

import cv2
import numpy as np


DEFAULT_CHECKERBOARD = (8, 5)
DEFAULT_SQUARE_SIZE = 3.0
DEFAULT_IMAGES = "task2/images_jpg/*.jpg"
DEFAULT_OUTPUT_DIR = "task2/output"
DEFAULT_MIN_IMAGES = 3
IMAGE_EXTENSIONS = {".bmp", ".heic", ".jpeg", ".jpg", ".png", ".tif", ".tiff"}


def parse_checkerboard(value: str) -> tuple[int, int]:
    """Parse ``COLSxROWS`` into the number of internal corner columns/rows."""

    match = re.fullmatch(r"\s*(\d+)\s*[xX×]\s*(\d+)\s*", value)
    if match is None:
        raise argparse.ArgumentTypeError(
            "棋盘格必须写成 COLSxROWS，例如 8x5（表示内角点数量）"
        )

    cols, rows = (int(part) for part in match.groups())
    if cols < 2 or rows < 2:
        raise argparse.ArgumentTypeError("棋盘格的列数和行数都必须至少为 2")
    return cols, rows


def parse_positive_float(value: str) -> float:
    try:
        number = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("必须是正数") from exc
    if not np.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("必须是正数")
    return number


def parse_positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("必须是正整数") from exc
    if number < 1:
        raise argparse.ArgumentTypeError("必须是正整数")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="使用 OpenCV 棋盘格照片标定相机内参并计算重投影误差。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--checkerboard",
        type=parse_checkerboard,
        default=f"{DEFAULT_CHECKERBOARD[0]}x{DEFAULT_CHECKERBOARD[1]}",
        metavar="COLSxROWS",
        help="棋盘格内角点的列数和行数",
    )
    parser.add_argument(
        "--square-size",
        type=parse_positive_float,
        default=DEFAULT_SQUARE_SIZE,
        metavar="CM",
        help="单个方格实际边长，单位 cm；外参 tvec 也以 cm 计",
    )
    parser.add_argument(
        "--images",
        default=DEFAULT_IMAGES,
        metavar="PATH_OR_GLOB",
        help="图片目录、单个图片或 glob 路径",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        metavar="DIR",
        help="标定参数和可选结果的输出目录",
    )
    parser.add_argument(
        "--min-images",
        type=parse_positive_int,
        default=DEFAULT_MIN_IMAGES,
        metavar="N",
        help="调用 calibrateCamera 所需的最少有效视图数",
    )
    parser.add_argument(
        "--save-corners",
        action="store_true",
        help="保存角点检测可视化到 output-dir/corners/（不打开 GUI）",
    )
    parser.add_argument(
        "--undistort",
        action="store_true",
        help="保存有效图片的畸变校正结果到 output-dir/undistorted/",
    )
    return parser


def _is_image_path(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS


def collect_image_paths(pattern: str) -> list[str]:
    """Collect deterministic image paths from a directory, file, or glob."""

    expanded = os.path.expanduser(pattern)
    candidate = Path(expanded)
    if candidate.is_dir():
        paths: Iterable[Path] = sorted(
            (path for path in candidate.iterdir() if _is_image_path(path)),
            key=lambda path: str(path),
        )
    elif candidate.is_file():
        paths = [candidate] if _is_image_path(candidate) else []
    else:
        paths = sorted(
            (
                Path(path)
                for path in glob.glob(expanded)
                if _is_image_path(Path(path))
            ),
            key=lambda path: str(path),
        )
    return [str(path) for path in paths]


def build_object_points(checkerboard: tuple[int, int], square_size: float) -> np.ndarray:
    cols, rows = checkerboard
    object_points = np.zeros((cols * rows, 3), dtype=np.float32)
    object_points[:, :2] = np.mgrid[0:cols, 0:rows].T.reshape(-1, 2)
    object_points *= np.float32(square_size)
    return object_points


def _size_text(image_size: tuple[int, int]) -> str:
    return f"{image_size[0]}x{image_size[1]}"


def _read_failure_reason(filename: str) -> str:
    if Path(filename).suffix.lower() == ".heic":
        return (
            "无法读取：cv2.imread 返回 None；当前 OpenCV 不能直接读取 HEIC，"
            "请先转换为 JPEG"
        )
    return "无法读取：cv2.imread 返回 None"


def _print_counts(
    total_count: int,
    valid_count: int,
    failed_count: int,
    read_failure_count: int,
    corner_failure_count: int,
    size_mismatch_count: int,
) -> None:
    print(
        "统计："
        f"总图片 {total_count}，有效 {valid_count}，失败 {failed_count}；"
        f"读取失败 {read_failure_count}，角点失败 {corner_failure_count}，"
        f"尺寸不一致 {size_mismatch_count}"
    )


def _save_corner_overlays(
    valid_paths: Sequence[str],
    valid_corners: Sequence[np.ndarray],
    checkerboard: tuple[int, int],
    output_dir: Path,
) -> None:
    corners_dir = output_dir / "corners"
    corners_dir.mkdir(parents=True, exist_ok=True)
    for index, (filename, corners) in enumerate(zip(valid_paths, valid_corners), start=1):
        image = cv2.imread(filename)
        if image is None:
            print(f"[WARN] 角点可视化无法读取：{filename}")
            continue
        display = image.copy()
        cv2.drawChessboardCorners(display, checkerboard, corners, True)
        target = corners_dir / f"{index:02d}_{Path(filename).stem}.jpg"
        if not cv2.imwrite(str(target), display):
            print(f"[WARN] 角点可视化保存失败：{target}")


def _save_undistorted(
    valid_paths: Sequence[str],
    camera_matrix: np.ndarray,
    distortion_coefficients: np.ndarray,
    output_dir: Path,
) -> None:
    undistorted_dir = output_dir / "undistorted"
    undistorted_dir.mkdir(parents=True, exist_ok=True)
    for index, filename in enumerate(valid_paths, start=1):
        image = cv2.imread(filename)
        if image is None:
            print(f"[WARN] 畸变校正无法读取：{filename}")
            continue
        corrected = cv2.undistort(image, camera_matrix, distortion_coefficients)
        target = undistorted_dir / f"{index:02d}_{Path(filename).stem}.jpg"
        if not cv2.imwrite(str(target), corrected):
            print(f"[WARN] 畸变校正结果保存失败：{target}")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    checkerboard = args.checkerboard
    square_size = float(args.square_size)
    image_paths = collect_image_paths(args.images)

    if not image_paths:
        print(f"[ERROR] 未找到可读取的图片：{args.images}")
        return 1

    print(f"找到 {len(image_paths)} 张候选图片")
    object_points_template = build_object_points(checkerboard, square_size)
    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        30,
        0.001,
    )
    find_flags = cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE

    object_points: list[np.ndarray] = []
    image_points: list[np.ndarray] = []
    valid_paths: list[str] = []
    valid_corners: list[np.ndarray] = []
    failed_paths: list[str] = []
    failure_reasons: list[str] = []
    expected_image_size: tuple[int, int] | None = None
    read_failure_count = 0
    corner_failure_count = 0
    size_mismatch_count = 0

    for filename in image_paths:
        image = cv2.imread(filename)
        if image is None:
            reason = _read_failure_reason(filename)
            failed_paths.append(filename)
            failure_reasons.append(reason)
            read_failure_count += 1
            print(f"[FAILED] {filename}: {reason}")
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        current_image_size = (int(gray.shape[1]), int(gray.shape[0]))
        if expected_image_size is None:
            expected_image_size = current_image_size
        elif current_image_size != expected_image_size:
            reason = (
                f"尺寸不一致：期望 {_size_text(expected_image_size)}，"
                f"实际 {_size_text(current_image_size)}"
            )
            failed_paths.append(filename)
            failure_reasons.append(reason)
            size_mismatch_count += 1
            print(f"[FAILED] {filename}: {reason}")
            continue

        found, corners = cv2.findChessboardCorners(
            gray,
            checkerboard,
            flags=find_flags,
        )
        if not found:
            reason = f"未检测到 {checkerboard[0]}x{checkerboard[1]} 个内角点"
            failed_paths.append(filename)
            failure_reasons.append(reason)
            corner_failure_count += 1
            print(f"[FAILED] {filename}: {reason}")
            continue

        refined_corners = cv2.cornerSubPix(
            gray,
            corners,
            (11, 11),
            (-1, -1),
            criteria,
        )
        object_points.append(object_points_template.copy())
        image_points.append(refined_corners)
        valid_paths.append(filename)
        valid_corners.append(refined_corners)
        print(f"[OK] {filename}")

    valid_count = len(object_points)
    failed_count = len(failed_paths)
    _print_counts(
        len(image_paths),
        valid_count,
        failed_count,
        read_failure_count,
        corner_failure_count,
        size_mismatch_count,
    )

    if expected_image_size is None:
        print("[ERROR] 没有任何可读取图片，未生成标定参数")
        return 1

    if size_mismatch_count:
        print("[ERROR] 检测到混合图像尺寸；为避免错误标定，本次拒绝并未生成参数")
        return 1

    if valid_count < args.min_images:
        print(
            f"[ERROR] 有效图片仅 {valid_count} 张，少于 --min-images {args.min_images}；"
            "未生成标定参数"
        )
        return 1

    print(
        f"标定配置：checkerboard={checkerboard[0]}x{checkerboard[1]}，"
        f"square_size={square_size:g} cm（外参平移向量单位为 cm）"
    )
    try:
        rms_error, camera_matrix, distortion_coefficients, rotation_vectors, translation_vectors = cv2.calibrateCamera(
            object_points,
            image_points,
            expected_image_size,
            None,
            None,
        )
    except cv2.error as exc:
        print(f"[ERROR] cv2.calibrateCamera 失败：{exc}")
        return 1

    per_image_reprojection_error: list[float] = []
    all_point_distances: list[float] = []
    print("\n========== 每张图片的重投影误差 ==========")
    for filename, object_points_i, image_points_i, rvec, tvec in zip(
        valid_paths,
        object_points,
        image_points,
        rotation_vectors,
        translation_vectors,
    ):
        projected, _ = cv2.projectPoints(
            object_points_i,
            rvec,
            tvec,
            camera_matrix,
            distortion_coefficients,
        )
        difference = image_points_i.reshape(-1, 2) - projected.reshape(-1, 2)
        point_distances = np.linalg.norm(difference, axis=1)
        image_rms = float(np.sqrt(np.mean(np.square(point_distances))))
        per_image_reprojection_error.append(image_rms)
        all_point_distances.extend(float(value) for value in point_distances)
        print(f"{filename}: {image_rms:.6f} px")

    mean_reprojection_error = float(np.mean(all_point_distances))
    mean_per_image_rms = float(np.mean(per_image_reprojection_error))

    print("\n========== 标定结果 ==========")
    print(f"有效图片数量：{valid_count}")
    print(f"OpenCV RMS：{float(rms_error):.6f} px")
    print(f"逐图 RMS 算术平均：{mean_per_image_rms:.6f} px")
    print(f"逐角点欧氏距离全局平均（mean_reprojection_error）：{mean_reprojection_error:.6f} px")
    print("\n相机内参矩阵 K：")
    print(camera_matrix)
    print("\n畸变系数：")
    print(distortion_coefficients)
    print("\n内参参数：")
    print(f"fx = {camera_matrix[0, 0]:.6f}")
    print(f"fy = {camera_matrix[1, 1]:.6f}")
    print(f"cx = {camera_matrix[0, 2]:.6f}")
    print(f"cy = {camera_matrix[1, 2]:.6f}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "camera_params.npz"
    np.savez(
        output_path,
        camera_matrix=np.asarray(camera_matrix),
        distortion_coefficients=np.asarray(distortion_coefficients),
        rotation_vectors=np.asarray(rotation_vectors),
        translation_vectors=np.asarray(translation_vectors),
        rms_error=np.float64(rms_error),
        per_image_reprojection_error=np.asarray(
            per_image_reprojection_error,
            dtype=np.float64,
        ),
        mean_reprojection_error=np.float64(mean_reprojection_error),
        mean_per_image_rms=np.float64(mean_per_image_rms),
        image_size=np.asarray(expected_image_size, dtype=np.int32),
        checkerboard=np.asarray(checkerboard, dtype=np.int32),
        square_size=np.float64(square_size),
        image_paths=np.asarray(image_paths, dtype=str),
        valid_image_paths=np.asarray(valid_paths, dtype=str),
        failed_image_paths=np.asarray(failed_paths, dtype=str),
        failure_reasons=np.asarray(failure_reasons, dtype=str),
        total_image_count=np.int64(len(image_paths)),
        valid_image_count=np.int64(valid_count),
        failed_image_count=np.int64(failed_count),
        read_failure_count=np.int64(read_failure_count),
        corner_detection_failure_count=np.int64(corner_failure_count),
        size_mismatch_count=np.int64(size_mismatch_count),
    )

    if not output_path.is_file():
        print(f"[ERROR] 参数文件未生成：{output_path}")
        return 1

    # 新契约写入成功后，删除同一输出目录中的两个旧契约文件，避免提交者误取旧结果。
    for legacy_name in ("camera_calibration.npz", "calibration_result.txt"):
        legacy_path = output_dir / legacy_name
        if legacy_path.exists():
            legacy_path.unlink()
            print(f"[CLEANUP] 已移除旧结果：{legacy_path}")

    if args.save_corners:
        try:
            _save_corner_overlays(
                valid_paths,
                valid_corners,
                checkerboard,
                output_dir,
            )
        except (OSError, cv2.error) as exc:
            print(f"[WARN] 角点可视化失败，但不影响标定参数：{exc}")
    if args.undistort:
        try:
            _save_undistorted(
                valid_paths,
                camera_matrix,
                distortion_coefficients,
                output_dir,
            )
        except (OSError, cv2.error) as exc:
            print(f"[WARN] 畸变校正结果失败，但不影响标定参数：{exc}")

    print(f"\n[OK] 标定参数已保存：{output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
