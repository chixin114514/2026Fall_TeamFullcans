#!/usr/bin/env python3
"""Replot the recorded Unity flight and exact exercise solutions for the report."""
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "report" / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Arial", "DejaVu Sans"],
    "font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9,
    "legend.fontsize": 8, "legend.frameon": False, "svg.fonttype": "none", "pdf.fonttype": 42,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": 0.7, "lines.linewidth": 1.3,
    "savefig.facecolor": "white",
})
BLUE, ORANGE, GREY = "#24658A", "#BC6B39", "#666666"
WIDTH = 160 / 25.4


def save(fig, name):
    fig.savefig(OUT / (name + ".pdf"))
    fig.savefig(OUT / (name + ".svg"))
    fig.savefig(OUT / (name + ".png"), dpi=600)
    plt.close(fig)


def panel(ax, label, title):
    ax.set_title(label + "  " + title, loc="left", fontweight="bold", pad=9)
    ax.grid(axis="y", color="0.9", linewidth=0.5)
    ax.set_axisbelow(True)


d = np.genfromtxt(ROOT / "report/unity_flight.csv", delimiter=",", names=True)
assert len(d) > 0
assert np.isfinite(np.column_stack([d[k] for k in d.dtype.names])).all()
assert np.all(np.diff(d["t"]) > 0)
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
distances = np.linalg.norm(actual[:, None, :] - gates[None, :, :], axis=2)
indices = np.argmin(distances, axis=0)
assert np.all(np.diff(indices) > 0)
closest = distances[indices, np.arange(len(gates))]
error = np.linalg.norm(actual - desired, axis=1)
duration = float(d["trajectory_time"].max())
active = d["trajectory_time"] < duration - .01
hold_start = float(d["t"][~active][0])
summary = json.loads((ROOT / "report/unity_summary.json").read_text())
metrics = {
    "rows_total": len(d), "rows_active": int(active.sum()),
    "rows_hold": int((~active).sum()),
    "trajectory_duration_s": duration, "record_duration_s": float(d["t"][-1]),
    "hold_start_record_time_s": hold_start,
    "rms_tracking_error_m": float(np.sqrt(np.mean(error[active] ** 2))),
    "max_tracking_error_m": float(error[active].max()),
    "hold_error_min_m": float(error[~active].min()),
    "hold_error_max_m": float(error[~active].max()),
    "final_position_error_m": float(np.linalg.norm(actual[-1] - gates[-1])),
    "gate_center_visits": [dict(gate=i, time_s=float(d["t"][j]),
                                min_center_distance_m=float(closest[i]))
                           for i, j in enumerate(indices)],
}
for key in ("rms_tracking_error_m", "max_tracking_error_m", "final_position_error_m"):
    assert np.isclose(metrics[key], summary[key], rtol=1e-9, atol=1e-10), key
for computed, recorded in zip(metrics["gate_center_visits"], summary["gate_center_visits"]):
    assert computed["gate"] == recorded["gate"]
    assert np.isclose(computed["time_s"], recorded["time_s"])
    assert np.isclose(computed["min_center_distance_m"], recorded["min_center_distance_m"])
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
         (3.8, 2.2, "Trajectory generator", "Position + unwrapped yaw\nMinimum-snap polynomials"),
         (7.5, 2.2, "Lab 3 controller", "Desired and current state\nRotor commands"),
         (7.5, .05, "Unity + TESSE bridge", "Simulated dynamics\nand state feedback")]
