#!/usr/bin/env python3
"""Replot the recorded Unity race and exact exercise solutions for the report."""
import csv
import json
import os
import subprocess
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import BoundaryNorm, ListedColormap, Normalize
from matplotlib.patches import FancyBboxPatch
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "report" / "figures"
OUT.mkdir(exist_ok=True)
RUN = ROOT / "report/runs/unity-gpu-rviz-20261020"
EARLIER = ROOT / "report/runs/unity-gpu-fast-20261019"
plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9,
    "legend.fontsize": 8, "legend.frameon": False, "svg.fonttype": "none", "pdf.fonttype": 42,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": 0.7, "lines.linewidth": 1.3,
    "savefig.facecolor": "white",
})
BLUE, ORANGE, GREY, LIGHT = "#24658A", "#BC6B39", "#666666", "#EFF0F2"
WIDTH = 160 / 25.4

# Optional render-time alignment gate; QA files go to FIGURE_QA_DIR when it is set.
QA = Path(os.environ["FIGURE_QA_DIR"]) if os.environ.get("FIGURE_QA_DIR") else None
if QA:
    QA.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, os.environ.get("FIGURE_QA_SCRIPTS", ""))
    from audit_panel_alignment import require_matplotlib_panel_alignment


def save(fig, name, **alignment):
    if QA:
        fig.canvas.draw()
        require_matplotlib_panel_alignment(fig, json_out=QA / (name + ".alignment.json"),
                                           tolerance_pt=1.5, gutter_tolerance_pt=1.5, **alignment)
    fig.savefig(OUT / (name + ".pdf"))
    fig.savefig(OUT / (name + ".svg"))
    fig.savefig(OUT / (name + ".png"), dpi=600)
    plt.close(fig)


def panel(ax, label, title):
    ax.set_title((label + "  " + title).strip(), loc="left", fontweight="bold", pad=9)
    ax.grid(axis="y", color="0.9", linewidth=0.5)
    ax.set_axisbelow(True)


def label_gates(ax, gates, angles, distance=11):
    """Place each index beside its gate, perpendicular to the flight direction."""
    for i, (g, a) in enumerate(zip(gates, angles)):
        ax.annotate(str(i), g[:2], xytext=(-distance*np.sin(a), distance*np.cos(a)),
                    textcoords="offset points", ha="center", va="center", fontsize=8)


def load_flight(path):
    d = np.genfromtxt(path, delimiter=",", names=True)
    assert len(d) > 0
    assert np.isfinite(np.column_stack([d[k] for k in d.dtype.names])).all()
    assert np.all(np.diff(d["t"]) > 0)
    return d


def euler_deg(d):
    q = np.column_stack([d[k] for k in ["qx", "qy", "qz", "qw"]])
    norm = np.linalg.norm(q, axis=1)
    assert np.all(norm > 1e-8)
    qx, qy, qz, qw = (q / norm[:, None]).T
    roll = np.arctan2(2*(qw*qx+qy*qz), 1-2*(qx*qx+qy*qy))
    pitch = np.arcsin(np.clip(2*(qw*qy-qz*qx), -1, 1))
    yaw = np.unwrap(np.arctan2(2*(qw*qz+qx*qy), 1-2*(qy*qy+qz*qz)))
    return np.degrees(roll), np.degrees(pitch), np.degrees(yaw), norm


def high_frequency(values, half_window=12):
    """Residual after a local quadratic fit over 2*half_window+1 samples (0.5 s at 50 Hz)."""
    x = np.arange(-half_window, half_window+1)
    smoother = np.linalg.pinv(np.vander(x, 3, increasing=True))[0]
    residual = values - np.convolve(values, smoother[::-1], mode="same")
    residual[:half_window] = residual[-half_window:] = np.nan
    return residual


