#!/usr/bin/env python3
"""Generate every figure of the Lab 9 report from results/ into report/figures/.

D1  : results/d1/spy_pattern.txt  -> d1_spy_*.pdf   (original + predicted marginalisation patterns)
D6  : results/d6/{kimera/kimera.txt, orbslam/orb_slam3.txt, data.tum}
      -> d6_unaligned.pdf, d6_aligned.pdf, d6_ate_time.pdf ; results/d6/metrics.json
      results/d6/evo/traj_*_trajectories.png (evo_traj --save_plot) -> d6_evo_traj_*.png
"""
import copy
import json
import shutil
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from evo.core import metrics, sync  # noqa: E402
from evo.tools import file_interface  # noqa: E402

LAB = Path(__file__).resolve().parents[1]
RES = LAB / "results"
FIG = LAB / "report" / "figures"
FIG.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({"font.size": 9, "axes.titlesize": 9, "legend.fontsize": 8,
                     "savefig.bbox": "tight", "pdf.fonttype": 42})
C_GT, C_KIM, C_ORB = "0.35", "#1f77b4", "#d62728"


# --------------------------------------------------------------------------- D1
def load_spy():
    names = [f"x{i}" for i in range(1, 9)] + [f"l{i}" for i in range(1, 13)]
    idx = {n: i for i, n in enumerate(names)}
    A = np.eye(len(names), dtype=bool)
    for line in (RES / "d1" / "spy_pattern.txt").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        a, rest = line.split(":")
        for b in rest.split():
            A[idx[a], idx[b]] = A[idx[b], idx[a]] = True
    return names, A


def marginalize(names, A, drop):
    """Symbolic Schur complement: neighbours of the eliminated set become a clique
    (per connected component of the eliminated variables)."""
    A = A.copy()
    for d in drop:  # eliminate one at a time (exact for symbolic fill-in)
        i = names.index(d)
        nb = np.flatnonzero(A[i])
        A[np.ix_(nb, nb)] = True
        keep = [k for k in range(len(names)) if k != i]
        A = A[np.ix_(keep, keep)]
        names = [names[k] for k in keep]
    return names, A


def spy(ax, names, A, ref=None, title=""):
    n = len(names)
    npos = sum(nm.startswith("x") for nm in names)
    img = np.ones((n, n, 3))
    img[A] = (0.35, 0.35, 0.35)
    if ref is not None:
        img[A & ~ref] = (0.84, 0.15, 0.16)  # fill-in
    ax.imshow(img, interpolation="nearest")
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(names, rotation=90, fontsize=6)
    ax.set_yticklabels(names, fontsize=6)
    ax.set_xticks(np.arange(-.5, n), minor=True)
    ax.set_yticks(np.arange(-.5, n), minor=True)
    ax.grid(which="minor", color="0.85", lw=0.4)
    ax.tick_params(which="both", length=0)
    ax.axhline(npos - .5, color="k", lw=1)
    ax.axvline(npos - .5, color="k", lw=1)
    ax.set_title(title)


def d1():
    names, A = load_spy()
    cases = [
        ("d1_spy_original", names, A, None, "Original (8 poses, 12 landmarks)"),
    ]
    n6, A6 = marginalize(names, A, ["l2"])
    cases.append(("d1_spy_marg_l2", n6, A6, A[np.ix_([names.index(k) for k in n6],
                                                     [names.index(k) for k in n6])],
                  "After marginalising $l_2$"))
    n7, A7 = marginalize(names, A, [f"x{i}" for i in range(1, 8)])
    cases.append(("d1_spy_marg_past_poses", n7, A7,
                  A[np.ix_([names.index(k) for k in n7], [names.index(k) for k in n7])],
                  "After marginalising $x_1,\\dots,x_7$"))
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.9),
                             gridspec_kw={"width_ratios": [20, 19, 13]})
    for ax, (_, nm, M, ref, title) in zip(axes, cases):
        spy(ax, nm, M, ref, title)
    fig.savefig(FIG / "d1_spy_marginalization.pdf")
    plt.close(fig)

    # D1.8: which single eliminations create no fill-in
    nofill = []
    for v in names:
        n2, A2 = marginalize(names, A, [v])
        ref = A[np.ix_([names.index(k) for k in n2], [names.index(k) for k in n2])]
        if (A2 == ref).all():
            nofill.append(v)
    counts = {nm: int(A[i, 8:].sum()) for i, nm in enumerate(names[:8])}
    out = {"poses": 8, "landmarks": 12, "landmarks_per_pose": counts,
           "observers_of_l2": [names[i] for i in np.flatnonzero(A[names.index("l2"), :8])],
           "no_fill_in_variables": nofill}
    (RES / "d1" / "answers.json").write_text(json.dumps(out, indent=2))
    print("D1:", out)