for x, y, title, body in boxes:
    ax.add_patch(FancyBboxPatch((x, y), 2.35, 1.35, boxstyle="round,pad=0.04",
                               facecolor="#EFF4F6", edgecolor="#9BAFBA", linewidth=.8))
    ax.text(x+1.175, y+1.05, title, ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(x+1.175, y+.48, body, ha="center", va="center", fontsize=8, linespacing=1.5)
arrow = dict(arrowstyle="->", color=GREY, lw=1)
ax.annotate("", xy=(3.76, 2.86), xytext=(2.49, 2.86), arrowprops=arrow)
ax.text(3.12, 3.16, "Waypoints", ha="center", fontsize=8)
ax.annotate("", xy=(7.46, 2.86), xytext=(6.19, 2.86), arrowprops=arrow)
ax.text(6.82, 3.16, "Desired state", ha="center", fontsize=8)
ax.annotate("", xy=(9.2, 1.44), xytext=(9.2, 2.16), arrowprops=arrow)
ax.text(9.0, 1.8, "Commands", ha="right", fontsize=8)
ax.plot([7.46, 4.96, 4.96], [.73, .73, 2.06], color=GREY, lw=1)
ax.annotate("", xy=(4.96, 2.16), xytext=(4.96, 2.0), arrowprops=arrow)
ax.text(4.55, 1.36, "Current state", ha="right", fontsize=8)
ax.annotate("", xy=(7.85, 2.16), xytext=(7.85, 1.44), arrowprops=arrow)
ax.text(7.69, 1.8, "State", ha="right", fontsize=8)
ax.text(.15, .55, "Gate poses are published at 5 Hz.\nReferences use elapsed ROS simulation time.",
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

# Figure 3: all samples are retained, including the terminal hold.
fig, axes = plt.subplots(2, 1, figsize=(WIDTH, 5.1), gridspec_kw={"height_ratios": [2.3, 1]})
fig.subplots_adjust(left=.1, right=.98, top=.93, bottom=.1, hspace=.56)
ax = axes[0]
ax.plot(desired[:, 0], desired[:, 1], color=GREY, linestyle="--", label="Reference", zorder=3)
ax.plot(actual[:, 0], actual[:, 1], color=BLUE, label="Recorded position", zorder=2)
ax.scatter(gates[:, 0], gates[:, 1], s=28, marker="s", facecolor="white", edgecolor=ORANGE, label="Gate centre", zorder=4)
for i, g in enumerate(gates):
    ax.annotate(str(i), g[:2], xytext=(4, 5), textcoords="offset points", fontsize=8)
ax.scatter(*actual[0, :2], s=25, color=BLUE, marker="o")
ax.annotate("Start", actual[0, :2], xytext=(-28, 7), textcoords="offset points", fontsize=8)
ax.set(xlabel="World x (m)", ylabel="World y (m)", xlim=(-53, 4), ylim=(-14, 20))
ax.set_aspect("equal", adjustable="box")
ax.legend(loc="upper right", fontsize=8)
panel(ax, "a", "Course geometry and recorded flight")
ax = axes[1]
ax.axvspan(hold_start, d["t"][-1], color="#EFF0F2", label="Terminal reference held")
ax.plot(d["t"], desired[:, 2], color=GREY, linestyle="--")
ax.plot(d["t"], actual[:, 2], color=BLUE)
ax.set(xlabel="Recorded simulation time (s)", ylabel="World z (m)", xlim=(0, 122))
ax.legend(loc="upper right", fontsize=8)
panel(ax, "b", "Altitude through the course")
save(fig, "unity_trajectory")

# Figure 4: active tracking and terminal errors are displayed without averaging away peaks.
fig, axes = plt.subplots(2, 1, figsize=(WIDTH, 3.55))
fig.subplots_adjust(left=.11, right=.98, top=.92, bottom=.14, hspace=.72)
ax = axes[0]
ax.axvspan(hold_start, d["t"][-1], color="#EFF0F2")
ax.plot(d["t"], error, color=BLUE)
ax.hlines(.20, hold_start, d["t"][-1], color=ORANGE, linestyle="--", linewidth=1)
ax.text(96, .64, "Terminal hold", color=GREY, fontsize=8)
ax.text(4, .64, "Active tracking: RMS 0.319 m; maximum 0.578 m", fontsize=8)
ax.scatter(d["t"][-1], error[-1], s=17, color=ORANGE, zorder=4)
ax.set(xlabel="Recorded simulation time (s)", ylabel="Position error (m)", xlim=(0, 123), ylim=(0, .72))
panel(ax, "a", "Tracking error over the complete recording")
ax = axes[1]
ax.vlines(np.arange(12), 0, closest, color="#AFC3CF", linewidth=2)
ax.scatter(np.arange(12), closest, color=BLUE, s=24, zorder=3)
for i, value in enumerate(closest):
    ax.text(i, value+.022, "{:.3f}".format(value), ha="center", fontsize=8)
ax.set(xlabel="Gate index", ylabel="Closest centre distance (m)", xticks=np.arange(12), ylim=(0, .55), xlim=(-.6, 11.6))
panel(ax, "b", "Closest recorded approach to each gate")
save(fig, "unity_errors")

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
from matplotlib.colors import ListedColormap, BoundaryNorm
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
angles = np.array([gate_angles[i] for i in range(12)])
fig, ax = plt.subplots(figsize=(WIDTH, 4.15))
fig.subplots_adjust(left=.09, right=.97, bottom=.14, top=.87)
ax.plot(gates[:,0], gates[:,1], color="0.8", linestyle=":", label="Gate order")
ax.scatter(gates[:,0], gates[:,1], marker="s", s=28, color=ORANGE)
ax.quiver(gates[:,0], gates[:,1], 2*np.cos(angles), 2*np.sin(angles),
          angles="xy", scale_units="xy", scale=1, color=BLUE, width=.005)
for i,g in enumerate(gates):
    ax.annotate(str(i), g[:2], xytext=(4,5), textcoords="offset points", fontsize=8)
ax.set(xlabel="World x (m)", ylabel="World y (m)", xlim=(-54,5), ylim=(-14,20))
ax.set_aspect("equal", adjustable="box")
panel(ax, "", "Gate-centre positions and map yaw directions")
ax.text(.98,.03,"Arrow length is a display scale, not gate size", transform=ax.transAxes,
        ha="right", fontsize=8, color=GREY)
save(fig, "gate_headings")

fig = plt.figure(figsize=(WIDTH, 4.15))
ax = fig.add_subplot(111, projection="3d")
ax.plot(*desired.T, color=GREY, linestyle="--", label="Reference")
ax.plot(*actual.T, color=BLUE, label="Recorded position")
ax.scatter(*gates.T, color=ORANGE, marker="s", s=22, label="Gate centre")
for i,g in enumerate(gates):
    ax.text(g[0],g[1],g[2]+.22,str(i),fontsize=8)
ax.set(xlabel="World x (m)", ylabel="World y (m)", zlabel="World z (m)")
ax.set_box_aspect((54,28,16)); ax.view_init(elev=24, azim=-65)
ax.legend(loc="upper left", fontsize=8)
ax.set_title("Spatial reference and recorded flight", fontsize=10, pad=12)
fig.subplots_adjust(left=0, right=.96, bottom=.02, top=.91)
save(fig, "unity_3d")

# All timestamps appear in these coordinate and signed-residual panels.
fig, axes = plt.subplots(3,1,figsize=(WIDTH,3.75),sharex=True)
fig.subplots_adjust(left=.13,right=.98,bottom=.15,top=.91,hspace=.65)
for i,ax in enumerate(axes):
    ax.axvspan(hold_start,d["t"][-1],color="#EFF0F2")
    ax.plot(d["t"],desired[:,i],color=GREY,linestyle="--",label="Reference")
    ax.plot(d["t"],actual[:,i],color=BLUE,label="Recorded")
    ax.set(ylabel="World %s (m)"%"xyz"[i],xlim=(0,122))
    panel(ax,chr(97+i),"%s coordinate"%"XYZ"[i])
axes[0].legend(loc="upper right",ncol=2)
axes[-1].set_xlabel("Recorded simulation time (s)")
save(fig,"axis_tracking")
residual = actual-desired
axis_rms = np.sqrt(np.mean(residual[active]**2,axis=0))
assert np.isclose(np.sum(axis_rms**2),metrics["rms_tracking_error_m"]**2)
fig, axes = plt.subplots(3,1,figsize=(WIDTH,3.75),sharex=True)
fig.subplots_adjust(left=.13,right=.98,bottom=.15,top=.91,hspace=.65)
for i,ax in enumerate(axes):
    ax.axvspan(hold_start,d["t"][-1],color="#EFF0F2")
    ax.axhline(0,color="0.5",linewidth=.7)
    ax.plot(d["t"],residual[:,i],color=BLUE)
    ax.set(ylabel="Δ%s (m)"%"xyz"[i],xlim=(0,122))
    panel(ax,chr(97+i),"%s residual; active RMS %.3f m"%("XYZ"[i],axis_rms[i]))
axes[-1].set_xlabel("Recorded simulation time (s)")
save(fig,"signed_errors")

fig,axes=plt.subplots(1,2,figsize=(WIDTH,3.05))
fig.subplots_adjust(left=.10,right=.98,bottom=.24,top=.81,wspace=.36)
bins=np.linspace(0,.6,25)
assert error.max()<=bins[-1]
for mask,color,label in [(active,BLUE,"Active flight"),(~active,ORANGE,"Terminal hold")]:
    values=error[mask]
    axes[0].hist(values,bins=bins,weights=np.full(len(values),100/len(values)),
                 histtype="step",color=color,label=label,linewidth=1.5)
    axes[1].plot(np.sort(values),100*np.arange(1,len(values)+1)/len(values),color=color,label=label)
axes[0].set(xlabel="Position error (m)",ylabel="Samples per bin (%)")
axes[1].set(xlabel="Position error (m)",ylabel="Cumulative samples (%)",ylim=(0,102))
axes[0].legend(loc="upper right",fontsize=8)
panel(axes[0],"a","Error distribution")
panel(axes[1],"b","Empirical cumulative distribution")
save(fig,"error_distribution")

q=np.column_stack([d[k] for k in ["qx","qy","qz","qw"]])
norm=np.linalg.norm(q,axis=1)
assert np.all(norm>1e-8)
q=q/norm[:,None]
qx,qy,qz,qw=q.T
roll=np.arctan2(2*(qw*qx+qy*qz),1-2*(qx*qx+qy*qy))
pitch=np.arcsin(np.clip(2*(qw*qy-qz*qx),-1,1))
yaw=np.unwrap(np.arctan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz)))
fig,axes=plt.subplots(3,1,figsize=(WIDTH,3.75),sharex=True)
fig.subplots_adjust(left=.13,right=.98,bottom=.15,top=.91,hspace=.65)
for i,(ax,values,name) in enumerate(zip(axes,[roll,pitch,yaw],["Roll","Pitch","Unwrapped yaw"])):
    ax.axvspan(hold_start,d["t"][-1],color="#EFF0F2")
    ax.plot(d["t"],np.degrees(values),color=BLUE)
    ax.set(ylabel="Angle (deg)",xlim=(0,122))
    panel(ax,chr(97+i),name)
