#!/usr/bin/env python3
"""Generate reproducible analytical figures for the official OpenCV aloe run.

The script reads only the default run arrays and its validity mask.  It keeps
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
    """Select an installed CJK-capable font, with a safe fallback."""

    installed = {font.name for font in font_manager.fontManager.ttflist}
    for candidate in (
        "Heiti SC",
        "Hiragino Sans GB",
        "Arial Unicode MS",
        "SimHei",
        "Songti SC",
        "DejaVu Sans",
    ):
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
        raise FileNotFoundError(f"无法读取有效掩码: {VALID_MASK_FILE}")

    if disparity.shape != depth_proxy.shape or disparity.shape != mask_png.shape:
        raise ValueError(
            "disparity_raw.npy、depth_proxy.npy 和 valid_mask.png 尺寸不一致: "
            f"{disparity.shape}, {depth_proxy.shape}, {mask_png.shape}"
        )

    valid_from_raw = np.isfinite(disparity) & (disparity > 15.0)
    valid_from_png = mask_png > 0
    if not np.array_equal(valid_from_raw, valid_from_png):
        raise ValueError("valid_mask.png 与 params.json 规定的有效视差规则不一致")
    if not np.all(np.isnan(depth_proxy[~valid_from_raw])):
        raise ValueError("无效视差位置的 depth_proxy 不是 NaN")

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
                    raise ValueError(f"未知网格统计量: {statistic}")
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
            raise OSError(f"图文件未生成或为空: {path}")


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
    ax.set_xlabel("匹配图像横坐标 $x$（像素）")
    ax.set_ylabel("匹配图像纵坐标 $y$（像素）")
    ax.set_title("空间有效匹配覆盖率")
    colorbar = fig.colorbar(mesh, ax=ax, pad=0.02, fraction=0.046)
    colorbar.set_label("网格内有效像素比例")
    colorbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    valid_count = int(valid.sum())
    total_count = int(valid.size)
    ax.text(
        0.01,
        -0.16,
        f"每个网格：有效像素数 / 网格总像素数；整体 $n_{{valid}}={valid_count:,}$ / "
        f"$n_{{total}}={total_count:,}$（{valid.mean():.2%}）",
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
    ax.set_xlabel("有效视差 $d$（像素）")
    ax.set_ylabel("有效像素数")
    ax.set_title("有效视差分布与分位数")
    ax.text(
        0.02,
        0.96,
        "阴影：P25–P75",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=8,
        bbox={"facecolor": "white", "edgecolor": "#B0B0B0", "alpha": 0.85, "pad": 3},
    )
    ax.text(
        0.99,
        0.96,
        f"$n={values.size:,}$\n范围：{values.min():.3f}–{values.max():.3f} px",
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
        ("左上", (slice(0, half_height), slice(0, half_width))),
        ("右上", (slice(0, half_height), slice(half_width, None))),
        ("左下", (slice(half_height, None), slice(0, half_width))),
        ("右下", (slice(half_height, None), slice(half_width, None))),
    )
    output = []
    for name, region in regions:
        region_valid = valid[region]
        region_disparity = disparity[region][region_valid].astype(np.float64)
        output.append((name, region_disparity, int(region_valid.sum()), float(region_valid.mean())))
    return output


def _plot_spatial_disparity(disparity: np.ndarray, valid: np.ndarray) -> list[dict[str, float | int | str]]:
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
    heatmap_ax.set_xlabel("横坐标 $x$（像素）")
    heatmap_ax.set_ylabel("纵坐标 $y$（像素）")
    heatmap_ax.set_title("(a) 网格内有效视差中位数")
    colorbar = fig.colorbar(mesh, ax=heatmap_ax, pad=0.02, fraction=0.046)
    colorbar.set_label("中位视差（像素）")
    heatmap_ax.text(
        0.01,
        -0.16,
        "灰色网格表示该位置没有有效匹配；统计仅使用有限且 $d>15$ 的像素。",
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
        f"全局中位数={global_median:.2f} px",
        transform=box_ax.get_yaxis_transform(),
        ha="right",
        va="bottom",
        color="#3568A8",
        fontsize=8,
    )
    box_ax.set_xticks(range(1, len(quadrants) + 1))
    box_ax.set_xticklabels([name for name, _, _, _ in quadrants], fontsize=8)
    box_ax.set_ylabel("有效视差 $d$（像素）")
    box_ax.set_title("(b) 四象限近远差异")
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
    content = f"""# Task 2 新增分析图数据说明

本文件由 `generate_analysis_figures.py` 根据官方 OpenCV aloe 样例的实际运行产物生成，供报告 Worker 编写图注和结果分析时使用。三张图均不使用用户照片，也不引入第二组算法或人工标注数据。

