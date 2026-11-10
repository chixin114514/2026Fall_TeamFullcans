#!/usr/bin/env python3
"""Build every report figure from results/ and print the LaTeX table rows.

  python3 scripts/make_figures.py

Inputs : results/d6a_pair/<config>/*.png|stats.csv   (run_experiments.py pair)
         results/d6b_video/<bag>/<config>/stats.csv   (run_experiments.py video)
         results/d8_flow/<bag>/frames/*.png           (run_flow.sh)
Outputs: report/figures/*.{jpg,pdf}, results/summary.json
"""
import csv
import json
from pathlib import Path

import cv2
import matplotlib
import matplotlib.ticker

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

LAB5 = Path(__file__).resolve().parents[1]
RES = LAB5 / "results"
FIG = LAB5 / "report" / "figures"

PAIR_BEST = {"SIFT": "SIFT_default", "SURF": "SURF_default",
             "ORB": "ORB_8lvl_2000", "FAST+BRIEF": "FAST_default"}
VIDEO = ["SIFT", "SURF", "ORB", "FAST", "LK"]
# Variant with the most inliers on both bags (results/d6b_video/<bag>/<variant>).
VIDEO_BEST = {"SIFT": "SIFT_c002", "SURF": "SURF", "ORB": "ORB_2000",
              "FAST": "FAST_t10", "LK": "LK_1000"}
LABEL = {"SIFT": "SIFT", "SURF": "SURF", "ORB": "ORB", "FAST": "FAST+BRIEF", "LK": "Harris+LK"}
# One hue family per descriptor type (blue: float, red: binary); LK, the best method, in black.
COLOR = {"SIFT": "#3B6FA8", "SURF": "#9DBDDF", "ORB": "#B5403F", "FAST": "#E9A3A0", "LK": "#1A1A1A"}
BAG_TITLE = {"30fps": "Real: 30fps_424x240", "smooth": "Simulated: smooth-trajectory"}
BAG_SHORT = {"30fps": "real (424×240)", "smooth": "simulated (720×480)"}
SMOOTH = 15  # centred moving average over 15 frame pairs (0.5 s) in the per-frame plot

plt.rcParams.update({
    "font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8, "legend.fontsize": 8,
    "xtick.labelsize": 7, "ytick.labelsize": 7, "pdf.fonttype": 42,
    "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.7,
    "legend.frameon": False,
})


def read_rows(path):
    with open(path) as f:
        return [{k: float(v) for k, v in r.items()} for r in csv.DictReader(f)]


def average(rows):
    keys = ["kp1", "kp2", "matches", "good_matches", "inliers", "inlier_ratio", "time_ms"]
    out = {k: float(np.mean([r[k] for r in rows])) for k in keys}
    out["frames"] = len(rows)
    return out


def save_jpg(name, img, width=None):
    if width is not None and img.shape[1] > width:
        img = cv2.resize(img, (width, int(img.shape[0] * width / img.shape[1])),
                         interpolation=cv2.INTER_AREA)
    cv2.imwrite(str(FIG / name), img, [cv2.IMWRITE_JPEG_QUALITY, 90])


def hstack_pad(images, gap=10):
    h = max(i.shape[0] for i in images)
    padded = []
    for k, i in enumerate(images):
        p = np.full((h, i.shape[1] + (gap if k else 0), 3), 255, np.uint8)
        p[:i.shape[0], (gap if k else 0):] = i
        padded.append(p)
    return np.hstack(padded)


