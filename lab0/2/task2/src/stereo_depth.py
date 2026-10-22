#!/usr/bin/env python3
"""Estimate stereo disparity and relative depth for OpenCV's aloe image pair.

The aloe sample does not come with a verified baseline, focal length, or Q
matrix.  Consequently this program deliberately reports only the proxy
quantity ``relative_depth = 1 / disparity`` (arbitrary scale), not metric
depth or a metric point cloud.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path
from typing import Any, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_LEFT = PROJECT_ROOT / "task2" / "data" / "aloeL.jpg"
DEFAULT_RIGHT = PROJECT_ROOT / "task2" / "data" / "aloeR.jpg"
DEFAULT_OUTPUT = PROJECT_ROOT / "task2" / "results"

# User-capture defaults.  The user pair is not calibrated, so this branch
# rectifies it from feature correspondences and reports relative depth only.
USER_ORB_FEATURES = 10000
USER_MATCH_RATIO = 0.70
USER_RANSAC_THRESHOLD = 1.0
USER_RANSAC_CONFIDENCE = 0.999
USER_MIN_DISPARITY = -64
USER_NUM_DISPARITIES = 128
USER_BLOCK_SIZE = 5

# Keep the experiment parameters together so that the recorded JSON summary
# always describes the exact matcher configuration used for a run.
WINDOW_SIZE = 3
MIN_DISPARITY = 16
NUM_DISPARITIES = 96  # OpenCV requires this to be a positive multiple of 16.
BLOCK_SIZE = 5
P1 = 8 * WINDOW_SIZE**2  # one-channel grayscale input
P2 = 32 * WINDOW_SIZE**2
DISP_SCALE = 16.0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Compute StereoSGBM disparity and uncalibrated relative depth "
            "(1/disparity) for a stereo image pair."
        )
    )
    parser.add_argument(
        "--left",
        default=str(DEFAULT_LEFT),
        help=f"left image (default: {DEFAULT_LEFT})",
    )
    parser.add_argument(
        "--right",
        default=str(DEFAULT_RIGHT),
        help=f"right image (default: {DEFAULT_RIGHT})",
    )
    parser.add_argument(
        "--out-dir",
        default=str(DEFAULT_OUTPUT),
        help=f"result directory (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--no-pyrdown",
        action="store_true",
        help="disable the official-sample-style one-level image downsampling",
    )
    parser.add_argument(
        "--rectify-uncalibrated",
        action="store_true",
        help="estimate F with ORB and rectify an uncalibrated stereo pair",
    )
    return parser


def _resolve_user_path(raw_path: str, project_root: Path) -> Path:
    """Resolve an absolute path or a useful project/CWD-relative path.

    Defaults are absolute and therefore stable regardless of the launch
    directory.  For a user override, an existing CWD-relative path wins;
    otherwise a project-root-relative path is used.  This supports both
    ``task2/data/foo.jpg`` from the project root and ``data/foo.jpg`` from
    inside ``task2`` without changing the default contract.
    """

    path = Path(raw_path).expanduser()
    if path.is_absolute():
        return path

    cwd_path = (Path.cwd() / path).resolve()
    project_path = (project_root / path).resolve()
    if cwd_path.exists() or not project_path.exists():
        return cwd_path
    return project_path


def _load_dependencies() -> tuple[Any, Any]:
    """Import optional runtime dependencies with an actionable error."""

    try:
        import cv2  # type: ignore
        import numpy as np  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "本程序需要 OpenCV 和 NumPy；当前 Python 环境缺少 "
            f"{exc.name!r}。请先安装 task2/requirements.txt 中的依赖。"
        ) from exc
    return cv2, np


def _require_input_image(cv2: Any, path: Path, label: str) -> Any:
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        if not path.exists():
            raise FileNotFoundError(f"{label}不存在: {path}")
        raise ValueError(f"{label}无法由 OpenCV 读取为彩色图像: {path}")
    if getattr(image, "size", 0) == 0:
        raise ValueError(f"{label}为空图像: {path}")
    return image


def _save_image(cv2: Any, path: Path, image: Any) -> None:
    """Save one image and fail loudly if OpenCV reports a write failure."""

    if not bool(cv2.imwrite(str(path), image)):
        raise OSError(f"图像保存失败: {path}")
    if not path.is_file() or path.stat().st_size == 0:
        raise OSError(f"图像文件未生成或为空: {path}")


def _save_array(np: Any, path: Path, array: Any) -> None:
    np.save(path, array)
    if not path.is_file() or path.stat().st_size == 0:
        raise OSError(f"NumPy 数据文件未生成或为空: {path}")


def _save_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if not path.is_file() or path.stat().st_size == 0:
        raise OSError(f"参数摘要未生成或为空: {path}")


def _normalise_valid(np: Any, values: Any, valid: Any) -> Any:
    """Map valid values to 8-bit display range; invalid pixels remain black."""

    display = np.zeros(values.shape, dtype=np.uint8)
    if not bool(np.any(valid)):
        return display

    valid_values = values[valid]
    lower, upper = np.percentile(valid_values, (1.0, 99.0))
    if not np.isfinite(lower) or not np.isfinite(upper):
        return display
    if upper <= lower:
        upper = lower + 1.0

    scaled = (np.clip(values, lower, upper) - lower) / (upper - lower)
    display[valid] = np.asarray(scaled[valid] * 255.0, dtype=np.uint8)
    return display


def _matcher_parameters() -> dict[str, int]:
    return {
        "window_size": WINDOW_SIZE,
        "min_disparity": MIN_DISPARITY,
        "num_disparities": NUM_DISPARITIES,
        "block_size": BLOCK_SIZE,
        "P1": P1,
        "P2": P2,
        "disp12MaxDiff": 1,
        "uniquenessRatio": 10,
        "speckleWindowSize": 100,
        "speckleRange": 32,
    }


def _largest_valid_rectangle(np: Any, mask: Any) -> tuple[int, int, int, int]:
    """Return the largest axis-aligned rectangle fully covered by ``mask``."""

    height, width = mask.shape
    histogram = np.zeros(width, dtype=np.int32)
    best_area = 0
    best = (0, 0, 0, 0)
    for row in range(height):
        histogram = np.where(mask[row], histogram + 1, 0)
        stack: list[tuple[int, int]] = []
        for column in range(width + 1):
            current = int(histogram[column]) if column < width else 0
            start = column
            while stack and stack[-1][1] > current:
                left, bar_height = stack.pop()
                area = bar_height * (column - left)
                if area > best_area:
                    best_area = area
                    best = (left, row - bar_height + 1, column - left, bar_height)
                start = left
            if not stack or stack[-1][1] < current:
                stack.append((start, current))
    if best_area == 0:
        raise RuntimeError("无标定校正后的左右图没有共同有效区域。")
    return best


def _feature_rectification(cv2: Any, np: Any, left_gray: Any, right_gray: Any) -> dict[str, Any]:
    """Find ORB correspondences, estimate F, and return rectification data."""

    orb = cv2.ORB_create(
        nfeatures=USER_ORB_FEATURES,
        scaleFactor=1.2,
        nlevels=8,
        fastThreshold=10,
    )
    keypoints_left, descriptors_left = orb.detectAndCompute(left_gray, None)
    keypoints_right, descriptors_right = orb.detectAndCompute(right_gray, None)
    if descriptors_left is None or descriptors_right is None:
        raise RuntimeError("ORB 未能在左右图像中提取描述子，无法进行无标定校正。")

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    knn_matches = matcher.knnMatch(descriptors_left, descriptors_right, k=2)
    good_matches = [
        first
        for pair in knn_matches
        if len(pair) == 2
        for first, second in [pair]
        if first.distance < USER_MATCH_RATIO * second.distance
    ]
    if len(good_matches) < 8:
        raise RuntimeError(f"ORB 比率筛选后仅有 {len(good_matches)} 个匹配，无法估计 F。")

    points_left = np.float32(
        [keypoints_left[match.queryIdx].pt for match in good_matches]
    )
    points_right = np.float32(
        [keypoints_right[match.trainIdx].pt for match in good_matches]
    )
    fundamental, inlier_mask = cv2.findFundamentalMat(
        points_left,
        points_right,
        cv2.FM_RANSAC,
        USER_RANSAC_THRESHOLD,
        USER_RANSAC_CONFIDENCE,
    )
    if fundamental is None or inlier_mask is None or fundamental.shape != (3, 3):
        raise RuntimeError("RANSAC 未能估计有效 3x3 基础矩阵 F。")
    inliers = inlier_mask.ravel().astype(bool)
    if int(np.count_nonzero(inliers)) < 50:
        raise RuntimeError(
            f"RANSAC 内点仅 {int(np.count_nonzero(inliers))} 个，不能可靠校正。"
        )

    inlier_left = points_left[inliers]
    inlier_right = points_right[inliers]
    image_size = (int(left_gray.shape[1]), int(left_gray.shape[0]))
    success, homography_left, homography_right = cv2.stereoRectifyUncalibrated(
        inlier_left,
        inlier_right,
        fundamental,
        image_size,
        threshold=USER_RANSAC_THRESHOLD,
    )
    if not success or homography_left is None or homography_right is None:
        raise RuntimeError("stereoRectifyUncalibrated 未能返回有效校正单应矩阵。")

    def transform(homography: Any, points: Any) -> Any:
        return cv2.perspectiveTransform(points.reshape(-1, 1, 2), homography).reshape(-1, 2)

    rectified_points_left = transform(homography_left, inlier_left)
    rectified_points_right = transform(homography_right, inlier_right)
    before_dx = inlier_left[:, 0] - inlier_right[:, 0]
    before_dy = inlier_left[:, 1] - inlier_right[:, 1]
    after_dx = rectified_points_left[:, 0] - rectified_points_right[:, 0]
    after_dy = rectified_points_left[:, 1] - rectified_points_right[:, 1]

    return {
        "keypoints_left": len(keypoints_left),
        "keypoints_right": len(keypoints_right),
        "ratio_matches": len(good_matches),
        "inlier_count": int(np.count_nonzero(inliers)),
        "fundamental": fundamental,
        "homography_left": homography_left,
        "homography_right": homography_right,
        "inlier_left": inlier_left,
        "inlier_right": inlier_right,
        "rectified_points_left": rectified_points_left,
        "rectified_points_right": rectified_points_right,
        "before_dx": before_dx,
        "before_dy": before_dy,
        "after_dx": after_dx,
        "after_dy": after_dy,
    }


def _percentile_summary(np: Any, values: Any) -> dict[str, float]:
    return {
        "median": float(np.median(values)),
        "p90_abs": float(np.percentile(np.abs(values), 90.0)),
        "min": float(np.min(values)),
        "max": float(np.max(values)),
    }


def _run_uncalibrated_user(
    *,
    left_path: Path,
    right_path: Path,
    output_dir: Path,
    no_pyrdown: bool,
    cv2: Any,
    np: Any,
) -> dict[str, Any]:
    """Run the user-photo branch with feature-based uncalibrated rectification."""

    left_color = _require_input_image(cv2, left_path, "用户左图")
    right_color = _require_input_image(cv2, right_path, "用户右图")
    if left_color.shape[:2] != right_color.shape[:2]:
        raise ValueError(
            "用户左右图像尺寸不一致: "
            f"left={left_color.shape[:2]}, right={right_color.shape[:2]}"
        )
    left_gray = cv2.cvtColor(left_color, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_color, cv2.COLOR_BGR2GRAY)
    geometry = _feature_rectification(cv2, np, left_gray, right_gray)
    image_size = (left_gray.shape[1], left_gray.shape[0])
    ones = np.full(left_gray.shape, 255, dtype=np.uint8)
    valid_left = cv2.warpPerspective(
        ones, geometry["homography_left"], image_size, flags=cv2.INTER_NEAREST
    )
    valid_right = cv2.warpPerspective(
        ones, geometry["homography_right"], image_size, flags=cv2.INTER_NEAREST
    )
    common = (valid_left > 0) & (valid_right > 0)
    crop_x, crop_y, crop_width, crop_height = _largest_valid_rectangle(np, common)

    rectified_left_full = cv2.warpPerspective(
        left_color, geometry["homography_left"], image_size
    )
    rectified_right_full = cv2.warpPerspective(
        right_color, geometry["homography_right"], image_size
    )
    rectified_left = rectified_left_full[
        crop_y : crop_y + crop_height, crop_x : crop_x + crop_width
    ]
    rectified_right = rectified_right_full[
        crop_y : crop_y + crop_height, crop_x : crop_x + crop_width
    ]
    rectified_points_left = geometry["rectified_points_left"].copy()
    rectified_points_right = geometry["rectified_points_right"].copy()
    rectified_points_left -= np.array([crop_x, crop_y], dtype=np.float32)
    rectified_points_right -= np.array([crop_x, crop_y], dtype=np.float32)

    if not no_pyrdown:
        rectified_left = cv2.pyrDown(rectified_left)
        rectified_right = cv2.pyrDown(rectified_right)
        rectified_points_left /= 2.0
        rectified_points_right /= 2.0
    match_left = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2GRAY)
    match_right = cv2.cvtColor(rectified_right, cv2.COLOR_BGR2GRAY)
    if match_left.shape != match_right.shape:
        raise ValueError("校正后的左右图像尺寸不一致。")

    after_dx = rectified_points_left[:, 0] - rectified_points_right[:, 0]
    after_dy = rectified_points_left[:, 1] - rectified_points_right[:, 1]
    if float(np.percentile(np.abs(after_dy), 90.0)) > 2.0:
        raise RuntimeError("校正后垂直视差 P90 超过 2 px，拒绝生成不可靠结果。")

    matcher = cv2.StereoSGBM_create(
        minDisparity=USER_MIN_DISPARITY,
        numDisparities=USER_NUM_DISPARITIES,
        blockSize=USER_BLOCK_SIZE,
        P1=P1,
        P2=P2,
        disp12MaxDiff=1,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=32,
    )
    disparity = matcher.compute(match_left, match_right).astype(np.float32) / DISP_SCALE
    finite = np.isfinite(disparity) & (disparity > USER_MIN_DISPARITY - 1)
    positive = finite & (disparity > 0)
    if float(np.mean(positive)) < 0.05:
        raise RuntimeError("正视差有效像素少于 5%，拒绝伪造相对深度结果。")
    disparity_raw = np.where(finite, disparity, np.nan).astype(np.float32)
    with np.errstate(divide="ignore", invalid="ignore"):
        relative_depth = np.where(positive, 1.0 / disparity_raw, np.nan).astype(np.float32)

    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "left": output_dir / "left.png",
        "right": output_dir / "right.png",
        "rectified_left": output_dir / "rectified_left.png",
        "rectified_right": output_dir / "rectified_right.png",
        "rectification_check": output_dir / "rectification_check.png",
        "disparity_raw": output_dir / "disparity_raw.npy",
        "disparity_visualisation": output_dir / "disparity.png",
        "valid_mask": output_dir / "valid_mask.png",
        "relative_depth": output_dir / "depth_proxy.npy",
        "relative_depth_visualisation": output_dir / "depth_proxy.png",
        "parameters": output_dir / "params.json",
        "evidence": output_dir / "run_evidence.md",
    }
    _save_image(cv2, outputs["left"], left_color)
    _save_image(cv2, outputs["right"], right_color)
    _save_image(cv2, outputs["rectified_left"], rectified_left)
    _save_image(cv2, outputs["rectified_right"], rectified_right)
    check = np.hstack((rectified_left.copy(), rectified_right.copy()))
    for y in range(0, check.shape[0], max(1, check.shape[0] // 8)):
        cv2.line(check, (0, y), (check.shape[1] - 1, y), (0, 255, 0), 1)
    _save_image(cv2, outputs["rectification_check"], check)
    _save_array(np, outputs["disparity_raw"], disparity_raw)
    _save_image(
        cv2,
        outputs["disparity_visualisation"],
        _normalise_valid(np, disparity_raw, positive),
    )
    _save_image(cv2, outputs["valid_mask"], positive.astype(np.uint8) * 255)
    _save_array(np, outputs["relative_depth"], relative_depth)
    _save_image(
        cv2,
        outputs["relative_depth_visualisation"],
        _normalise_valid(np, relative_depth, positive),
    )

    finite_values = disparity_raw[finite]
    positive_values = disparity_raw[positive]
    valid_ratio = float(np.mean(positive))
    metadata: dict[str, Any] = {
        "input": {
            "left": str(left_path),
            "right": str(right_path),
            "left_semantics": "IMG_5572 / user-provided left photo",
            "right_semantics": "IMG_5573 / user-provided right photo",
            "order_preserved": True,
            "original_size": {
                "width": int(left_color.shape[1]),
                "height": int(left_color.shape[0]),
            },
        },
        "decode": {
            "method": "macOS qlmanage -t Quick Look thumbnail",
            "note": "sips conversion was not used because the HEIC gain map produced black output.",
            "decoded_work_images": "task2/data/user_capture/decoded/left.png and right.png",
        },
        "feature_geometry": {
            "detector": "ORB",
            "orb_features": USER_ORB_FEATURES,
            "ratio_test": USER_MATCH_RATIO,
            "keypoints_left": geometry["keypoints_left"],
            "keypoints_right": geometry["keypoints_right"],
            "ratio_matches": geometry["ratio_matches"],
            "ransac_inliers": geometry["inlier_count"],
            "fundamental_matrix": geometry["fundamental"].tolist(),
            "before_horizontal_x_left_minus_x_right": _percentile_summary(np, geometry["before_dx"]),
            "before_vertical_y_left_minus_y_right": _percentile_summary(np, geometry["before_dy"]),
            "after_horizontal_x_left_minus_x_right": _percentile_summary(np, after_dx),
            "after_vertical_y_left_minus_y_right": _percentile_summary(np, after_dy),
            "crop_xywh": [crop_x, crop_y, crop_width, crop_height],
            "crop_method": "largest axis-aligned rectangle fully covered by warped common mask",
            "homography_left": geometry["homography_left"].tolist(),
            "homography_right": geometry["homography_right"].tolist(),
        },
        "preprocessing": {
            "pyrdown": not no_pyrdown,
            "processed_size": {
                "width": int(match_left.shape[1]),
                "height": int(match_left.shape[0]),
            },
            "grayscale_for_matching": True,
        },
        "matcher": "StereoSGBM",
        "matcher_parameters": {
            "min_disparity": USER_MIN_DISPARITY,
            "num_disparities": USER_NUM_DISPARITIES,
            "block_size": USER_BLOCK_SIZE,
            "P1": P1,
            "P2": P2,
            "disp12MaxDiff": 1,
            "uniquenessRatio": 10,
            "speckleWindowSize": 100,
            "speckleRange": 32,
        },
        "disparity": {
            "definition": "x_left - x_right after rectification",
            "opencv_fixed_point_scale": DISP_SCALE,
            "finite_rule": f"finite and disparity > {USER_MIN_DISPARITY - 1}",
            "relative_depth_rule": "finite and disparity > 0",
            "finite_pixel_ratio": float(np.mean(finite)),
            "positive_pixel_ratio": valid_ratio,
            "finite_min_pixels": float(np.min(finite_values)),
            "finite_max_pixels": float(np.max(finite_values)),
            "positive_min_pixels": float(np.min(positive_values)),
            "positive_max_pixels": float(np.max(positive_values)),
            "negative_or_zero_finite_count": int(np.count_nonzero(finite & ~positive)),
            "unit": "pixels",
        },
        "relative_depth": {
            "formula": "1 / disparity for positive disparity only",
            "array_file": outputs["relative_depth"].name,
            "scale": "arbitrary",
            "unit": None,
            "metric_depth_available": False,
            "note": "No user-provided physical baseline; no metric depth or metric point cloud is claimed.",
        },
        "runtime": {
            "python": sys.version,
            "python_version": platform.python_version(),
            "opencv": cv2.__version__,
            "numpy": np.__version__,
            "command": " ".join(sys.argv),
        },
        "outputs": {key: str(path) for key, path in outputs.items()},
    }
    _save_json(outputs["parameters"], metadata)
    evidence = f"""# 用户自摄双目结果证据

