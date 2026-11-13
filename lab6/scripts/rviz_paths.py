#!/usr/bin/env python3
"""RViz helper: turn the pose topics of lab_6/pose_estimation into trajectories.

/gt_path        ground-truth camera trajectory
/est_path       per-frame estimates, each anchored on the previous ground-truth pose
/odom_path      estimates chained on each other only (visual odometry, drifts over time)
/map_cloud      coloured point cloud of the scene: depth back-projected with the
                ground-truth camera pose and accumulated on a voxel grid
TF world -> camera_gt so the RViz view can follow the camera.
"""
import os
import threading
import time

# 4x4 matrices only: OpenBLAS worker threads would busy-wait and eat >1 CPU core.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np  # noqa: E402
import rospy
import tf2_ros
from geometry_msgs.msg import PoseStamped, TransformStamped
from nav_msgs.msg import Path
from sensor_msgs.msg import Image, PointCloud2, PointField
from tf.transformations import quaternion_matrix, quaternion_from_matrix

MAX_POSES = 4000
# Pinhole intrinsics of the TESSE left camera (also hard-coded in pose_estimation.cpp).
FX = FY = 415.69219381653056
CX, CY = 360.0, 240.0
STRIDE = 6          # use every 6th pixel in u and v
EVERY = 3           # integrate every 3rd frame
VOXEL = 0.10        # m
MAX_RANGE = 12.0    # m
MAX_POINTS = 600000
MAP_PERIOD = 1.0    # s (wall clock) between map publications
# The simulator's depth camera renders the drone's own model (the RGB camera does not):
# pixels that are this close in almost every frame are the drone and are masked out.
SELF_NEAR = 1.5     # m
SELF_FRACTION = 0.9
SELF_MIN_FRAMES = 15
# Gate glow: red light bleeds onto walls in the RGB image (see deglow).
RED_EXCESS = 12     # R - max(G, B) above which a pixel is red-tinted
GATE_R = 245        # tube core is saturated in R; the halo is not
GATE_COLOUR = (230, 30, 30)


def to_mat(p):
    T = quaternion_matrix([p.orientation.x, p.orientation.y, p.orientation.z, p.orientation.w])
    T[:3, 3] = [p.position.x, p.position.y, p.position.z]
    return T


def to_pose(T, stamp):
    m = PoseStamped()
    m.header.frame_id, m.header.stamp = "world", stamp
    m.pose.position.x, m.pose.position.y, m.pose.position.z = T[:3, 3]
    q = quaternion_from_matrix(T)
    m.pose.orientation.x, m.pose.orientation.y, m.pose.orientation.z, m.pose.orientation.w = q
    return m