d = load_flight(RUN / "unity_flight.csv")
actual = np.column_stack([d[k] for k in ("x", "y", "z")])
desired = np.column_stack([d[k] for k in ("xd", "yd", "zd")])
gate_list = []
gate_angles = {}
with (ROOT / "simulator_data/StreamingAssets/vnav-2020-lab4_static_tfs.csv").open() as f:
    for row in csv.reader(f):
        if row and row[0].startswith("red_square_drone_door"):
            index = int(row[0].split("(")[1].rstrip(")")) if "(" in row[0] else 0
            gate_list.append((index, [float(row[1]), float(row[3]), float(row[2])]))
            q = np.array([-float(row[4]), -float(row[6]), -float(row[5]), float(row[7])])
            q /= np.linalg.norm(q)
            qx, qy, qz, qw = q
            gate_angles[index] = np.arctan2(2*(qw*qz+qx*qy), 1-2*(qy*qy+qz*qz))
gate_list.sort()
assert [i for i, _ in gate_list] == list(range(12))
gates = np.array([g for _, g in gate_list])
angles = np.array([gate_angles[i] for i in range(12)])
distances = np.linalg.norm(actual[:, None, :] - gates[None, :, :], axis=2)
indices = np.argmin(distances, axis=0)
assert np.all(np.diff(indices) > 0)
closest = distances[indices, np.arange(len(gates))]
gate_times = d["t"][indices]
error = np.linalg.norm(actual - desired, axis=1)
duration = float(d["trajectory_time"].max())
active = d["trajectory_time"] < duration
hold_start = float(d["t"][~active][0])
t_end = float(d["t"][-1])
speed = np.linalg.norm(np.gradient(actual, d["t"], axis=0), axis=1)
ref_speed = np.linalg.norm(np.gradient(desired, d["t"], axis=0), axis=1)
roll, pitch, yaw, qnorm = euler_deg(d)
tilt_hf = np.sqrt(high_frequency(roll)**2 + high_frequency(pitch)**2)
residual = actual - desired
axis_rms = np.sqrt(np.mean(residual[active]**2, axis=0))
summary = json.loads((RUN / "unity_summary.json").read_text())
metrics = {
    "rows_total": len(d), "rows_active": int(active.sum()), "rows_hold": int((~active).sum()),
    "trajectory_duration_s": duration, "record_duration_s": t_end,
    "hold_start_record_time_s": hold_start, "hold_duration_s": t_end - hold_start,
    "rms_tracking_error_m": float(np.sqrt(np.mean(error[active]**2))),
    "max_tracking_error_m": float(error[active].max()),
    "active_error_quantiles_m": dict(zip(["median", "p95"], map(float, np.quantile(error[active], [.5, .95])))),
    "axis_rms_m": dict(zip("xyz", map(float, axis_rms))),
    "hold_error_min_m": float(error[~active].min()),
    "hold_error_max_m": float(error[~active].max()),
    "final_position_error_m": float(np.linalg.norm(actual[-1] - gates[-1])),
    "peak_speed_m_s": float(speed.max()), "peak_reference_speed_m_s": float(ref_speed.max()),
    "mean_course_speed_m_s": float(np.sum(np.linalg.norm(np.diff(desired[active], axis=0), axis=1)) / duration),
    "path_length_m": float(np.sum(np.linalg.norm(np.diff(desired[active], axis=0), axis=1))),
    "peak_tilt_deg": float(np.max(np.degrees(np.arccos(np.clip(
        np.cos(np.radians(roll))*np.cos(np.radians(pitch)), -1, 1))))),
    "high_frequency_tilt_rms_deg": float(np.sqrt(np.nanmean(tilt_hf[active]**2))),
    "quaternion_norm_range": [float(qnorm.min()), float(qnorm.max())],
    "gate_center_visits": [dict(gate=i, time_s=float(gate_times[i]), min_center_distance_m=float(closest[i]))
                           for i in range(12)],
}
assert np.isclose(np.sum(axis_rms**2), metrics["rms_tracking_error_m"]**2)
for key in ("max_tracking_error_m", "final_position_error_m"):
    assert np.isclose(metrics[key], summary[key], rtol=1e-6), key
assert np.isclose(metrics["rms_tracking_error_m"], summary["rms_tracking_error_m"], rtol=2e-3)
assert np.isclose(metrics["high_frequency_tilt_rms_deg"], summary["high_frequency_tilt_rms_deg"], rtol=.05)
for computed, recorded in zip(metrics["gate_center_visits"], summary["gate_center_visits"]):
    assert computed["gate"] == recorded["gate"]
    assert np.isclose(computed["min_center_distance_m"], recorded["min_center_distance_m"])

