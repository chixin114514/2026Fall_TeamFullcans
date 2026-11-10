#!/usr/bin/env python3
"""Race clock drawn in the top-left corner of the Unity window.

The Unity player cannot be changed, so this is a borderless window placed
over it on the same X display (the Xephyr window shown on Windows, or the
headless Xvfb display), which screen recordings capture too. It shows
race_timer.py's /race/status: READY, a running clock in simulation time from
the first touch of gate 0, the clock frozen at the last gate, then the
official time (green) once Unity has confirmed every gate, or DNF.

  DISPLAY=:97 race_overlay.py [--x 4 --y 24]
"""
import argparse
import json
import sys
import threading
import tkinter as tk

import rospy
from rosgraph_msgs.msg import Clock
from std_msgs.msg import String

COLOURS = {'waiting': '#ffffff', 'running': '#ffd23c', 'stopped': '#ffffff',
           'finished': '#3cff6e', 'dnf': '#ff4b4b'}


class Overlay:
    def __init__(self, args):
        self.lock = threading.Lock()
        self.status = {'state': 'waiting', 'gates': 0, 'total': 12}
        self.now = 0.0
        rospy.Subscriber('/race/status', String, self.on_status, queue_size=10)
        rospy.Subscriber('/clock', Clock, self.on_clock, queue_size=1)
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('+%d+%d' % (args.x, args.y))
        self.root.configure(bg='black')
        self.clock = tk.Label(self.root, font=('DejaVu Sans Mono', args.size, 'bold'),
                              bg='black', fg='white', padx=8, pady=0, anchor='w')
        self.info = tk.Label(self.root, font=('DejaVu Sans Mono', max(9, args.size // 2)),
                             bg='black', fg='#bbbbbb', padx=8, pady=2, anchor='w')
        self.clock.pack(fill='x')
        self.info.pack(fill='x')
        self.root.after(30, self.refresh)
        self.root.after(500, self.keep_on_top)

    def on_status(self, msg):
        with self.lock:
            self.status = json.loads(msg.data)

    def on_clock(self, msg):
        with self.lock:
            self.now = msg.clock.to_sec()

    def refresh(self):
        if rospy.is_shutdown():
            self.root.destroy()
            return
        with self.lock:
            status, now = dict(self.status), self.now
        state = status.get('state', 'waiting')
        gates = 'Gates %d/%d' % (status.get('gates', 0), status.get('total', 12))
        if state == 'waiting':
            text, info = 'READY', 'Lab4 race  ' + gates
        elif state == 'running':
            text, info = '%.3f s' % max(0.0, now - status['start']), gates
        elif state == 'stopped':
            text, info = '%.3f s' % status['time'], 'checking gates with Unity...'
        elif state == 'finished':
            text, info = '%.3f s' % status['time'], 'FINISH  all gates green'
        else:
            text, info = 'DNF', 'missed gate(s) %s' % status.get('missed', [])
        self.clock.configure(text=text, fg=COLOURS.get(state, 'white'))
        self.info.configure(text=info)
        self.root.after(30, self.refresh)

    def keep_on_top(self):
        # No window manager runs on the Unity display, so raise it ourselves.
        self.root.lift()
        self.root.after(500, self.keep_on_top)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--x', type=int, default=4, help='left edge on the Unity display [px]')
    ap.add_argument('--y', type=int, default=24, help='top edge, below Unity\'s FPS text [px]')
    ap.add_argument('--size', type=int, default=26, help='clock font size')
    args = ap.parse_args(rospy.myargv(argv=sys.argv)[1:])
    rospy.init_node('race_overlay', disable_signals=True)
    overlay = Overlay(args)
    try:
        overlay.root.mainloop()
    except KeyboardInterrupt:
        pass
    rospy.signal_shutdown('overlay closed')


if __name__ == '__main__':
    main()
