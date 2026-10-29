#!/usr/bin/env python3
"""Run the lab5 feature trackers and store per-frame statistics in results/.

  python3 scripts/run_experiments.py pair            # D3-D6a, box.png -> box_in_scene.png
  python3 scripts/run_experiments.py video [names]   # D6b/D7 on the two rosbags

Needs a running roscore and `source ~/vnav-builds/lab5_ws/devel/setup.bash`.
Every run writes results/<group>/<config>/{stats.csv,params.json,stdout.txt}.
"""
import argparse
import csv
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

LAB5 = Path(__file__).resolve().parents[1]
RESULTS = LAB5 / "results"
IMAGES = LAB5 / "feature_tracking" / "images"
DATASETS = Path(os.environ.get("LAB5_DATASETS", Path.home() / "datasets/vnav/lab5"))

# Bags of Deliverable 6.b: name -> (file, image topic)
BAGS = {
    "30fps": ("30fps_424x240_2018-10-01-18-35-06.bag", "/camera/color/image_raw"),
    "smooth": ("vnav-lab5-smooth-trajectory.bag", "/tesse/left_cam/rgb/image_raw"),
}

# Pair-of-images configurations (Deliverable 6.a). "default" = stencil params.
PAIR_CONFIGS = {
    "SIFT_default": {"descriptor": "SIFT"},
    "SURF_default": {"descriptor": "SURF"},
    "SURF_h400": {"descriptor": "SURF", "surf_hessian_threshold": 400.0},
    "ORB_default": {"descriptor": "ORB"},  # 500 features, 1 level, BF Hamming
    "ORB_flann_lsh": {"descriptor": "ORB", "bf_matcher": False},
    "ORB_8lvl": {"descriptor": "ORB", "orb_nlevels": 8},
    "ORB_8lvl_2000": {"descriptor": "ORB", "orb_nlevels": 8, "orb_nfeatures": 2000},
    "FAST_default": {"descriptor": "FAST"},  # threshold 10, BRIEF-32, BF Hamming
    "FAST_flann_lsh": {"descriptor": "FAST", "bf_matcher": False},
    "FAST_t30": {"descriptor": "FAST", "fast_threshold": 30},
}

# Video configurations (Deliverable 6.b / 7). For each method the table uses
# the variant with the most inliers (see make_figures.py: VIDEO_BEST).
VIDEO_CONFIGS = {
    "SIFT": {"descriptor": "SIFT"},
    "SIFT_c002": {"descriptor": "SIFT", "sift_contrast_threshold": 0.02},
    "SURF": {"descriptor": "SURF"},
    "SURF_h400": {"descriptor": "SURF", "surf_hessian_threshold": 400.0},
    "ORB_stencil": {"descriptor": "ORB"},  # 500 features, 1 level
    "ORB": {"descriptor": "ORB", "orb_nlevels": 8, "orb_nfeatures": 1000},
    "ORB_2000": {"descriptor": "ORB", "orb_nlevels": 8, "orb_nfeatures": 2000},
    "FAST_t10": {"descriptor": "FAST", "fast_threshold": 10},
    "FAST": {"descriptor": "FAST", "fast_threshold": 20},
    "FAST_t30": {"descriptor": "FAST", "fast_threshold": 30},
    "LK": {"descriptor": "LK"},  # 500 Harris corners, min distance 10 px
    "LK_1000": {"descriptor": "LK", "lk_max_corners": 1000, "lk_min_distance": 5.0},
}

# Every output frame of --frames-for configs goes here (outside the repo,
# only used to encode the videos in video/).
FRAMES = Path(os.environ.get("LAB5_FRAMES", Path.home() / "vnav-builds/lab5_frames"))


def ros_args(params):
    out = []
    for k, v in params.items():
        if isinstance(v, bool):
            v = "true" if v else "false"
        out.append(f"_{k}:={v}")
    return out


def summarize(csv_path):
    with open(csv_path) as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return {"frames": 0}
    keys = ["kp1", "kp2", "matches", "good_matches", "inliers", "inlier_ratio", "time_ms"]
    summary = {k: sum(float(r[k]) for r in rows) / len(rows) for k in keys}
    summary["frames"] = len(rows)
    return summary


NODE = "/lab5_tracker"


def clear_params():
    # `rosrun ... _param:=value` leaves the private params on the parameter
    # server; without this a config would inherit values from the previous one.
    subprocess.run(["rosparam", "delete", NODE], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


def prepare(group, name, params):
    clear_params()
    out = RESULTS / group / name
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    params = dict(params, stats_csv=str(out / "stats.csv"), output_dir=str(out), show=False)
    (out / "params.json").write_text(json.dumps(params, indent=2) + "\n")
    return out, params


def run_pair(names):
    for name in names or PAIR_CONFIGS:
        out, params = prepare("d6a_pair", name, PAIR_CONFIGS[name])
        params.update(mode=0, repeat=20, img1_path=str(IMAGES / "box.png"),
                      img2_path=str(IMAGES / "box_in_scene.png"))
        res = subprocess.run(["rosrun", "lab_5", "track_features", *ros_args(params),
                              f"__name:={NODE[1:]}"],
                             capture_output=True, text=True, timeout=120)
        (out / "stdout.txt").write_text(res.stdout + res.stderr)
        print(name, json.dumps(summarize(out / "stats.csv")))


def run_video(names, bags, rate, frames_for):
    for bag_name in bags:
        bag_file, topic = BAGS[bag_name]
        for name in names or VIDEO_CONFIGS:
            out, params = prepare(f"d6b_video/{bag_name}", name, VIDEO_CONFIGS[name])
            params.update(mode=1, save_frame=150)
            if name in frames_for:
                frames = FRAMES / bag_name / name
                shutil.rmtree(frames, ignore_errors=True)
                frames.mkdir(parents=True)
                params["frames_dir"] = str(frames)
            log = open(out / "stdout.txt", "w")
            node = subprocess.Popen(
                ["rosrun", "lab_5", "track_features", *ros_args(params),
                 f"/images_topic:={topic}", f"__name:={NODE[1:]}"],
                stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            time.sleep(2.0)  # let the subscriber connect before playing
            subprocess.run(["rosbag", "play", "-q", "-r", str(rate), str(DATASETS / bag_file),
                            "--topics", topic], check=True, stdout=subprocess.DEVNULL)
            # Wait for the node to drain its queue (csv stops growing).
            last = -1
            while True:
                time.sleep(1.5)
                size = (out / "stats.csv").stat().st_size
                if size == last:
                    break
                last = size
            node.send_signal(signal.SIGINT)
            node.wait(timeout=30)
            log.close()
            print(bag_name, name, json.dumps(summarize(out / "stats.csv")), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["pair", "video"])
    ap.add_argument("names", nargs="*")
    ap.add_argument("--bags", nargs="*", default=list(BAGS))
    ap.add_argument("--rate", type=float, default=0.5,
                    help="rosbag play rate; slow enough that no frame is dropped")
    ap.add_argument("--frames-for", nargs="*", default=[],
                    help="configs whose every output frame is saved (for the videos)")
    args = ap.parse_args()
    if args.what == "pair":
        run_pair(args.names)
    else:
        run_video(args.names, args.bags, args.rate, set(args.frames_for))


if __name__ == "__main__":
    sys.exit(main())