axes[-1].set_xlabel("Recorded simulation time (s)")
save(fig,"recorded_attitude")
np.savetxt(OUT/"recorded_attitude.csv",np.column_stack([d["t"],np.degrees(roll),np.degrees(pitch),np.degrees(yaw)]),
           delimiter=",",header="t,roll_deg,pitch_deg,yaw_unwrapped_deg",comments="")

fig,axes=plt.subplots(2,1,figsize=(WIDTH,3.4),sharex=True)
fig.subplots_adjust(left=.13,right=.98,bottom=.16,top=.89,hspace=.65)
th=d["t"][~active]-hold_start
axes[0].plot(th,error[~active],color=BLUE)
axes[0].axhline(.2,color=ORANGE,linestyle="--",label="Offline terminal tolerance")
axes[0].scatter(th[-1],error[-1],color=ORANGE,s=20,zorder=3)
axes[0].set(ylabel="Position error (m)")
axes[0].legend(loc="upper right",fontsize=8)
panel(axes[0],"a","Error after the final reference is reached")
axes[1].plot(th,actual[~active,2],color=BLUE,label="Recorded altitude")
axes[1].plot(th,desired[~active,2],color=GREY,linestyle="--",label="Reference altitude")
axes[1].set(xlabel="Time since terminal hold began (s)",ylabel="World z (m)",xlim=(0,th[-1]))
axes[1].legend(loc="lower right",fontsize=8)
panel(axes[1],"b","Vertical response during terminal hold")
save(fig,"terminal_detail")

