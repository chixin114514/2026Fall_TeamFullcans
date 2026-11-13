#!/usr/bin/env python3
"""Build every report figure from results/ and print the numbers used in the report.

  python3 scripts/make_figures.py

Inputs : results/rpe/<method>.csv         (scripts/run_experiments.py)
         results/sweep/<method>_<px>.csv  (scripts/run_experiments.py --sweep)
Outputs: report/figures/*.pdf, results/summary.json,
         results/figqa/ (panel-alignment and collision audits of each figure)
"""
import json
import subprocess
import sys
from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

LAB6 = Path(__file__).resolve().parents[1]
RES = LAB6 / "results"
FIG = LAB6 / "report" / "figures"
QA = RES / "figqa"
# Optional QA helpers (nature-figure skill); figures are produced without them.
SKILL = Path.home() / ".claude/skills/nature-figure/scripts"
sys.path.insert(0, str(SKILL))
try:
    from audit_panel_alignment import require_matplotlib_panel_alignment
except ImportError:  # pragma: no cover
    require_matplotlib_panel_alignment = None

MM = 1 / 25.4
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "pdf.fonttype": 42, "svg.fonttype": "none",
    "font.size": 7, "axes.titlesize": 7, "axes.labelsize": 7, "legend.fontsize": 6.5,
    "xtick.labelsize": 6.5, "ytick.labelsize": 6.5,
    "axes.spines.right": False, "axes.spines.top": False, "axes.linewidth": 0.6,
    "xtick.major.width": 0.6, "ytick.major.width": 0.6,
    "xtick.major.size": 2.5, "ytick.major.size": 2.5,
    "legend.frameon": False, "lines.linewidth": 0.8,
})

# One family for the essential-matrix solvers (blue), black for the 2-point solver
# that uses the known rotation, red for the 3D-3D solver; no-RANSAC runs in grey.
METHODS = {
    "5pt": dict(label="5-point Nistér", color="#0F4D92"),
    "8pt": dict(label="8-point Longuet-Higgins", color="#7FA7D6"),
    "2pt": dict(label="2-point (known R)", color="#272727"),
    "arun": dict(label="3-point Arun (3D–3D)", color="#B64342"),
    "5pt_noransac": dict(label="5-point, no RANSAC", color="#9E9E9E"),
    "8pt_noransac": dict(label="8-point, no RANSAC", color="#C9C9C9"),
    "arun_noransac": dict(label="Arun, no RANSAC", color="#E9A6A1"),
}
SMOOTH_S = 2.0  # centred rolling median window for the time plots, in seconds


def load(name, base=RES / "rpe"):
    d = pd.read_csv(base / f"{name}.csv")
    return d


def rolling(d, col):
    s = d.set_index(pd.to_timedelta(d["t"], unit="s"))[col]
    return s.rolling(f"{int(SMOOTH_S * 1000)}ms", center=True, min_periods=1).median().values


def plain_log(ax, which="xy", subs=(1.0, 2.0, 5.0)):
    """Log axis with decimal tick labels (no mathtext exponents, which render at 0.7x size)."""
    fmt = mpl.ticker.FuncFormatter(lambda v, _: f"{v:g}")
    for name in which:
        axis = ax.xaxis if name == "x" else ax.yaxis
        axis.set_major_locator(mpl.ticker.LogLocator(base=10, subs=subs))
        axis.set_major_formatter(fmt)
        axis.set_minor_locator(mpl.ticker.LogLocator(base=10, subs=np.arange(2, 10)))
        axis.set_minor_formatter(mpl.ticker.NullFormatter())


def panel_label(ax, s):
    ax.text(-0.075, 1.02, s, transform=ax.transAxes, fontsize=8, fontweight="bold",
            va="bottom", ha="left")


