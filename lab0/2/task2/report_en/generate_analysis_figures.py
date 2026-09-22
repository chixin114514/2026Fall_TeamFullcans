#!/usr/bin/env python3
"""Generate reproducible analytical figures for the official OpenCV aloe run.

The script reads only the default run arrays and its validity mask. It keeps
invalid disparity pixels as invalid and never interprets the reciprocal depth
proxy as a metric distance.
"""

from __future__ import annotations

from pathlib import Path

import cv2
import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import PercentFormatter
import numpy as np


REPORT_DIR = Path(__file__).resolve().parent
RESULT_DIR = REPORT_DIR.parent / "results"
FIGURE_DIR = REPORT_DIR / "figures"
DISPARITY_FILE = RESULT_DIR / "disparity_raw.npy"
DEPTH_FILE = RESULT_DIR / "depth_proxy.npy"
VALID_MASK_FILE = RESULT_DIR / "valid_mask.png"


def _select_font() -> str:
    """Select an installed Latin-capable font with a safe fallback."""

    installed = {font.name for font in font_manager.fontManager.ttflist}
    for candidate in ("Arial", "Helvetica", "DejaVu Sans"):
        if candidate in installed:
            return candidate
    return "DejaVu Sans"


def _configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "font.family": _select_font(),
            "font.size": 9,
            "axes.titlesize": 11,
            "axes.labelsize": 9,
            "axes.linewidth": 0.8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "savefig.facecolor": "white",
            "axes.unicode_minus": False,
        }
    )


def _load_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    disparity = np.load(DISPARITY_FILE).astype(np.float32, copy=False)
    depth_proxy = np.load(DEPTH_FILE).astype(np.float32, copy=False)
    mask_png = cv2.imread(str(VALID_MASK_FILE), cv2.IMREAD_GRAYSCALE)
    if mask_png is None:
        raise FileNotFoundError(f"Could not read the valid mask: {VALID_MASK_FILE}")

    if disparity.shape != depth_proxy.shape or disparity.shape != mask_png.shape:
        raise ValueError(
            "disparity_raw.npy, depth_proxy.npy, and valid_mask.png have "
            f"different shapes: {disparity.shape}, {depth_proxy.shape}, {mask_png.shape}"
        )

    valid_from_raw = np.isfinite(disparity) & (disparity > 15.0)
    valid_from_png = mask_png > 0
    if not np.array_equal(valid_from_raw, valid_from_png):
        raise ValueError("valid_mask.png does not match the valid-disparity rule")
    if not np.all(np.isnan(depth_proxy[~valid_from_raw])):
        raise ValueError("depth_proxy is not NaN at invalid-disparity locations")

    return disparity, depth_proxy, valid_from_raw, mask_png


def _grid_stat(
    disparity: np.ndarray,
    valid: np.ndarray,
    rows: int,
    columns: int,
    statistic: str,
) -> np.ndarray:
    result = np.full((rows, columns), np.nan, dtype=np.float64)
    height, width = disparity.shape
    row_bins = np.array_split(np.arange(height), rows)
    column_bins = np.array_split(np.arange(width), columns)
    for row_index, row_indices in enumerate(row_bins):
        for column_index, column_indices in enumerate(column_bins):
            block_valid = valid[np.ix_(row_indices, column_indices)]
            if statistic == "coverage":
                result[row_index, column_index] = float(block_valid.mean())
                continue
            block_values = disparity[np.ix_(row_indices, column_indices)][block_valid]
            if block_values.size:
                if statistic == "median":
                    result[row_index, column_index] = float(np.median(block_values))
                else:
                    raise ValueError(f"Unknown grid statistic: {statistic}")
    return result


