#!/usr/bin/env python3
"""Fly a race_opt.py spline on the Unity drone.

Reference playback and the geometric controller run in one callback per
/current_state message, so rotor commands leave as soon as Unity's state
arrives. Compared with the Lab3 controller this adds

  * body-rate feedforward from the reference jerk (differential flatness),
  * a constant yaw (the drone's collider is square, so heading is free),
  * prediction of the state by `lead` seconds to cover the bridge and the
    20 ms Unity physics step.

The drone first hovers at the spawn point, then starts the spline. The desired
state is also published on /desired_state for logging and RViz.
"""
import json
import threading
import time

import numpy as np
import rospy
from geometry_msgs.msg import PoseStamped, Quaternion, Transform, Twist, Vector3
from mav_msgs.msg import Actuators
from nav_msgs.msg import Odometry, Path
from trajectory_msgs.msg import MultiDOFJointTrajectoryPoint

G = 9.81
CF, CD, ARM = 1e-3, 1e-5, 0.3


def basis(tau, k):
    row = np.zeros(8)
    for i in range(k, 8):
        row[i] = np.prod(range(i - k + 1, i + 1)) * tau ** (i - k)
    return row


class Trajectory:
    def __init__(self, path, time_scale):
        data = json.load(open(path))
        self.coef = np.array(data['coef'])
        self.T = np.array(data['durations']) * time_scale
        self.scale = time_scale
        self.t_knot = np.r_[0.0, np.cumsum(self.T)]
        self.duration = self.t_knot[-1]
        self.gate_times = np.array(data['gate_knot_times']) * time_scale

    def __call__(self, t):
        t = min(max(t, 0.0), self.duration)
        s = int(np.clip(np.searchsorted(self.t_knot, t, side='right') - 1, 0, len(self.T) - 1))
        T = self.T[s]
        tau = (t - self.t_knot[s]) / T
        return [basis(tau, k) @ self.coef[s] / T ** k for k in range(4)]


def quat_matrix(x, y, z, w):
    return np.array([
        [1 - 2*(y*y + z*z), 2*(x*y - z*w), 2*(x*z + y*w)],
        [2*(x*y + z*w), 1 - 2*(x*x + z*z), 2*(y*z - x*w)],
        [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x*x + y*y)]])


def vee(S):
    return np.array([S[2, 1], S[0, 2], S[1, 0]])


def rodrigues(w, dt):
    angle = np.linalg.norm(w) * dt
    if angle < 1e-9:
        return np.eye(3)
    k = w / np.linalg.norm(w)
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * K @ K


a = ARM / np.sqrt(2.0)
ALLOCATION = np.array([[CF, CF, CF, CF],
                       [a*CF, a*CF, -a*CF, -a*CF],
                       [-a*CF, a*CF, a*CF, -a*CF],
                       [CD, -CD, CD, -CD]])
F2W = np.linalg.inv(ALLOCATION)