e = load_flight(EARLIER / "unity_flight.csv")
e_roll, e_pitch, _, _ = euler_deg(e)
e_hf = np.sqrt(high_frequency(e_roll)**2 + high_frequency(e_pitch)**2)
e_active = e["trajectory_time"] < e["trajectory_time"].max()
metrics["earlier_unsynchronised"] = {
    "trajectory_duration_s": float(e["trajectory_time"].max()),
    "high_frequency_tilt_rms_deg": float(np.sqrt(np.nanmean(e_hf[e_active]**2))),
    "high_frequency_tilt_peak_deg": float(np.nanmax(e_hf[e_active])),
}
metrics["high_frequency_tilt_peak_deg"] = float(np.nanmax(tilt_hf[active]))
(OUT / "verified_metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
with (OUT / "gate_metrics.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["gate", "time_s", "min_center_distance_m"])
    writer.writeheader()
    writer.writerows(metrics["gate_center_visits"])

# Figure 1: node and topic topology from the implemented ROS interfaces.
fig, ax = plt.subplots(figsize=(WIDTH, 2.25))
fig.subplots_adjust(left=.01, right=.99, top=.98, bottom=.04)
ax.set(xlim=(0, 10), ylim=(0, 4)); ax.axis("off")
boxes = [(0.1, 2.2, "Gate poses", "Coordinate conversion\nand gate ordering"),
         (3.8, 2.2, "Trajectory generator", "Minimum snap with\nper-segment times"),
         (7.5, 2.2, "Lab 3 controller", "Matched desired and\ncurrent state"),
         (7.5, .05, "Unity simulator", "Quadrotor dynamics\nand state feedback")]
for x, y, title, body in boxes:
    ax.add_patch(FancyBboxPatch((x, y), 2.35, 1.35, boxstyle="round,pad=0.04",
                               facecolor="#EFF4F6", edgecolor="#9BAFBA", linewidth=.8))
    ax.text(x+1.175, y+1.05, title, ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(x+1.175, y+.48, body, ha="center", va="center", fontsize=8, linespacing=1.5)
arrow = dict(arrowstyle="->", color=GREY, lw=1)
ax.annotate("", xy=(3.76, 2.86), xytext=(2.49, 2.86), arrowprops=arrow)
ax.text(3.12, 3.16, "Waypoints", ha="center", fontsize=8)
ax.annotate("", xy=(7.46, 3.06), xytext=(6.19, 3.06), arrowprops=arrow)
ax.text(6.82, 3.3, "Desired state", ha="center", fontsize=8)
ax.annotate("", xy=(7.46, 2.62), xytext=(6.19, 2.62), arrowprops=arrow)
ax.text(6.82, 2.36, "Synced state", ha="center", fontsize=8)
ax.annotate("", xy=(9.2, 1.44), xytext=(9.2, 2.16), arrowprops=arrow)
ax.text(9.05, 1.8, "Commands", ha="right", fontsize=8)
ax.plot([7.46, 4.96, 4.96], [.73, .73, 2.06], color=GREY, lw=1)
ax.annotate("", xy=(4.96, 2.16), xytext=(4.96, 2.0), arrowprops=arrow)
ax.text(4.8, 1.36, "Current state", ha="right", fontsize=8)
ax.text(.15, .55, "Each state is forwarded only after the\nreference sampled at its own time stamp.",
        fontsize=8, color=GREY, va="center")
save(fig, "system_overview")

# Figure 2: exact polynomials, not experimental observations.
t = np.linspace(0, 1, 501)
polys = [(t, np.ones_like(t), BLUE, "Endpoint positions only"),
         (4*t-3*t*t, 4-6*t, ORANGE, "Terminal velocity: quadratic"),
         (.25*t+4.5*t*t-3.75*t**3, .25+9*t-11.25*t*t, GREY, "Terminal velocity: cubic")]
fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 3.1))
fig.subplots_adjust(left=.085, right=.98, top=.86, bottom=.36, wspace=.32)
for p, v, color, label in polys:
    axes[0].plot(t, p, color=color, label=label)
    axes[1].plot(t, v, color=color)
axes[0].set(xlabel="Normalised time, t", ylabel="Position, P(t)")
axes[1].set(xlabel="Normalised time, t", ylabel="Velocity, P′(t)")
axes[1].axhline(0, color="0.65", lw=.6)
panel(axes[0], "a", "Optimal position profiles")
panel(axes[1], "b", "Velocity and terminal condition")
fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=1,
           bbox_to_anchor=(.5, -.005), fontsize=8)