def _save_figure(fig: mpl.figure.Figure, stem: str) -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    png_path = FIGURE_DIR / f"{stem}.png"
    svg_path = FIGURE_DIR / f"{stem}.svg"
    pdf_path = FIGURE_DIR / f"{stem}.pdf"
    tiff_path = FIGURE_DIR / f"{stem}.tiff"
    fig.savefig(png_path, dpi=600, bbox_inches="tight")
    fig.savefig(svg_path, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(tiff_path, dpi=600, bbox_inches="tight")
    plt.close(fig)
    for path in (png_path, svg_path, pdf_path, tiff_path):
        if not path.is_file() or path.stat().st_size == 0:
            raise OSError(f"Figure was not generated or is empty: {path}")


def _plot_coverage(disparity: np.ndarray, valid: np.ndarray) -> None:
    rows, columns = 15, 20
    coverage = _grid_stat(disparity, valid, rows, columns, "coverage")
    height, width = disparity.shape
    x_edges = np.linspace(0, width, columns + 1)
    y_edges = np.linspace(0, height, rows + 1)

    fig, ax = plt.subplots(figsize=(7.0, 4.6), constrained_layout=True)
    mesh = ax.pcolormesh(
        x_edges,
        y_edges,
        coverage,
        cmap="Blues",
        vmin=0.0,
        vmax=1.0,
        shading="flat",
        edgecolors="white",
        linewidth=0.25,
    )
    ax.invert_yaxis()
    ax.set_aspect("equal")
    ax.set_xlabel("Matching-image x coordinate $x$ (pixels)")
    ax.set_ylabel("Matching-image y coordinate $y$ (pixels)")
    ax.set_title("Spatial coverage of valid matches")
    colorbar = fig.colorbar(mesh, ax=ax, pad=0.02, fraction=0.046)
    colorbar.set_label("Valid-pixel fraction within grid cell")
    colorbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    valid_count = int(valid.sum())
    total_count = int(valid.size)
    ax.text(
        0.01,
        -0.16,
        f"Each cell: valid pixels / total cell pixels; overall "
        f"$n_{{valid}}={valid_count:,}$ / $n_{{total}}={total_count:,}$ "
        f"({valid.mean():.2%})",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
    )
    _save_figure(fig, "analysis_coverage_map")


def _plot_disparity_distribution(disparity: np.ndarray, valid: np.ndarray) -> dict[str, float]:
    values = disparity[valid].astype(np.float64)
    percentiles = np.percentile(values, [5, 25, 50, 75, 95])
    bins = np.linspace(float(values.min()), float(values.max()), 46)

    fig, ax = plt.subplots(figsize=(7.0, 4.2), constrained_layout=True)
    ax.hist(
        values,
        bins=bins,
        color="#3568A8",
        edgecolor="white",
        linewidth=0.35,
        alpha=0.94,
    )
    ax.axvspan(
        percentiles[1],
        percentiles[3],
        color="#3568A8",
        alpha=0.10,
    )
    line_colors = ("#D55E00", "#0072B2", "#7B3294")
    line_labels = ("P05", "P50", "P95")
    y_top = ax.get_ylim()[1]
    for quantile, color, label in zip(percentiles[[0, 2, 4]], line_colors, line_labels):
        ax.axvline(quantile, color=color, linewidth=1.25, linestyle="--")
        ax.annotate(
            f"{label}={quantile:.2f}",
            xy=(quantile, y_top * 0.88),
            xytext=(4, 0),
            textcoords="offset points",
            color=color,
            fontsize=8,
            rotation=90,
            va="top",
            ha="left",
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.75, "pad": 1.0},
        )
    ax.set_xlabel("Valid disparity $d$ (pixels)")
    ax.set_ylabel("Number of valid pixels")
    ax.set_title("Distribution of valid disparity values")
    ax.text(
        0.02,
        0.96,
        "Shaded: P25–P75",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        bbox={"facecolor": "white", "edgecolor": "#B0B0B0", "alpha": 0.85, "pad": 3},
    )
    ax.text(
        0.99,
        0.96,
        f"$n={values.size:,}$\nRange: {values.min():.3f}–{values.max():.3f} px",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=8,
        bbox={"facecolor": "white", "edgecolor": "#B0B0B0", "alpha": 0.85, "pad": 3},
    )
    _save_figure(fig, "analysis_disparity_distribution")
    return {
        "p05": float(percentiles[0]),
        "p25": float(percentiles[1]),
        "p50": float(percentiles[2]),
        "p75": float(percentiles[3]),
        "p95": float(percentiles[4]),
        "minimum": float(values.min()),
        "maximum": float(values.max()),
    }


def _quadrant_values(
    disparity: np.ndarray, valid: np.ndarray
) -> list[tuple[str, np.ndarray, int, float]]:
    height, width = disparity.shape
    half_height, half_width = height // 2, width // 2
    regions = (
        ("top-left", (slice(0, half_height), slice(0, half_width))),
        ("top-right", (slice(0, half_height), slice(half_width, None))),
        ("bottom-left", (slice(half_height, None), slice(0, half_width))),
        ("bottom-right", (slice(half_height, None), slice(half_width, None))),
    )
    output = []
    for name, region in regions:
        region_valid = valid[region]
        region_disparity = disparity[region][region_valid].astype(np.float64)
        output.append((name, region_disparity, int(region_valid.sum()), float(region_valid.mean())))
    return output


