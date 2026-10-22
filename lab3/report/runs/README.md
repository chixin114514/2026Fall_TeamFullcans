# Lab3 Unity runs

## unity-gpu-20261020 (current delivery)

The two videos were moved to `report/video/` after recording.

Official `lab3.x86_64` on x86_64 Ubuntu 20.04 / Noetic, rendered by the RTX 4060
through Mesa D3D12 (WSL2), `/current_state` at 50 Hz. Gains `kx=14, kv=6, kr=20,
komega=3` (`controller_pkg/config/gains_gpu.yaml`, tuning notes in that file).

- `../../video/unity_gpu_sim.mp4`: Unity window, chase camera, 69 s, 30 fps.
- `../../video/rviz_gpu.mp4`: RViz at the same time. The cyan actual path keeps the last lap and
  lies under the yellow desired circle once the takeoff transient scrolls away.
- `unity_flight.csv`, `unity_metrics.json`, `unity_tracking.pdf/png`: telemetry
  and metrics. `unity_flight.bag` is local only (`*.bag` is ignored by git).

Steady window t >= 8*pi s compared with the earlier Box64 run in `report/`:

| Metric | Box64 (kx 2, kv 2.4, kr 1.8, kω 0.7) | GPU (kx 14, kv 6, kr 20, kω 3) |
| --- | ---: | ---: |
| Position RMS | 0.306 m | 0.041 m |
| Position max | 0.585 m | 0.103 m |
| Radial RMS | 0.083 m | 0.0024 m |
| Radial max | 0.173 m | 0.0053 m |
| Fitted radius | 5.074 m | 4.998 m |
| Height range | 1.56–1.86 m | 1.98–1.99 m |

`traj_tracking.launch` now sets `takeoff:=true`. The drone used to start with a
5 m position error and a 166° yaw error against a reference already moving at
2.5 m/s, so it spun at up to 400°/s and climbed to 2.6–2.9 m. Now `traj_publisher`
reads the spawn pose and flies a 6 s minimum-jerk path to the circle start while
yawing to 0°, hovers 3 s, then ramps the rate up over 6 s. Those 12 s are at
negative `trajectory_time`; from t = 3 s on, the reference is exactly the official
`x=5 sin(t/2), y=5 cos(t/2), yaw=-t/2`. In the takeoff the peak body rate is 60°/s,
height never exceeds 1.98 m, and the position error stays under 0.085 m through
the first two laps. `takeoff:=false` restores the original start at t=0.