def label(img, text):
    img = img.copy()
    cv2.rectangle(img, (0, 0), (12 * len(text) + 16, 30), (255, 255, 255), -1)
    cv2.putText(img, text, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    return img


def pair_figures(summary):
    d = RES / "d6a_pair"
    sift = d / "SIFT_default"
    kp = hstack_pad([cv2.imread(str(sift / "keypoints_img1.png")),
                     cv2.imread(str(sift / "keypoints_img2.png"))])
    save_jpg("d3_sift_keypoints.jpg", kp, 1600)
    save_jpg("d4_sift_matches_all.jpg", cv2.imread(str(sift / "matches_all.png")), 1400)
    save_jpg("d4_sift_matches_ratio.jpg", cv2.imread(str(sift / "matches_good.png")), 1400)
    save_jpg("d5_sift_inliers.jpg", cv2.imread(str(sift / "inliers_outliers.png")), 1400)
    tiles = [label(cv2.imread(str(d / cfg / "inliers_outliers.png")),
                   name + (" (2000 feat., 8 levels)" if name == "ORB" else ""))
             for name, cfg in PAIR_BEST.items() if name != "SIFT"]
    tiles.append(label(cv2.imread(str(d / "ORB_default" / "inliers_outliers.png")),
                       "ORB (stencil: 500 feat., 1 level)"))
    w = min(t.shape[1] for t in tiles)
    tiles = [cv2.resize(t, (w, int(t.shape[0] * w / t.shape[1]))) for t in tiles]
    grid = np.vstack([hstack_pad(tiles[0:2]), np.full((10, 2 * w + 10, 3), 255, np.uint8),
                      hstack_pad(tiles[2:4])])
    save_jpg("d6a_inliers_grid.jpg", grid, 1600)
    summary["pair"] = {cfg.name: average(read_rows(cfg / "stats.csv"))
                       for cfg in sorted(d.iterdir()) if (cfg / "stats.csv").exists()}
    funnel_figure(summary["pair"])


def moving_average(y, n=SMOOTH):
    y = np.asarray(y, float)
    k = np.ones(n)
    return np.convolve(y, k, "same") / np.convolve(np.ones_like(y), k, "same")


def per_frame_figure(per_bag):
    """Rows: datasets; columns: inliers and inlier ratio, smoothed. LK drawn last and thicker."""
    fig, axes = plt.subplots(len(per_bag), 2, figsize=(6.5, 2.1 * len(per_bag) + 0.4),
                             sharex="row", squeeze=False)
    order = ["SURF", "FAST", "SIFT", "ORB", "LK"]  # light colours first, hero on top
    for row, (bag, rows) in zip(axes, per_bag.items()):
        lo = 100
        for m in order:
            f = [x["frame"] for x in rows[m]]
            lw = 1.4 if m == "LK" else 0.9
            ratio = moving_average([100 * x["inlier_ratio"] for x in rows[m]])
            lo = min(lo, ratio.min())
            row[0].plot(f, moving_average([x["inliers"] for x in rows[m]]), lw=lw,
                        color=COLOR[m], label=LABEL[m])
            row[1].plot(f, ratio, lw=lw, color=COLOR[m])
        row[0].set_ylabel("inliers per pair")
        row[1].set_ylabel("inlier ratio (%)")
        row[1].set_ylim(5 * np.floor(lo / 5) - 2, 100.5)
        row[0].set_ylim(bottom=0)
        row[0].set_title(BAG_TITLE[bag], loc="left", fontweight="bold")
        for ax in row:
            ax.grid(alpha=0.25, lw=0.5)
            ax.margins(x=0.01)
    for ax in axes[-1]:
        ax.set_xlabel("frame pair")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    idx = [labels.index(LABEL[m]) for m in VIDEO]
    fig.legend([handles[i] for i in idx], [labels[i] for i in idx], ncol=5,
               loc="upper center", bbox_to_anchor=(0.5, 1.0), handlelength=1.6)
    fig.tight_layout(rect=(0, 0, 1, 0.95), h_pad=1.2)
    fig.savefig(FIG / "d6b_per_frame.pdf")
    plt.close(fig)


def timing_figure(video):
    fig, ax = plt.subplots(figsize=(4.25, 2.3))
    bags = list(video)
    x = np.arange(len(VIDEO))
    w = 0.38
    for k, bag in enumerate(bags):
        t = [video[bag].get(m, {}).get("time_ms", np.nan) for m in VIDEO]
        bars = ax.bar(x + (k - 0.5) * w, t, w, label=BAG_SHORT[bag],
                      color=["#4D4D4D", "#B3B3B3"][k])
        # Values inside the bar tops so they never cross the budget line or gridlines.
        ax.bar_label(bars, fmt="%.0f", fontsize=6.5, padding=-8,
                     color=["white", "#1A1A1A"][k])
    ax.axhline(1000 / 30, color="#B5403F", lw=0.8, ls="--")
    ax.text(len(VIDEO) - 0.5, 1000 / 30 * 1.12, "30 Hz budget (33 ms)", color="#B5403F",
            ha="right", va="bottom", fontsize=7)
    ax.set_xticks(x)
    ax.set_xticklabels([LABEL[m] for m in VIDEO])
    ax.set_ylabel("time per frame pair (ms)")
    ax.set_yscale("log")
    ax.set_ylim(1, 400)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.88))
    fig.tight_layout()
    fig.savefig(FIG / "d6b_timing.pdf")
    plt.close(fig)