def save(fig, name):
    FIG.mkdir(parents=True, exist_ok=True)
    QA.mkdir(parents=True, exist_ok=True)
    fig.canvas.draw()
    if require_matplotlib_panel_alignment is not None:
        require_matplotlib_panel_alignment(
            fig, json_out=str(QA / f"{name}.alignment.json"),
            overlay_svg=str(QA / f"{name}.alignment.svg"),
            tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True)
    pdf = FIG / f"{name}.pdf"
    fig.savefig(pdf, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    audit = SKILL / "audit_figure_collisions.py"
    if audit.exists():
        r = subprocess.run([sys.executable, str(audit), str(pdf),
                            "--json-out", str(QA / f"{name}.collision-audit.json")],
                           capture_output=True, text=True)
        if r.returncode == 0 or "verdict" in r.stdout.lower():
            verdict = [line for line in r.stdout.splitlines() if line.strip()][-1:] or ["?"]
            print(f"  {name}: collision audit -> {verdict[0]}")
        else:
            print(f"  {name}: collision audit NOT AUDITABLE (needs Python >= 3.9 + PyMuPDF)")
    text = SKILL / "audit_pdf_text.py"
    if text.exists():
        r = subprocess.run([sys.executable, str(text), str(pdf)], capture_output=True, text=True)
        verdict = [line for line in r.stdout.splitlines() if line.startswith("verdict")] or ["?"]
        print(f"  {name}: text-size audit -> {verdict[0]}")
    print(f"→ {pdf.relative_to(LAB6)}")


def time_axis(frames):
    t0 = min(d["stamp"].min() for d in frames.values())
    for d in frames.values():
        d["t"] = d["stamp"] - t0


def fig_time(frames, names, name, rot_floor, tran_col, tran_label, tran_scale=1.0, notes=None):
    """Two stacked panels sharing the time axis: rotation error and translation error."""
    fig, axes = plt.subplots(2, 1, figsize=(180 * MM, 105 * MM), sharex=True)
    for ax, col, ylabel, scale in (
            (axes[0], "rot_err_deg", "Rotation error (deg)", 1.0),
            (axes[1], tran_col, tran_label, tran_scale)):
        for n in names:
            d, m = frames[n], METHODS[n]
            y = np.clip(d[col].values * scale, rot_floor if col == "rot_err_deg" else 1e-6, None)
            ax.plot(d["t"], y, color=m["color"], lw=0.35, alpha=0.35, rasterized=True)
            ax.plot(d["t"], np.clip(rolling(d, col) * scale, y.min(), None), color=m["color"],
                    lw=1.0, label=m["label"])
        ax.set_yscale("log")
        plain_log(ax, "y")
        ax.set_ylabel(ylabel)
        ax.grid(axis="y", which="major", lw=0.3, color="#E3E3E3")
    axes[1].set_xlabel("Time (s)")
    axes[0].legend(loc="upper left", ncol=len(names), bbox_to_anchor=(0, 1.16))
    if notes:
        for ax_idx, text in notes:
            axes[ax_idx].text(0.995, 0.075, text, transform=axes[ax_idx].transAxes,
                              ha="right", va="bottom", fontsize=6, color="#4D4D4D",
                              bbox=dict(fc="white", ec="none", pad=0.6))
    panel_label(axes[0], "a")
    panel_label(axes[1], "b")
    axes[0].set_xlim(0, max(frames[n]["t"].max() for n in names))
    fig.align_ylabels(axes)
    save(fig, name)


def ecdf(ax, x, **kw):
    x = np.sort(x[np.isfinite(x)])
    ax.step(x, np.arange(1, len(x) + 1) / len(x), where="post", **kw)


def fig_cdf(frames, names, name):
    fig, axes = plt.subplots(1, 2, figsize=(180 * MM, 62 * MM))
    for n in names:
        d, m = frames[n], METHODS[n]
        ls = "--" if "noransac" in n else "-"
        if n != "2pt":  # rotation is given to the 2-point solver
            ecdf(axes[0], d["rot_err_deg"].values, color=m["color"], lw=1.0, ls=ls, label=m["label"])
        ecdf(axes[1], d["tran_err_unit"].values, color=m["color"], lw=1.0, ls=ls, label=m["label"])
    axes[0].set_xscale("log")
    axes[0].set_xlabel("Rotation error (deg)")
    axes[1].set_xscale("log")
    plain_log(axes[0], "x", subs=(1.0,))
    plain_log(axes[1], "x", subs=(1.0,))
    axes[0].set_xlim(1e-3, 300)
    axes[1].set_xlim(1e-3, 2.5)
    axes[1].set_xlabel("Translation-direction error (unit vectors)")
    for ax in axes:
        ax.set_ylabel("Fraction of frame pairs")
        ax.set_ylim(0, 1.0)
        ax.grid(which="major", lw=0.3, color="#E3E3E3")
    axes[0].axvline(1.0, color="#767676", lw=0.6, ls=":")
    axes[1].axvline(0.5, color="#767676", lw=0.6, ls=":")
    axes[1].axvline(0.1, color="#767676", lw=0.6, ls=":")
    handles, labels = axes[1].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, bbox_to_anchor=(0.5, 1.07))
    panel_label(axes[0], "a")
    panel_label(axes[1], "b")
    fig.tight_layout()
    save(fig, name)