save(fig, "single_segment")
np.savetxt(OUT / "single_segment.csv", np.column_stack([t]+[p for p,_,_,_ in polys]+[v for _,v,_,_ in polys]),
           delimiter=",", header="t,p_linear,p_quadratic,p_cubic,v_linear,v_quadratic,v_cubic", comments="")

# Reduced objectives are exact consequences of the exercise constraints.
fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 2.8))
fig.subplots_adjust(left=.09, right=.98, bottom=.23, top=.82, wspace=.32)
u = np.linspace(-4, 4, 401)
axes[0].plot(u, 1+u*u/3, color=BLUE)
axes[0].scatter([0], [1], color=ORANGE, zorder=3)
axes[0].annotate("Minimum: (0, 1)", (0, 1), xytext=(.3, 2.0), fontsize=8)
axes[0].set(xlabel=r"Free coefficient $p_2$", ylabel="Cost J")
panel(axes[0], "a", "Position constraints only")
u = np.linspace(-8, 0, 401)
axes[1].plot(u, 4+u+2*u*u/15, color=BLUE)
axes[1].scatter([-15/4, 0], [17/8, 4], color=[ORANGE, GREY], zorder=3)
axes[1].annotate("Cubic: J = 17/8", (-15/4, 17/8), xytext=(-6.4, 2.75), fontsize=8)
axes[1].annotate("Quadratic: J = 4", (0, 4), xytext=(-5.8, 4.45), fontsize=8)
axes[1].set(xlabel=r"Free coefficient $p_3$", ylabel="Cost J")
panel(axes[1], "b", "Terminal velocity constrained")
save(fig, "reduced_objectives")

# A condition map distinguishes imposed continuity from natural conditions.
condition = np.full((8, 4), 3)
condition[:4, [0, 3]] = 0
condition[0, 1:3] = 0
condition[1:4, 1:3] = 1
condition[4:7, 1:3] = 2
fig, ax = plt.subplots(figsize=(WIDTH, 3.8))
fig.subplots_adjust(left=.21, right=.98, bottom=.25, top=.83)
ax.imshow(condition, cmap=ListedColormap(["#B8CFDE", "#E5CAA9", "#BAD5CE", "#F1F1F1"]),
          norm=BoundaryNorm(np.arange(-.5,4.5), 4), aspect="auto", interpolation="nearest")
for r in range(8):
    for c in range(4):
        ax.text(c, r, ["F", "C", "N", "·"][condition[r,c]], ha="center", va="center", fontsize=10)
ax.set(xticks=range(4), xticklabels=[r"Start $t_0$", r"Interior $t_1$", r"Interior $t_2$", r"End $t_3$"],
       yticks=range(8), yticklabels=["Position", "Velocity", "Acceleration", "Jerk", "Snap", "5th derivative", "6th derivative", "7th derivative"])
ax.set_title("Minimum-snap conditions for three degree-seven segments", fontsize=10, pad=12)
fig.text(.5, .09, "F: prescribed value     C: imposed continuity     N: natural continuity\n·: not prescribed at the boundary / no matching condition at the knot",
         ha="center", fontsize=8, linespacing=1.7)
save(fig, "continuity_map")

# Course headings use the same Unity-to-ROS quaternion conversion as the publisher.
fig, ax = plt.subplots(figsize=(WIDTH, 4.15))
fig.subplots_adjust(left=.09, right=.97, bottom=.14, top=.87)
ax.plot(gates[:,0], gates[:,1], color="0.8", linestyle=":", label="Gate order")
ax.scatter(gates[:,0], gates[:,1], marker="s", s=28, color=ORANGE)
ax.quiver(gates[:,0], gates[:,1], 2*np.cos(angles), 2*np.sin(angles),
          angles="xy", scale_units="xy", scale=1, color=BLUE, width=.005)