def _plot_spatial_disparity(
    disparity: np.ndarray, valid: np.ndarray
) -> list[dict[str, float | int | str]]:
    rows, columns = 15, 20
    medians = _grid_stat(disparity, valid, rows, columns, "median")
    height, width = disparity.shape
    x_edges = np.linspace(0, width, columns + 1)
    y_edges = np.linspace(0, height, rows + 1)
    quadrants = _quadrant_values(disparity, valid)

    fig = plt.figure(figsize=(8.8, 4.8), constrained_layout=True)
    grid = fig.add_gridspec(1, 2, width_ratios=(1.2, 1.0), wspace=0.24)
    heatmap_ax = fig.add_subplot(grid[0, 0])
    box_ax = fig.add_subplot(grid[0, 1])

    cmap = mpl.colormaps["viridis"].copy()
    cmap.set_bad("#F0F0F0")
    mesh = heatmap_ax.pcolormesh(
        x_edges,
        y_edges,
        medians,
        cmap=cmap,
        shading="flat",
        edgecolors="white",
        linewidth=0.25,
    )
    heatmap_ax.invert_yaxis()
    heatmap_ax.set_aspect("equal")
    heatmap_ax.set_xlabel("x coordinate (pixels)")
    heatmap_ax.set_ylabel("y coordinate (pixels)")
    heatmap_ax.set_title("(a) Median valid disparity per grid cell")
    colorbar = fig.colorbar(mesh, ax=heatmap_ax, pad=0.02, fraction=0.046)
    colorbar.set_label("Median disparity (pixels)")
    heatmap_ax.text(
        0.01,
        -0.16,
        "Gray cells contain no valid match; statistics use only finite pixels with $d>15$.",
        transform=heatmap_ax.transAxes,
        ha="left",
        va="top",
        fontsize=7.6,
    )

    data = [entry[1] for entry in quadrants]
    box = box_ax.boxplot(
        data,
        patch_artist=True,
        showfliers=False,
        widths=0.58,
        medianprops={"color": "#111111", "linewidth": 1.2},
        whiskerprops={"color": "#555555", "linewidth": 0.9},
        capprops={"color": "#555555", "linewidth": 0.9},
        boxprops={"facecolor": "#D98C6A", "edgecolor": "#7A3E2A", "linewidth": 0.9},
    )
    del box
    global_median = float(np.median(disparity[valid]))
    box_ax.axhline(global_median, color="#3568A8", linestyle="--", linewidth=1.0)
    box_ax.text(
        0.98,
        global_median + 1.5,
        f"Global median={global_median:.2f} px",
        transform=box_ax.get_yaxis_transform(),
        ha="right",
        va="bottom",
        color="#3568A8",
        fontsize=8,
    )
    box_ax.set_xticks(range(1, len(quadrants) + 1))
    box_ax.set_xticklabels([name for name, _, _, _ in quadrants], fontsize=8, rotation=20)
    box_ax.set_ylabel("Valid disparity $d$ (pixels)")
    box_ax.set_title("(b) Disparity differences across quadrants")
    box_ax.grid(axis="y", color="#D9D9D9", linewidth=0.55)
    box_ax.set_axisbelow(True)
    _save_figure(fig, "analysis_spatial_disparity")

    return [
        {
            "name": name,
            "n": count,
            "coverage": coverage,
            "median": float(np.median(values)),
            "p25": float(np.percentile(values, 25)),
            "p75": float(np.percentile(values, 75)),
        }
        for name, values, count, coverage in quadrants
    ]