def video_figures(summary):
    d = RES / "d6b_video"
    summary["video"] = {}
    per_bag = {}
    for bag in ["30fps", "smooth"]:
        if not (d / bag).exists():
            continue
        rows = {m: read_rows(d / bag / VIDEO_BEST[m] / "stats.csv") for m in VIDEO}
        per_bag[bag] = rows
        summary["video"][bag] = {m: average(r) for m, r in rows.items()}
        summary.setdefault("video_sweep", {})[bag] = {
            cfg.name: average(read_rows(cfg / "stats.csv"))
            for cfg in sorted((d / bag).iterdir()) if (cfg / "stats.csv").exists()}

        frames = [label(cv2.imread(str(d / bag / VIDEO_BEST[m] / "inliers_outliers.png")), LABEL[m])
                  for m in ["SIFT", "SURF", "ORB", "FAST"]]
        if len(frames) == 4:
            grid = np.vstack([hstack_pad(frames[0:2]),
                              np.full((10, frames[0].shape[1] * 2 + 10, 3), 255, np.uint8),
                              hstack_pad(frames[2:4])])
            save_jpg(f"d6b_{bag}_frame150.jpg", grid, 1600)
        lk = d / bag / VIDEO_BEST["LK"] / "lk_tracks.png"
        if lk.exists():
            save_jpg(f"d7_{bag}_lk_tracks.jpg", cv2.imread(str(lk)), 1000)

    if per_bag:
        per_frame_figure(per_bag)
        timing_figure(summary["video"])
        tradeoff_figure(summary["video_sweep"])
        ratio_distribution_figure(per_bag)


def fibonacci_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    theta = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)], 1)


def sphere_contour(cx, cz, r):
    """Analytic ellipse of D1 for a sphere centred at (cx, 0, cz): centre u0, semi-axes."""
    k = cx ** 2 + cz ** 2 - r ** 2
    u0 = cx * cz / (cz ** 2 - r ** 2)
    return u0, r * np.sqrt(k) / (cz ** 2 - r ** 2), r / np.sqrt(cz ** 2 - r ** 2)


def sphere_figure():
    """D1: analytic contours vs. projected surface samples, and the elongation off axis."""
    r, cz = 1.0, 5.0
    pts = fibonacci_sphere(200_000)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(6.5, 2.3))
    t = np.linspace(0, 2 * np.pi, 400)
    for cx in [0, 3, 6]:
        p = pts * r + [cx, 0, cz]
        ax.scatter(p[::40, 0] / p[::40, 2], p[::40, 1] / p[::40, 2], s=0.3, color="#9DBDDF",
                   rasterized=True, lw=0)
        u0, a, b = sphere_contour(cx, cz, r)
        ax.plot(u0 + a * np.cos(t), b * np.sin(t), color="#1A1A1A", lw=1)
        ax.plot(cx / cz, 0, "x", color="#B5403F", ms=4, mew=1)
        ax.text(u0, -b - 0.06, f"$c_x={cx}$", ha="center", va="top", fontsize=8)
    ax.set_xlim(-0.35, 1.65)
    ax.set_ylim(-0.5, 0.5)
    ax.set_aspect("equal", adjustable="box")
    bx.set_box_aspect(0.5)
    ax.set_xlabel("$u$")
    ax.set_ylabel("$v$")
    ax.set_title("a  Contours for $r=1$, $c_z=5$", loc="left", fontweight="bold")

    cxs = np.linspace(0, 10, 200)
    ratio = [sphere_contour(c, cz, r)[1] / sphere_contour(c, cz, r)[2] for c in cxs]
    bx.plot(np.degrees(np.arctan(cxs / cz)), ratio, color="#1A1A1A", lw=1, label="analytic")
    for cx in [0, 2, 4, 6, 8, 10]:  # numerical check: extents of the projected samples
        p = pts * r + [cx, 0, cz]
        u, v = p[:, 0] / p[:, 2], p[:, 1] / p[:, 2]
        bx.plot(np.degrees(np.arctan(cx / cz)), (u.max() - u.min()) / (v.max() - v.min()), "o",
                color="#3B6FA8", ms=3.5, label="projected samples" if cx == 0 else None)
    bx.set_xlabel("angle of sphere centre off the optical axis (deg)")
    bx.set_ylabel("$a_{\\mathrm{radial}}/a_{\\perp}$")
    bx.set_title("b  Elongation of the ellipse", loc="left", fontweight="bold")
    bx.legend(loc="upper left")
    fig.tight_layout(w_pad=2)
    fig.savefig(FIG / "d1_sphere_projection.pdf", dpi=300)
    plt.close(fig)