def fig_sweep(name):
    rows = []
    for f in sorted((RES / "sweep").glob("*.csv")):
        method, px = f.stem.rsplit("_", 1)
        if method == "arun":  # 3D threshold in meters, see sweep3d_table()
            continue
        d = pd.read_csv(f)
        rows.append(dict(method=method, px=float(px), n=len(d),
                         tran_med=d["tran_err_unit"].median(),
                         rot_med=d["rot_err_deg"].median(),
                         inlier=(d["n_inliers"] / d["n_matches"]).median(),
                         time_ms=d["time_ms"].median()))
    s = pd.DataFrame(rows).sort_values(["method", "px"])
    fig, axes = plt.subplots(1, 3, figsize=(180 * MM, 52 * MM))
    for method in [k for k in METHODS if k in set(s["method"])]:
        g, m = s[s["method"] == method], METHODS[method]
        kw = dict(color=m["color"], marker="o", ms=2.5, lw=1.0, label=m["label"])
        axes[0].plot(g["px"], g["tran_med"], **kw)
        if method != "2pt":
            axes[1].plot(g["px"], g["rot_med"], **kw)
        axes[2].plot(g["px"], 100 * g["inlier"], **kw)
    axes[0].set_ylabel("Median translation-direction error")
    axes[1].set_ylabel("Median rotation error (deg)")
    axes[2].set_ylabel("Median inlier ratio (%)")
    for ax in axes:
        ax.set_xscale("log")
        ax.set_xlabel("RANSAC threshold (px)")
        ax.set_xticks(sorted(s["px"].unique()))
        ax.get_xaxis().set_major_formatter(mpl.ticker.FormatStrFormatter("%g"))
        ax.xaxis.set_minor_locator(mpl.ticker.NullLocator())
        ax.grid(which="major", lw=0.3, color="#E3E3E3")
    axes[0].set_yscale("log")
    axes[1].set_yscale("log")
    plain_log(axes[0], "y")
    plain_log(axes[1], "y")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.08))
    for ax, l in zip(axes, "abc"):
        panel_label(ax, l)
    fig.tight_layout(w_pad=2.0)
    save(fig, name)
    return s


def sweep3d_table():
    rows = []
    for f in sorted((RES / "sweep").glob("arun_*.csv"), key=lambda f: float(f.stem.split("_")[1])):
        d = pd.read_csv(f)
        rows.append(dict(thr_m=float(f.stem.split("_")[1]), n=len(d),
                         rot_med_deg=d["rot_err_deg"].median(),
                         tran_med_mm=1e3 * d["tran_err_m"].median(),
                         tu_med=d["tran_err_unit"].median(),
                         inlier=(d["n_inliers"] / d["n_matches"]).median()))
    return pd.DataFrame(rows)


def stats(d):
    rot, tu, tm = d["rot_err_deg"], d["tran_err_unit"], d["tran_err_m"]
    return dict(
        frames=int(len(d)), valid=float(d["valid"].mean()),
        rot_med_deg=float(rot.median()), rot_p90_deg=float(rot.quantile(0.9)),
        rot_lt1deg=float((rot < 1).mean()), rot_lt01deg=float((rot < 0.1).mean()),
        tu_med=float(tu.median()), tu_p90=float(tu.quantile(0.9)),
        tu_lt05=float((tu < 0.5).mean()), tu_lt01=float((tu < 0.1).mean()),
        tm_med_mm=float(1e3 * tm.median()),
        gt_step_med_mm=float(1e3 * d["gt_tran_norm"].median()),
        matches_med=float(d["n_matches"].median()),
        inlier_ratio_med=float((d["n_inliers"] / d["n_matches"]).median()),
        time_ms_med=float(d["time_ms"].median()),
    )


