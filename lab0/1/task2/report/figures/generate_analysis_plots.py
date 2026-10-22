#!/usr/bin/env python3
"""Generate report figures from the official camera calibration result.

The script deliberately plots per-view observables and model responses.  It does
not present the single global camera matrix or distortion vector as 18 separate
intrinsic estimates.
"""

from pathlib import Path

import cv2
import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


ROOT = Path(__file__).resolve().parents[3]
FIGURES = Path(__file__).resolve().parent
RESULT = ROOT / "task2" / "output" / "camera_params.npz"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "legend.fontsize": 8,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.unicode_minus": False,
    }
)


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(FIGURES / filename, format="pdf", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def rodrigues(vector: np.ndarray) -> np.ndarray:
    """Return the rotation matrix for an OpenCV Rodrigues vector."""

    theta = float(np.linalg.norm(vector))
    if theta < 1e-12:
        return np.eye(3)
    axis = vector / theta
    x, y, z = axis
    skew = np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])
    return np.eye(3) * np.cos(theta) + (1.0 - np.cos(theta)) * np.outer(axis, axis) + np.sin(theta) * skew


def load_result() -> dict[str, np.ndarray]:
    with np.load(RESULT, allow_pickle=False) as data:
        return {key: data[key] for key in data.files}


def plot_per_image_rms(data: dict[str, np.ndarray]) -> None:
    errors = data["per_image_reprojection_error"].astype(float)
    names = [Path(str(path)).stem.replace("IMG_", "") for path in data["valid_image_paths"]]
    x = np.arange(len(errors))
    median = float(np.median(errors))
    global_rms = float(data["rms_error"])
    mean = float(data["mean_per_image_rms"])
    colors = ["#4C78A8"] * len(errors)
    colors[int(np.argmax(errors))] = "#D62728"
    colors[int(np.argmin(errors))] = "#2CA02C"

    fig, ax = plt.subplots(figsize=(8.0, 3.5))
    ax.bar(x, errors, color=colors, edgecolor="white", linewidth=0.5)
    ax.axhline(median, color="#F58518", linewidth=1.3, label=f"Median: {median:.3f} px")
    ax.axhline(global_rms, color="#D62728", linestyle="--", linewidth=1.1, label=f"Global OpenCV RMS: {global_rms:.3f} px")
    ax.axhline(mean, color="#54A24B", linestyle=":", linewidth=1.3, label=f"Mean per-image RMS: {mean:.3f} px")
    ax.set_xlabel("Valid image (filename suffix)")
    ax.set_ylabel("RMS reprojection error (pixels)")
    ax.set_title("Reprojection error varies across the 18 valid views")
    ax.set_xticks(x, names, rotation=45, ha="right")
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.grid(axis="y", alpha=0.25)
    ax.legend(loc="upper left", frameon=True)
    ax.text(
        0.995,
        0.97,
        f"min={errors.min():.3f} px\nmax={errors.max():.3f} px",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8,
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "alpha": 0.8, "edgecolor": "0.75"},
    )
    save(fig, "per_image_rms.pdf")


def plot_translation(data: dict[str, np.ndarray]) -> None:
    translations = data["translation_vectors"].reshape(-1, 3).astype(float)
    names = [Path(str(path)).stem.replace("IMG_", "") for path in data["valid_image_paths"]]
    x = np.arange(len(translations))
    distance = np.linalg.norm(translations, axis=1)

    fig, axes = plt.subplots(2, 1, figsize=(8.0, 5.2), sharex=True, constrained_layout=True)
    axes[0].plot(x, translations[:, 0], "o-", label="$t_x$")
    axes[0].plot(x, translations[:, 1], "s-", label="$t_y$")
    axes[0].plot(x, translations[:, 2], "^-", label="$t_z$")
    axes[0].axhline(0.0, color="0.55", linewidth=0.8)
    axes[0].set_ylabel("Translation component (cm)")
    axes[0].set_title("Estimated checkerboard pose changes across views")
    axes[0].legend(ncol=3, loc="upper left")
    axes[0].grid(alpha=0.25)
    axes[1].plot(x, distance, "o-", color="#6A3D9A", label="$||t||$")
    axes[1].set_ylabel("Board-origin distance (cm)")
    axes[1].set_xlabel("Valid image (filename suffix)")
    axes[1].legend(loc="upper left")
    axes[1].grid(alpha=0.25)
    axes[1].set_xticks(x, names, rotation=45, ha="right")
    save(fig, "pose_translation.pdf")


def plot_orientation(data: dict[str, np.ndarray]) -> None:
    rvecs = data["rotation_vectors"].reshape(-1, 3).astype(float)
    names = [Path(str(path)).stem.replace("IMG_", "") for path in data["valid_image_paths"]]
    x = np.arange(len(rvecs))
    rnorm = np.degrees(np.linalg.norm(rvecs, axis=1))
    tilt = []
    for rvec in rvecs:
        rotation = rodrigues(rvec)
        board_normal_in_camera = rotation[:, 2]
        tilt.append(np.degrees(np.arccos(np.clip(board_normal_in_camera[2], -1.0, 1.0))))
    tilt = np.asarray(tilt)

    fig, axes = plt.subplots(2, 1, figsize=(8.0, 5.2), sharex=True, constrained_layout=True)
    axes[0].plot(x, rvecs[:, 0], "o-", label="$r_x$")
    axes[0].plot(x, rvecs[:, 1], "s-", label="$r_y$")
    axes[0].plot(x, rvecs[:, 2], "^-", label="$r_z$")
    axes[0].set_ylabel("Rodrigues component (rad)")
    axes[0].set_title("Orientation estimates and board tilt")
    axes[0].legend(ncol=3, loc="upper left")
    axes[0].grid(alpha=0.25)
    axes[1].plot(x, rnorm, "o-", label="$||r||$ (axis-angle norm)")
    axes[1].plot(x, tilt, "s-", label="Board-normal tilt")
    axes[1].set_ylabel("Angle (degrees)")
    axes[1].set_xlabel("Valid image (filename suffix)")
    axes[1].legend(loc="upper left")
    axes[1].grid(alpha=0.25)
    axes[1].set_xticks(x, names, rotation=45, ha="right")
    save(fig, "pose_orientation.pdf")