class Paths:
    def __init__(self):
        self.paths = {k: Path() for k in ("gt", "est", "odom")}
        for p in self.paths.values():
            p.header.frame_id = "world"
        self.pubs = {k: rospy.Publisher(f"/{k}_path", Path, queue_size=1) for k in self.paths}
        self.est_wait, self.gt_wait = {}, {}  # stamp -> pose, waiting for the other topic
        self.prev_gt = None     # ground truth of the previous processed frame
        self.odom = None        # chained estimate
        self.tf = tf2_ros.TransformBroadcaster()
        self.dirty = set()
        self.map_sent = 0.0
        # wall clock: sim time runs slower than real time when the bag is played at 0.15x
        threading.Thread(target=self.flush_loop, daemon=True).start()
        # scene map
        self.rgb, self.depth = {}, {}         # stamp -> image array, last few frames
        self.map_keys = np.empty(0, np.int64)
        self.map_xyz = np.empty((0, 3), np.float32)
        self.map_rgb = np.empty(0, np.uint32)
        self.n_frames = 0
        self.near_count, self.n_depth = None, 0   # drone self-occlusion statistics
        self.map_lock = threading.Lock()
        self.map_pub = rospy.Publisher("/map_cloud", PointCloud2, queue_size=1)
        rospy.Subscriber("/rgb_images_topic", Image, self.on_rgb, queue_size=5, buff_size=2**24)
        rospy.Subscriber("/depth_images_topic", Image, self.on_depth, queue_size=5, buff_size=2**24)
        rospy.Subscriber("/gt_camera_pose", PoseStamped, self.on_gt, queue_size=100)
        rospy.Subscriber("/camera_pose", PoseStamped, self.on_est, queue_size=100)

    def append(self, key, msg):
        path = self.paths[key]
        if path.poses and msg.header.stamp < path.poses[-1].header.stamp:  # bag looped
            for p in self.paths.values():
                p.poses = []
            self.odom = self.prev_gt = None  # the scene is static: the map is kept
        path.poses.append(msg)
        del path.poses[:-MAX_POSES]
        path.header.stamp = msg.header.stamp
        self.dirty.add(key)

    def flush_loop(self):
        while not rospy.is_shutdown():
            self.flush()
            time.sleep(0.1)

    def flush(self):
        # Republishing whole paths on every message costs a full CPU core; 10 Hz is enough for RViz.
        dirty, self.dirty = self.dirty, set()
        for key in dirty:
            if key == "map":
                if time.time() - self.map_sent < MAP_PERIOD:
                    self.dirty.add("map")       # try again on a later tick
                    continue
                self.map_sent = time.time()
                self.publish_map()
            else:
                self.pubs[key].publish(self.paths[key])

    def chain(self, stamp):
        """Both topics carry the same image stamp; chain once both have arrived (any order)."""
        if stamp not in self.est_wait or stamp not in self.gt_wait:
            return
        T_est, T_gt = self.est_wait.pop(stamp), self.gt_wait.pop(stamp)
        if self.odom is None or self.prev_gt is None:
            self.odom = T_est                           # start on the ground truth
        else:
            self.odom = self.odom @ (np.linalg.inv(self.prev_gt) @ T_est)  # T^{t-1}_t
        self.prev_gt = T_gt
        self.append("odom", to_pose(self.odom, stamp))
        for d in (self.est_wait, self.gt_wait):         # drop unmatched leftovers
            for k in [k for k in d if k < stamp]:
                del d[k]

    def on_est(self, msg):
        self.append("est", msg)
        self.est_wait[msg.header.stamp] = to_mat(msg.pose)
        self.chain(msg.header.stamp)

    @staticmethod
    def keep_last(d, stamp, value, n=150):
        d[stamp] = value
        while len(d) > n:
            d.pop(next(iter(d)))

    def on_rgb(self, msg):
        img = np.frombuffer(msg.data, np.uint8).reshape(msg.height, msg.width, -1)[::STRIDE, ::STRIDE, :3]
        if msg.encoding.startswith("bgr"):
            img = img[..., ::-1]
        self.keep_last(self.rgb, msg.header.stamp, img.copy())

    def on_depth(self, msg):
        if msg.encoding == "16UC1":
            d = np.frombuffer(msg.data, np.uint16).reshape(msg.height, msg.width).astype(np.float32) * 1e-3
        else:  # 32FC1, metres
            d = np.frombuffer(msg.data, np.float32).reshape(msg.height, msg.width)
        d = d[::STRIDE, ::STRIDE].copy()
        near = np.isfinite(d) & (d < SELF_NEAR)
        self.near_count = near.astype(np.int32) if self.near_count is None else self.near_count + near
        self.n_depth += 1
        self.keep_last(self.depth, msg.header.stamp, d)

    def integrate(self, stamp, T_wc):
        d, c = self.depth.get(stamp), self.rgb.get(stamp)
        if d is None or c is None:
            rospy.logwarn_throttle(5, f"map: no images for {stamp.to_sec():.3f} "
                                      f"(cached {len(self.depth)} depth, {len(self.rgb)} rgb)")
            return
        if self.n_depth < SELF_MIN_FRAMES:
            return                                       # drone mask not learnt yet
        self_mask = self.near_count >= SELF_FRACTION * self.n_depth
        c = self.deglow(c, d)
        v, u = np.mgrid[0:d.shape[0], 0:d.shape[1]] * STRIDE
        ok = np.isfinite(d) & (d > 0.2) & (d < MAX_RANGE) & ~self_mask
        z = d[ok]
        p_c = np.stack([(u[ok] - CX) / FX * z, (v[ok] - CY) / FY * z, z], 1)  # optical frame
        p_w = (p_c @ T_wc[:3, :3].T + T_wc[:3, 3]).astype(np.float32)
        col = c[ok].astype(np.uint32)
        rgb = (col[:, 0] << 16) | (col[:, 1] << 8) | col[:, 2]
        ijk = np.floor(p_w / VOXEL).astype(np.int64) + (1 << 20)
        keys = (ijk[:, 0] << 42) | (ijk[:, 1] << 21) | ijk[:, 2]
        with self.map_lock:
            self._merge(keys, p_w, rgb)
        self.dirty.add("map")
        rospy.loginfo_throttle(5, f"map: {len(self.map_xyz)} points")

    def _merge(self, keys, p_w, rgb):
        keys = np.concatenate([self.map_keys, keys])
        xyz = np.concatenate([self.map_xyz, p_w])
        rgb = np.concatenate([self.map_rgb, rgb])
        keys, first = np.unique(keys, return_index=True)        # one point per voxel
        self.map_keys, self.map_xyz, self.map_rgb = keys, xyz[first], rgb[first]
        if len(self.map_keys) > MAX_POINTS:
            keep = np.random.default_rng(0).choice(len(self.map_keys), MAX_POINTS, replace=False)
            keep.sort()
            self.map_keys, self.map_xyz, self.map_rgb = (a[keep] for a in (self.map_keys, self.map_xyz, self.map_rgb))

    @staticmethod
    def deglow(c, d=None):
        """Grey out the red glow that gates cast on walls and floor; keep the gate tubes red.

        Across a gate the tube core is saturated (R ~ 255, G = B ~ 190) and the halo is a
        red gradient with R < ~210, so the core is told apart by its red channel."""
        c = c.astype(np.int16)
        red = c[..., 0] - np.maximum(c[..., 1], c[..., 2])
        tinted = red > RED_EXCESS
        tube = tinted & (c[..., 0] >= GATE_R)
        glow = tinted & ~tube
        grey = np.maximum(c[..., 1], c[..., 2])
        c[glow] = grey[glow][:, None]
        c[tube] = GATE_COLOUR
        return c.astype(np.uint8)

    def publish_map(self):
        with self.map_lock:
            xyz, rgb = self.map_xyz, self.map_rgb
        n = len(xyz)
        buf = np.empty(n, dtype=[("x", "<f4"), ("y", "<f4"), ("z", "<f4"), ("rgb", "<u4")])
        buf["x"], buf["y"], buf["z"] = xyz.T
        buf["rgb"] = rgb
        m = PointCloud2()
        m.header.frame_id, m.header.stamp = "world", rospy.Time.now()
        m.height, m.width = 1, n
        m.fields = [PointField(name, 4 * i, PointField.FLOAT32, 1) for i, name in enumerate("xyz")]
        m.fields.append(PointField("rgb", 12, PointField.FLOAT32, 1))  # packed RGB, RViz convention
        m.is_bigendian, m.point_step, m.row_step, m.is_dense = False, 16, 16 * n, True
        m.data = buf.tobytes()
        self.map_pub.publish(m)

    def on_gt(self, msg):
        self.append("gt", msg)
        self.n_frames += 1
        if self.n_frames % EVERY == 0:
            self.integrate(msg.header.stamp, to_mat(msg.pose))
        self.gt_wait[msg.header.stamp] = to_mat(msg.pose)
        self.chain(msg.header.stamp)
        t = TransformStamped()
        t.header = msg.header
        t.child_frame_id = "camera_gt"
        t.transform.translation.x = msg.pose.position.x
        t.transform.translation.y = msg.pose.position.y
        t.transform.translation.z = msg.pose.position.z
        t.transform.rotation = msg.pose.orientation
        self.tf.sendTransform(t)

if __name__ == "__main__":
    rospy.init_node("lab6_rviz_paths")
    Paths()
    rospy.spin()
