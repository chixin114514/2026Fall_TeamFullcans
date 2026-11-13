#!/usr/bin/env python3
"""Run every pose estimator on the office bag and write one RPE csv per method.

For each configuration: start lab_6/pose_estimation with --rpe_csv, play the bag,
wait until the node has drained its frame queue (csv stops growing), stop the node.
The node buffers frames, so every frame pair is evaluated whatever the play rate.

    source ~/vnav-builds/lab6_ws/devel/setup.bash
    python3 scripts/run_experiments.py [--bag ~/datasets/vnav/lab6/office.bag] [--only 5pt 2pt]
    python3 scripts/run_experiments.py --sweep     # 2D RANSAC threshold sweep, first 60 s
    python3 scripts/run_experiments.py --sweep3d   # Arun RANSAC threshold sweep, first 60 s
    # bonus: Lab 4 race bag (scripts/record_race_bag.sh), flight segment only
    python3 scripts/run_experiments.py --race
"""
import argparse
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

LAB6 = Path(__file__).resolve().parents[1]
OUT = LAB6 / "results" / "rpe"
SWEEP_OUT = LAB6 / "results" / "sweep"
SWEEP_PX = [0.1, 0.2, 0.3, 0.5, 1.0]
SWEEP_METHODS = ["5pt", "8pt", "2pt"]
SWEEP_3D_M = [0.005, 0.01, 0.02, 0.05, 0.1]

# name -> (pose_estimator, use_ransac)
CONFIGS = {
    "5pt": (0, True),
    "8pt": (1, True),
    "2pt": (2, True),
    "arun": (3, True),
    "5pt_noransac": (0, False),
    "8pt_noransac": (1, False),
    "arun_noransac": (3, False),
}

IMAGE_TOPICS = ["/tesse/left_cam/rgb/image_raw", "/tesse/depth_cam/mono/image_raw"]
RACE_BAG = LAB6 / "results" / "race" / "race.bag"
RACE_OUT = LAB6 / "results" / "race" / "rpe"


def wait_quiet(path: Path, quiet_s: float, proc: subprocess.Popen):
    """Wait until `path` has not grown for quiet_s seconds."""
    last, t_last = -1, time.time()
    while proc.poll() is None:
        size = path.stat().st_size if path.exists() else 0
        if size != last:
            last, t_last = size, time.time()
        elif time.time() - t_last > quiet_s:
            return
        time.sleep(0.5)


def run(name, estimator, ransac, args, out=OUT, ransac_px=None, ransac_3d_m=None):
    out.mkdir(parents=True, exist_ok=True)
    csv = out / f"{name}.csv"
    log = open(out / f"{name}.log", "w")
    ransac_px = args.ransac_px if ransac_px is None else ransac_px
    ransac_3d_m = args.ransac_3d_m if ransac_3d_m is None else ransac_3d_m
    node = subprocess.Popen(
        ["rosrun", "lab_6", "pose_estimation",
         f"--pose_estimator={estimator}", f"--use_ransac={str(ransac).lower()}",
         "--scale_translation=true", f"--ransac_px={ransac_px}", f"--ransac_max_iter={args.max_iter}",
         f"--ransac_3d_m={ransac_3d_m}", f"--rpe_csv={csv}",
         f"/ground_truth_pose:={args.gt_topic}",
         "/rgb_images_topic:=/tesse/left_cam/rgb/image_raw",
         "/depth_images_topic:=/tesse/depth_cam/mono/image_raw"],
        stdout=log, stderr=subprocess.STDOUT, preexec_fn=os.setsid)
    time.sleep(2.0)  # let the subscribers connect
    t0 = time.time()
    play = ["rosbag", "play", "-q", f"-r{args.rate}", args.bag,
            "--topics", args.gt_topic, *IMAGE_TOPICS]
    if args.duration:
        play[3:3] = ["-u", str(args.duration)]
    if args.start:
        play[3:3] = ["-s", str(args.start)]
    subprocess.run(play, check=True, stdout=subprocess.DEVNULL)
    wait_quiet(csv, 10.0, node)
    os.killpg(os.getpgid(node.pid), signal.SIGINT)
    try:
        node.wait(timeout=20)
    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(node.pid), signal.SIGKILL)
    rows = sum(1 for _ in open(csv)) - 1 if csv.exists() else 0
    print(f"{name}: {rows} frame pairs in {time.time() - t0:.0f} s -> {csv}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bag", default=os.path.expanduser("~/datasets/vnav/lab6/office.bag"))
    ap.add_argument("--rate", type=float, default=1.0)
    ap.add_argument("--ransac_px", type=float, default=0.1)
    ap.add_argument("--ransac_3d_m", type=float, default=0.01)
    ap.add_argument("--max_iter", type=int, default=5000)
    ap.add_argument("--duration", type=float, default=0.0, help="play only N s (0: all)")
    ap.add_argument("--start", type=float, default=0.0, help="skip the first N s of the bag")
    ap.add_argument("--gt_topic", default="/tesse/odom")
    ap.add_argument("--out", default=None, help="output directory (default results/rpe)")
    ap.add_argument("--race", action="store_true",
                    help="Lab 4 race bag: /current_state ground truth, flight segment, results/race/rpe")
    ap.add_argument("--only", nargs="*", default=list(CONFIGS))
    ap.add_argument("--sweep", action="store_true", help="2D RANSAC threshold sweep instead")
    ap.add_argument("--sweep3d", action="store_true", help="Arun RANSAC threshold sweep instead")
    args = ap.parse_args()
    out = Path(args.out) if args.out else OUT
    if args.race:
        # The drone hovers before take-off; the flight lasts from about 2 s to 20 s into the bag.
        args.bag, args.gt_topic = str(RACE_BAG), "/current_state"
        out = Path(args.out) if args.out else RACE_OUT
        args.start, args.duration = args.start or 1.5, args.duration or 21.0

    core = None
    if subprocess.run(["rostopic", "list"], capture_output=True).returncode != 0:
        core = subprocess.Popen(["roscore"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                preexec_fn=os.setsid)
        time.sleep(3.0)
    try:
        if args.sweep3d:
            args.duration = args.duration or 60.0
            for m in SWEEP_3D_M:
                run(f"arun_{m:g}", CONFIGS["arun"][0], True, args, SWEEP_OUT, ransac_3d_m=m)
        elif args.sweep:
            args.duration = args.duration or 60.0
            for method in SWEEP_METHODS:
                for px in SWEEP_PX:
                    run(f"{method}_{px:g}", CONFIGS[method][0], True, args, SWEEP_OUT, px)
        else:
            for name in args.only:
                run(name, *CONFIGS[name], args, out)
    finally:
        if core:
            os.killpg(os.getpgid(core.pid), signal.SIGINT)


if __name__ == "__main__":
    sys.exit(main())