def plot_distortion(data: dict[str, np.ndarray]) -> None:
    camera_matrix = data["camera_matrix"].astype(float)
    k1, k2, p1, p2, k3 = data["distortion_coefficients"].reshape(-1).astype(float)[:5]
    width, height = data["image_size"].astype(float)
    cx, cy = camera_matrix[0, 2], camera_matrix[1, 2]
    fx, fy = camera_matrix[0, 0], camera_matrix[1, 1]
    image_corners = np.array(
        [[0, 0], [width, 0], [0, height], [width, height]], dtype=float
    )
    normalized_corners = (image_corners - np.array([cx, cy])) / np.array([fx, fy])
    max_radius = float(np.linalg.norm(normalized_corners, axis=1).max())
    radii = np.linspace(0.0, max_radius, 300)
    radial_scale = 1.0 + k1 * radii**2 + k2 * radii**4 + k3 * radii**6

    angles = np.linspace(0.0, 2.0 * np.pi, 720, endpoint=False)
    x = radii[:, None] * np.cos(angles)[None, :]
    y = radii[:, None] * np.sin(angles)[None, :]
    r2 = x * x + y * y
    radial = 1.0 + k1 * r2 + k2 * r2**2 + k3 * r2**3
    x_tangential = 2.0 * p1 * x * y + p2 * (r2 + 2.0 * x * x)
    y_tangential = p1 * (r2 + 2.0 * y * y) + 2.0 * p2 * x * y
    tangential_magnitude = np.sqrt(x_tangential**2 + y_tangential**2)
    tangent_q10, tangent_median, tangent_q90 = np.percentile(
        tangential_magnitude, [10, 50, 90], axis=1
    )

    fig, axes = plt.subplots(2, 1, figsize=(7.8, 5.2), sharex=True, constrained_layout=True)
    axes[0].plot(radii, radial_scale, color="#1F77B4", linewidth=1.8)
    axes[0].axhline(1.0, color="0.5", linestyle="--", linewidth=0.9)
    axes[0].set_ylabel("Radial scale factor")
    axes[0].set_title("Distortion response computed from the global OpenCV model")
    axes[0].grid(alpha=0.25)
    axes[1].fill_between(radii, tangent_q10, tangent_q90, color="#FF7F0E", alpha=0.25, label="10th-90th percentile over angle")
    axes[1].plot(radii, tangent_median, color="#D95F02", linewidth=1.8, label="Median tangential displacement")
    axes[1].set_xlabel("Normalized radius $r$")
    axes[1].set_ylabel("Tangential displacement\n(normalized units)")
    axes[1].legend(loc="upper left")
    axes[1].grid(alpha=0.25)
    save(fig, "distortion_profile.pdf")


def plot_corner_coverage(data: dict[str, np.ndarray]) -> None:
    checkerboard = tuple(int(value) for value in data["checkerboard"])
    valid_paths = [Path(str(path)) for path in data["valid_image_paths"]]
    all_points = []
    width, height = (int(value) for value in data["image_size"])
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    find_flags = cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE
    for path in valid_paths:
        image_path = path if path.is_absolute() else ROOT / path
        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise RuntimeError(f"Cannot read calibration image: {image_path}")
        found, corners = cv2.findChessboardCorners(image, checkerboard, flags=find_flags)
        if not found:
            raise RuntimeError(f"Corner detection failed while plotting: {image_path}")
        corners = cv2.cornerSubPix(image, corners, (11, 11), (-1, -1), criteria)
        all_points.append(corners.reshape(-1, 2) / np.array([width, height]))
    points = np.concatenate(all_points, axis=0)

    fig, ax = plt.subplots(figsize=(6.2, 5.0))
    ax.scatter(points[:, 0], points[:, 1], s=5, alpha=0.22, color="#1F77B4", edgecolors="none")
    ax.scatter([0.5], [0.5], marker="+", s=90, linewidths=1.5, color="#D62728", label="Image center")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(1.0, 0.0)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("Normalized image x coordinate")
    ax.set_ylabel("Normalized image y coordinate")
    ax.set_title(f"Detected corner coverage ({len(valid_paths)} views, {len(points)} corners)")
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right")
    save(fig, "corner_coverage.pdf")


def main() -> None:
    data = load_result()
    plot_per_image_rms(data)
    plot_translation(data)
    plot_orientation(data)
    plot_distortion(data)
    plot_corner_coverage(data)
    print("Generated: per_image_rms.pdf, pose_translation.pdf, pose_orientation.pdf, distortion_profile.pdf, corner_coverage.pdf")


if __name__ == "__main__":
    main()