状态：`DONE_WITH_CONCERNS`

- 左图语义：`IMG_5572`；右图语义：`IMG_5573`；顺序未交换。
- HEIC 使用 macOS `qlmanage -t` 解码；`sips` 未用于生成工作图，因为 HDR gain map 会产生黑图。
- ORB 比率筛选匹配：{geometry['ratio_matches']}；F-RANSAC 内点：{geometry['inlier_count']}。
- 校正前垂直视差中位数/P90(abs)：{float(np.median(geometry['before_dy'])):.4f} / {float(np.percentile(np.abs(geometry['before_dy']), 90)):.4f} px。
- 校正后垂直视差中位数/P90(abs)：{float(np.median(after_dy)):.4f} / {float(np.percentile(np.abs(after_dy), 90)):.4f} px。
- 校正后 `x_left - x_right` 中位数：{float(np.median(after_dx)):.4f} px；未交换左右语义。
- 有限视差比例：{float(np.mean(finite)):.6%}；正视差比例：{valid_ratio:.6%}。
- 正视差范围：{float(np.min(positive_values)):.4f} .. {float(np.max(positive_values)):.4f} px。
- 相对深度范围：{float(np.nanmin(relative_depth)):.8f} .. {float(np.nanmax(relative_depth)):.8f}（任意尺度）。
- 裁剪：最大共同有效轴对齐矩形 `{crop_x},{crop_y},{crop_width},{crop_height}`，不是手工凭感觉裁剪。
- 限制：未提供实际基线，不能声称米制绝对深度。
"""
    outputs["evidence"].write_text(evidence, encoding="utf-8")
    return metadata


def run(
    *,
    left_path: Path,
    right_path: Path,
    output_dir: Path,
    no_pyrdown: bool,
    cv2: Any,
    np: Any,
) -> dict[str, Any]:
    """Run the complete image-to-result pipeline and return run metadata."""

    left_color = _require_input_image(cv2, left_path, "左图")
    right_color = _require_input_image(cv2, right_path, "右图")
    if left_color.shape[:2] != right_color.shape[:2]:
        raise ValueError(
            "左右图像尺寸不一致: "
            f"left={left_color.shape[:2]}, right={right_color.shape[:2]}"
        )

    left_gray = cv2.cvtColor(left_color, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_color, cv2.COLOR_BGR2GRAY)

    if no_pyrdown:
        left_processed = left_color
        right_processed = right_color
        left_match = left_gray
        right_match = right_gray
    else:
        left_processed = cv2.pyrDown(left_color)
        right_processed = cv2.pyrDown(right_color)
        left_match = cv2.pyrDown(left_gray)
        right_match = cv2.pyrDown(right_gray)

    if left_match.shape != right_match.shape:
        raise ValueError(
            "预处理后的左右图像尺寸不一致: "
            f"left={left_match.shape}, right={right_match.shape}"
        )
    height, width = left_match.shape[:2]
    minimum_width = MIN_DISPARITY + NUM_DISPARITIES + BLOCK_SIZE
    if width <= minimum_width:
        raise ValueError(
            f"匹配图像宽度 {width} 太小；至少需要大于 {minimum_width} 像素。"
        )

    matcher = cv2.StereoSGBM_create(
        minDisparity=MIN_DISPARITY,
        numDisparities=NUM_DISPARITIES,
        blockSize=BLOCK_SIZE,
        P1=P1,
        P2=P2,
        disp12MaxDiff=1,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=32,
    )
    disparity = matcher.compute(left_match, right_match).astype(np.float32) / DISP_SCALE
    valid = np.isfinite(disparity) & (disparity > MIN_DISPARITY - 1)
    if not bool(np.any(valid)):
        raise RuntimeError("StereoSGBM 未产生有效视差像素，无法生成相对深度。")

    disparity_raw = np.where(valid, disparity, np.nan).astype(np.float32)
    with np.errstate(divide="ignore", invalid="ignore"):
        relative_depth = np.where(valid, 1.0 / disparity_raw, np.nan).astype(np.float32)

    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "left": output_dir / "left.png",
        "right": output_dir / "right.png",
        "disparity_raw": output_dir / "disparity_raw.npy",
        "disparity_visualisation": output_dir / "disparity.png",
        "valid_mask": output_dir / "valid_mask.png",
        "relative_depth": output_dir / "depth_proxy.npy",
        "relative_depth_visualisation": output_dir / "depth_proxy.png",
        "parameters": output_dir / "params.json",
    }

    _save_image(cv2, outputs["left"], left_processed)
    _save_image(cv2, outputs["right"], right_processed)
    _save_array(np, outputs["disparity_raw"], disparity_raw)
    _save_image(
        cv2,
        outputs["disparity_visualisation"],
        _normalise_valid(np, disparity_raw, valid),
    )
    _save_image(cv2, outputs["valid_mask"], valid.astype(np.uint8) * 255)
    _save_array(np, outputs["relative_depth"], relative_depth)
    _save_image(
        cv2,
        outputs["relative_depth_visualisation"],
        _normalise_valid(np, relative_depth, valid),
    )

    valid_values = disparity[valid]
    valid_ratio = float(np.count_nonzero(valid)) / float(valid.size)
    metadata: dict[str, Any] = {
        "input": {
            "left": str(left_path),
            "right": str(right_path),
            "original_size": {
                "width": int(left_color.shape[1]),
                "height": int(left_color.shape[0]),
            },
        },
        "preprocessing": {
            "pyrdown": not no_pyrdown,
            "processed_size": {"width": int(width), "height": int(height)},
            "grayscale_for_matching": True,
        },
        "matcher": "StereoSGBM",
        "matcher_parameters": _matcher_parameters(),
        "disparity": {
            "opencv_fixed_point_scale": DISP_SCALE,
            "invalid_rule": f"finite and disparity > {MIN_DISPARITY - 1}",
            "valid_pixel_ratio": valid_ratio,
            "valid_min_pixels": float(np.min(valid_values)),
            "valid_max_pixels": float(np.max(valid_values)),
            "unit": "pixels",
        },
        "relative_depth": {
            "formula": "1 / disparity",
            "array_file": outputs["relative_depth"].name,
            "scale": "arbitrary",
            "unit": None,
            "metric_depth_available": False,
            "note": "No verified focal length, baseline, or Q matrix was supplied for aloe.",
        },
        "runtime": {
            "python": sys.version,
            "python_version": platform.python_version(),
            "opencv": cv2.__version__,
            "numpy": np.__version__,
            "command": " ".join(sys.argv),
        },
        "outputs": {key: str(path) for key, path in outputs.items()},
    }
    _save_json(outputs["parameters"], metadata)
    return metadata


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    left_path = _resolve_user_path(args.left, PROJECT_ROOT)
    right_path = _resolve_user_path(args.right, PROJECT_ROOT)
    output_dir = _resolve_user_path(args.out_dir, PROJECT_ROOT)

    try:
        cv2, np = _load_dependencies()
        if args.rectify_uncalibrated:
            metadata = _run_uncalibrated_user(
                left_path=left_path,
                right_path=right_path,
                output_dir=output_dir,
                no_pyrdown=args.no_pyrdown,
                cv2=cv2,
                np=np,
            )
        else:
            metadata = run(
                left_path=left_path,
                right_path=right_path,
                output_dir=output_dir,
                no_pyrdown=args.no_pyrdown,
                cv2=cv2,
                np=np,
            )
    except (FileNotFoundError, OSError, RuntimeError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1

    disparity = metadata["disparity"]
    print("双目深度估计完成（相对深度，不是米制绝对深度）")
    print(f"左图输入: {metadata['input']['left']}")
    print(f"右图输入: {metadata['input']['right']}")
    if args.rectify_uncalibrated:
        print(f"RANSAC 内点数: {metadata['feature_geometry']['ransac_inliers']}")
        print(
            "校正后垂直视差 median/P90(abs): "
            f"{metadata['feature_geometry']['after_vertical_y_left_minus_y_right']['median']:.3f} / "
            f"{metadata['feature_geometry']['after_vertical_y_left_minus_y_right']['p90_abs']:.3f} px"
        )
        print(f"正视差有效像素比例: {disparity['positive_pixel_ratio']:.2%}")
        print(
            "正 disparity 范围: "
            f"{disparity['positive_min_pixels']:.3f} .. "
            f"{disparity['positive_max_pixels']:.3f} px"
        )
    else:
        print(f"有效视差像素比例: {disparity['valid_pixel_ratio']:.2%}")
        print(
            "有效 disparity 范围: "
            f"{disparity['valid_min_pixels']:.3f} .. "
            f"{disparity['valid_max_pixels']:.3f} px"
        )
    print("relative_depth: 1 / disparity（无单位，任意尺度）")
    print(f"结果目录: {output_dir}")
    for name, path in metadata["outputs"].items():
        print(f"  {name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
