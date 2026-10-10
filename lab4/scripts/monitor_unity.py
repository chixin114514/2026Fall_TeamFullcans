#!/usr/bin/env python3
"""Record live telemetry from the official Unity flight and detect final hold."""
import csv
import os
import time
import threading
import numpy as np
import rospy
from nav_msgs.msg import Odometry
from trajectory_msgs.msg import MultiDOFJointTrajectoryPoint

rospy.init_node('unity_race_monitor')
lock = threading.Lock()
target = [None]
rows = []
last_progress = [0.0, 0.0]
started = [None]
last_log = [0.0]

def desired(m):
    if m.transforms:
        with lock: target[0] = m

def current(m):
    with lock: d = target[0]
    if d is None: return
    stamp = m.header.stamp.to_sec()
    t = d.time_from_start.to_sec()
    if started[0] is None: started[0] = stamp
    p = m.pose.pose.position
    pd = d.transforms[0].translation
    q = m.pose.pose.orientation
    rows.append([stamp-started[0],p.x,p.y,p.z,pd.x,pd.y,pd.z,t,q.x,q.y,q.z,q.w])
    if t > last_progress[0] + 1e-5: last_progress[:] = [t,stamp]
    if stamp-last_log[0] > 5:
        error = np.linalg.norm([p.x-pd.x,p.y-pd.y,p.z-pd.z])
        print('trajectory_time={:.2f} position=({:.2f},{:.2f},{:.2f}) error={:.3f}m'.format(t,p.x,p.y,p.z,error),flush=True)
        last_log[0] = stamp

rospy.Subscriber('/desired_state',MultiDOFJointTrajectoryPoint,desired,queue_size=1)
rospy.Subscriber('/current_state',Odometry,current,queue_size=100)
finish = time.monotonic() + 600
complete = False
while not rospy.is_shutdown() and time.monotonic() < finish:
    time.sleep(.2)
    if rows and last_progress[0] > 5:
        row = rows[-1]
        held = row[0]+started[0]-last_progress[1]
        if held > 10:
            error = np.linalg.norm(np.array(row[1:4])-row[4:7])
            if error < .2 or held > 30:
                complete = error < .2
                print('Final hold: {:.1f}s error={:.4f}m complete={}'.format(held,error,complete),flush=True)
                break
os.makedirs('/workspace/lab4/report',exist_ok=True)
with open('/workspace/lab4/report/unity_flight.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['t','x','y','z','xd','yd','zd','trajectory_time','qx','qy','qz','qw']);w.writerows(rows)
if not complete: raise RuntimeError('Unity run did not reach a settled final pose')
