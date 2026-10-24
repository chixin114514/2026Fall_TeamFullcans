#!/usr/bin/env python3
"""Lap timer for the official Lab4 Unity course.

Unity turns a gate green in OnTriggerEnter, as soon as any collider of the
drone overlaps the gate's trigger box; the drone does not have to cross the
gate plane. This node rebuilds both boxes from the scene data and times the
race from the first touch of gate 0 to the first touch of gate 11 in
simulation time, interpolating between state samples. Unity evaluates
triggers only every 20 ms physics step, so its own colour change can lag the
interpolated touch by up to one step.

Collisions reported by the bridge and the gate hits Unity writes to its player
log are listed as a cross-check. A jump of more than 3 m between two states
(a respawn) starts a new attempt.
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import rospy
from nav_msgs.msg import Odometry
from visualization_msgs.msg import Marker

try:
    from tesse_ros_bridge.msg import CollisionStats
except ImportError:
    CollisionStats = None

LAB4_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_TFS = os.path.join(
    LAB4_DIR, 'simulator_data/StreamingAssets/vnav-2020-lab4_static_tfs.csv')
UNITY_LOG = os.path.expanduser(
    '~/.config/unity3d/DefaultCompany/tesse_vnav_scenes/Player.log')
DRONE_COLLIDER_NAME = 'tesse_aero_quadrotor_agent'

# Unity (x, y, z) -> ROS (x, z, y); applied on both sides of a rotation.
UNITY_TO_ROS = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=float)


def quat_matrix(x, y, z, w):
    return np.array([
        [1 - 2*(y*y + z*z), 2*(x*y - z*w), 2*(x*z + y*w)],
        [2*(x*y + z*w), 1 - 2*(x*x + z*z), 2*(y*z - x*w)],
        [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x*x + y*y)]])


def load_gates(path=STATIC_TFS):
    """Trigger boxes of red_square_drone_door (0..11) as (center, axes, half sizes).

    Scene hierarchy: door -> orientation_correction (90 deg about Unity y) ->
    sprite (scale 0.5, 0.5, 1) with a BoxCollider trigger of size
    (4.667, 4.6, 0.2) centred at (-0.0403, 0, 0).
    """
    correction = quat_matrix(0.0, 0.7071068, 0.0, 0.7071068)
    gates = {}
    with open(path) as f:
        for line in f:
            fields = line.strip().split(',')
            if not fields[0].startswith('red_square_drone_door'):
                continue
            name = fields[0]
            index = 0 if name == 'red_square_drone_door' else int(name.split('(')[1].rstrip(')'))
            x, y, z, qx, qy, qz, qw = map(float, fields[1:8])
            rotation = quat_matrix(qx, qy, qz, qw) @ correction
            center = np.array([x, y, z]) + rotation @ np.array([-0.0403248 * 0.5, 0.0, 0.0])
            gates[index] = (UNITY_TO_ROS @ center,
                            UNITY_TO_ROS @ rotation @ UNITY_TO_ROS,
                            np.array([4.667062 * 0.25, 4.6 * 0.25, 0.1]))
    return [gates[i] for i in sorted(gates)]


# Drone colliders in the ROS body frame (agent scale 2): the body box
# (1.068 x 1.068 x 0.190) and the two landing-skid capsules, boxed.
DRONE_BOXES = [
    (np.array([0.0028, 0.0024, -0.0401]), np.array([0.534, 0.534, 0.0951])),
    (np.array([-0.16, 0.0, -0.192]), np.array([0.008, 0.183, 0.008])),
    (np.array([0.16, 0.0, -0.192]), np.array([0.008, 0.183, 0.008])),
]


def obb_overlap(c1, r1, h1, c2, r2, h2):
    """Separating axis test for two oriented boxes (axes are matrix columns)."""
    rot = r1.T @ r2
    abs_rot = np.abs(rot) + 1e-9
    t = r1.T @ (c2 - c1)
    for i in range(3):
        if abs(t[i]) > h1[i] + abs_rot[i] @ h2:
            return False
    for j in range(3):
        if abs(t @ rot[:, j]) > h1 @ abs_rot[:, j] + h2[j]:
            return False
    for i in range(3):
        for j in range(3):
            i1, i2 = (i + 1) % 3, (i + 2) % 3
            j1, j2 = (j + 1) % 3, (j + 2) % 3
            ra = h1[i1]*abs_rot[i2, j] + h1[i2]*abs_rot[i1, j]
            rb = h2[j1]*abs_rot[i, j2] + h2[j2]*abs_rot[i, j1]
            if abs(t[i2]*rot[i1, j] - t[i1]*rot[i2, j]) > ra + rb:
                return False
    return True


def touches(gate, position, rotation):
    center, axes, half = gate
    return any(obb_overlap(position + rotation @ offset, rotation, size, center, axes, half)
               for offset, size in DRONE_BOXES)


class RaceTimer:
    def __init__(self, args):
        self.args = args
        self.gates = load_gates()
        self.marker_pub = rospy.Publisher('/race/timer', Marker, queue_size=1, latch=True)
        self.attempt = 0
        self.reset()
        self.log_path = args.unity_log
        self.log_offset = os.path.getsize(self.log_path) if os.path.exists(self.log_path) else 0
        rospy.Subscriber('/current_state', Odometry, self.on_state, queue_size=100)
        if CollisionStats is not None:
            rospy.Subscriber('/tesse/collision', CollisionStats, self.on_collision, queue_size=100)

    def reset(self):
        self.attempt += 1
        self.prev = None
        self.touch = [None] * len(self.gates)
        self.collisions = []
        self.finished = False
        self.reported = False
        self.from_unity = []
        self.unity_hits = []
        if self.attempt > 1:
            rospy.loginfo('Attempt %d: waiting for gate 0', self.attempt)

    def on_collision(self, msg):
        if msg.is_collision and self.touch[0] is not None and not self.finished:
            if not self.collisions or self.collisions[-1][1] != msg.object_name:
                self.collisions.append((msg.header.stamp.to_sec(), msg.object_name))
                rospy.logwarn('Collision with %s', msg.object_name)

    def on_state(self, msg):
        p = msg.pose.pose.position
        q = msg.pose.pose.orientation
        sample = (msg.header.stamp.to_sec(), np.array([p.x, p.y, p.z]),
                  quat_matrix(q.x, q.y, q.z, q.w))
        if self.prev is not None and np.linalg.norm(sample[1] - self.prev[1]) > 3.0:
            if self.touch[0] is not None and not self.reported:
                self.report()
            self.reset()
        if self.prev is not None and not self.finished:
            self.check(self.prev, sample)
        self.prev = sample
        self.read_unity_log()
        # Report once Unity has had time to log the last trigger.
        if self.finished and not self.reported and sample[0] - self.touch[-1] > 0.5:
            self.report()

    def check(self, a, b):
        for i, gate in enumerate(self.gates):
            if self.touch[i] is not None or not touches(gate, b[1], b[2]):
                continue
            if touches(gate, a[1], a[2]):
                stamp = a[0]
            else:
                lo, hi = 0.0, 1.0
                for _ in range(20):
                    mid = 0.5 * (lo + hi)
                    if touches(gate, a[1] + mid * (b[1] - a[1]), b[2]):
                        hi = mid
                    else:
                        lo = mid
                stamp = a[0] + hi * (b[0] - a[0])
            self.touch[i] = stamp
            speed = np.linalg.norm(b[1] - a[1]) / max(b[0] - a[0], 1e-6)
            if i == 0:
                rospy.loginfo('GO  gate  0 touched, timer started (%.1f m/s)', speed)
            else:
                start = self.touch[0]
                rospy.loginfo('    gate %2d  %s  (%.1f m/s)', i,
                              '%7.3f s' % (stamp - start) if start is not None else '  (before start)',
                              speed)
            self.publish_marker()
        if self.touch[-1] is not None and self.touch[0] is not None:
            self.finished = True

    def read_unity_log(self):
        if not os.path.exists(self.log_path):
            return
        size = os.path.getsize(self.log_path)
        if size < self.log_offset:
            self.log_offset = 0
        if size == self.log_offset:
            return
        with open(self.log_path, 'rb') as f:
            f.seek(self.log_offset)
            data = f.read()
        self.log_offset = size
        hits = sum(1 for line in data.decode('utf-8', 'replace').splitlines()
                   if line.strip() == DRONE_COLLIDER_NAME)
        if hits and self.prev is not None:
            # Stamp with the newest state; the log is read on every state.
            self.unity_hits.append((self.prev[0], hits))

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.header.stamp = rospy.Time.now()
        marker.ns = 'race_timer'
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD
        marker.pose.position.x, marker.pose.position.y, marker.pose.position.z = -24.0, 17.0, 6.0
        marker.pose.orientation.w = 1.0
        marker.scale.z = 2.0
        marker.color.r = marker.color.g = marker.color.b = marker.color.a = 1.0
        passed = sum(t is not None for t in self.touch)
        if self.touch[0] is not None and self.touch[-1] is not None and passed == len(self.gates):
            marker.text = 'Race time %.3f s' % (self.touch[-1] - self.touch[0])
        else:
            marker.text = 'Gates %d/%d' % (passed, len(self.gates))
        self.marker_pub.publish(marker)

    def unity_events(self):
        """One OnTriggerEnter per drone collider; group hits closer than 0.1 s."""
        events = []
        for stamp, count in self.unity_hits:
            if events and stamp - events[-1] < 0.1:
                continue
            events.append(stamp)
        return events

    def fill_from_unity(self):
        """Unity is the reference: a gate the box model calls missed counts as
        touched when Unity logged a trigger no other gate explains, between
        the neighbouring gates. Its time is the log time minus the median
        log delay of the gates both agree on."""
        events = self.unity_events()
        matched, delays = set(), []
        for t in self.touch:
            if t is None:
                continue
            for k, e in enumerate(events):
                if k not in matched and -0.05 <= e - t <= 0.25:
                    matched.add(k)
                    delays.append(e - t)
                    break
        if not delays:
            return
        delay = float(np.median(delays))
        self.from_unity = []
        for i, t in enumerate(self.touch):
            if t is not None:
                continue
            before = max([x for x in self.touch[:i] if x is not None], default=-np.inf)
            after = min([x for x in self.touch[i + 1:] if x is not None], default=np.inf)
            for k, e in enumerate(events):
                if k not in matched and before < e - delay < after:
                    matched.add(k)
                    self.touch[i] = e - delay
                    self.from_unity.append(i)
                    break

    def report(self):
        self.reported = True
        self.fill_from_unity()
        start = self.touch[0]
        missed = [i for i, t in enumerate(self.touch) if t is None]
        lines = ['', '=== Lab4 race, attempt %d ===' % self.attempt]
        previous = start
        for i, stamp in enumerate(self.touch):
            if stamp is None:
                lines.append('gate %2d   MISSED' % i)
                continue
            lines.append('gate %2d  %8.3f s   split %6.3f s' % (i, stamp - start, stamp - previous))
            previous = stamp
        result = {'attempt': self.attempt, 'gate_touch_stamps': self.touch,
                  'missed_gates': missed, 'collisions': self.collisions,
                  'unity_log_hits': self.unity_hits}
        if missed:
            lines.append('DNF: %d gate(s) missed' % len(missed))
        else:
            out_of_order = [i for i in range(1, len(self.touch)) if self.touch[i] < self.touch[i - 1]]
            result['race_time'] = self.touch[-1] - start
            result['out_of_order'] = out_of_order
            lines.append('RACE TIME  %.3f s  (gate 0 -> gate 11, sim time)' % result['race_time'])
            if out_of_order:
                lines.append('note: gates touched out of order: %s' % out_of_order)
        lines.append('collisions during the race: %d %s' % (
            len(self.collisions), sorted({name for _, name in self.collisions})))
        events = self.unity_events()
        if self.from_unity:
            lines.append('gates timed from the Unity log (box model saw no overlap): %s' % self.from_unity)
        result['from_unity_log'] = self.from_unity
        unconfirmed = [i for i, t in enumerate(self.touch)
                       if t is not None and not any(-0.05 <= e - t <= 0.25 for e in events)]
        result['unity_trigger_events'] = events
        result['unconfirmed_by_unity'] = unconfirmed
        lines.append('Unity trigger events: %d (gate touches predicted: %d); not confirmed by Unity: %s' % (
            len(events), sum(t is not None for t in self.touch), unconfirmed or 'none'))
        print('\n'.join(lines), flush=True)
        if self.args.output:
            with open(self.args.output, 'a') as f:
                f.write(json.dumps(result) + '\n')
        self.publish_marker()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--unity-log', default=UNITY_LOG,
                        help='Unity player log (default: %(default)s)')
    parser.add_argument('--output', help='append each result as a JSON line to this file')
    args = parser.parse_args(rospy.myargv(argv=sys.argv)[1:])
    rospy.init_node('race_timer')
    timer = RaceTimer(args)
    rospy.on_shutdown(lambda: timer.touch[0] is not None and not timer.reported and timer.report())
    rospy.loginfo('Race timer ready: waiting for gate 0')
    rospy.spin()


if __name__ == '__main__':
    main()
