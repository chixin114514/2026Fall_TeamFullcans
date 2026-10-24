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
COLOR = {"SIFT": "#1f77b4", "SURF": "#ff7f0e", "ORB": "#2ca02c", "FAST": "#d62728", "LK": "#9467bd"}
BAG_TITLE = {"30fps": "30fps_424x240 (real RealSense)", "smooth": "vnav-lab5-smooth-trajectory (simulated)"}


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


def video_figures(summary):
    d = RES / "d6b_video"
    summary["video"] = {}
    for bag in ["30fps", "smooth"]:
        if not (d / bag).exists():
            continue
        rows = {m: read_rows(d / bag / VIDEO_BEST[m] / "stats.csv") for m in VIDEO}
        summary["video"][bag] = {m: average(r) for m, r in rows.items()}
        summary.setdefault("video_sweep", {})[bag] = {
            cfg.name: average(read_rows(cfg / "stats.csv"))
            for cfg in sorted((d / bag).iterdir()) if (cfg / "stats.csv").exists()}

        fig, axes = plt.subplots(1, 2, figsize=(10, 3.2))
        for m, r in rows.items():
            f = [x["frame"] for x in r]
            axes[0].plot(f, [x["inliers"] for x in r], lw=0.8, color=COLOR[m], label=LABEL[m])
            axes[1].plot(f, [100 * x["inlier_ratio"] for x in r], lw=0.8, color=COLOR[m])
        axes[0].set_ylabel("# inliers")
        axes[1].set_ylabel("inlier ratio [%]")
        for ax in axes:
            ax.set_xlabel("frame pair")
            ax.grid(alpha=0.3)
        axes[1].set_ylim(0, 102)
        axes[0].legend(fontsize=8, ncol=3)
        fig.suptitle(BAG_TITLE[bag], fontsize=10)
        fig.tight_layout()
        fig.savefig(FIG / f"d6b_{bag}_per_frame.pdf")
        plt.close(fig)

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

    # Timing bar chart (both bags)
    if summary["video"]:
        fig, ax = plt.subplots(figsize=(6, 2.8))
        bags = list(summary["video"])
        x = np.arange(len(VIDEO))
        for k, bag in enumerate(bags):
            t = [summary["video"][bag].get(m, {}).get("time_ms", np.nan) for m in VIDEO]
            ax.bar(x + (k - 0.5) * 0.38, t, 0.38, label=bag, color=["#4c72b0", "#dd8452"][k])
        ax.set_xticks(x)
        ax.set_xticklabels([LABEL[m] for m in VIDEO])
        ax.set_ylabel("ms per frame pair")
        ax.set_yscale("log")
        ax.grid(axis="y", alpha=0.3)
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(FIG / "d6b_timing.pdf")
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