label_gates(ax, gates, angles)
ax.set(xlabel="World x (m)", ylabel="World y (m)", xlim=(-54,5), ylim=(-14,20))
ax.set_aspect("equal", adjustable="box")
panel(ax, "", "Gate-centre positions and map yaw directions"); ax.grid(False)
ax.text(.98,.03,"Arrow length is a display scale, not gate size", transform=ax.transAxes,
        ha="right", fontsize=8, color=GREY)
save(fig, "gate_headings")

# Hero figure: the whole race, coloured by speed, with speed and altitude through time.
fig = plt.figure(figsize=(WIDTH, 6.4))
grid = fig.add_gridspec(3, 1, height_ratios=[3.1, 1, 1], left=.1, right=.98, top=.95, bottom=.075, hspace=.5)
ax = fig.add_subplot(grid[0])
cax = ax.inset_axes([.64, .86, .3, .035])
points = actual[:, :2].reshape(-1, 1, 2)
segments = LineCollection(np.concatenate([points[:-1], points[1:]], axis=1),
                          cmap="cividis", norm=Normalize(0, 8), linewidth=2.2)
segments.set_array(speed[:-1])
ax.add_collection(segments)
ax.plot(desired[:, 0], desired[:, 1], color="white", linewidth=.6, linestyle=(0, (2, 2)), zorder=3)
ax.scatter(gates[:, 0], gates[:, 1], s=30, marker="s", facecolor="white", edgecolor=ORANGE, linewidth=1.1, zorder=4)
label_gates(ax, gates, angles)
ax.scatter(*actual[0, :2], s=22, color="black", zorder=5)
ax.annotate("Start", actual[0, :2], xytext=(-30, 2), textcoords="offset points", fontsize=8)
ax.set(xlabel="World x (m)", ylabel="World y (m)", xlim=(-53, 4), ylim=(-14, 20))
ax.set_aspect("equal", adjustable="box")
panel(ax, "a", "Recorded flight through the 12 gates"); ax.grid(False)
fig.colorbar(segments, cax=cax, orientation="horizontal")
cax.set_title("Recorded speed (m s$^{-1}$)", fontsize=8, pad=3)
cax.tick_params(labelsize=8)
speed_ax = fig.add_subplot(grid[1])
z_ax = fig.add_subplot(grid[2], sharex=speed_ax)
for axis in (speed_ax, z_ax):
    axis.axvspan(hold_start, t_end, color=LIGHT)
    for gt in gate_times[:-1]:
        axis.axvline(gt, color="0.85", linewidth=.6, zorder=0)
speed_ax.axhline(8, color=ORANGE, linestyle="--", linewidth=1)
speed_ax.text(19.4, 6.6, "Allocation limit, 8 m s$^{-1}$", fontsize=8, color=ORANGE)
speed_ax.plot(d["t"], ref_speed, color=GREY, linestyle="--", label="Reference")
speed_ax.plot(d["t"], speed, color=BLUE, label="Recorded")
speed_ax.set(ylabel="Speed (m s$^{-1}$)", ylim=(0, 9.5), xlim=(0, t_end))
speed_ax.legend(loc="center right", ncol=1)
plt.setp(speed_ax.get_xticklabels(), visible=False)
panel(speed_ax, "b", "Speed; thin lines mark gate passages")
z_ax.plot(d["t"], desired[:, 2], color=GREY, linestyle="--")
z_ax.plot(d["t"], actual[:, 2], color=BLUE)
z_ax.text(hold_start+.3, 3.0, "Final reference held", fontsize=8, color=GREY)
z_ax.set(xlabel="Simulation time (s)", ylabel="World z (m)", ylim=(0, 4))
panel(z_ax, "c", "Altitude")
save(fig, "race_overview", exclude_axes=[cax], exemptions=[dict(
    panels=["a"], checks=["column"], reason="Equal-aspect course map keeps metric geometry")])

