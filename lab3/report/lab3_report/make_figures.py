"""Render report figures from retained measurements; never run a simulator.

Team-work figures use the GPU TESSE run in ../runs/unity-gpu-20261020.
Individual-work figures use the deliverable-2 derivation and numerical log.
"""
from pathlib import Path
import json
import os
import re
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
DATA = HERE.parent
RUN = DATA / 'runs' / 'unity-gpu-20261020'
VIDEO = DATA / 'video'
OUT = HERE / 'figures'
QA = HERE / 'qa'
OUT.mkdir(exist_ok=True)
QA.mkdir(exist_ok=True)

# Render-time panel alignment gate from the nature-figure skill, when present.
SKILL = Path(os.environ.get('NATURE_FIGURE_SCRIPTS', Path.home()/'.claude/skills/nature-figure/scripts'))
sys.path.insert(0, str(SKILL))
try:
    from audit_panel_alignment import require_matplotlib_panel_alignment
except ImportError:
    require_matplotlib_panel_alignment = None

plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 8, 'axes.titlesize': 8.5, 'axes.labelsize': 8, 'xtick.labelsize': 7, 'ytick.labelsize': 7,
    'axes.spines.top': False, 'axes.spines.right': False, 'axes.linewidth': .7,
    'legend.frameon': False, 'svg.fonttype': 'none', 'pdf.fonttype': 42,
    'lines.linewidth': 1.1, 'mathtext.default': 'regular'})
BLUE, ORANGE, GRAY, PURPLE, GREEN = '#286C91', '#C57A30', '#777777', '#685687', '#397C64'
LIGHT = '#B9B9B9'
MM = 1/25.4


def title(ax, text):
    ax.set_title(text, loc='left', fontweight='bold')