# Each gate gets a complete distance trace and a +/-2 s local projection.
local_counts=[]
for start in [0,6]:
    fig,axes=plt.subplots(2,3,figsize=(WIDTH,2.9),sharex=True,sharey=True)
    fig.subplots_adjust(left=.10,right=.98,bottom=.19,top=.88,hspace=.70,wspace=.20)
    for ax,i in zip(axes.flat,range(start,start+6)):
        ax.axvspan(hold_start,d["t"][-1],color="#EFF0F2")
        ax.plot(d["t"],distances[:,i],color=BLUE,linewidth=1)
        ax.scatter(d["t"][indices[i]],closest[i],color=ORANGE,s=15,zorder=3)
        ax.set(xlim=(0,122),ylim=(0,60))
        panel(ax,"", "Gate %d; %.2f s"%(i,d["t"][indices[i]]))
    fig.text(.015,.55,"Centre distance (m)",rotation=90,va="center",fontsize=9)
    for ax in axes[-1]:ax.set_xlabel("Simulation time (s)")
    save(fig,"gate_distances_%02d_%02d"%(start,start+5))

    fig,axes=plt.subplots(2,3,figsize=(WIDTH,3.15),sharex=True,sharey=True)
    fig.subplots_adjust(left=.10,right=.98,bottom=.26,top=.88,hspace=.75,wspace=.20)
    for ax,i in zip(axes.flat,range(start,start+6)):
        mask=np.abs(d["t"]-d["t"][indices[i]])<=2
        assert mask.sum()>1
        local_counts.append(dict(gate=i,rows=int(mask.sum()),window_s=2))
        direction=np.array([np.cos(angles[i]),np.sin(angles[i])])
        for positions,color,style,label in [(desired,GREY,"--","Reference"),(actual,BLUE,"-","Recorded")]:
            delta=positions[mask]-gates[i]
            assert np.max(np.abs(delta[:,:2]@direction)) < 4.5
            assert np.max(np.abs(delta[:,2])) < 2
            ax.plot(delta[:,:2]@direction,delta[:,2],color=color,linestyle=style,label=label)
        ax.scatter([0],[0],color=ORANGE,s=24,marker="s",label="Gate centre",zorder=4)
        ax.axhline(0,color="0.85",linewidth=.5)
        ax.set(xlim=(-4.5,4.5),ylim=(-2,2))
        ax.set_aspect("equal",adjustable="box")
        panel(ax,"","Gate %d; %.3f m"%(i,closest[i]))
    fig.text(.015,.56,"Height offset (m)",rotation=90,va="center",fontsize=9)
    fig.text(.54,.14,"Along-heading offset (m)",ha="center",fontsize=9)
    fig.legend(*axes.flat[0].get_legend_handles_labels(),loc="lower center",ncol=3,bbox_to_anchor=(.5,0),fontsize=8)
    save(fig,"gate_local_%02d_%02d"%(start,start+5))