## 统一数据口径

- 输入数组：`disparity_raw.npy`、`depth_proxy.npy`；交叉核对 `valid_mask.png`。
- 数组尺寸：`{disparity.shape[1]} x {disparity.shape[0]}`，总像素 $n_{{total}}={total_count:,}$。
- 有效规则：视差为有限值且 $d>15$ px；该规则生成的布尔掩码与 `valid_mask.png` 逐像素完全一致。
- 有效样本：$n_{{valid}}={valid_count:,}$，占总像素 `{valid.mean():.4%}`；无效视差和对应相对深度保持 `NaN`，没有用零填补。
- 视差单位是像素。`depth_proxy=1/d` 仅为任意尺度的相对深度代理；当前 aloe 图像对没有经核验的 $f$、$B$ 或 $Q$，因此图中不写米、厘米，也不把代理值当作绝对深度。

## 图 1：`analysis_coverage_map`

- 内容：将匹配图像划分为 15 行 × 20 列网格，每个格子的颜色为该格内有效像素数除以格子总像素数。
- 关键数值：全局有效覆盖率 `{valid.mean():.4%}`；颜色范围 0–100%。
- 可支持的结论：有效匹配并非均匀分布，边界、遮挡或纹理不足区域会形成低覆盖率网格；这解释了为什么无效区域不应被当作零深度。
- 解释边界：网格覆盖率是匹配质量/可用性指标，不是深度误差，也不是物体分割结果。
- 建议图注：*“空间有效匹配覆盖率。颜色表示 15×20 网格内满足有限且 $d>15$ px 的视差像素比例；统计覆盖全部 `{valid_count:,}` 个有效像素，整体覆盖率为 `{valid.mean():.2%}`。”*

## 图 2：`analysis_disparity_distribution`

- 内容：全部 `{valid_count:,}` 个有效视差像素的直方图；阴影区为 P25–P75，虚线标出 P05、P50、P95。
- 实测分位数：P05=`{distribution['p05']:.4f}` px，P25=`{distribution['p25']:.4f}` px，P50=`{distribution['p50']:.4f}` px，P75=`{distribution['p75']:.4f}` px，P95=`{distribution['p95']:.4f}` px。
- 实测范围：`{distribution['minimum']:.4f}`–`{distribution['maximum']:.4f}` px。
- 可支持的结论：有效视差存在明显分布宽度；不同像素对应的匹配位移不同。较大的视差对应较小的 `1/d` 相对深度代理，但这只能说明相对前后顺序。
- 解释边界：直方图没有比较算法优劣；由于使用的是单次 StereoSGBM 运行，不能将分布宽度解释为误差或置信区间。
- 建议图注：*“有效视差分布（$n={valid_count:,}$）。所有统计仅使用有限且 $d>15$ px 的像素；阴影为 P25–P75，虚线为 P05、P50 和 P95。视差为像素单位。”*

## 图 3：`analysis_spatial_disparity`

- (a) 内容：同样的 15×20 网格，但颜色表示网格内有效视差的中位数；无有效样本的格子置为灰色。
- (b) 内容：按匹配图像中心划分左上、右上、左下、右下四个区域，箱线图使用各区全部有效视差；异常点只为可读性隐藏，没有从分位数和中位数计算中删除。
- 四象限统计：

| 区域 | 有效像素数 | 区域覆盖率 | 中位数（px） | P25–P75（px） |
|---|---:|---:|---:|---:|
"""
    for item in quadrants:
        content += (
            f"| {item['name']} | {item['n']:,} | {item['coverage']:.2%} | "
            f"{item['median']:.4f} | {item['p25']:.4f}–{item['p75']:.4f} |\n"
        )
    content += f"""
- 可支持的结论：视差在图像位置上有空间异质性；本次运行中右下区域的中位视差为 `{quadrants[-1]['median']:.4f}` px，而右上区域为 `{quadrants[1]['median']:.4f}` px。结合 $Z=fB/d$ 的单调关系，这些区域在相对意义上具有不同前后层次；不能据此声称物理距离。
- 解释边界：四象限只是图像坐标分组，不等价于语义物体类别；箱线图不是独立实验重复，也不提供统计显著性检验。
- 建议图注：*“空间视差与四象限比较。（a）颜色为网格内有效视差中位数，灰色表示无有效匹配；（b）四象限内全部有效视差的箱线图，横线为中位数，箱体为 P25–P75，须为 1.5×IQR。区域样本数和覆盖率标于横轴。”*

## 统一限制

这三张图都是同一次官方 aloe 图像对、同一组 StereoSGBM 参数产生的诊断性分析。它们用于说明有效匹配的空间覆盖、视差分布和相对近远关系，不应被写成米制深度精度、算法对比或真值误差结论。
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
