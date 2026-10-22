"""Plot analytic Lab 2 trajectories and the saved TF samples."""

from pathlib import Path
import re

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent
FIGURES = ROOT / "figures"
BLUE = "#0077BB"
ORANGE = "#EE7733"
TEAL = "#009988"
BLACK = "#222222"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
})


def finish(fig, name):
    fig.savefig(FIGURES / name, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)


t = np.linspace(0, 2 * np.pi, 801)
sin_t, cos_t = np.sin(t), np.cos(t)
sin_2t, cos_2t = np.sin(2 * t), np.cos(2 * t)

# World-frame paths from the prescribed position equations.
fig, axes = plt.subplots(1, 2, figsize=(6.9, 2.5))
axes[0].plot(cos_t, sin_t, color=BLUE, lw=1.7)
axes[0].plot(1, 0, "o", color=BLACK, ms=3.5)
axes[0].set(xlabel=r"$x_w$", ylabel=r"$y_w$", title="AV1: world $x$-$y$ projection")
axes[0].set_aspect("equal", adjustable="box")
axes[0].set_xlim(-1.15, 1.15)
axes[0].set_ylim(-1.15, 1.15)
axes[1].plot(sin_t, cos_2t, color=ORANGE, lw=1.7)
axes[1].plot(0, 1, "o", color=BLACK, ms=3.5)
axes[1].set(xlabel=r"$x_w$", ylabel=r"$z_w$", title="AV2: world $x$-$z$ projection")
axes[1].set_xlim(-1.15, 1.15)
axes[1].set_ylim(-1.15, 1.15)
for ax in axes:
    ax.grid(color="#dddddd", lw=0.45)
fig.tight_layout(w_pad=2.0)
finish(fig, "world_analytic.pdf")

# Components of AV2's position expressed in AV1 over two revolutions of AV1.
relative_x = 0.5 * sin_2t - 1
relative_y = 0.5 * cos_2t - 0.5
relative_z = cos_2t
fig, ax = plt.subplots(figsize=(3.4, 2.35))
ax.plot(t, relative_x, color=BLUE, lw=1.5, label=r"$x_2^1$")
ax.plot(t, relative_y, color=ORANGE, lw=1.5, ls="--", label=r"$y_2^1$")
ax.plot(t, relative_z, color=TEAL, lw=1.5, ls=":", label=r"$z_2^1$")
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
ax.set(xlabel=r"$t$", ylabel="AV2 position in AV1")
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.65, 1.15)
ax.grid(color="#dddddd", lw=0.45)
ax.legend(ncol=3, loc="upper center", frameon=False)
fig.tight_layout()
finish(fig, "relative_components.pdf")

# First three values in Table II of main.tex.
table_samples = np.array([
    [-1.149, -0.977, -0.955],
    [-1.479, -0.356, 0.288],
    [-0.682, -0.114, 0.771],
])
# Three further tf_echo translations saved in runtime_evidence.txt.
log_text = (ROOT / "runtime_evidence.txt").read_text()
log_rows = re.findall(r"- Translation: \[([^]]+)\]", log_text)
assert len(log_rows) == 3, "Expected three saved tf_echo translations"
log_samples = np.array([[float(value) for value in row.split(",")] for row in log_rows])

def plane_projection(samples):
    x, y, z = samples.T
    return x + 1, (y + 0.5 + 2 * z) / np.sqrt(5)

for group in (table_samples, log_samples):
    residual = group[:, 2] - (2 * group[:, 1] + 1)
    assert np.max(np.abs(residual)) <= 0.0011

fig, ax = plt.subplots(figsize=(3.4, 3.25))
ax.plot(0.5 * sin_2t, np.sqrt(5) / 2 * cos_2t,
        color=BLACK, lw=1.4, label="Model")
ax.scatter(*plane_projection(table_samples), s=23, marker="o", facecolors="white",
           edgecolors=BLUE, linewidths=1.2, label="Capture A", zorder=3)
ax.scatter(*plane_projection(log_samples), s=28, marker="x", color=ORANGE,
           linewidths=1.3, label="Capture B", zorder=3)
ax.axhline(0, color="#aaaaaa", lw=0.5)
ax.axvline(0, color="#aaaaaa", lw=0.5)
ax.set(xlabel=r"$x_p$", ylabel=r"$y_p$")
ax.set_xlim(-0.66, 0.66)
ax.set_ylim(-1.25, 1.25)
ax.set_aspect("equal", adjustable="box")
ax.grid(color="#dddddd", lw=0.45)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False)
fig.tight_layout()
finish(fig, "relative_ellipse_samples.pdf")