# --------------------------------------------------------------------------- D6
def d6():
    d = RES / "d6"
    gt = file_interface.read_tum_trajectory_file(str(d / "data.tum"))
    est = {
        "Kimera-VIO": file_interface.read_tum_trajectory_file(str(d / "kimera" / "kimera.txt")),
        "ORB-SLAM3": file_interface.read_tum_trajectory_file(str(d / "orbslam" / "orb_slam3.txt")),
    }
    color = {"Kimera-VIO": C_KIM, "ORB-SLAM3": C_ORB}
    res = {"gt": {"poses": gt.num_poses, "length_m": float(gt.path_length),
                  "t0": float(gt.timestamps[0]), "t1": float(gt.timestamps[-1])}}

    # ---------- unaligned (each in its own world frame), top + side view
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for name, tr in est.items():
        p = tr.positions_xyz
        axes[0].plot(p[:, 0], p[:, 1], color=color[name], lw=1, label=name)
        axes[0].plot(*p[0, :2], "o", color=color[name], ms=4)
        axes[1].plot(tr.timestamps - gt.timestamps[0], p[:, 2], color=color[name], lw=1,
                     label=name)
        res[name] = {"poses": tr.num_poses, "t0": float(tr.timestamps[0]),
                     "t1": float(tr.timestamps[-1]), "length_m": float(tr.path_length),
                     "start_xyz": p[0].tolist(), "end_xyz": p[-1].tolist()}
    axes[0].set(xlabel="x [m]", ylabel="y [m]", title="Top view (x-y), no alignment")
    axes[0].axis("equal")
    axes[1].set(xlabel="t [s] (from first ground-truth stamp)", ylabel="z [m]",
                title="Height z(t), no alignment")
    for ax in axes:
        ax.grid(alpha=.3)
        ax.legend()
    fig.savefig(FIG / "d6_unaligned.pdf")
    plt.close(fig)

    # ---------- aligned to GT (SE(3) Umeyama, as evo_traj --align)
    aligned = {}
    for name, tr in est.items():
        ref, e = sync.associate_trajectories(gt, tr, max_diff=0.01)
        e_se3 = copy.deepcopy(e)
        r, t, s = e_se3.align(ref, correct_scale=False)
        ape = metrics.APE(metrics.PoseRelation.translation_part)
        ape.process_data((ref, e_se3))
        st = ape.get_all_statistics()
        e_sim = copy.deepcopy(e)
        _, _, scale = e_sim.align(ref, correct_scale=True)
        ape_s = metrics.APE(metrics.PoseRelation.translation_part)
        ape_s.process_data((ref, e_sim))
        rot = metrics.APE(metrics.PoseRelation.rotation_angle_deg)
        rot.process_data((ref, e_se3))
        # odometric drift: align only the first matched pose (evo --align_origin) and
        # look at the end-point error, as for a pure odometry evaluation
        e_o = copy.deepcopy(e)
        e_o.align_origin(ref)
        dev = np.linalg.norm(e_o.positions_xyz - ref.positions_xyz, axis=1)
        drift = float(dev[-1])
        # rotation that maps the estimate's world frame onto the GT world frame
        yaw = float(np.degrees(np.arctan2(r[1, 0], r[0, 0])))
        tilt = float(np.degrees(np.arccos(np.clip(r[2, 2], -1, 1))))
        res[name].update({
            "matched_poses": e.num_poses,
            "ate_se3": {k: float(v) for k, v in st.items()},
            "rot_err_deg_se3": {k: float(v) for k, v in rot.get_all_statistics().items()},
            "ate_sim3_rmse": float(ape_s.get_statistic(metrics.StatisticsType.rmse)),
            "sim3_scale": float(scale),
            "align_R": r.tolist(), "align_t": t.tolist(),
            "align_yaw_deg": yaw, "align_tilt_deg": tilt,
            "end_error_origin_align_m": drift,
            "max_error_origin_align_m": float(dev.max()),
            "ref_length_m": float(ref.path_length),
        })
        aligned[name] = (ref, e_se3, ape.error)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
    ref0 = aligned["ORB-SLAM3"][0]
    axes[0].plot(gt.positions_xyz[:, 0], gt.positions_xyz[:, 1], "--", color=C_GT, lw=1.2,
                 label="Ground truth")
    axes[1].plot(gt.timestamps - gt.timestamps[0], gt.positions_xyz[:, 2], "--", color=C_GT,
                 lw=1.2, label="Ground truth")
    for name, (ref, e, _) in aligned.items():
        p = e.positions_xyz
        axes[0].plot(p[:, 0], p[:, 1], color=color[name], lw=.9, label=name)
        axes[1].plot(e.timestamps - gt.timestamps[0], p[:, 2], color=color[name], lw=.9,
                     label=name)
    axes[0].set(xlabel="x [m]", ylabel="y [m]", title="Top view, SE(3)-aligned to ground truth")
    axes[0].axis("equal")
    axes[1].set(xlabel="t [s]", ylabel="z [m]", title="Height z(t), aligned")
    for ax in axes:
        ax.grid(alpha=.3)
        ax.legend()
    fig.savefig(FIG / "d6_aligned.pdf")
    plt.close(fig)
    del ref0

    fig, ax = plt.subplots(figsize=(10, 2.8))
    for name, (ref, e, err) in aligned.items():
        ax.plot(e.timestamps - gt.timestamps[0], err, color=color[name], lw=.9,
                label=f"{name} (RMSE {res[name]['ate_se3']['rmse']:.3f} m)")
    ax.set(xlabel="t [s]", ylabel="position error [m]",
           title="Absolute trajectory error after SE(3) alignment")
    ax.grid(alpha=.3)
    ax.legend()
    fig.savefig(FIG / "d6_ate_time.pdf")
    plt.close(fig)

    # the evo_traj plots themselves (handout commands, saved by scripts/evaluate.sh)
    for tag in ("unaligned", "aligned"):
        src = d / "evo" / f"traj_{tag}_trajectories.png"
        if src.exists():
            shutil.copyfile(src, FIG / f"d6_evo_traj_{tag}.png")

    (d / "metrics.json").write_text(json.dumps(res, indent=2))
    print(json.dumps({k: (v if k == "gt" else {kk: vv for kk, vv in v.items()
                                                if kk not in ("align_R",)})
                      for k, v in res.items()}, indent=1))