# Assemble full decoded frames in Python; source pixels are not edited.
frame_meta=json.loads((OUT/"video_frames/frames.json").read_text())
assert len(frame_meta["frames"])==12
for start in [0,6]:
    fig,axes=plt.subplots(2,3,figsize=(WIDTH,3.25))
    fig.subplots_adjust(left=.015,right=.985,bottom=.025,top=.92,hspace=.18,wspace=.045)
    for ax,item,letter in zip(axes.flat,frame_meta["frames"][start:start+6],"abcdef"):
        raw=plt.imread(OUT/"video_frames"/item["image"])
        assert raw.shape[:2]==(600,960)
        ax.imshow(raw,interpolation="none");ax.axis("off")
        ax.set_title("%s  Playback: %d s"%(letter,item["requested_playback_time_s"]),loc="left",fontsize=9,pad=6)
    save(fig,"video_sequence_%d"%(start//6+1))

expanded={"axis_rms_m":dict(zip("xyz",map(float,axis_rms))),
          "active_error_quantiles_m":dict(zip(["median","p90","p95"],map(float,np.quantile(error[active],[.5,.9,.95])))),
          "quaternion_norm_range":[float(norm.min()),float(norm.max())],
          "local_gate_windows":local_counts,
          "local_gate_window_definition":"All rows within +/-2 seconds of each whole-record closest approach",
          "video_time_basis":frame_meta["time_basis"]}
(OUT/"expanded_metrics.json").write_text(json.dumps(expanded,indent=2)+"\n")
print(json.dumps(metrics, indent=2))
print(json.dumps(expanded,indent=2))