def vanishing_figure():
    """D2: images of parallel lines with u_z != 0 meet at v_inf; with u_z = 0 they stay parallel."""
    starts = [(-2, -1, 4), (-2, 1.5, 4), (1.5, -1.5, 3), (0, 1, 6), (-3, 0, 5)]
    lam = np.linspace(0, 400, 4000)
    XLIM, YLIM = (-1, 2.2), (-0.7, 0.8)
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.5))
    for ax, u, title in [(axes[0], (1, 0.5, 1), "a  $u=[1\\ 0.5\\ 1]^\\top$ ($u_z\\neq0$)"),
                         (axes[1], (1, 0.5, 0), "b  $u=[1\\ 0.5\\ 0]^\\top$ ($u_z=0$)")]:
        u = np.asarray(u, float) / np.linalg.norm(u)
        for p0 in starts:
            p = np.asarray(p0, float) + lam[:, None] * u
            x, y = p[:, 0] / p[:, 2], p[:, 1] / p[:, 2]
            keep = (x < XLIM[1]) & (y < YLIM[1])  # end the line at the frame instead of clipping
            ax.plot(x[keep], y[keep], color="#3B6FA8", lw=1)
            ax.plot(p0[0] / p0[2], p0[1] / p0[2], "o", color="#3B6FA8", ms=2.5)
        if u[2] != 0:
            ax.plot(u[0] / u[2], u[1] / u[2], "o", mfc="none", mec="#B5403F", ms=7, mew=1.2)
            ax.text(u[0] / u[2], u[1] / u[2] + 0.1, "$v_\\infty=(u_x/u_z,\\ u_y/u_z)$",
                    fontsize=8, color="#B5403F", ha="center", va="bottom")
        ax.set_xlim(*XLIM)
        ax.set_ylim(*YLIM)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("$u$")
        ax.set_ylabel("$v$")
        ax.set_title(title, loc="left", fontweight="bold")
    fig.tight_layout(w_pad=2)
    fig.savefig(FIG / "d2_vanishing_points.pdf")
    plt.close(fig)


def funnel_figure(pair):
    """D6a: keypoints -> ratio test -> RANSAC for the best configuration of every method."""
    stages = [("kp1", "keypoints (queries)"), ("good_matches", "after ratio test"),
              ("inliers", "RANSAC inliers")]
    fig, ax = plt.subplots(figsize=(4.25, 2.4))
    x = np.arange(len(PAIR_BEST))
    w = 0.27
    for k, (key, name) in enumerate(stages):
        vals = [pair[cfg][key] for cfg in PAIR_BEST.values()]
        bars = ax.bar(x + (k - 1) * w, vals, w, label=name,
                      color=["#D9D9D9", "#8C8C8C", "#1A1A1A"][k])
        ax.bar_label(bars, fmt="%.0f", fontsize=6.5, padding=1)
    ax.set_xticks(x)
    ax.set_xticklabels([m if m != "ORB" else "ORB\n(2000, 8 levels)" for m in PAIR_BEST])
    ax.set_yscale("log")
    ax.set_ylim(5, 5e3)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
    ax.set_ylabel("count (box pair)")
    ax.legend(ncol=3, loc="lower center", bbox_to_anchor=(0.5, 1.0), handlelength=1.2,
              columnspacing=1)
    fig.tight_layout()
    fig.savefig(FIG / "d6a_match_funnel.pdf")
    plt.close(fig)


# Video configurations per method, ordered by number of keypoints.
SWEEP = {"SIFT": ["SIFT", "SIFT_c002"], "SURF": ["SURF_h400", "SURF"],
         "ORB": ["ORB_stencil", "ORB", "ORB_2000"], "FAST": ["FAST_t30", "FAST", "FAST_t10"],
         "LK": ["LK", "LK_1000"]}