def fig_race(frames, names, name):
    """Bonus: Lab 4 race. a, ground-truth motion per frame; b, rotation error; c, translation-direction error."""
    fig, axes = plt.subplots(3, 1, figsize=(180 * MM, 120 * MM), sharex=True,
                             gridspec_kw=dict(height_ratios=[0.7, 1, 1]))
    ref = frames[names[0]]
    axes[0].plot(ref["t"], ref["gt_tran_norm"] * 1e2, color="#4D4D4D", lw=1.0)
    axes[0].set_ylabel("Camera step (cm)")
    axes[0].set_ylim(0, None)
    axes[0].grid(axis="y", lw=0.3, color="#E3E3E3")
    for ax, col, ylabel, floor in ((axes[1], "rot_err_deg", "Rotation error (deg)", 1e-3),
                                   (axes[2], "tran_err_unit", "Translation error (unit vectors)", 1e-4)):
        for n in names:
            if n == "2pt" and col == "rot_err_deg":
                continue
            d, m = frames[n], METHODS[n]
            ax.plot(d["t"], np.clip(d[col].values, floor, None), color=m["color"], lw=0.9,
                    marker="o", ms=1.2, label=m["label"])
        ax.set_yscale("log")
        plain_log(ax, "y")
        ax.set_ylabel(ylabel)
        ax.grid(axis="y", which="major", lw=0.3, color="#E3E3E3")
    axes[2].set_xlabel("Time since take-off segment start (s)")
    axes[2].legend(loc="upper left", ncol=len(names), bbox_to_anchor=(0, 3.62), frameon=False)
    for ax, lab in zip(axes, "abc"):
        panel_label(ax, lab)
    axes[0].set_xlim(0, max(frames[n]["t"].max() for n in names))
    fig.align_ylabels(axes)
    save(fig, name)


def main():
    names = [n for n in METHODS if (RES / "rpe" / f"{n}.csv").exists()]
    frames = {n: load(n) for n in names}
    time_axis(frames)

    summary = {n: stats(frames[n]) for n in names}
    rot_floor = 1e-3
    fig_time(frames, [n for n in ("5pt", "8pt", "2pt") if n in frames], "d4_rpe_time", rot_floor,
             "tran_err_unit", "Translation error (unit vectors)",
             notes=[(0, "2-point: rotation taken from ground truth, error at the axis floor")])
    if "arun" in frames:
        fig_time(frames, [n for n in ("arun", "arun_noransac") if n in frames], "d5_arun_rpe_time",
                 rot_floor, "tran_err_m", "Translation error (mm)", tran_scale=1e3)
    fig_cdf(frames, names, "d4_d5_error_cdf")
    if (RES / "sweep").exists():
        sweep = fig_sweep("d4_threshold_sweep")
        summary["_sweep"] = sweep.to_dict(orient="records")
        s3 = sweep3d_table()
        summary["_sweep3d"] = s3.to_dict(orient="records")
        print(sweep.to_string(float_format="%.4g"))
        print(s3.to_string(float_format="%.4g"))

    race_dir = RES / "race" / "rpe"
    race_names = [n for n in METHODS if (race_dir / f"{n}.csv").exists()]
    if race_names:
        race = {n: load(n, race_dir) for n in race_names}
        time_axis(race)
        fig_race(race, [n for n in ("5pt", "8pt", "2pt", "arun") if n in race], "bonus_race_rpe")
        summary["_race"] = {n: stats(race[n]) for n in race_names}

    (RES / "summary.json").write_text(json.dumps(summary, indent=2))
    cols = ["frames", "rot_med_deg", "rot_lt1deg", "tu_med", "tu_lt05", "tu_lt01", "tm_med_mm",
            "inlier_ratio_med", "time_ms_med"]
    print(pd.DataFrame({k: v for k, v in summary.items() if not k.startswith("_")}).T[cols]
          .to_string(float_format="%.4g"))
    if "_race" in summary:
        print("race:")
        print(pd.DataFrame(summary["_race"]).T[cols + ["gt_step_med_mm", "matches_med"]]
              .to_string(float_format="%.4g"))


if __name__ == "__main__":
    main()
