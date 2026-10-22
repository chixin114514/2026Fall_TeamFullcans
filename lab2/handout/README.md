# Lab 2 Submission

This folder contains the ROS package source and the final report PDF.

- `two_drones_pkg/`: complete catkin package, including both C++ nodes, `package.xml`, `CMakeLists.txt`, launch file, RViz config, and drone mesh.
- `lab2_report.pdf`: final lab report.

## Build and run

Copy `two_drones_pkg/` into a catkin workspace's `src/` directory, then run:

```bash
catkin build
source devel/setup.bash
roslaunch two_drones_pkg two_drones.launch
```

For the static scene:

```bash
roslaunch two_drones_pkg two_drones.launch static:=True
```