# --------------------------------------------------------------------------- D7
def d7():
    """LDSO + Kimera + ORB-SLAM3, each Sim(3)-aligned (scale corrected) to ground truth."""
    d6d, d = RES / "d6", RES / "d7"
    gt = file_interface.read_tum_trajectory_file(str(d6d / "data.tum"))
    est = {
        "Kimera-VIO": d6d / "kimera" / "kimera.txt",
        "ORB-SLAM3": d6d / "orbslam" / "orb_slam3.txt",
        "LDSO": d / "ldso.txt",
        "LDSO (no loop closure)": d / "ldso_noloop.txt",
    }
    color = {"Kimera-VIO": C_KIM, "ORB-SLAM3": C_ORB, "LDSO": "#2ca02c",
             "LDSO (no loop closure)": "#9467bd"}
    res, aligned = {}, {}
    for name, path in est.items():
        tr = file_interface.read_tum_trajectory_file(str(path))
        ref, e = sync.associate_trajectories(gt, tr, max_diff=0.01)
        e_se3 = copy.deepcopy(e)
        e_se3.align(ref, correct_scale=False)
        ape_se3 = metrics.APE(metrics.PoseRelation.translation_part)
        ape_se3.process_data((ref, e_se3))
        _, _, s = e.align(ref, correct_scale=True)
        ape = metrics.APE(metrics.PoseRelation.translation_part)
        ape.process_data((ref, e))
        st = ape.get_all_statistics()
        res[name] = {"poses": tr.num_poses, "matched_poses": e.num_poses,
                     "t0": float(tr.timestamps[0]), "t1": float(tr.timestamps[-1]),
                     "raw_length": float(tr.path_length), "sim3_scale": float(s),
                     "ate_sim3": {k: float(v) for k, v in st.items()},
                     "ate_se3_rmse": float(ape_se3.get_statistic(metrics.StatisticsType.rmse))}
        aligned[name] = (e, ape.error)

    fig = plt.figure(figsize=(10, 6.6))
    gs = fig.add_gridspec(2, 2, height_ratios=[2.2, 1])
    ax = fig.add_subplot(gs[0, 0])
    ax.plot(gt.positions_xyz[:, 0], gt.positions_xyz[:, 1], "--", color=C_GT, lw=1.2,
            label="Ground truth")
    for name in ("Kimera-VIO", "ORB-SLAM3", "LDSO"):
        p = aligned[name][0].positions_xyz
        ax.plot(p[:, 0], p[:, 1], color=color[name], lw=.9, label=name)
    ax.set(xlabel="x [m]", ylabel="y [m]", title="x-y plane, Sim(3)-aligned (scale corrected)")
    ax.axis("equal")
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(gt.positions_xyz[:, 0], gt.positions_xyz[:, 1], "--", color=C_GT, lw=1.2,
             label="Ground truth")
    for name in ("LDSO", "LDSO (no loop closure)"):
        p = aligned[name][0].positions_xyz
        ax2.plot(p[:, 0], p[:, 1], color=color[name], lw=.9, label=name)
    ax2.set(xlabel="x [m]", ylabel="y [m]", title="LDSO with / without loop closure")
    ax2.axis("equal")
    ax3 = fig.add_subplot(gs[1, :])
    for name, (e, err) in aligned.items():
        ax3.plot(e.timestamps - gt.timestamps[0], err, color=color[name], lw=.9,
                 label=f"{name} (RMSE {res[name]['ate_sim3']['rmse']:.3f} m)")
    ax3.set(xlabel="t [s]", ylabel="position error [m]",
            title="Absolute trajectory error after Sim(3) alignment")
    for a in (ax, ax2, ax3):
        a.grid(alpha=.3)
        a.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIG / "d7_sim3_aligned.pdf")
    plt.close(fig)

    src = d / "evo" / "traj_sim3_xy_trajectories.png"
    if src.exists():
        shutil.copyfile(src, FIG / "d7_evo_traj_sim3_xy.png")
    (d / "metrics.json").write_text(json.dumps(res, indent=2))
    print("D7:", json.dumps({k: {**{kk: v[kk] for kk in ("poses", "matched_poses",
                                                         "sim3_scale", "ate_se3_rmse")},
                                 "ate_sim3_rmse": v["ate_sim3"]["rmse"]}
                             for k, v in res.items()}, indent=1))


if __name__ == "__main__":
    d1()
    if (RES / "d6" / "data.tum").exists():
        d6()
    else:
        print("results/d6/data.tum missing: run scripts/evaluate.sh first")
    if (RES / "d7" / "ldso.txt").exists():
        d7()
    else:
        print("results/d7/ldso.txt missing: run scripts/run_ldso.sh + evaluate_d7.sh first")