# Tracking accuracy across the race, at every gate and during the final hold.
fig = plt.figure(figsize=(WIDTH, 4.6))
grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.1], left=.1, right=.98, top=.93, bottom=.11,
                        hspace=.62, wspace=.3)
ax = fig.add_subplot(grid[0, :])
ax.axvspan(hold_start, t_end, color=LIGHT)
ax.plot(d["t"], 100*error, color=BLUE)
ax.text(1, 13, "Active flight: RMS %.1f cm, maximum %.1f cm" % (100*metrics["rms_tracking_error_m"],
        100*metrics["max_tracking_error_m"]), fontsize=8)
ax.text(hold_start+.3, 13, "Final hold", fontsize=8, color=GREY)
ax.set(xlabel="Simulation time (s)", ylabel="Position error (cm)", xlim=(0, t_end), ylim=(0, 15))
panel(ax, "a", "Tracking error over the complete recording")
ax = fig.add_subplot(grid[1, 0])
ax.vlines(np.arange(12), 0, 100*closest, color="#AFC3CF", linewidth=2)
ax.scatter(np.arange(12), 100*closest, color=BLUE, s=22, zorder=3)
ax.set(xlabel="Gate index", ylabel="Distance to centre (cm)", xticks=np.arange(12), ylim=(0, 10), xlim=(-.6, 11.6))
panel(ax, "b", "Closest approach to each gate")
ax = fig.add_subplot(grid[1, 1])
th = d["t"][~active] - hold_start
ax.plot(th, 100*error[~active], color=BLUE)
ax.scatter(th[-1], 100*error[-1], color=ORANGE, s=18, zorder=3)
ax.annotate("%.1f cm" % (100*error[-1]), (th[-1], 100*error[-1]), xytext=(-30, 9),
            textcoords="offset points", fontsize=8, color=ORANGE)
ax.set(xlabel="Time in final hold (s)", ylabel="Position error (cm)", xlim=(0, th[-1]+.3), ylim=(0, 10))
panel(ax, "c", "Settling at the last gate")
save(fig, "tracking_accuracy")

# Attitude: the race demands large tilts, and the state-stamped reference keeps them smooth.
fig, axes = plt.subplots(2, 1, figsize=(WIDTH, 3.9))
fig.subplots_adjust(left=.1, right=.98, top=.92, bottom=.13, hspace=.62)
ax = axes[0]
ax.axvspan(hold_start, t_end, color=LIGHT)
ax.plot(d["t"], roll, color=BLUE, label="Roll")
ax.plot(d["t"], pitch, color=ORANGE, label="Pitch")
ax.set(ylabel="Angle (deg)", xlim=(0, t_end), xlabel="Simulation time (s)")
ax.legend(loc="upper right", ncol=2)
panel(ax, "a", "Recorded roll and pitch")
ax = axes[1]
te = e["t"] / e["trajectory_time"].max()
tf = d["t"] / duration
ax.plot(te[e_active], e_hf[e_active], color="0.6", linewidth=.9,
        label="Timer-sampled reference (%.2f° RMS)" % metrics["earlier_unsynchronised"]["high_frequency_tilt_rms_deg"])
ax.plot(tf[active], tilt_hf[active], color=BLUE, linewidth=1.1,
        label="State-stamped reference (%.2f° RMS)" % metrics["high_frequency_tilt_rms_deg"])
ax.set(xlabel="Fraction of the race completed", ylabel="Tilt jitter (deg)", xlim=(0, 1), ylim=(0, 3))
ax.legend(loc="upper right")
panel(ax, "b", "High-frequency tilt, residual to a 0.5 s local fit")
save(fig, "attitude_smoothness")