class RaceNode:
    def __init__(self):
        self.kx = rospy.get_param('~kx', 14.0)
        self.kv = rospy.get_param('~kv', 6.0)
        self.kr = rospy.get_param('~kr', 12.0)
        self.komega = rospy.get_param('~komega', 2.2)
        # Identified from rotor commands and body rates (one 20 ms step of delay):
        # Unity's inertia in the ROS body frame is about diag(0.11, 0.21, 0.11).
        self.inertia = np.array(rospy.get_param('~inertia', [0.1, 0.1, 0.1]), dtype=float)
        self.ff_alpha = rospy.get_param('~ff_alpha', False)
        self.lead = rospy.get_param('~lead', 0.0)
        self.ff_omega = rospy.get_param('~ff_omega', True)
        self.hover_time = rospy.get_param('~hover_time', 2.0)
        self.yaw = rospy.get_param('~yaw', 0.0)
        self.yaw_free = rospy.get_param('~yaw_free', False)
        self.reversible = rospy.get_param('~reversible', False)
        self.fb_tilt_thrust = rospy.get_param('~fb_tilt_thrust', 0.0)
        self.att_lead = rospy.get_param('~att_lead', 0.0)
        self.traj = Trajectory(rospy.get_param('~trajectory'), rospy.get_param('~time_scale', 1.0))
        # Learned reference offsets from race_ilc.py (position, velocity, acceleration).
        self.correction = None
        if rospy.get_param('~correction', ''):
            data = np.load(rospy.get_param('~correction'))
            self.correction = (data['t'], data['dx'], data['dv'], data['da'])
        self.start = self.traj(0.0)[0]
        self.phase = 'hover'
        self.hover_since = None
        self.t0 = None
        self.rotor_pub = rospy.Publisher('/rotor_speed_cmds', Actuators, queue_size=1, tcp_nodelay=True)
        self.desired_pub = rospy.Publisher('/desired_state', MultiDOFJointTrajectoryPoint, queue_size=10)
        self.path_pub = rospy.Publisher('/desired_path', Path, queue_size=1, latch=True)
        self.publish_path()
        self.lock = threading.Lock()
        self.last_state = None
        self.stall_after = rospy.get_param('~stall_after', 0.0)
        rospy.Subscriber('/current_state', Odometry, self.on_state, queue_size=1, tcp_nodelay=True)
        if self.stall_after > 0.0:
            threading.Thread(target=self.stall_watchdog, daemon=True).start()
        rospy.loginfo('Race trajectory %.2f s (gates at %.2f .. %.2f s), lead %.3f s',
                      self.traj.duration, self.traj.gate_times[0], self.traj.gate_times[-1], self.lead)

    def publish_path(self):
        path = Path()
        path.header.frame_id = 'world'
        for t in np.arange(0.0, self.traj.duration, 0.02):
            pose = PoseStamped()
            pose.header.frame_id = 'world'
            p = self.traj(t)[0]
            pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = p
            pose.pose.orientation.w = 1.0
            path.poses.append(pose)
        self.path_pub.publish(path)

    def reference(self, stamp):
        if self.phase == 'hover':
            zero = np.zeros(3)
            return self.start, zero, zero, zero
        t = stamp - self.t0
        x, v, a, j = self.traj(t)
        if self.correction is not None:
            ct, dx, dv, da = self.correction
            x = x + np.array([np.interp(t, ct, dx[:, i]) for i in range(3)])
            v = v + np.array([np.interp(t, ct, dv[:, i]) for i in range(3)])
            a = a + np.array([np.interp(t, ct, da[:, i]) for i in range(3)])
        return x, v, a, j

    def reference_rate(self, stamp):
        """World angular velocity of the reference thrust direction."""
        _, _, a, j = self.reference(stamp)
        f = a + G * np.array([0, 0, 1.0])
        b3 = f / np.linalg.norm(f)
        return np.cross(b3, (j - (j @ b3) * b3) / max(np.linalg.norm(f), 1.0))

    def on_state(self, msg):
        stamp = msg.header.stamp.to_sec()
        p = msg.pose.pose.position
        q = msg.pose.pose.orientation
        v = msg.twist.twist.linear
        w = msg.twist.twist.angular
        x = np.array([p.x, p.y, p.z])
        vel = np.array([v.x, v.y, v.z])
        R = quat_matrix(q.x, q.y, q.z, q.w)
        omega_world = np.array([w.x, w.y, w.z])

        if self.phase == 'hover':
            if np.linalg.norm(x - self.start) < 0.15 and np.linalg.norm(vel) < 0.2:
                if self.hover_since is None:
                    self.hover_since = stamp
                elif stamp - self.hover_since > self.hover_time:
                    self.phase = 'race'
                    self.t0 = stamp
                    rospy.loginfo('GO at t=%.3f', stamp)
            else:
                self.hover_since = None
        if self.phase == 'race':
            with self.lock:
                self.last_state = (stamp, time.monotonic(), x, vel, R, omega_world)
        self.control(stamp, x, vel, R, omega_world, msg.header.stamp)

    def stall_watchdog(self):
        """A fresh Unity stalls its main thread for 0.08-0.16 s the first time
        it draws a green gate. Its network thread still takes rotor commands,
        and afterwards it runs the missed physics steps back to back with the
        last one received. Meanwhile, keep sending the command for the middle
        of the stretch it will have to catch up, from the last state flown
        forward along the plan."""
        while not rospy.is_shutdown():
            time.sleep(0.005)
            with self.lock:
                last = self.last_state
            if last is None or self.phase != 'race':
                continue
            stamp, wall, x, vel, R, omega_world = last
            gap = time.monotonic() - wall
            if gap < self.stall_after or stamp - self.t0 > self.traj.duration:
                continue
            dt = 0.5 * gap
            ref_a = self.reference(stamp + 0.5 * dt)[2]
            self.control(stamp + dt, x + vel * dt + 0.5 * ref_a * dt * dt, vel + ref_a * dt,
                         rodrigues(omega_world, dt) @ R, omega_world, rospy.Time.from_sec(stamp + dt))

    def control(self, stamp, x, vel, R, omega_world, header_stamp):
        # Predict the state at the time the command takes effect.
        lead = self.lead
        ref_x, ref_v, ref_a, ref_j = self.reference(stamp + lead)
        if self.att_lead > 0.0 and self.phase == 'race':
            # The attitude trails the thrust direction by about one physics
            # step; at 20 g a few degrees is metres per second squared, so aim
            # the feedforward thrust further ahead than the position.
            _, _, ref_a, ref_j = self.reference(stamp + lead + self.att_lead)
        if lead > 0.0:
            x = x + vel * lead + 0.5 * ref_a * lead * lead
            vel = vel + ref_a * lead
            R = rodrigues(omega_world, lead) @ R
        omega = R.T @ omega_world

        A = -self.kx * (x - ref_x) - self.kv * (vel - ref_v) + G * np.array([0, 0, 1.0]) + ref_a
        b3 = A / np.linalg.norm(A)
        if self.fb_tilt_thrust > 0.0:
            # With little planned thrust, feedback alone would swing the
            # thrust axis around faster than Unity's 7 rad/s cap: point the
            # axis mostly by the plan and fade feedback in with the thrust.
            A_ref = G * np.array([0, 0, 1.0]) + ref_a
            weight = min(1.0, np.linalg.norm(A_ref) / self.fb_tilt_thrust)
            axis = A_ref + weight * (A - A_ref)
            b3 = axis / np.linalg.norm(axis)
        direction = 1.0
        if self.reversible and b3 @ R[:, 2] < 0.0:
            # Unity's rotors also push backwards (thrust ~ w|w|): align the
            # body axis with -A and command negative thrust instead of
            # flipping over.
            b3 = -b3
            direction = -1.0
        if self.yaw_free:
            # Smallest rotation from the current thrust axis to b3: no yaw
            # target, so no singularity when the drone tilts past 90 degrees.
            axis = np.cross(R[:, 2], b3)
            sin_angle = np.linalg.norm(axis)
            angle = np.arctan2(sin_angle, R[:, 2] @ b3)
            Rd = rodrigues(axis / sin_angle, angle) @ R if sin_angle > 1e-9 else R.copy()
        else:
            b1c = np.array([np.cos(self.yaw), np.sin(self.yaw), 0.0])
            b2 = np.cross(b3, b1c)
            b2 /= np.linalg.norm(b2)
            Rd = np.column_stack([np.cross(b2, b3), b2, b3])
        thrust = A @ R[:, 2]

        omega_d = np.zeros(3)
        alpha_d = np.zeros(3)
        if self.ff_omega and self.phase == 'race':
            f = np.linalg.norm(ref_a + G * np.array([0, 0, 1.0]))
            # d(b3)/dt; flips sign with b3 when the thrust is reversed.
            h = direction * (ref_j - (ref_j @ b3) * b3) / max(f, 1.0)
            omega_d = np.array([-h @ Rd[:, 1], h @ Rd[:, 0], 0.0])
            if self.ff_alpha:
                eps = 0.01
                rate = (self.reference_rate(stamp + lead + eps) - self.reference_rate(stamp + lead - eps)) / (2 * eps)
                alpha_d = R.T @ rate
        er = 0.5 * vee(Rd.T @ R - R.T @ Rd)
        ew = omega - R.T @ Rd @ omega_d
        # Gains are per 0.1 kg m^2, so each axis gets the same bandwidth.
        moment = (self.inertia / 0.1 * (-self.kr * er - self.komega * ew)
                  + self.inertia * alpha_d + np.cross(omega, self.inertia * omega))
        wrench = np.r_[thrust, moment]
        s = F2W @ wrench
        speeds = np.sign(s) * np.sqrt(np.abs(s))
        if not np.all(np.isfinite(speeds)):
            return
        cmd = Actuators()
        cmd.header.stamp = header_stamp
        cmd.angular_velocities = speeds.tolist()
        self.rotor_pub.publish(cmd)

        point = MultiDOFJointTrajectoryPoint()
        point.transforms = [Transform(Vector3(*ref_x), Quaternion(0, 0, np.sin(self.yaw / 2), np.cos(self.yaw / 2)))]
        point.velocities = [Twist(Vector3(*ref_v), Vector3())]
        point.accelerations = [Twist(Vector3(*ref_a), Vector3())]
        point.time_from_start = rospy.Duration.from_sec(0.0 if self.t0 is None else stamp + lead - self.t0)
        self.desired_pub.publish(point)


def main():
    rospy.init_node('race_node')
    RaceNode()
    rospy.spin()


if __name__ == '__main__':
    main()