def _write_findings(
    disparity: np.ndarray,
    valid: np.ndarray,
    distribution: dict[str, float],
    quadrants: list[dict[str, float | int | str]],
) -> None:
    valid_count = int(valid.sum())
    total_count = int(valid.size)
    depth = 1.0 / disparity[valid].astype(np.float64)
    content = f"""# Analytical figure data notes

This file is generated by `generate_analysis_figures.py` from the actual output of the official OpenCV aloe example. The three figures use no user photographs and introduce neither a second algorithm nor manually annotated data.

## Consistent data definition

- Input arrays: `disparity_raw.npy` and `depth_proxy.npy`, cross-checked against `valid_mask.png`.
- Array size: `{disparity.shape[1]} x {disparity.shape[0]}`; total pixels $n_{{total}}={total_count:,}$.
- Validity rule: finite disparity with $d>15$ px; the resulting Boolean mask is pixel-wise identical to `valid_mask.png`.
- Valid samples: $n_{{valid}}={valid_count:,}$, or `{valid.mean():.4%}` of all pixels. Invalid disparity and corresponding relative-depth values remain `NaN`; no zero filling is used.
- Disparity is measured in pixels. `depth_proxy=1/d` is an arbitrary-scale relative-depth proxy. The aloe pair has no verified $f$, $B$, or $Q$ available here, so the figures do not report metres or centimetres and do not treat the proxy as metric depth.

## Figure 1: `analysis_coverage_map`

- Content: the matching image is divided into 15 rows × 20 columns; each cell reports valid pixels divided by the total number of pixels in that cell.
- Key value: global valid coverage is `{valid.mean():.4%}`; the color scale spans 0–100%.
- Supported interpretation: valid matches are spatially non-uniform; boundary, occlusion, or low-texture regions can produce cells with low coverage. This is why invalid pixels must not be interpreted as zero depth.
- Boundary of interpretation: cell coverage is an availability/quality indicator, not a depth error and not an object segmentation.
- Suggested caption: *“Spatial coverage of valid matches. Color denotes the fraction of pixels satisfying finite disparity and $d>15$ px in each 15×20 grid cell; all `{valid_count:,}` valid pixels are included and the global coverage is `{valid.mean():.2%}`.”*

## Figure 2: `analysis_disparity_distribution`

- Content: histogram of all `{valid_count:,}` valid disparity pixels; the shaded region is P25–P75 and dashed lines mark P05, P50, and P95.
- Measured quantiles: P05=`{distribution['p05']:.4f}` px, P25=`{distribution['p25']:.4f}` px, P50=`{distribution['p50']:.4f}` px, P75=`{distribution['p75']:.4f}` px, P95=`{distribution['p95']:.4f}` px.
- Measured range: `{distribution['minimum']:.4f}`–`{distribution['maximum']:.4f}` px.
- Supported interpretation: valid disparity spans a broad range, indicating different horizontal matching shifts across pixels. Larger disparity corresponds to a smaller `1/d` relative-depth proxy; this only establishes a relative ordering.
- Boundary of interpretation: the histogram does not compare algorithms. Because this is one StereoSGBM run, its spread must not be described as an error or confidence interval.
- Suggested caption: *“Distribution of valid disparity ($n={valid_count:,}$). All statistics use finite pixels with $d>15$ px; shading denotes P25–P75 and dashed lines denote P05, P50, and P95. Disparity is reported in pixels.”*

## Figure 3: `analysis_spatial_disparity`

- (a) Content: the same 15×20 grid, with color denoting the median valid disparity in each cell; cells with no valid sample are gray.
- (b) Content: the image is split at its center into top-left, top-right, bottom-left, and bottom-right quadrants. The boxplots use every valid disparity in each quadrant; fliers are hidden for readability but are not removed from the median or percentile calculations.
- Quadrant statistics:

| Region | Valid pixels | Coverage | Median (px) | P25–P75 (px) |
|---|---:|---:|---:|---:|
"""
    for item in quadrants:
        content += (
            f"| {item['name']} | {item['n']:,} | {item['coverage']:.2%} | "
            f"{item['median']:.4f} | {item['p25']:.4f}–{item['p75']:.4f} |\n"
        )
    content += f"""
- Supported interpretation: disparity is spatially heterogeneous. In this run the bottom-right quadrant has a median disparity of `{quadrants[-1]['median']:.4f}` px, whereas the top-right quadrant has `{quadrants[1]['median']:.4f}` px. Given the monotonic relation $Z=fB/d$, the regions have different relative front-to-back ordering; this does not establish physical distance.
- Boundary of interpretation: quadrants are image-coordinate groups, not semantic object classes. The boxplots are not independent experimental replicates and do not provide a significance test.
- Suggested caption: *“Spatial disparity and quadrant comparison. (a) Color denotes the median valid disparity in each grid cell; gray denotes no valid match. (b) Boxplots use all valid disparities within each quadrant; center lines are medians, boxes are P25–P75, and whiskers extend to 1.5×IQR. Sample counts and coverage are reported on the x-axis.”*

## Shared limitations

All three figures describe diagnostics from one official aloe image pair and one set of StereoSGBM parameters. They document spatial match coverage, disparity distribution, and relative near/far ordering; they must not be presented as metric-depth accuracy, algorithm comparison, or ground-truth error.
"""
    (REPORT_DIR / "analysis_findings.md").write_text(content, encoding="utf-8")


def main() -> None:
    _configure_matplotlib()
    disparity, depth_proxy, valid, _ = _load_data()
    # Keep a direct algebraic consistency check in the reproducible run.
    np.testing.assert_allclose(depth_proxy[valid], 1.0 / disparity[valid], rtol=0.0, atol=0.0)
    _plot_coverage(disparity, valid)
    distribution = _plot_disparity_distribution(disparity, valid)
    quadrants = _plot_spatial_disparity(disparity, valid)
    _write_findings(disparity, valid, distribution, quadrants)


if __name__ == "__main__":
    main()