def save(fig, name, align=None):
    if require_matplotlib_panel_alignment is not None and align is not None:
        require_matplotlib_panel_alignment(fig, json_out=QA/f'{name}.alignment.json',
            tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True, **align)
    fig.savefig(OUT/f'{name}.pdf', bbox_inches='tight', facecolor='white')
    fig.savefig(OUT/f'{name}.svg', bbox_inches='tight', facecolor='white')
    fig.savefig(OUT/f'{name}.png', dpi=600, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ---------------------------------------------------------------- GPU flight
# Every logged sample is plotted. Phases follow the reference definition:
# t < 0 start sequence (6 s transfer, 3 s hover, first half of the 6 s ramp),
# 0 <= t < 8*pi initial two periods, t >= 8*pi steady window for statistics.
d = np.genfromtxt(RUN/'unity_flight.csv', delimiter=',', names=True)
t = d['trajectory_time']
p = np.column_stack([d[k] for k in 'xyz'])
pd = np.column_stack([d[k+'d'] for k in 'xyz'])
e = p - pd
err = np.linalg.norm(e, axis=1)
T = 4*np.pi
s = t >= 2*T
pre = t < 0
lap = ~pre & ~s
assert np.isfinite(np.column_stack((t, p, pd))).all() and np.all(np.diff(t) >= 0) and np.all(np.diff(d['t']) > 0)

# Error in the reference's moving frame: along-track, radial, vertical.
# For t >= 3 s the reference is exactly x=5 sin(t/2), y=5 cos(t/2).
th = t/2
tan = np.column_stack([np.cos(th), -np.sin(th)])
rad = np.column_stack([np.sin(th), np.cos(th)])
e_al = np.sum(e[:, :2]*tan, axis=1)
e_rd = np.sum(e[:, :2]*rad, axis=1)
r_dev = np.linalg.norm(p[:, :2], axis=1) - 5
phase = np.unwrap(np.arctan2(p[s, 0], p[s, 1]))
yaw_err = np.angle(np.exp(1j*(d['yaw']-d['yawd'])))
omega = np.degrees(np.linalg.norm(np.column_stack([d['wx_world'], d['wy_world'], d['wz_world']]), axis=1))
rms = lambda v: float(np.sqrt(np.mean(np.square(v))))
stale = np.r_[False, np.diff(t) == 0]  # reference not advanced since previous state sample
jitter = np.r_[False, ~np.isclose(np.diff(t), .02)]  # reference step of 0 or 40 ms
m = {'samples': len(t), 'state_rate_hz': float(1/np.median(np.diff(d['t']))),
     'start_sequence_samples': int(pre.sum()), 'initial_period_samples': int(lap.sum()), 'steady_samples': int(s.sum()),
     'repeated_reference_times': int(np.sum(np.diff(t) == 0)),
     'samples_above_6cm_after_t0': int(np.sum((err > .06) & (t >= 0))),
     'stale_reference_samples_above_6cm_after_t0': int(np.sum((err > .06) & (t >= 0) & stale)),
     'steady_position_rms_fresh_reference_m': rms(err[s & ~stale]),
     'reference_step_counts_0_20_40ms': [int(np.sum(np.diff(t) == 0)), int(np.sum(np.isclose(np.diff(t), .02))), int(np.sum(np.isclose(np.diff(t), .04)))],
     'steady_along_track_median_m': float(np.median(e_al[s])),
     'steady_along_track_regular_step_mean_m': float(e_al[s & ~jitter].mean()),
     'steady_position_rms_m': rms(err[s]), 'steady_position_max_m': float(err[s].max()),
     'steady_component_rms_m': np.sqrt(np.mean(e[s]**2, axis=0)).tolist(),
     'steady_along_track_mean_m': float(e_al[s].mean()), 'steady_along_track_rms_m': rms(e_al[s]),
     'steady_along_track_time_offset_ms': float(e_al[s].mean()/2.5*1e3),
     'steady_radial_rms_m': rms(r_dev[s]), 'steady_radial_max_m': float(np.abs(r_dev[s]).max()),
     'steady_vertical_rms_m': rms(e[s, 2]), 'steady_vertical_mean_m': float(e[s, 2].mean()),
     'steady_height_range_m': [float(p[s, 2].min()), float(p[s, 2].max())],
     'steady_yaw_rms_deg': float(np.degrees(rms(yaw_err[s]))),
     'observed_steady_laps': float((phase[-1]-phase[0])/(2*np.pi)),
     'start_sequence_position_max_m': float(err[pre].max()),
     'initial_periods_position_max_m': float(err[lap].max()),
     'flight_height_max_m': float(p[:, 2].max()),
     'start_sequence_body_rate_max_deg_s': float(omega[t < 3].max()),
     'spawn_position_m': p[0].tolist(), 'spawn_yaw_deg': float(np.degrees(d['yaw'][0]))}
shares = np.array([np.mean(e_al[s]**2), np.mean(e_rd[s]**2), np.mean(e[s, 2]**2)])/np.mean(err[s]**2)
assert np.isclose(shares.sum(), 1, atol=1e-6)
m['steady_squared_error_share_along_radial_vertical'] = shares.tolist()
existing = json.loads((RUN/'unity_metrics.json').read_text())
for k in ('steady_position_rms_m', 'steady_position_max_m', 'steady_radial_rms_m', 'observed_steady_laps'):
    assert np.isclose(m[k], existing[k], rtol=1e-9), (k, m[k], existing[k])
(QA/'recomputed_metrics.json').write_text(json.dumps(m, indent=2)+'\n')


def shade_phases(ax, label=False):
    ax.axvspan(t[0], 0, color=GRAY, alpha=.10, lw=0)
    ax.axvspan(0, 2*T, color=ORANGE, alpha=.10, lw=0)
    ax.axvline(2*T, color=GRAY, ls=':', lw=.8)
    if label:
        y = .45
        ax.text(-1, y, 'Start', transform=ax.get_xaxis_transform(), ha='right', va='center', fontsize=6.5, color=GRAY)
        ax.text(T, y, 'First two periods', transform=ax.get_xaxis_transform(), ha='center', va='center', fontsize=6.5, color=ORANGE)
        ax.text((2*T+t[-1])/2, y, 'Steady window', transform=ax.get_xaxis_transform(), ha='center', va='center', fontsize=6.5, color=BLUE)


# Figure: official tracking overview (hero = top view; time traces support it).
fig = plt.figure(figsize=(160*MM, 112*MM), layout='constrained')
gs = fig.add_gridspec(3, 2, width_ratios=[1, 1.12])
a = fig.add_subplot(gs[:, 0])
a.plot(pd[t >= 0, 0], pd[t >= 0, 1], color=LIGHT, lw=3.2, solid_capstyle='round', label='Reference circle')
a.plot(p[pre, 0], p[pre, 1], color=GRAY, lw=1, label='Start sequence')
a.plot(p[lap, 0], p[lap, 1], color=ORANGE, lw=.9, label='First two periods')
a.plot(p[s, 0], p[s, 1], color=BLUE, lw=.9, label='Steady window')
a.scatter(*p[0, :2], s=16, color=GRAY, zorder=5)
a.annotate('Spawn', p[0, :2], xytext=(6, -10), textcoords='offset points', fontsize=6.5, color=GRAY)
a.set(xlabel='x (m)', ylabel='y (m)', aspect='equal', xlim=(-6.2, 6.2), ylim=(-6.2, 6.2))
a.legend(loc='upper center', bbox_to_anchor=(.5, -.12), ncol=2, fontsize=6.5, handlelength=1.6)
title(a, 'a  Top view')
b = fig.add_subplot(gs[0, 1])
b.plot(t, pd[:, 2], color=LIGHT, lw=2.4)
b.plot(t, p[:, 2], color=BLUE, lw=.9)
b.set(ylabel='Height (m)', ylim=(.6, 2.2)); shade_phases(b, label=True)
b.text(.985, .08, f'max {m["flight_height_max_m"]:.3f} m, target 2 m', transform=b.transAxes, ha='right', fontsize=6.5)
title(b, 'b  Height')
c = fig.add_subplot(gs[1, 1], sharex=b)
c.plot(t, err*100, color=BLUE, lw=.8)
c.scatter(t[jitter], err[jitter]*100, s=3, color=ORANGE, lw=0, zorder=4)
c.set(ylabel='|e| (cm)', ylim=(0, 12)); shade_phases(c)
c.text(.015, .9, '• reference step ≠ 20 ms', transform=c.transAxes, va='top', fontsize=6.5, color=ORANGE)
c.text(.985, .99, f'steady RMS {m["steady_position_rms_m"]*100:.1f} cm', transform=c.transAxes, ha='right', va='top', fontsize=6.5)
title(c, 'c  Position-error norm')
f = fig.add_subplot(gs[2, 1], sharex=b)
f.plot(t[s], r_dev[s]*1e3, color=BLUE, lw=.8)
f.axhline(0, color=GRAY, ls=':', lw=.8)
f.set(xlabel='Trajectory time (s)', ylabel='r − 5 m (mm)', ylim=(-8, 8), xlim=(t[0], t[-1]))
f.text(.985, .9, f'RMS {m["steady_radial_rms_m"]*1e3:.1f} mm', transform=f.transAxes, ha='right', va='top', fontsize=6.5)
shade_phases(f)
title(f, 'd  Radius deviation, steady window')
for ax in (b, c):
    ax.tick_params(labelbottom=False)
for ax in (b, c, f):
    pass
save(fig, 'official_tracking', align={'exemptions': [{'panels': ['a'], 'checks': ['row'],
    'reason': 'equal-aspect hero top view spans three stacked time traces'}]})


# Figure: start sequence from the spawn pose to the official circle.
w = t < 2*T
fig = plt.figure(figsize=(160*MM, 92*MM), layout='constrained')
gs = fig.add_gridspec(2, 2)
a = fig.add_subplot(gs[0, 0])
for j, (col, lab) in enumerate(zip([BLUE, ORANGE, PURPLE], 'xyz')):
    a.plot(t[w], pd[w, j], color=col, lw=2.6, alpha=.35)
    a.plot(t[w], p[w, j], color=col, lw=.9, label=lab)
a.set(ylabel='Position (m)', ylim=(-6, 6)); a.legend(ncol=3, loc='lower left', fontsize=6.5, handlelength=1.4)
title(a, 'a  Position: reference (wide) and measured')
b = fig.add_subplot(gs[0, 1], sharex=a)
b.plot(t[w], np.degrees(np.unwrap(d['yawd'][w])), color=LIGHT, lw=2.6)
b.plot(t[w], np.degrees(np.unwrap(d['yaw'][w])), color=BLUE, lw=.9)
b.set(ylabel='Yaw (deg)')
title(b, 'b  Heading, short way to 0°')
c = fig.add_subplot(gs[1, 0], sharex=a)
c.plot(t[w], err[w]*100, color=BLUE, lw=.8)
c.scatter(t[w & jitter], err[w & jitter]*100, s=3, color=ORANGE, lw=0, zorder=4)
c.set(ylabel='|e| (cm)', ylim=(0, 10), xlabel='Trajectory time (s)')
c.text(.62, .97, f'max {m["initial_periods_position_max_m"]*100:.1f} cm', transform=c.transAxes, ha='center', va='top', fontsize=6.5)
title(c, 'c  Position-error norm')
f = fig.add_subplot(gs[1, 1], sharex=a)
f.plot(t[w], omega[w], color=BLUE, lw=.8)
f.set(ylabel='|ω| (deg/s)', ylim=(0, 80), xlabel='Trajectory time (s)', xlim=(t[0], 2*T))
f.text(.985, .9, f'max {m["start_sequence_body_rate_max_deg_s"]:.0f} deg/s', transform=f.transAxes, ha='right', va='top', fontsize=6.5)
title(f, 'd  Angular-rate magnitude')
for ax in (a, b, c, f):
    ax.axvspan(t[0], -6, color=GRAY, alpha=.10, lw=0)
    ax.axvspan(-6, -3, color=GREEN, alpha=.08, lw=0)
    ax.axvspan(-3, 3, color=ORANGE, alpha=.10, lw=0)
    pass
for x0, x1, txt, y in ((t[0], -6, 'Transfer', .93), (-6, -3, 'Hover', .80), (-3, 3, 'Rate\nramp', .93)):
    c.text((x0+x1)/2, y, txt, transform=c.get_xaxis_transform(), ha='center', va='top', fontsize=6)
for ax in (a, b):
    ax.tick_params(labelbottom=False)
save(fig, 'takeoff_transition', align={})


# Figure: steady-window error in the reference frame.
fig, axs = plt.subplots(2, 2, figsize=(160*MM, 92*MM), layout='constrained')
comp = [(e_al, 'Along-track', BLUE), (e_rd, 'Radial', ORANGE), (e[:, 2], 'Vertical', PURPLE)]
for ax, (v, lab, col), tag in zip(axs.flat[:3], comp, 'abc'):
    ax.plot(t[s], v[s]*100, color=col, lw=.8)
    ax.scatter(t[s & jitter], v[s & jitter]*100, s=3, color=GRAY, lw=0, zorder=4)
    ax.axhline(0, color=GRAY, ls=':', lw=.8)
    ax.set(xlabel='Trajectory time (s)', ylabel=f'{lab} (cm)', xlim=(t[s][0], t[s][-1]), ylim=(-4, 12))
    title(ax, f'{tag}  {lab} error')
axs[0, 1].text(.985, .95, '• reference step ≠ 20 ms', transform=axs[0, 1].transAxes, ha='right', va='top', fontsize=6.5, color=GRAY)
axs[0, 0].text(.985, .97, f'mean {m["steady_along_track_mean_m"]*100:.1f} cm = {m["steady_along_track_time_offset_ms"]:.1f} ms at 2.5 m/s',
               transform=axs[0, 0].transAxes, ha='right', va='top', fontsize=6.5)
ax = axs[1, 1]
vals = np.array([rms(e_al[s]), rms(e_rd[s]), rms(e[s, 2])])*100
ax.bar([0, 1, 2], vals, color=[c for _, _, c in comp], width=.55)
for j, (v, sh) in enumerate(zip(vals, shares)):
    ax.text(j, v+.12, f'{v:.2f} cm\n{sh*100:.1f}%' if sh < .01 else f'{v:.2f} cm\n{sh*100:.0f}%', ha='center', va='bottom', fontsize=6.5)
ax.set(xticks=[0, 1, 2], xticklabels=['Along', 'Radial', 'Vertical'], ylabel='RMS (cm)', ylim=(0, 5.4))
title(ax, 'd  RMS and share of squared error')
save(fig, 'component_errors', align={})


# Figure: gain selection, from the tuning record
# kept in gains_used.yaml (one 50 s circle per setting; final flight from CSV).
log = (RUN/'gains_used.yaml').read_text()
rows = re.findall(r'kx (\d+),\s*kv ([\d.]+),\s*kr ([\d.]+),\s*komega ([\d.]+)[^:]*:\s*(?:unstable, )?([\d.]+) m RMS', log)
assert len(rows) == 5, rows
labels = [f'({float(a):g}, {float(b):g}, {float(c):g}, {float(dd):g})' for a, b, c, dd, _ in rows]
rmsv = [float(r[-1]) for r in rows]
labels.append('(14, 6, 20, 3)  final flight'); rmsv.append(m['steady_position_rms_m'])
kind = ['base', 'tune', 'tune', 'sel', 'unst', 'final']
col = {'base': GRAY, 'tune': LIGHT, 'sel': BLUE, 'unst': ORANGE, 'final': BLUE}
order = [1, 2, 3, 5, 4]  # tuning steps on this simulator, final flight, unstable set
fig, ax = plt.subplots(figsize=(150*MM, 58*MM), layout='constrained')
ys = np.arange(len(order))[::-1]
for y, i in zip(ys, order):
    ax.barh(y, rmsv[i], height=.56, color=col[kind[i]], hatch='////' if kind[i] == 'final' else None,
            edgecolor='white' if kind[i] == 'final' else 'none', lw=0)
    ax.text(rmsv[i]*1.12, y, f'{rmsv[i]:.3f} m' + ('  unstable' if kind[i] == 'unst' else ''), va='center', fontsize=7)
assert min(rmsv) > 0
ax.set_xscale('log')
ax.set_xticks([.03, .1, .3, 1, 3]); ax.set_xticklabels(['0.03', '0.1', '0.3', '1', '3']); ax.minorticks_off()
ax.set(yticks=ys, yticklabels=[labels[i] for i in order], xlim=(.02, 6), ylim=(-.6, len(order)-.4),
       xlabel='Steady position RMS error (m), t ≥ 8π s')
ax.text(-.02, 1.04, '$(k_x, k_v, k_R, k_\\Omega)$', transform=ax.transAxes, ha='right', fontsize=8)
ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
save(fig, 'gain_comparison', align={})
(QA/'gain_record.json').write_text(json.dumps(dict(zip(labels, rmsv)), indent=2)+'\n')


# Figure: commands. The simulator allocation (controller header) maps signed
# squared rotor speeds back to the commanded thrust and body moments.
rotors = np.column_stack([d[f'rotor{i}'] for i in range(1, 5)])
assert np.isfinite(rotors).all()
cf, cdrag, arm = 1e-3, 1e-5, .3/np.sqrt(2)
F_sim = np.array([[cf]*4, [arm*cf, arm*cf, -arm*cf, -arm*cf], [-arm*cf, arm*cf, arm*cf, -arm*cf], [cdrag, -cdrag, cdrag, -cdrag]])
wrench = (rotors*np.abs(rotors))@F_sim.T
f_need = np.sqrt(9.81**2 + 1.25**2)  # m*|g e3 + a_d| for m = 1 kg on the circle
m.update({'steady_thrust_mean_n': float(wrench[s, 0].mean()), 'steady_thrust_std_n': float(wrench[s, 0].std()),
          'circle_thrust_feedforward_n': float(f_need),
          'steady_moment_std_nm': wrench[s, 1:].std(axis=0).tolist(),
          'steady_negative_rotor_command_fraction': float(np.mean(rotors[s] < 0)),
          'rotor_command_range_rad_s': [float(rotors.min()), float(rotors.max())]})
(QA/'recomputed_metrics.json').write_text(json.dumps(m, indent=2)+'\n')
zoom = (t >= 40) & (t <= 42)
fig = plt.figure(figsize=(160*MM, 98*MM), layout='constrained')
gs = fig.add_gridspec(2, 2)
a = fig.add_subplot(gs[0, :])
# Samples logged before the first controller output carry all-zero commands;
# the collective-thrust trace starts at the first published command.
live = np.any(rotors != 0, axis=1)
m['samples_before_first_command'] = int(np.argmax(live))
a.plot(t[live], wrench[live, 0], color=BLUE, lw=.8)
a.axhline(f_need, color=GRAY, ls='--', lw=.8)
a.text(t[-1], f_need-.05, f'm|g e$_3$ + a$_d$| = {f_need:.2f} N', ha='right', va='top', fontsize=7.5, color=GRAY)
a.text(.985, .95, f'steady {m["steady_thrust_mean_n"]:.2f} ± {m["steady_thrust_std_n"]:.2f} N (mean ± s.d.)', transform=a.transAxes, ha='right', va='top', fontsize=6.5)
shade_phases(a)
a.set(xlabel='Trajectory time (s)', ylabel='f (N)', xlim=(t[0], t[-1]), ylim=(9.3, 10.6))
title(a, 'a  Commanded collective thrust')
b = fig.add_subplot(gs[1, 0])
for j, (col, lab) in enumerate(zip([BLUE, ORANGE, PURPLE], ['$M_x$', '$M_y$', '$M_z$'])):
    b.plot(t[zoom], wrench[zoom, j+1], color=col, lw=.8, marker='o', ms=1.4, label=lab)
b.set(xlabel='Trajectory time (s)', ylabel='Moment (N m)', xlim=(40, 42), ylim=(-3.4, 2.6))
b.legend(ncol=3, fontsize=7.5, loc='lower right', handlelength=1.2)
title(b, 'b  Moment commands, 2 s excerpt')
c = fig.add_subplot(gs[1, 1], sharex=b)
for j, color in enumerate([BLUE, ORANGE, PURPLE, GREEN]):
    c.plot(t[zoom], rotors[zoom, j], color=color, lw=.8, marker='o', ms=1.4, label=f'{j+1}')
c.axhline(0, color=GRAY, ls=':', lw=.8)
c.set(xlabel='Trajectory time (s)', ylabel='ω (rad/s)', ylim=(-240, 170))
c.legend(ncol=4, fontsize=6.5, loc='lower right', title='Rotor', title_fontsize=6.5, handlelength=1.2)
title(c, 'c  Signed rotor commands, same excerpt')
save(fig, 'rotor_commands', align={'exemptions': [{'panels': ['a'], 'checks': ['column'],
    'reason': 'full-width time trace spans both lower panels'}]})


# Figure: unmodified video frames (Unity at 40 s, RViz at 64 s of the recordings).
uni = plt.imread(VIDEO/'unity_gpu_frame.png')
rvz = plt.imread(VIDEO/'rviz_gpu_frame.png')[62:770, 364:1264]  # RViz 3D view only
fig, axs = plt.subplots(1, 2, figsize=(160*MM, 52*MM), layout='constrained', gridspec_kw={'width_ratios': [960/600, 900/708]})
for ax, img, lab in zip(axs, [uni, rvz], ['a  Unity/TESSE chase camera', 'b  RViz, last lap under the reference']):
    ax.imshow(img); ax.set_axis_off(); title(ax, lab)
save(fig, 'simulator_views')


# ------------------------------------------------------- Individual work
# Exercise numbering, checked against the official top-view diagram.
Fa = np.array([[1, 1, 1, 1], [1, -1, -1, 1], [1, 1, -1, -1], [-1, 1, -1, 1]])
Fb = Fa.copy(); Fb[3] = [-1, 1, 1, -1]
assert np.linalg.matrix_rank(Fa) == 4 and np.linalg.matrix_rank(Fb) == 3
assert np.all(Fb[3] == -Fb[1]) and np.all(Fb@np.array([1, -1, 1, -1]) == 0)
fig, axs = plt.subplots(1, 2, figsize=(160*MM, 70*MM), layout='constrained')
positions = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
for ax, signs, label in zip(axs, [[-1, 1, -1, 1], [-1, 1, 1, -1]], ['a  Original layout: rank 4', 'b  Reversed rotors 3 and 4: rank 3']):
    for i, ((x, y), sign) in enumerate(zip(positions, signs), 1):
        ax.plot([0, x*(1-.36/np.hypot(x, y))], [0, y*(1-.36/np.hypot(x, y))], color=GRAY, lw=2, zorder=0)
        c = BLUE if sign < 0 else ORANGE
        ax.add_patch(Circle((x, y), .34, facecolor=c, edgecolor='white'))
        ax.text(x, y, str(i), ha='center', va='center', color='white', fontsize=11)
        ax.text(x, y-.55, ('CCW rotor' if sign < 0 else 'CW rotor')+'\n'+('$M_z<0$' if sign < 0 else '$M_z>0$'), ha='center', va='center', fontsize=7.5)
    ax.annotate('', xy=(.6, 0), xytext=(0, 0), arrowprops={'arrowstyle': '->', 'lw': .8})
    ax.annotate('', xy=(0, .6), xytext=(0, 0), arrowprops={'arrowstyle': '->', 'lw': .8})
    ax.text(.66, 0, 'x', va='center'); ax.text(0, .66, 'y', ha='center')
    ax.set(xlim=(-1.65, 1.65), ylim=(-1.85, 1.65), aspect='equal')
    ax.axis('off'); title(ax, label)
save(fig, 'rotor_layout')

fig, ax = plt.subplots(figsize=(160*MM, 63*MM)); ax.set(xlim=(0, 10), ylim=(0, 4)); ax.axis('off')
boxes = [(.1, 2.4, 2.15, .85, 'Trajectory publisher\nStart sequence + circle'),
         (3.1, 2.4, 2.25, .85, 'Geometric controller\nForce, attitude and allocation'),
         (6.3, 2.4, 3.55, .85, 'Unity/TESSE simulator\nMotor commands and simulated motion'),
         (3.2, .15, 2.25, .85, 'TESSE ROS bridge\nOdometry feedback, 50 Hz')]
for x, y, wd, h, txt in boxes:
    ax.add_patch(FancyBboxPatch((x, y), wd, h, boxstyle='round,pad=0.05,rounding_size=0.06', facecolor='#EDF3F7', edgecolor=BLUE, lw=.8))
    ax.text(x+wd/2, y+h/2, txt, ha='center', va='center', fontsize=7)
for start, end in [((2.3, 2.82), (3.02, 2.82)), ((5.4, 2.82), (6.22, 2.82)), ((8.05, 2.35), (5.5, .65)), ((4.3, 1.04), (4.3, 2.34))]:
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=10, lw=.9, color=GRAY))
ax.text(2.62, 3.55, '/desired_state', ha='center', fontsize=7)
ax.text(5.8, 3.55, '/rotor_speed_cmds', ha='center', fontsize=7)
ax.text(4.45, 1.65, '/current_state\n'+r'$\Omega = R^T\Omega_{world}$', va='center', fontsize=7.5)
ax.text(7.8, 1.0, 'Simulator state\nvia UDP', ha='center', fontsize=7)
ax.text(1.18, 2.1, 'spawn pose\n(takeoff:=true)', ha='center', va='top', fontsize=6.5, color=GRAY)
ax.add_patch(FancyArrowPatch((3.15, 1.0), (1.4, 2.32), arrowstyle='-|>', mutation_scale=8, lw=.7, color=LIGHT, ls='--'))
fig.tight_layout(pad=.2); save(fig, 'control_loop')

log = (DATA/'numerical_validation.txt').read_text()
blocks = re.findall(r'mode=(.*?)\nsteady_rms_position_error_m=([\deE.+-]+)', log)
cases = {cfg: float(value) for cfg, value in blocks}
vals = [cases['circle dt=0.001 drag=1 compensation=0'], cases['circle dt=0.001 drag=1 compensation=1']]
assert np.all(np.isfinite(vals)) and vals[0] > 0 and vals[1] > 0
fig, ax = plt.subplots(figsize=(135*MM, 54*MM), layout='constrained')
ax.barh([1, 0], vals, height=.46, color=[GRAY, BLUE])
ax.set(yticks=[1, 0], yticklabels=['Drag, no compensation', 'Drag, compensation enabled'], xlabel='Steady 3D position RMS error (m)', xlim=(0, .105), ylim=(-.55, 1.65))
for y, v in zip([1, 0], vals): ax.text(v+.002, y, f'{v:.5f} m', va='center', fontsize=8)
ax.set_title('Independent rigid-body model with the prescribed quadratic drag', loc='left', fontsize=8.5)
ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
save(fig, 'drag_compensation')
print(json.dumps(m, indent=2))
