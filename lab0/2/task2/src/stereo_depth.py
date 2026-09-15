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