# Each gate gets a +/-1 s local projection on the gate heading.
local_counts = []
for start in [0, 6]:
    fig, axes = plt.subplots(2, 3, figsize=(WIDTH, 3.15), sharex=True, sharey=True)
    fig.subplots_adjust(left=.10, right=.98, bottom=.26, top=.88, hspace=.75, wspace=.20)
    for ax, i in zip(axes.flat, range(start, start+6)):
        # The last gate is approached as the reference ends, so its window ends there.
        mask = np.abs(d["t"]-min(gate_times[i], hold_start)) <= 1
        assert mask.sum() > 1
        local_counts.append(dict(gate=i, rows=int(mask.sum()), window_s=1))
        direction = np.array([np.cos(angles[i]), np.sin(angles[i])])
        for positions, color, style, label in [(desired, GREY, "--", "Reference"), (actual, BLUE, "-", "Recorded")]:
            delta = positions[mask]-gates[i]
            along = delta[:, :2] @ direction
            keep = np.abs(along) <= 4.5
            ax.plot(along[keep], delta[keep, 2], color=color, linestyle=style, label=label)
        ax.scatter([0], [0], color=ORANGE, s=24, marker="s", label="Gate centre", zorder=4)
        ax.axhline(0, color="0.85", linewidth=.5)
        ax.set(xlim=(-4.5, 4.5), ylim=(-1.5, 1.5))
        panel(ax, "", "Gate %d; %.1f cm" % (i, 100*closest[i]))
    fig.text(.015, .56, "Height offset (m)", rotation=90, va="center", fontsize=9)
    fig.text(.54, .14, "Along-heading offset (m)", ha="center", fontsize=9)
    fig.legend(*axes.flat[0].get_legend_handles_labels(), loc="lower center", ncol=3, bbox_to_anchor=(.5, 0), fontsize=8)
    save(fig, "gate_local_%02d_%02d" % (start, start+5))

# Decoded frames from the simultaneous Unity and RViz recordings; only the RViz frame is cropped to its 3D view.
frames = OUT / "video_frames"
frames.mkdir(exist_ok=True)
import imageio_ffmpeg
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
unity_times = [5, 8, 11, 14, 17, 21]
rviz_time, rviz_crop = 26, (243, 570, 366, 1262)
for name, video, at in [("unity_%02ds.png" % s, "unity_gpu_race.mp4", s) for s in unity_times] + \
                       [("rviz_%02ds.png" % rviz_time, "rviz_gpu_race.mp4", rviz_time)]:
    subprocess.run([ffmpeg, "-v", "error", "-y", "-ss", str(at), "-i", str(ROOT/"report/video"/video),
                    "-frames:v", "1", str(frames/name)], check=True)
(frames / "frames_gpu.json").write_text(json.dumps({
    "unity": {"video": "report/video/unity_gpu_race.mp4", "playback_times_s": unity_times,
              "transform": "Full 960x600 frame, no crop or colour adjustment"},
    "rviz": {"video": "report/video/rviz_gpu_race.mp4", "playback_time_s": rviz_time,
             "crop_rows_cols": rviz_crop, "transform": "Cropped to the 3D view, no colour adjustment"},
    "time_basis": "Video playback time; both videos were recorded simultaneously"}, indent=2) + "\n")
fig = plt.figure(figsize=(WIDTH, 5.75))
grid = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1.79], left=.015, right=.985, top=.95, bottom=.01,
                        hspace=.2, wspace=.045)
for k, (s, letter) in enumerate(zip(unity_times, "abcdef")):
    ax = fig.add_subplot(grid[k // 3, k % 3])
    raw = plt.imread(frames/("unity_%02ds.png" % s))
    assert raw.shape[:2] == (600, 960)
    ax.imshow(raw, interpolation="none"); ax.axis("off")
    ax.set_title("%s  %d s" % (letter, s), loc="left", fontsize=9, pad=4)
ax = fig.add_subplot(grid[2, :])
raw = plt.imread(frames/("rviz_%02ds.png" % rviz_time))
assert raw.shape[:2] == (800, 1280)
r0, r1, c0, c1 = rviz_crop
ax.imshow(raw[r0:r1, c0:c1], interpolation="none"); ax.axis("off")
ax.set_title("g  RViz at %d s: planned path and recorded path" % rviz_time, loc="left", fontsize=9, pad=4)
save(fig, "race_video")

expanded = {"local_gate_windows": local_counts,
            "local_gate_window_definition": "Rows within +/-1 s of each closest approach (gate 11: of the end of the reference), clipped to +/-4.5 m along the gate heading"}
(OUT/"expanded_metrics.json").write_text(json.dumps(expanded, indent=2)+"\n")
print(json.dumps(metrics, indent=2))