def tradeoff_figure(sweep):
    """D6b: time vs. inliers for every configuration; the configuration used in the tables is filled."""
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.7), sharey=False)
    for ax, (bag, cfgs) in zip(axes, sweep.items()):
        for m in VIDEO:
            pts = [cfgs[c] for c in SWEEP[m] if c in cfgs]
            ax.plot([p["time_ms"] for p in pts], [p["inliers"] for p in pts], "-o", color=COLOR[m],
                    lw=1, ms=3.5, mfc="white", label=LABEL[m])
            best = cfgs[VIDEO_BEST[m]]
            ax.plot(best["time_ms"], best["inliers"], "o", color=COLOR[m], ms=5.5, mec="#1A1A1A",
                    mew=0.6)
        ax.axvline(1000 / 30, color="#B5403F", lw=0.8, ls="--")
        ax.text(1000 / 30 * 1.08, 0.97, "30 Hz", color="#B5403F", fontsize=7, va="top",
                transform=ax.get_xaxis_transform())
        ax.set_xscale("log")
        ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
        ax.set_xlim(1, 250)
        ax.set_ylim(bottom=0)
        ax.set_xlabel("time per frame pair (ms)")
        ax.set_ylabel("inliers per pair")
        ax.set_title(BAG_TITLE[bag], loc="left", fontweight="bold")
    fig.legend(*axes[0].get_legend_handles_labels(), ncol=5, loc="upper center",
               bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(rect=(0, 0, 1, 0.92), w_pad=2)
    fig.savefig(FIG / "d6b_tradeoff.pdf")
    plt.close(fig)


def ratio_distribution_figure(per_bag):
    """D7: per-frame inlier ratio; boxes = quartiles, whiskers = 5th/95th percentile."""
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 2.4))
    for ax, (bag, rows) in zip(axes, per_bag.items()):
        data = [[100 * x["inlier_ratio"] for x in rows[m]] for m in VIDEO]
        bp = ax.boxplot(data, whis=(5, 95), showfliers=False, widths=0.55, patch_artist=True,
                        medianprops=dict(color="#1A1A1A", lw=1))
        for patch, m in zip(bp["boxes"], VIDEO):
            patch.set(facecolor=COLOR[m], edgecolor="#1A1A1A", lw=0.6,
                      alpha=0.9 if m != "LK" else 1)
        if "LK" in VIDEO:
            bp["medians"][VIDEO.index("LK")].set_color("white")
        ax.set_xticks(range(1, len(VIDEO) + 1))
        ax.set_xticklabels([LABEL[m] for m in VIDEO], fontsize=6.5)
        ax.set_ylabel("inlier ratio per pair (%)")
        ax.set_title(BAG_TITLE[bag], loc="left", fontweight="bold")
        ax.grid(axis="y", alpha=0.25, lw=0.5)
    fig.tight_layout(w_pad=2)
    fig.savefig(FIG / "d7_ratio_distribution.pdf")
    plt.close(fig)


def flow_figure():
    for bag in ["30fps", "smooth"]:
        frames = sorted((RES / "d8_flow" / bag / "frames").glob("*.png"))
        if frames:
            save_jpg(f"d8_{bag}_farneback.jpg", cv2.imread(str(frames[len(frames) // 2])), 1400)


def latex_rows(table):
    order = [("kp1", "\\# of Keypoints in Img 1", "{:.0f}"),
             ("kp2", "\\# of Keypoints in Img 2", "{:.0f}"),
             ("matches", "\\# of Matches", "{:.0f}"),
             ("good_matches", "\\# of Good Matches", "{:.0f}"),
             ("inliers", "\\# of Inliers", "{:.0f}"),
             ("inlier_ratio", "Inlier Ratio", "{:.1f}\\%"),
             ("time_ms", "Time / pair [ms]", "{:.1f}")]
    lines = []
    for key, name, fmt in order:
        vals = [fmt.format(100 * t[key] if key == "inlier_ratio" else t[key]) for t in table]
        lines.append(f"{name} & " + " & ".join(vals) + " \\\\")
    return "\n".join(lines)


def main():
    FIG.mkdir(parents=True, exist_ok=True)
    summary = {}
    sphere_figure()
    vanishing_figure()
    pair_figures(summary)
    video_figures(summary)
    flow_figure()
    (RES / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print("% D6a (pair):", list(PAIR_BEST))
    print(latex_rows([summary["pair"][c] for c in PAIR_BEST.values()]))
    for bag, t in summary.get("video", {}).items():
        print(f"% D6b/D7 {bag}:", [m for m in VIDEO if m in t],
              "frames:", [t[m]["frames"] for m in VIDEO if m in t])
        print(latex_rows([t[m] for m in VIDEO if m in t]))
    print("% sweep: config & kp1 & good & inliers & ratio & ms   (pair | 30fps | smooth)")
    for cfg, p in summary["pair"].items():
        print(f"{cfg} & {p['kp1']:.0f} & {p['good_matches']:.0f} & {p['inliers']:.0f} & "
              f"{100 * p['inlier_ratio']:.1f} & {p['time_ms']:.1f} \\\\")
    for bag, sweep in summary.get("video_sweep", {}).items():
        for cfg, p in sweep.items():
            print(f"{bag} {cfg} & {p['kp1']:.0f} & {p['good_matches']:.0f} & {p['inliers']:.0f} & "
                  f"{100 * p['inlier_ratio']:.1f} & {p['time_ms']:.1f} \\\\")


if __name__ == "__main__":
    main()
