# Codex conversation

## User

https://vnav.mit.edu/labs_2023/lab3/exercises.html 完成这里面的任务

## Assistant

我先阅读实验要求和当前项目文件，确认需要完成的代码、数据与交付内容，再逐项实现。

## Activity

    Opened https://vnav.mit.edu/labs_2023/lab3/exercises.html

## Activity

    $ pwd; rg --files -g 'AGENTS.md' -g '!build/**' -g '!devel/**' -g '!install/**' -g '!log/**' -g '!logs/**' -g '!**/.git/**'
    /home/chixin/f29xs/2026Fall_TeamFullcans/lab3
    ✗ (1) • 0ms

## Activity

    $ ls -la; rg --files --hidden -g '!.git/**' -g '!build/**' -g '!devel/**' -g '!install/**'; for p in /AGENTS.md /home/AGENTS.md /home/chixin/AGENTS.md /home/chixin/f29xs/AGENTS.md /home/chixin/f29xs/2026Fall_TeamFullcans/AGENTS.md; do if [ -f "$p" ]; then cat "$p"; fi; done; git status --short; git rev-parse --show-toplevel
    total 8
    drwxrwxr-x 2 chixin chixin 4096 Oct 10 10:11 .
    drwxrwxr-x 7 chixin chixin 4096 Oct 10 10:11 ..
    /home/chixin/f29xs/2026Fall_TeamFullcans
    ✓ • 0ms

## Activity

    Searched the web

## Activity

    $ ls -la ..; rg --files ../lab1 ../lab2 2>/dev/null | head -50; command -v roscore catkin catkin_make cmake g++ pdflatex ffmpeg xvfb-run; ls /opt/ros /usr/include/eigen3 /home/chixin/vnav_ws /home/chixin/vnav-builds 2>/dev/null; git remote -v
    total 32
    drwxrwxr-x 7 chixin chixin 4096 Oct 10 10:11 .
    drwxrwxr-x 3 chixin chixin 4096 Sep 20 15:21 ..
    drwxrwxr-x 8 chixin chixin 4096 Oct 10 10:14 .git
    -rw-rw-r-- 1 chixin chixin   61 Oct 10 09:57 .gitignore
    drwxrwxr-x 4 chixin chixin 4096 Sep 20 15:22 lab0
    drwxrwxr-x 5 chixin chixin 4096 Oct 10 09:57 lab1
    drwxrwxr-x 5 chixin chixin 4096 Oct 10 09:57 lab2
    drwxrwxr-x 2 chixin chixin 4096 Oct 10 10:11 lab3
    ../lab2/README.md
    ../lab2/handout/README.md
    ../lab2/handout/two_drones_pkg/launch/two_drones.launch
    ../lab1/vnav-codes/lab9/Dockerfile_KIMERA
    ../lab1/vnav-codes/lab9/run_docker.sh
    ../lab2/handout/two_drones_pkg/config/default.rviz
    ../lab2/handout/two_drones_pkg/CMakeLists.txt
    ../lab1/vnav-codes/lab9/params/ImuParams.yaml
    ../lab1/vnav-codes/lab9/params/DisplayParams.yaml
    ../lab1/vnav-codes/lab9/params/FrontendParams.yaml
    ../lab1/vnav-codes/lab9/params/LcdParams.yaml
    ../lab1/vnav-codes/lab9/params/LeftCameraParams.yaml
    ../lab2/handout/two_drones_pkg/src/plots_publisher_node.cpp
    ../lab2/handout/two_drones_pkg/src/frames_publisher_node.cpp
    ../lab2/handout/two_drones_pkg/package.xml
    ../lab2/handout/two_drones_pkg/mesh/quadrotor.dae
    ../lab1/vnav-codes/lab9/params/flags/Mesher.flags
    ../lab1/vnav-codes/lab9/params/flags/RegularVioBackend.flags
    ../lab1/vnav-codes/lab9/params/flags/Visualizer3D.flags
    ../lab1/vnav-codes/lab9/params/flags/stereoVIOEuroc.flags
    ../lab1/vnav-codes/lab9/params/flags/VioBackend.flags
    ../lab1/vnav-codes/lab9/params/PipelineParams.yaml
    ../lab1/vnav-codes/lab9/params/BackendParams.yaml
    ../lab1/vnav-codes/lab9/params/RightCameraParams.yaml
    ../lab1/vnav-codes/lab9/orb_slam.patch
    ../lab1/vnav-codes/lab9/Dockerfile_ORBSLAM3
    ../lab1/vnav-codes/lab9/fix_timestamps.py
    ../lab1/vnav-codes/README.md
    ../lab1/vnav-codes/test.txt
    ../lab1/vnav-codes/lab6/launch/video_tracking.launch
    ../lab1/vnav-codes/lab6/README.md
    ../lab2/report/figures/dynamic_av1_rviz.png
    ../lab2/report/figures/relative_components.pdf
    ../lab2/report/figures/static_rviz.png
    ../lab2/report/figures/relative_ellipse_samples.pdf
    ../lab2/report/figures/world_analytic.pdf
    ../lab2/report/figures/dynamic_world_rviz.png
    ../lab2/report/runtime_evidence.txt
    ../lab2/report/ieeeconf.cls
    ../lab1/vnav-codes/lab6/include/pose_estimation.h
    ../lab1/vnav-codes/lab6/include/lab6_utils.h
    ../lab1/vnav-codes/lab6/include/tracker_shim.h
    ../lab2/report/output/pdf/lab2_report.pdf
    ../lab2/report/plot_analysis.py
    ../lab2/report/main.tex
    ../lab1/vnav-codes/lab6/rviz/office.rviz
    ../lab1/vnav-codes/lab6/install/lab_6.rosinstall
    ../lab1/vnav-codes/lab6/CMakeLists.txt
    ../lab1/vnav-codes/lab6/src/tracker_shim.cpp
    ../lab1/vnav-codes/lab6/src/pose_estimation.cpp
    /usr/bin/cmake
    /usr/bin/g++
    /opt/ros:
    jazzy
    
    /usr/include/eigen3:
    Eigen
    signature_of_eigen3_matrix_library
    unsupported
    origin    https://github.com/chixin114514/2026Fall_TeamFullcans.git (fetch)
    origin    https://github.com/chixin114514/2026Fall_TeamFullcans.git (push)
    ✓ • 0ms

## Activity

    Opened https://vnav.mit.edu/labs_2023/lab3/

## Activity

    $ rg --files ../lab1/vnav-codes/lab3; cat ../lab2/README.md; cat ../lab1/vnav-codes/lab3/controller_pkg/src/controller_node.cpp; cat ../lab1/vnav-codes/lab3/controller_pkg/src/traj_publisher.cpp; rg --files /tmp -g '*noetic*' -g '*lab2*' -g '*tectonic*' -g 'AGENTS.md' 2>/dev/null | head -50; ls -la /tmp | head -45; cat ../.gitignore
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/README.md
    ../lab1/vnav-codes/lab3/catkin_simple/README.md
    ../lab1/vnav-codes/lab3/catkin_simple/cmake/catkin_simple-extras.cmake.em
    ../lab1/vnav-codes/lab3/catkin_simple/CMakeLists.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/README.md
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/tests/test_import.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/tests/__init__.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/requirements.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/setup.cfg
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/bar/include/bar/hello.h
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/notebooks/python-lidar-test.ipynb
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/notebooks/python_demonstration.ipynb
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/notebooks/python_quadrotor_demo.ipynb
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/bar/msg/HeaderString.msg
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/bar/src/hello.cpp
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/bar/package.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/msgs.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/utils.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/env.pyc
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/env.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/__init__.pyc
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/utils.pyc
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/msgs.pyc
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/__init__.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse.egg-info/dependency_links.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse.egg-info/top_level.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse.egg-info/SOURCES.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse.egg-info/PKG-INFO
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse.egg-info/requires.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/LICENSE
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/setup.py
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/foo/src/main.cpp
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/foo/package.xml
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/catkin_simple
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/srv/RepositionRequestService.srv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/srv/ObjectSpawnRequestService.srv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/srv/SceneRequestService.srv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/launch/tesse_quadrotor_bridge.launch
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/launch/play_traj.launch
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/launch/record_traj.launch
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/launch/tesse_bridge.launch
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/launch/maps.launch
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/baz/include/baz/world.h
    ../lab1/vnav-codes/lab3/catkin_simple/test/scenarios/hello_world/baz/package.xml
    ../lab1/vnav-codes/lab3/catkin_simple/package.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_3.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/object_data_0.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/cam_data_0.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_6.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_4.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/lidar_data_0.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_0.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_1.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_5.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/data/metadata_2.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/tests/test_utils.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/rviz/tesse_rss.rviz
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/params/map_tfs.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/params/noise_model.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/params/tesse_agent_params.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/params/camera_params.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/params/object_spawn_params.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/params/lidar_params.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/msg/CollisionStats.msg
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/rqt_multiplot/tesse.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/maps/city.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/maps/city_roads.yaml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/maps/city.png
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/maps/city_roads.png
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/install/tesse_ros_bridge.rosinstall
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/CMakeLists.txt
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/setup.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/key_teleop/key_teleop.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/key_teleop/LICENSE
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/noise_simulator.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/noise_simulator.pyc
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.pyc
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/quadrotor_control_interface.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/__init__.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/package.xml
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/scripts/rosbag_record.bash
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/scripts/traj_saver.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/scripts/notebooks/tesse_nn_training.ipynb
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/scripts/traj_loader.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/scripts/restamp_rosbag.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/scripts/convert_static_tf_csv.py
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/trajectories/traj_apartment.csv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/trajectories/traj_subway_long.csv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/trajectories/traj_office_long.csv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/trajectories/traj_neighborhood.csv
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/trajectories/traj_neighborhood_2.csv
    ../lab1/vnav-codes/lab3/controller_pkg/launch/traj_tracking.launch
    ../lab1/vnav-codes/lab3/controller_pkg/rviz/lab3.rviz
    ../lab1/vnav-codes/lab3/controller_pkg/CMakeLists.txt
    ../lab1/vnav-codes/lab3/controller_pkg/src/controller_node.cpp
    ../lab1/vnav-codes/lab3/controller_pkg/src/traj_publisher.cpp
    ../lab1/vnav-codes/lab3/controller_pkg/package.xml
    # Lab 2 - ROS / TF 两架无人机
    
    本目录实现 Notion 实验要求中的 ROS Noetic 包 `two_drones_pkg`。
    
    ## 构建与运行
    
    将 `two_drones_pkg` 放入 catkin workspace 的 `src` 目录后：
    
    ```bash
    cd ~/vnav_ws
    catkin build
    source devel/setup.bash
    
    # 静态场景
    roslaunch two_drones_pkg two_drones.launch static:=True
    
    # 动态场景
    roslaunch two_drones_pkg two_drones.launch
    ```
    
    动态场景中：
    
    - AV1 的世界坐标为 `[cos(t), sin(t), 0]`，姿态为 roll = pitch = 0、yaw = t；
    - AV2 的世界坐标为 `[sin(t), 0, cos(2t)]`，姿态与世界坐标系平行；
    - `frames_publisher_node` 以 50 Hz 发布 `world -> av1` 和 `world -> av2`；
    - `plots_publisher_node` 查询 TF，并在 `/visuals` 发布两个网格和三条轨迹。
    
    在 RViz 的 Global Options 中把 Fixed Frame 从 `world` 改成 `av1`，可观察 AV2 相对于 AV1 的轨迹。
    
    ## Deliverable 1：节点、主题与 launch
    
    静态场景的节点：
    
    - `/av1broadcaster`：发布 `world -> av1` 静态 TF；
    - `/av2broadcaster`：发布 `world -> av2` 静态 TF；
    - `/plots_publisher_node`：订阅 `/tf`、`/tf_static`，发布 `/visuals`；
    - `/rviz`：订阅 `/visuals`、`/tf`、`/tf_static`。
    
    动态场景用 `/frames_publisher_node` 替换前两个静态 TF broadcaster。
    
    不使用 launch 时，可在不同终端运行：
    
    ```bash
    roscore
    rosrun tf2_ros static_transform_publisher 1 0 0 0 0 0 1 world av1
    rosrun tf2_ros static_transform_publisher 0 0 1 0 0 0 1 world av2
    rosrun two_drones_pkg plots_publisher_node
    rosrun rviz rviz -d $(rospack find two_drones_pkg)/config/default.rviz
    ```
    
    `static:=True` 时 launch 中的 `if` 分组启动两个静态 broadcaster，并用 `unless` 禁止动态节点；省略该参数时默认值为 `false`，因此启动动态 TF 节点，两个无人机随时间运动。
    
    ## 轨迹校验
    
    AV2 在 AV1 坐标系中的位置由
    
    ```text
    o_2^1(t) = R_z(-t) (o_2^w(t) - o_1^w(t))
           = [sin(t) cos(t) - 1, -sin(t)^2, cos(2t)]^T
    ```
    
    给出，因此满足平面关系 `z = 2y + 1`。以 AV1 坐标 `(-1, -1/2, 0)` 为中心后，可取平面内正交坐标，使轨迹为
    
    ```text
    x_p = 1/2 sin(2t),    y_p = sqrt(5)/2 cos(2t)
    ```
    
    所以相对轨迹是半轴 `1/2` 和 `sqrt(5)/2` 的椭圆。
    #include <ros/ros.h>
    
    #include <tf2_geometry_msgs/tf2_geometry_msgs.h>
    #include <tf2/LinearMath/Quaternion.h>
    #include <tf2/utils.h>
    #include <mav_msgs/Actuators.h>
    #include <nav_msgs/Odometry.h>
    #include <trajectory_msgs/MultiDOFJointTrajectoryPoint.h>
    #include <cmath>
    
    #define PI M_PI
    
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    //  PART 0 |  16.485 - Fall 2019  - Lab 3 coding assignment
    // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    //
    //  In this code, we ask you to implement a geometric controller for a
    //  simulated UAV, following the publication:
    //
    //  [1] Lee, Taeyoung, Melvin Leoky, N. Harris McClamroch. "Geometric tracking
    //      control of a quadrotor UAV on SE (3)." Decision and Control (CDC),
    //      49th IEEE Conference on. IEEE, 2010
    //
    //  We use variable names as close as possible to the conventions found in the
    //  paper, however, we have slightly different conventions for the aerodynamic
    //  coefficients of the propellers (refer to the lecture notes for these).
    //  Additionally, watch out for the different conventions on reference frames
    //  (see Lab 3 Handout for more details).
    //
    //  The include below is strongly suggested [but not mandatory if you have
    //  better alternatives in mind :)]. Eigen is a C++ library for linear algebra
    //  that will help you significantly with the implementation. Check the
    //  quick reference page to learn the basics:
    //
    //  https://eigen.tuxfamily.org/dox/group__QuickRefPage.html
    
    #include <eigen3/Eigen/Dense>
    
    // If you choose to use Eigen, tf2 provides useful functions to convert tf2
    // messages to eigen types and vice versa.
    #include <tf2_eigen/tf2_eigen.h>
    
    // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    //                                 end part 0
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    class controllerNode{
      ros::NodeHandle nh;
    
      // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      //  PART 1 |  Declare ROS callback handlers
      // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
      //
      // In this section, you need to declare:
      //   1. two subscribers (for the desired and current UAVStates)
      //   2. one publisher (for the propeller speeds)
      //   3. a timer for your main control loop
      //
      // ~~~~ begin solution
      //
      //     **** FILL IN HERE ***
      //
      // ~~~~ end solution
      // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
      //                                 end part 1
      // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
      // Controller parameters
      double kx, kv, kr, komega; // controller gains - [1] eq (15), (16)
    
      // Physical constants (we will set them below)
      double m;              // mass of the UAV
      double g;              // gravity acceleration
      double d;              // distance from the center of propellers to the c.o.m.
      double cf,             // Propeller lift coefficient
             cd;             // Propeller drag coefficient
      Eigen::Matrix3d J;     // Inertia Matrix
      Eigen::Vector3d e3;    // [0,0,1]
      Eigen::MatrixXd F2W;   // Wrench-rotor speeds map
    
      // Controller internals (you will have to set them below)
      // Current state
      Eigen::Vector3d x;     // current position of the UAV's c.o.m. in the world frame
      Eigen::Vector3d v;     // current velocity of the UAV's c.o.m. in the world frame
      Eigen::Matrix3d R;     // current orientation of the UAV
      Eigen::Vector3d omega; // current angular velocity of the UAV's c.o.m. in the *body* frame
    
      // Desired state
      Eigen::Vector3d xd;    // desired position of the UAV's c.o.m. in the world frame
      Eigen::Vector3d vd;    // desired velocity of the UAV's c.o.m. in the world frame
      Eigen::Vector3d ad;    // desired acceleration of the UAV's c.o.m. in the world frame
      double yawd;           // desired yaw angle
    
      double hz;             // frequency of the main control loop
    
    
      static Eigen::Vector3d Vee(const Eigen::Matrix3d& in){
        Eigen::Vector3d out;
        out << in(2,1), in(0,2), in(1,0);
        return out;
      }
    
      static double signed_sqrt(double val){
        return val>0?sqrt(val):-sqrt(-val);
      }
    
    public:
      controllerNode():e3(0,0,1),F2W(4,4),hz(1000.0){
    
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          //  PART 2 |  Initialize ROS callback handlers
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //
          // In this section, you need to initialize your handlers from part 1.
          // Specifically:
          //  - bind controllerNode::onDesiredState() to the topic "desired_state"
          //  - bind controllerNode::onCurrentState() to the topic "current_state"
          //  - bind controllerNode::controlLoop() to the created timer, at frequency
          //    given by the "hz" variable
          //
          // Hints:
          //  - use the nh variable already available as a class member
          //  - read the lab 3 handout to fnd the message type
          //
          // ~~~~ begin solution
          //
          //     **** FILL IN HERE ***
          //
          // ~~~~ end solution
    
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //                                 end part 2
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          //  PART 6 [NOTE: save this for last] |  Tune your gains!
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //
          // Live the life of a control engineer! Tune these parameters for a fast
          // and accurate controller.
          //
          // Controller gains
          //
          //
          // **** FIDDLE WITH THESE! ***
          // Change them in the provided launch file.
          nh.getParam("kx", kx);
          nh.getParam("kv", kv);
          nh.getParam("kr", kr);
          nh.getParam("komega", komega);
          ROS_INFO("Gain values:\nkx: %f \nkv: %f \nkr: %f \nkomega: %f\n", kx, kv, kr, komega);
    
          //
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //                                 end part 6
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
          // Initialize constants
          m = 1.0;
          cd = 1e-5;
          cf = 1e-3;
          g = 9.81;
          d = 0.3;
          J << 1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0;
      }
    
      void onDesiredState(const trajectory_msgs::MultiDOFJointTrajectoryPoint& des_state){
    
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          //  PART 3 | Objective: fill in xd, vd, ad, yawd
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //
          // 3.1 Get the desired position, velocity and acceleration from the in-
          //     coming ROS message and fill in the class member variables xd, vd
          //     and ad accordingly. You can ignore the angular acceleration.
          //
          // Hint: use "v << vx, vy, vz;" to fill in a vector with Eigen.
          //
          // ~~~~ begin solution
          //
          //     **** FILL IN HERE ***
          //
          // ~~~~ end solution
          //
          // 3.2 Extract the yaw component from the quaternion in the incoming ROS
          //     message and store in the yawd class member variable
          //
          //  Hints:
          //    - use the methods tf2::getYaw(...)
          //    - maybe you want to use also tf2::fromMsg(...)
          //
          // ~~~~ begin solution
          //
          //     **** FILL IN HERE ***
          //
          // ~~~~ end solution
          //
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //                                 end part 3
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      }
    
      void onCurrentState(const nav_msgs::Odometry& cur_state){
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          //  PART 4 | Objective: fill in x, v, R and omega
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //
          // Get the current position and velocity from the incoming ROS message and
          // fill in the class member variables x, v, R and omega accordingly.
          //
          //  CAVEAT: cur_state.twist.twist.angular is in the world frame, while omega
          //          needs to be in the body frame!
          //
          // ~~~~ begin solution
          //
          //     **** FILL IN HERE ***
          //
          // ~~~~ end solution
          //
          // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          //                                 end part 4
          // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      }
    
      void controlLoop(const ros::TimerEvent& t){
        Eigen::Vector3d ex, ev, er, eomega;
    
        // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        //  PART 5 | Objective: Implement the controller!
        // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        //
        // 5.1 Compute position and velocity errors. Objective: fill in ex, ev.
        //  Hint: [1], eq. (6), (7)
        //
        // ~~~~ begin solution
        //
        //     **** FILL IN HERE ***
        //
        // ~~~~ end solution
    
        // 5.2 Compute the Rd matrix.
        //
        //  Hint: break it down in 3 parts:
        //    - b3d vector = z-body axis of the quadrotor, [1] eq. (12)
        //    - check out [1] fig. (3) for the remaining axes [use cross product]
        //    - assemble the Rd matrix, eigen offers: "MATRIX << col1, col2, col3"
        //
        //  CAVEATS:
        //    - Compare the reference frames in the Lab 3 handout with Fig. 1 in the
        //      paper. The z-axes are flipped, which affects the signs of:
        //         i) the gravity term and
        //        ii) the overall sign (in front of the fraction) in equation (12)
        //            of the paper
        //    - remember to normalize your axes!
        //
        // ~~~~ begin solution
        //
        //     **** FILL IN HERE ***
        //
        // ~~~~ end solution
        //
        // 5.3 Compute the orientation error (er) and the rotation-rate error (eomega)
        //  Hints:
        //     - [1] eq. (10) and (11)
        //     - you can use the Vee() static method implemented above
        //
        //  CAVEAT: feel free to ignore the second addend in eq (11), since it
        //          requires numerical differentiation of Rd and it has negligible
        //          effects on the closed-loop dynamics.
        //
        // ~~~~ begin solution
        //
        //     **** FILL IN HERE ***
        //
        // ~~~~ end solution
        //
        // 5.4 Compute the desired wrench (force + torques) to control the UAV.
        //  Hints:
        //     - [1] eq. (15), (16)
    
        // CAVEATS:
        //    - Compare the reference frames in the Lab 3 handout with Fig. 1 in the
        //      paper. The z-axes are flipped, which affects the signs of:
        //         i) the gravity term
        //        ii) the overall sign (in front of the bracket) in equation (15)
        //            of the paper
        //
        //    - feel free to ignore all the terms involving \Omega_d and its time
        //      derivative as they are of the second order and have negligible
        //      effects on the closed-loop dynamics.
        //
        // ~~~~ begin solution
        //
        //     **** FILL IN HERE ***
        //
        // ~~~~ end solution
    
        // 5.5 Recover the rotor speeds from the wrench computed above
        //
        //  Hints:
        //     - [1] eq. (1)
        //
        // CAVEATs:
        //     - we have different conventions for the arodynamic coefficients,
        //       Namely: C_{\tau f} = c_d / c_f
        //               (LHS paper [1], RHS our conventions [lecture notes])
        //
        //     - Compare the reference frames in the Lab 3 handout with Fig. 1 in the
        //       paper. In the paper [1], the x-body axis [b1] is aligned with a
        //       quadrotor arm, whereas for us, it is 45° from it (i.e., "halfway"
        //       between b1 and b2). To resolve this, check out equation 6.9 in the
        //       lecture notes!
        //
        //     - The thrust forces are **in absolute value** proportional to the
        //       square of the propeller speeds. Negative propeller speeds - although
        //       uncommon - should be a possible outcome of the controller when
        //       appropriate. Note that this is the case in unity but not in real
        //       life, where propellers are aerodynamically optimized to spin in one
        //       direction!
        //
        // ~~~~ begin solution
        //
        //     **** FILL IN HERE ***
        //
        // ~~~~ end solution
        //
        // 5.6 Populate and publish the control message
        //
        // Hint: do not forget that the propeller speeds are signed (maybe you want
        // to use signed_sqrt function).
        //
        // ~~~~ begin solution
        //
        //     **** FILL IN HERE ***
        //
        // ~~~~ end solution
        //
        // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        //           end part 5, congrats! Start tuning your gains (part 6)
        // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      }
    };
    
    int main(int argc, char** argv){
      ros::init(argc, argv, "controller_node");
      controllerNode n;
      ros::spin();
    }
    #include <ros/ros.h>
    #include <tf2_ros/transform_broadcaster.h>
    #include <tf2/LinearMath/Quaternion.h>
    #include <tf2/LinearMath/Vector3.h>
    #include <std_msgs/String.h>
    #include <trajectory_msgs/MultiDOFJointTrajectoryPoint.h>
    #include <sstream>
    #include <iostream>
    
    #include <math.h>
    
    #define STATIC_POSE 0
    
    #define PI M_PI
    
    #define TFOUTPUT 1
    int main(int argc, char **argv)
    {
        ros::init(argc, argv, "traj_publisher");
        ros::NodeHandle n;
        ros::Publisher desired_state_pub = n.advertise<trajectory_msgs::MultiDOFJointTrajectoryPoint>("desired_state", 1);
        ros::Rate loop_rate(100);
        ros::Time start(ros::Time::now());
    
    #if TFOUTPUT
        tf2_ros::TransformBroadcaster br;
    #endif
    
        int count = 0;
        while (ros::ok()) {
            tf2::Vector3 origin(0,0,0);
    
            double t = (ros::Time::now()-start).toSec();
    
            // Quantities to fill in
            geometry_msgs::TransformStamped desired_pose;
            desired_pose.header.stamp = ros::Time::now();
            desired_pose.header.frame_id = "world";
            desired_pose.child_frame_id = "av-desired";
    
            geometry_msgs::Twist velocity;
            velocity.linear.x = velocity.linear.y = velocity.linear.z = 0;
            velocity.angular.x = velocity.angular.y = velocity.angular.z = 0;
            geometry_msgs::Twist acceleration;
            acceleration.linear.x = acceleration.linear.y = acceleration.linear.z = 0;
            acceleration.angular.x = acceleration.angular.y = acceleration.angular.z = 0;
    
    #if STATIC_POSE
            // Static Pose
            tf2::Vector3 displacement(0,0,2);
            tf2::Vector3 trans = origin + displacement;
    
            desired_pose.transform.translation.x = trans.x();
            desired_pose.transform.translation.y = trans.y();
            desired_pose.transform.translation.z = trans.z();
    
            tf2::Quaternion q;
            q.setRPY(0,0,PI/4);
            count++;
            std::cout<<"Desired Orientation" << count << std::endl;
    
            desired_pose.transform.rotation.x = q.x();
            desired_pose.transform.rotation.y = q.y();
            desired_pose.transform.rotation.z = q.z();
            desired_pose.transform.rotation.w = q.w();
    #else
            // Circle
            double R = 5.0;
            double timeScale = 2.0;
            tf2::Vector3 trans = origin + tf2::Vector3(R*sin(t/timeScale), R*cos(t/timeScale), 2);
            desired_pose.transform.translation.x = trans.x();
            desired_pose.transform.translation.y = trans.y();
            desired_pose.transform.translation.z = trans.z();
    
            tf2::Quaternion q;
            q.setRPY(0,0,-t/timeScale);
            desired_pose.transform.rotation.x = q.x();
            desired_pose.transform.rotation.y = q.y();
            desired_pose.transform.rotation.z = q.z();
            desired_pose.transform.rotation.w = q.w();
            velocity.linear.x = R*cos(t/timeScale)/timeScale;
            velocity.linear.y = -R*sin(t/timeScale)/timeScale;
            velocity.linear.z = 0;
    
            velocity.angular.x = 0.0;
            velocity.angular.y = 0.0;
            velocity.angular.z = -1.0/timeScale;
    
            acceleration.linear.x = -R*sin(t/timeScale)/timeScale/timeScale;
            acceleration.linear.y = -R*cos(t/timeScale)/timeScale/timeScale;
            acceleration.linear.z = 0;
    #endif
    
            // Publish
            trajectory_msgs::MultiDOFJointTrajectoryPoint msg;
            msg.transforms.resize(1);
            msg.transforms[0] = desired_pose.transform;
            msg.velocities.resize(1);
            msg.velocities[0] = velocity;
            msg.accelerations.resize(1);
            msg.accelerations[0] = acceleration;
            desired_state_pub.publish(msg);
    
            std::stringstream ss;
            ss << "Trajectory Position"
               << " x:" << desired_pose.transform.translation.x
               << " y:" << desired_pose.transform.translation.y
               << " z:" << desired_pose.transform.translation.z;
            ROS_INFO("%s", ss.str().c_str());
    
    #if TFOUTPUT
            br.sendTransform(desired_pose);
    #endif
    
            ros::spinOnce();
    
            loop_rate.sleep();
            ++count;
        }
    
    
        return 0;
    }
    total 4552
    drwxrwxrwt 23 root   root      4096 Oct 10 10:11 .
    drwxr-xr-x 23 root   root      4096 Oct  9 15:09 ..
    drwxrwxrwt  2 root   root      4096 Oct 10  2026 .ICE-unix
    -r--r--r--  1 chixin chixin      11 Oct 10  2026 .X0-lock
    -r--r--r--  1 chixin chixin      11 Oct 10  2026 .X1-lock
    -r--r--r--  1 gdm    gdm         11 Oct 10  2026 .X1024-lock
    -r--r--r--  1 gdm    gdm         11 Oct 10  2026 .X1025-lock
    drwxrwxrwt  2 root   root      4096 Oct 10  2026 .X11-unix
    drwxrwxrwt  2 root   root      4096 Oct 10  2026 .XIM-unix
    drwxrwxrwt  2 root   root      4096 Oct 10  2026 .font-unix
    drwxrwxrwt  2 root   root      4096 Oct 10  2026 VMwareDnD
    drwxrwxr-x  2 chixin chixin    4096 Oct 10 10:13 codex-bwrap-synthetic-mount-targets-1000
    drwx------  2 root   root      4096 Oct 10 10:11 codex-daemon-0
    drwx------  2 chixin chixin    4096 Oct 10 09:15 codex-daemon-1000
    drwxrwxr-x  2 chixin chixin    4096 Oct 10 09:09 lazydocker-unpack
    -rw-rw-r--  1 chixin chixin 4548216 Oct 10 09:09 lazydocker_0.25.2_Linux_arm64.tar.gz
    drwx------  3 root   root      4096 Oct 10  2026 snap-private-tmp
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-ModemManager.service-AKxF3I
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-colord.service-9JFZGv
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-polkit.service-sxCwwp
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-power-profiles-daemon.service-Woijaq
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-switcheroo-control.service-OI0VXk
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-systemd-logind.service-aYEePF
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-systemd-oomd.service-6uygS2
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-systemd-resolved.service-SnlY6Q
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-systemd-timesyncd.service-XHv7kq
    drwx------  3 root   root      4096 Oct 10  2026 systemd-private-8e8470e077a244229880c8a3e071ebea-upower.service-CBYwLG
    drwx------  2 root   root      4096 Oct 10  2026 vmware-root_959-3979643072
    *.DS_Store
    *__pycache__*
    *.aux
    *.out
    *.bbl
    *.blg
    *.log
    *.zip
    ✓ • 0ms

## Assistant

实验包含两道个人题和一个团队控制器任务。当前 `lab3` 为空，但仓库里已有官方骨架；我会补齐答案、控制器和运行文档。环境目前装的是 ROS 2 Jazzy，我正在检查能否复用此前实验的 ROS Noetic 环境来编译和演示。

## Activity

    $ cat ../lab1/vnav-codes/lab3/controller_pkg/CMakeLists.txt ../lab1/vnav-codes/lab3/controller_pkg/package.xml ../lab1/vnav-codes/lab3/controller_pkg/launch/traj_tracking.launch; cat ../lab2/report/runtime_evidence.txt; command -v docker podman tectonic latex xelatex pandoc chromium google-chrome python3 curl; docker ps -a --format '{{.Names}}\t{{.Image}}\t{{.Status}}'; uname -m; ls /home/chixin; rg --files /home/chixin -g 'lab3.x86_64' -g '*lab3*.zip' -g 'tectonic' -g '*noetic*' -g 'AGENTS.md' 2>/dev/null | head -70
    cmake_minimum_required(VERSION 2.8.3)
    project(controller_pkg)
    
    include(CheckCXXCompilerFlag)
    
    CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
    CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
    
    if(COMPILER_SUPPORTS_CXX11)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wl,--no-as-needed")
    elseif(COMPILER_SUPPORTS_CXX0X)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
    endif()
    
    find_package(catkin REQUIRED COMPONENTS
      roscpp
      rospy
      std_msgs
      geometry_msgs
      mav_msgs
        tf
      tf2
    )
    
    catkin_package(CATKIN_DEPENDS
      roscpp
      std_msgs
      mav_msgs
      tf
      tf2
    )
    
    find_package(Eigen3)
    
    include_directories(${catkin_INCLUDE_DIRS})
    add_executable(controller_node src/controller_node.cpp)
    add_dependencies(controller_node ${catkin_EXPORTED_TARGETS})
    target_link_libraries(controller_node ${catkin_LIBRARIES})
    
    add_executable(traj_publisher src/traj_publisher.cpp)
    add_dependencies(traj_publisher ${catkin_EXPORTED_TARGETS})
    target_link_libraries(traj_publisher ${catkin_LIBRARIES})
    <?xml version="1.0"?>
    <package>
      <name>controller_pkg</name>
      <version>0.0.0</version>
      <description>The UAV controller package</description>
      <maintainer email="jnshi@mit.edu">Jingnan Shi</maintainer>
      <license>MIT</license>
      <buildtool_depend>catkin</buildtool_depend>
    
      <build_depend>roscpp</build_depend>
      <build_depend>rospy</build_depend>
      <build_depend>std_msgs</build_depend>
      <build_depend>tf</build_depend>
      <build_depend>tf2</build_depend>
      <build_depend>tf2_geometry_msgs</build_depend>
      <build_depend>tf2_eigen</build_depend>
      <build_depend>geometry_msgs</build_depend>
      <build_depend>mav_msgs</build_depend>
    
      <run_depend>roscpp</run_depend>
      <run_depend>rospy</run_depend>
      <run_depend>std_msgs</run_depend>
      <run_depend>tf</run_depend>
      <run_depend>tf2</run_depend>
      <run_depend>tf2_geometry_msgs</run_depend>
      <run_depend>tf2_eigen</run_depend>
      <run_depend>geometry_msgs</run_depend>
      <run_depend>mav_msgs</run_depend>
    
      <export>
      </export>
    </package>
    
    <launch>
      <!-- Launch desired trajectory -->
      <node name="traj_publisher" pkg="controller_pkg" type="traj_publisher"/>
    
      <!-- Launch our controller -->
      <node name="controller_node" pkg="controller_pkg" type="controller_node"/>
    
      <!-- Controller gains -->
      <param name="kx" type="double" value="1" />
      <param name="kv" type="double" value="1" />
      <param name="kr" type="double" value="1" />
      <param name="komega" type="double" value="1" />
    
    </launch>
    ===NODES===
    /frames_publisher_node
    /plots_publisher_node
    /rosout
    /rviz
    /tf_echo_1789906061900166964
    ===VISUALS===
    Type: visualization_msgs/MarkerArray
    
    Publishers:
     * /plots_publisher_node (http://chixin:42701/)
    
    Subscribers:
     * /rviz (http://chixin:42007/)
    
    
    ===TF===
    Type: tf2_msgs/TFMessage
    
    Publishers:
     * /frames_publisher_node (http://chixin:35643/)
    
    Subscribers:
     * /plots_publisher_node (http://chixin:42701/)
     * /rviz (http://chixin:42007/)
     * /tf_echo_1789906061900166964 (http://chixin:35895/)
    
    
    ===TF_STATIC===
    Type: tf2_msgs/TFMessage
    
    Publishers: None
    
    Subscribers:
     * /plots_publisher_node (http://chixin:42701/)
     * /rviz (http://chixin:42007/)
     * /tf_echo_1789906061900166964 (http://chixin:35895/)
    
    
    ===AV2_IN_AV1_SAMPLE===
    At time 1789906091.425
    - Translation: [-1.354, -0.147, 0.705]
    - Rotation: in Quaternion [0.000, 0.000, 0.196, 0.981]
                in RPY (radian) [0.000, -0.000, 0.394]
                in RPY (degree) [0.000, -0.000, 22.575]
    At time 1789906092.186
    - Translation: [-0.666, -0.128, 0.743]
    - Rotation: in Quaternion [0.000, 0.000, -0.182, 0.983]
                in RPY (radian) [0.000, 0.000, -0.366]
                in RPY (degree) [0.000, 0.000, -20.989]
    At time 1789906093.186
    - Translation: [-0.801, -0.959, -0.918]
    - Rotation: in Quaternion [0.000, 0.000, -0.631, 0.776]
                in RPY (radian) [0.000, 0.000, -1.366]
                in RPY (degree) [0.000, 0.000, -78.289]
    /usr/bin/docker
    /usr/bin/python3
    /usr/bin/curl
    permission denied while trying to connect to the docker API at unix:///var/run/docker.sock
    aarch64
    Desktop
    Documents
    Downloads
    Lab2
    Music
    Pictures
    Public
    Templates
    Videos
    f29xs
    fanhao
    snap
    ✓ • 0ms

## Activity

    Opened https://raw.githubusercontent.com/ros/geometry2/noetic-devel/tf2_eigen/include/tf2_eigen/tf2_eigen.h

## Activity

    $ curl -fL https://vnav.mit.edu/assets/images/lab3/drone_spinning.png -o /tmp/lab3_drone_spinning.png; curl -fL https://vnav.mit.edu/assets/images/lab3/sim_convention.png -o /tmp/lab3_sim_convention.png
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    
    ✓ • 11.17s

## Activity

    Viewed image /tmp/lab3_drone_spinning.png

## Activity

    $ sudo -n docker ps -a --format '{{.Names}}\t{{.Image}}\t{{.Status}}'; ls -la /home/chixin/Lab2; rg --files /home/chixin/Lab2 -g 'AGENTS.md' -g '*setup*' -g '*docker*' -g '*tex' -g '*noetic*' | head -50; python3 -c 'import importlib.util; print({m: bool(importlib.util.find_spec(m)) for m in ["numpy", "scipy", "matplotlib", "reportlab", "imageio", "PIL"]})'; ls /usr/bin/*latex* /usr/bin/*ffmpeg* /usr/bin/*rviz* 2>/dev/null; env | rg 'DISPLAY|PROXY|ROS'
    sudo: a password is required
    total 44
    drwxr-xr-x  7 chixin chixin 4096 Sep 20 20:07 .
    drwxr-x--- 23 chixin chixin 4096 Oct 10 10:11 ..
    drwxr-xr-x  3 root   root   4096 Sep 20 19:57 .catkin_tools
    drwxr-xr-x  4 root   root   4096 Sep 20 19:57 build
    drwxr-xr-x  5 root   root   4096 Sep 20 19:57 devel
    -rw-r--r--  1 root   root   1444 Sep 20 20:09 dynamic.log
    drwxr-xr-x  4 root   root   4096 Sep 20 19:57 logs
    -rw-r--r--  1 root   root   1409 Sep 20 20:08 runtime_evidence.txt
    drwxrwxr-x  3 chixin chixin 4096 Sep 20 19:57 src
    -rw-r--r--  1 root   root   1570 Sep 20 20:02 static.log
    -rw-rw-r--  1 chixin chixin  669 Sep 20 20:07 tf_sample.txt
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/generate_cached_setup.py
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/local_setup.zsh
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/local_setup.bash
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/setup.sh
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/local_setup.sh
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/local_setup.fish
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/setup.fish
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/_setup_util.py
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/setup.bash
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/installspace/setup.zsh
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/setup_cached.sh
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/stamps/two_drones_pkg/_setup_util.py.stamp
    /home/chixin/Lab2/build/two_drones_pkg/catkin_generated/stamps/two_drones_pkg/interrogate_setup_dot_py.py.stamp
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/local_setup.bash.EH74Y
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/setup.fish.Mk31j
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/local_setup.sh.QGx2l
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/setup.sh.tSqOi
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/local_setup.zsh.MH0XJ
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/setup.zsh.pZIal
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/setup.bash.Ude96
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/local_setup.fish.0x6Bg
    /home/chixin/Lab2/build/two_drones_pkg/atomic_configure/_setup_util.py.1gwPk
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/generate_cached_setup.py
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/local_setup.zsh
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/local_setup.bash
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/setup.sh
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/local_setup.sh
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/local_setup.fish
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/setup.fish
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/_setup_util.py
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/setup.bash
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/installspace/setup.zsh
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/setup_cached.sh
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/stamps/catkin_tools_prebuild/_setup_util.py.stamp
    /home/chixin/Lab2/build/catkin_tools_prebuild/catkin_generated/stamps/catkin_tools_prebuild/interrogate_setup_dot_py.py.stamp
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/setup.bash.JFMR8
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/setup.fish.HrZYU
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/local_setup.zsh.qc1vu
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/setup.zsh.qm9Ff
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/_setup_util.py.ITFNw
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/local_setup.bash.GelfL
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/local_setup.fish.LpPqb
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/local_setup.sh.uKp2T
    /home/chixin/Lab2/build/catkin_tools_prebuild/atomic_configure/setup.sh.mk6hP
    {'numpy': True, 'scipy': True, 'matplotlib': False, 'reportlab': False, 'imageio': False, 'PIL': True}
    /usr/bin/rst2latex
    ROS_VERSION=2
    ROS_PYTHON_VERSION=3
    ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET
    NO_PROXY=localhost,127.0.0.1,::1
    HTTPS_PROXY=http://192.168.103.1:7897
    HTTP_PROXY=http://192.168.103.1:7897
    ALL_PROXY=http://192.168.103.1:7897
    ROS_DISTRO=jazzy
    ✓ • 0ms

## Assistant

本机是 ARM64，当前只有 ROS 2 Jazzy；题目需要 ROS Noetic 和 TESSE。你是否有可用的 Noetic 环境、TESSE 模拟器路径，或现成的飞行视频公开链接？有的话请提供路径或链接；我会继续完成代码和书面交付。

## Activity

    Viewed image /tmp/lab3_sim_convention.png

## Activity

    $ rg -n 'angular|linear|twist|frame' ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.py | tail -35; cat ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/quadrotor_control_interface.py; cat ../lab1/vnav-codes/README.md; ls -l /var/run/docker.sock; id
    614:            world frame and the ENU right-handed frame is included.
    618:    # Calculate position and orientation in the right-hand body frame from enu.
    662:    ref_linear_velocity = [metadata['velocity'][0],
    665:    ref_angular_velocity = [-metadata['ang_vel'][0],
    671:    quadrotor_dict['velocity'] = ref_linear_velocity
    672:    quadrotor_dict['ang_vel'] = ref_angular_velocity
    683:        frame to a right-handed frame.
    686:        the right handed frame. These remain in a global reference frame,
    695:            from the ENU world frame to the right-handed body frame of the
    702:    # Convert the left-handed Unity frame to the right-handed ENU frame.
    712:    """ Get velocity in the body right-handed frame from raw metadata.
    714:        Metadata comes in as left-handed body-frame data, so we premultiply
    715:        by the transformation from left-handed to right-handed frames.
    722:            A 1x3 numpy array containing linear velocity of the agent
    723:            in the body-right-handed frame as [vx,vy,vz].
    729:    """ Get angular velocity in the body right-handed frame from raw metadata.
    731:        Metadata comes in as left-handed body-frame data, so we premultiply
    732:        by the transformation from left-handed to right-handed frames.
    739:            A 1x3 numpy array containing angular velocity of the agent
    740:            in the body-right-handed frame as [wx,wy,wz].
    745:    # body frame works. The above line *should* be right but isn't.
    757:    """ Get angular velocity in the body right-handed frame from current and
    762:        the ENU global frame.
    766:                from the body (right-handed) frame to the ENU frame.
    768:                matrix from the body (righ-handed) frame to the ENU frame.
    770:                frame and the current frame.
    773:            A 1x3 numpy array containing angular velocity of the agent in the
    787:    """ Get linear acceleration in the body right-handed frame via a finite
    790:        Velocities in the ENU frame are used for the finite difference as
    792:        difference between body frames at two timestamps.
    797:            vel_brh: A 1x3 numpy array containing linear velocity in the
    798:                body-right-handed frame at the current time.
    799:            prev_vel_brh: A 1x3 numpy array containing linear velocity in the
    800:                body-right-handed frame at the previous time.
    807:            A 1x3 numpy array containing the linear accelerations of the agent
    #!/usr/bin/env python
    
    import numpy as np
    import copy
    
    import rospy
    import tf
    import tf2_ros
    from std_msgs.msg import Header, String
    from sensor_msgs.msg import Image as ImageMsg
    from sensor_msgs.msg import Imu, CameraInfo
    from sensor_msgs.msg import LaserScan
    from nav_msgs.msg import Odometry
    from mav_msgs.msg import Actuators
    from geometry_msgs.msg import (
        Pose,
        PoseStamped,
        Point,
        PointStamped,
        TransformStamped,
        Quaternion,
        Twist,
        PoseWithCovarianceStamped,
        Vector3Stamped,
    )
    from ackermann_msgs.msg import AckermannDriveStamped
    from rosgraph_msgs.msg import Clock
    from cv_bridge import CvBridge, CvBridgeError
    
    import tesse_ros_bridge.utils
    from tesse_ros_bridge.noise_simulator import NoiseParams, NoiseSimulator
    
    from tesse_ros_bridge.srv import (
        SceneRequestService,
        ObjectSpawnRequestService,
        RepositionRequestService,
    )
    from tesse_ros_bridge.msg import CollisionStats
    from tesse_ros_bridge import brh_T_blh
    
    from tesse.msgs import *
    from tesse.env import *
    from tesse.utils import *
    
    
    class TesseQuadrotorControlInterface:
        def __init__(self):
            """This class provides a ROS interface for controlling TESSE quadrotor agents.
            ROS users can simply send propeller speeds command to predefined propeller speeds
            topic, and this interface will transmit the appropriate messages to TESSE simulator.
    
            Quadrotor agent is controlled by setting the speed of each propeller. The speeds are radians per second.
            """
            # Networking parameters
            self.sim_ip = rospy.get_param("~sim_ip", "127.0.0.1")
            self.self_ip = rospy.get_param("~self_ip", "127.0.0.1")
            self.use_broadcast = rospy.get_param("~use_broadcast", False)
            self.position_port = rospy.get_param("~position_port", 9000)
            self.metadata_port = rospy.get_param("~metadata_port", 9001)
            self.image_port = rospy.get_param("~image_port", 9002)
            self.udp_port = rospy.get_param("~udp_port", 9004)
            self.step_port = rospy.get_param("~step_port", 9005)
            self.scan_port = rospy.get_param("~lidar_port", 9006)
            self.scan_udp_port = rospy.get_param("~lidar_udp_port", 9007)
    
            # Topics
            self.props_speeds_topic = "quadrotor_control/rotor_speed_cmds"
    
            # Initialize the Env object to communicate with simulator
            self.env = Env(
                simulation_ip=self.sim_ip,
                own_ip=self.self_ip,
                position_port=self.position_port,
                metadata_port=self.metadata_port,
                image_port=self.image_port,
                step_port=self.step_port,
            )
    
            # setup control interface subscriber
            self.props_speeds_sub = rospy.Subscriber(
                self.props_speeds_topic, Actuators, self.props_control_cb
            )
    
        def props_control_cb(self, msg):
            """Callback function used for propeller speed control
    
            :param msg: A mav_msgs.msg.Actuators message. The field angular_velocities is used for setting the propeller speeds.
            """
            # read prop speeds
            speeds = msg.angular_velocities
            self.env.send(PropSpeeds(speeds[0], speeds[1], speeds[2], speeds[3]))
    
    
    if __name__ == "__main__":
        rospy.init_node("TesseQuadrotorControlInterface_node")
        node = TesseQuadrotorControlInterface()
        rospy.spin()
    # vnav-codes
    
    
    
    
    
    
    
    reference github repo: https://github.com/MIT-SPARK/VNAV-labs
    srw-rw---- 1 root docker 0 Oct 10  2026 /var/run/docker.sock
    uid=1000(chixin) gid=1000(chixin) groups=1000(chixin),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),114(lpadmin),123(lxd)
    ✓ • 0ms

## User

> 本机是 ARM64，当前只有 ROS 2 Jazzy；题目需要 ROS Noetic 和 TESSE。你是否有可用的 Noetic 环境、TESSE 模拟器路径，或现成的飞行视频公开链接？有的话请提供路径或链接；我会继续完成代码和书面交付。

我有docker

## Assistant

我已确认 Docker 存在，但当前用户没有访问 Docker socket 的权限，`sudo` 也需要密码。控制器还需要注意官方示意图中的电机编号、偏航力矩符号，以及世界坐标系到机体坐标系的角速度转换，我会按这些约定实现。

## Assistant

请在你自己的终端执行 `sudo setfacl -m u:chixin:rw /var/run/docker.sock`，执行成功后回复“好了”。这样我就能使用已有 Docker 环境编译和运行实验；当前阻碍来自系统文件权限。

## Activity

    $ mkdir -p controller_pkg/include/controller_pkg controller_pkg/src controller_pkg/launch controller_pkg/config controller_pkg/rviz report scripts; cp ../lab1/vnav-codes/lab3/controller_pkg/rviz/lab3.rviz controller_pkg/rviz/lab3.rviz; cat ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/launch/tesse_quadrotor_bridge.launch; rg -n 'Topic:|Value:|Frame:|Class:' controller_pkg/rviz/lab3.rviz | head -60; sed -n '640,677p' ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.py
    <!--
         Use RVIZ for visualization.
    -->
    <launch>
      <arg name="ns"                   default="tesse"/>
      <arg name="teleop"               default="false"/>
      <arg name="drive_with_ackermann" default="false"/>
      <arg name="params_dir"           default="$(find tesse_ros_bridge)/params"/>
      <arg name="use_gt_frames"        default="true"/>
      <arg name="enable_step_mode"     default="false"/>
    
      <!-- Network arguments -->
      <arg name="sim_ip"                default="127.0.0.1"/>
      <arg name="self_ip"               default="127.0.0.1"/>
      <arg name="use_broadcast"         default="true"/>
    
      <!-- Specify data to publish -->
      <!-- `publish_stereo_gry` toggles between publishing as mono8 (true) or rgb8 (false) \
            for both left/right stereo cameras -->
      <arg name="publish_clock"             default="true"/>
      <arg name="publish_metadata"          default="false"/>
      <arg name="publish_collisions"        default="false"/>
    
      <arg name="publish_imu"               default="true"/>
      <arg name="publish_odom"              default="true"/>
      <arg name="publish_noisy_imu"         default="false"/>
      <arg name="publish_imu_noise_biases"  default="false"/>
      <arg name="publish_noisy_odom"        default="false"/>
    
      <arg name="publish_stereo_rgb"        default="false"/>
      <arg name="publish_stereo_gry"        default="false"/>
      <arg name="publish_segmentation"      default="false"/>
      <arg name="publish_depth"             default="false"/>
      <arg name="publish_third_pov"         default="false"/>
    
      <arg name="publish_front_lidar"       default="false"/>
      <arg name="publish_rear_lidar"        default="false"/>
    
      <!-- Sanity check argument -->
      <arg name="stereo_baseline"      default="0.10"/>
    
      <!-- Sim arguments -->
      <!-- NOTE: `use_sim_time` should always be true for tesse! -->
      <arg name="use_sim_time"          default="true"/>
      <arg name="frame_rate"            default="20.0"/>
      <arg name="imu_rate"              default="200"/>
      <arg name="scan_rate"             default="40.0"/>
      <arg name="enable_collision"      default="true"/>
      <arg name="initial_scene"         default="1"/>
    
      <!-- Reference frame arguments -->
      <arg name="world_frame_id"        default="world"/>
      <arg name="map_frame_id"          default="map"/>
      <arg name="body_frame_id"         default="base_link"/>
      <arg name="body_frame_id_gt"      default="base_link_gt"/>
    
      <!-- If use_sim, simulator will publish -->
      <param name="/use_sim_time" value="$(arg use_sim_time)"/>
    
      <!-- Map servers -->
      <!-- <include file="$(find tesse_ros_bridge)/launch/maps.launch"/> -->
    
      <!-- Launch tesse ROS Bridge Node -->
      <node ns="$(arg ns)" name="tesse_ros_bridge" pkg="tesse_ros_bridge"
            type="tesse_ros_node.py" output="screen">
        <!-- Topics -->
        <remap from="imu/clean/imu"          to="imu/clean/imu"/>
        <remap from="imu/noisy/imu"          to="imu/noisy/imu"/>
        <remap from="imu/noisy/biases/gyro"  to="imu/noisy/biases/gyro"/>
        <remap from="imu/noisy/biases/accel" to="imu/noisy/biases/accel"/>
        <remap from="odom"                   to="/current_state"/>
    
        <remap from="left_cam/rgb/image_raw"   to="left_cam/rgb/image_raw"/>
        <remap from="left_cam/mono/image_raw"  to="left_cam/mono/image_raw"/>
        <remap from="right_cam/image_raw"      to="right_cam/image_raw"/>
        <remap from="seg_cam/rgb/image_raw"    to="seg_cam/rgb/image_raw"/>
        <remap from="depth_cam/mono/image_raw" to="depth_cam/mono/image_raw"/>
    
        <remap from="left_cam/camera_info"  to="left_cam/camera_info"/>
        <remap from="right_cam/camera_info" to="right_cam/camera_info"/>
        <remap from="seg_cam/camera_info"   to="seg_cam/camera_info"/>
        <remap from="depth_cam/camera_info" to="depth_cam/camera_info"/>
    
        <remap from="lidar/front_lidar/scan" to="lidar/front_lidar/scan"/>
        <remap from="lidar/rear_lidar/scan"  to="lidar/rear_lidar/scan"/>
    
        <!-- Interfacing params -->
        <param name="teleop"                value="$(arg teleop)"/>
        <param name="drive_with_ackermann"  value="$(arg drive_with_ackermann)"/>
        <param name="use_gt_frames"         value="$(arg use_gt_frames)"/>
        <param name="enable_step_mode"      value="$(arg enable_step_mode)"/>
    
        <!-- Network Unity params -->
        <param name="sim_ip"           value="$(arg sim_ip)"/>
        <param name="self_ip"          value="$(arg self_ip)"/>
        <param name="use_broadcast"    value="$(arg use_broadcast)"/>
        <param name="position_port"    value="9000"/>
        <param name="metadata_port"    value="9001"/>
        <param name="image_port"       value="9002"/>
        <param name="udp_port"         value="9004"/>
        <param name="step_port"        value="9005"/>
        <param name="lidar_port"       value="9006"/>
        <param name="lidar_udp_port"   value="9007"/>
    
        <!-- Data to publish -->
        <param name="publish_clock"            value="$(arg publish_clock)"/>
        <param name="publish_metadata"         value="$(arg publish_metadata)"/>
        <param name="publish_collisions"       value="$(arg publish_collisions)"/>
        <param name="publish_imu"              value="$(arg publish_imu)"/>
        <param name="publish_odom"             value="$(arg publish_odom)"/>
        <param name="publish_noisy_imu"        value="$(arg publish_noisy_imu)"/>
        <param name="publish_imu_noise_biases" value="$(arg publish_imu_noise_biases)"/>
        <param name="publish_noisy_odom"       value="$(arg publish_noisy_odom)"/>
        <param name="publish_stereo_rgb"       value="$(arg publish_stereo_rgb)"/>
        <param name="publish_stereo_gry"       value="$(arg publish_stereo_gry)"/>
        <param name="publish_segmentation"     value="$(arg publish_segmentation)"/>
        <param name="publish_depth"            value="$(arg publish_depth)"/>
        <param name="publish_third_pov"        value="$(arg publish_third_pov)"/>
        <param name="publish_front_lidar"      value="$(arg publish_front_lidar)"/>
        <param name="publish_rear_lidar"       value="$(arg publish_rear_lidar)"/>
    
        <!-- Simulator and rate parameters -->
        <param name="frame_rate"        value="$(arg frame_rate)"/>
        <param name="imu_rate"          value="$(arg imu_rate)"/>
        <param name="scan_rate"         value="$(arg scan_rate)"/>
        <param name="enable_collision"  value="$(arg enable_collision)"/>
        <param name="initial_scene"     value="$(arg initial_scene)"/>
    
        <!-- Frame parameters -->
        <param name="world_frame_id"       value="$(arg world_frame_id)"/>
        <param name="map_frame_id"         value="$(arg map_frame_id)"/>
        <param name="body_frame_id"        value="$(arg body_frame_id)"/>
        <param name="body_frame_id_gt"     value="$(arg body_frame_id_gt)"/>
    
        <!-- Load all parameter files -->
        <rosparam command="load" file="$(arg params_dir)/camera_params.yaml"/>
        <rosparam command="load" file="$(arg params_dir)/lidar_params.yaml"/>
        <rosparam command="load" file="$(arg params_dir)/noise_model.yaml"/>
        <rosparam command="load" file="$(arg params_dir)/tesse_agent_params.yaml"/>
        <rosparam command="load" file="$(arg params_dir)/object_spawn_params.yaml"/>
        <!-- <rosparam command="load" file="$(arg params_dir)/map_tfs.yaml"/> -->
      </node>
    
      <!-- Launch tesse ROS quadrotor control interface -->
      <node ns="$(arg ns)" name="quadrotor_control_interface" pkg="tesse_ros_bridge"
            type="quadrotor_control_interface.py" output="screen">
        <!-- Topics -->
        <remap from="quadrotor_control/rotor_speed_cmds"  to="/rotor_speed_cmds"/>
      </node>
    
    </launch>
    2:  - Class: rviz/Displays
    11:  - Class: rviz/Selection
    13:  - Class: rviz/Tool Properties
    20:  - Class: rviz/Views
    25:  - Class: rviz/Time
    35:  Class: ""
    39:      Class: rviz/Grid
    44:        Value: Lines
    53:      Reference Frame: <Fixed Frame>
    54:      Value: true
    55:    - Class: rviz/TF
    61:          Value: true
    63:          Value: true
    65:          Value: true
    78:      Value: true
    80:      Class: rviz_plugin_tutorials/Imu
    85:      Topic: /tesse/imu/clean/imu
    87:      Value: true
    89:      Class: rviz/Odometry
    95:          Frame: Local
    98:          Value: true
    103:          Value: true
    104:        Value: true
    118:        Value: Axes
    119:      Topic: /current_state
    121:      Value: true
    125:        Max Value: 10
    126:        Min Value: -10
    127:        Value: true
    130:      Class: rviz/LaserScan
    147:      Topic: /tesse/front_lidar/scan
    149:      Use Fixed Frame: true
    151:      Value: true
    155:        Max Value: 10
    156:        Min Value: -10
    157:        Value: true
    160:      Class: rviz/LaserScan
    177:      Topic: /tesse/rear_lidar/scan
    179:      Use Fixed Frame: true
    181:      Value: true
    183:      Class: rviz_plugin_tutorials/Imu
    188:      Topic: /tesse/imu/noisy/imu
    190:      Value: true
    195:    Fixed Frame: world
    199:    - Class: rviz/Interact
    201:    - Class: rviz/MoveCamera
    202:    - Class: rviz/Select
    203:    - Class: rviz/FocusCamera
    204:    - Class: rviz/Measure
    205:    - Class: rviz/SetInitialPose
    207:      Topic: /initialpose
    210:    - Class: rviz/SetGoal
    211:      Topic: /move_base_simple/goal
    212:    - Class: rviz/PublishPoint
    214:      Topic: /clicked_point
    215:  Value: true
    218:      Class: rviz/Orbit
    224:        Value: false
    235:      Target Frame: base_link_gt
    236:      Value: Orbit (rviz)
        processed_dict['velocity'] = vel_brh
        processed_dict['ang_vel'] = ang_vel_brh
        processed_dict['acceleration'] = acc_brh
        # processed_dict['ang_accel'] = ang_acc_brh
        processed_dict['time'] = metadata['time']
        processed_dict['collision_status'] = metadata['collision_status']
        processed_dict['collision_object'] = metadata['collision_object']
        processed_dict['transform'] = enu_T_brh
    
        # Temporary checks for quadrotor
        # position is consistent
        ref_position = [metadata['position'][0],
                        metadata['position'][2],
                        metadata['position'][1]]
        ref_orientation = [-metadata['quaternion'][0],
                           -metadata['quaternion'][2],
                           -metadata['quaternion'][1],
                           metadata['quaternion'][3]]
        #ref_orientation = [metadata['quaternion'][0],
        #                   metadata['quaternion'][1],
        #                   metadata['quaternion'][2],
        #                   metadata['quaternion'][3]]
        ref_linear_velocity = [metadata['velocity'][0],
                               metadata['velocity'][2],
                               metadata['velocity'][1]]
        ref_angular_velocity = [-metadata['ang_vel'][0],
                                -metadata['ang_vel'][2],
                                -metadata['ang_vel'][1]]
        quadrotor_dict = copy.deepcopy(processed_dict)
        quadrotor_dict['position'] = ref_position
        quadrotor_dict['quaternion'] = ref_orientation
        quadrotor_dict['velocity'] = ref_linear_velocity
        quadrotor_dict['ang_vel'] = ref_angular_velocity
    
        ref_transform = tf.transformations.quaternion_matrix(ref_orientation)
        ref_transform[:,3] = np.array(ref_position + [1])
        quadrotor_dict['transform'] = ref_transform
    
    ✓ • 0ms

## User

> 请在你自己的终端执行 `sudo setfacl -m u:chixin:rw /var/run/docker.sock`，执行成功后回复“好了”。这样我就能使用已有 Docker 环境编译和运行实验；当前阻碍来自系统文件权限。

sudo 密码是 asdfghjkl;'

## Activity

    $ stty -echo; sudo -S -p '' setfacl -m u:chixin:rw /var/run/docker.sock
    
    ✓ • 6.38s

## Activity

    $ docker ps -a --format '{{.Names}}\t{{.Image}}\t{{.Status}}'; docker images --format '{{.Repository}}:{{.Tag}}\t{{.Size}}'; ls -la /home/chixin/Downloads /home/chixin/Videos; rg -n 'image:|noetic|docker' ../lab0 ../lab1/README.md 2>/dev/null | head -30
    ros_noetic_lab2    ros_noetic_lab2_ready:local    Up 53 minutes
    ros_noetic_lab2_old    ros:noetic-ros-base-focal    Exited (137) 23 hours ago
    ros_noetic_lab2_ready:local    3.65GB
    ros:noetic-ros-base-focal    2.87GB
    /home/chixin/Downloads:
    total 8
    drwxr-xr-x  2 chixin chixin 4096 Sep 15 10:03 .
    drwxr-x--- 23 chixin chixin 4096 Oct 10 10:11 ..
    
    /home/chixin/Videos:
    total 8
    drwxr-xr-x  2 chixin chixin 4096 Sep 15 10:03 .
    drwxr-x--- 23 chixin chixin 4096 Oct 10 10:11 ..
    ../lab0/2/task2/src/stereo_depth.py:127:def _save_image(cv2: Any, path: Path, image: Any) -> None:
    ../lab0/1/task2/report/build/compact.txt:930:that really have one value per image: reprojection RMS, rotation and translation vectors, detected-corner
    ../lab0/1/task2/report/sections/analysis.tex:7:The camera matrix \(\mathbf K\) and distortion vector \(\mathbf d\) are fitted jointly from all valid views, so this experiment produces one global estimate of \(f_x,f_y,c_x,c_y\) and \((k_1,k_2,p_1,p_2,k_3)\). It would be methodologically incorrect to draw 18 apparent intrinsic-parameter trajectories by copying the same global values or by fitting a single planar view independently without reporting a separate uncertainty protocol. The additional figures therefore use quantities that really have one value per image: reprojection RMS, rotation and translation vectors, detected-corner locations, and the response of the fitted distortion model over normalized radius. This gives more diagnostic information without fabricating parameter fluctuations.
    ../lab0/1/task2/report/figures/generate_analysis_plots.py:204:            raise RuntimeError(f"Cannot read calibration image: {image_path}")
    ✓ • 57ms

## Activity

    $ docker inspect ros_noetic_lab2 --format '{{json .Mounts}}'; docker exec ros_noetic_lab2 bash -lc 'command -v catkin pdflatex xelatex ffmpeg Xvfb rviz; ls /opt/ros; ls /root; python3 -c "import importlib.util; print({m: bool(importlib.util.find_spec(m)) for m in [\"numpy\", \"scipy\", \"matplotlib\", \"reportlab\"]})"; rospack find mav_msgs; rospack find tf2_eigen'
    [{"Type":"bind","Source":"/tmp/.X11-unix","Destination":"/tmp/.X11-unix","Mode":"rw","RW":true,"Propagation":"rprivate"},{"Type":"bind","Source":"/home/chixin/f29xs/2026Fall_TeamFullcans","Destination":"/workspace/2026Fall_TeamFullcans","Mode":"rw","RW":true,"Propagation":"rprivate"}]
    /usr/bin/catkin
    noetic
    vnav_ws
    {'numpy': True, 'scipy': False, 'matplotlib': False, 'reportlab': False}
    bash: rospack: command not found
    bash: rospack: command not found
    ✗ (127) • 0ms

## Activity

    Searched the web

## Assistant

Docker 权限已打通，也找到了现成的 ROS Noetic 容器。接下来会在容器中编译控制器，并检查闭环轨迹跟踪效果；书面题会同时生成 LaTeX 源文件和 PDF。

## Activity

    file changes: Completed · 9 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/.gitignore
    .venv/
    build/
    devel/
    logs/
    report/*.aux
    report/*.log
    report/*.out
    report/*.toc
    *.bag
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/CMakeLists.txt
    cmake_minimum_required(VERSION 3.0.2)
    project(controller_pkg)
    add_compile_options(-std=c++11 -Wall -Wextra)
    
    find_package(catkin REQUIRED COMPONENTS
      roscpp geometry_msgs nav_msgs trajectory_msgs mav_msgs
      tf2 tf2_ros tf2_geometry_msgs tf2_eigen)
    find_package(Eigen3 REQUIRED)
    
    catkin_package(INCLUDE_DIRS include CATKIN_DEPENDS
      roscpp geometry_msgs nav_msgs trajectory_msgs mav_msgs
      tf2 tf2_ros tf2_geometry_msgs tf2_eigen DEPENDS EIGEN3)
    include_directories(include ${catkin_INCLUDE_DIRS} ${EIGEN3_INCLUDE_DIRS})
    
    foreach(node controller_node traj_publisher)
      add_executable(${node} src/${node}.cpp)
      add_dependencies(${node} ${catkin_EXPORTED_TARGETS})
      target_link_libraries(${node} ${catkin_LIBRARIES})
    endforeach()
    
    install(TARGETS controller_node traj_publisher
      RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
    install(DIRECTORY include/${PROJECT_NAME}/ DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
    install(DIRECTORY launch config rviz DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/config/gains.yaml
    # Initial gains for the official m=1 kg, J=I, reversible-rotor simulator.
    # kx: N/m; kv: N*s/m; kr: N*m; komega: N*m*s.
    kx: 6.0
    kv: 4.7
    kr: 64.0
    komega: 16.0
    hz: 1000.0
    state_timeout: 0.5
    desired_timeout: 0.5
    # Deliverable 2's drag is hypothetical; enable only for matching plant drag.
    compensate_drag: false
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/include/controller_pkg/geometric_controller.h
    #pragma once
    
    #include <Eigen/Dense>
    #include <cmath>
    
    namespace controller_pkg {
    
    struct State {
      Eigen::Vector3d x = Eigen::Vector3d::Zero();
      Eigen::Vector3d v = Eigen::Vector3d::Zero();
      Eigen::Matrix3d R = Eigen::Matrix3d::Identity();  // body -> world
      Eigen::Vector3d omega = Eigen::Vector3d::Zero();  // body frame
    };
    
    struct Reference {
      Eigen::Vector3d x = Eigen::Vector3d::Zero();
      Eigen::Vector3d v = Eigen::Vector3d::Zero();
      Eigen::Vector3d a = Eigen::Vector3d::Zero();
      double yaw = 0.0;
    };
    
    struct Gains {
      double kx = 6.0;
      double kv = 4.7;
      double kr = 64.0;
      double komega = 16.0;
    };
    
    struct Command {
      Eigen::Matrix3d Rd;
      Eigen::Vector4d wrench;  // thrust, body Mx, My, Mz
      Eigen::Vector4d rotor_speeds;  // signed rad/s, rotor order 1,2,3,4
    };
    
    // Lab 3 simulator constants; do not substitute real drone coefficients.
    class GeometricController {
     public:
      Gains gains;
      bool compensate_drag = false;
      const double m = 1.0, g = 9.81, d = 0.3, cf = 1e-3, cd = 1e-5;
      const Eigen::Matrix3d J = Eigen::Matrix3d::Identity();
    
      GeometricController() {
        // rho1=(+a,+a,0), rho2=(-a,+a,0), rho3=(-a,-a,0), rho4=(+a,-a,0).
        // rho x (0,0,cf*s): Mx=y*cf*s, My=-x*cf*s.
        // TESSE yaw signs: +,-,+,-. s_i = omega_i*abs(omega_i).
        const double a = d / std::sqrt(2.0);
        allocation_ << cf, cf, cf, cf,
                       a*cf, a*cf, -a*cf, -a*cf,
                       -a*cf, a*cf, a*cf, -a*cf,
                       cd, -cd, cd, -cd;
        F2W_ = allocation_.inverse();
      }
    
      const Eigen::Matrix4d& allocation() const { return allocation_; }
    
      static Eigen::Vector3d vee(const Eigen::Matrix3d& S) {
        return Eigen::Vector3d(S(2,1), S(0,2), S(1,0));
      }
    
      static Eigen::Vector3d dragWorld(const State& state) {
        const Eigen::Vector3d vb = state.R.transpose() * state.v;
        const Eigen::Vector3d drag_b =
            -Eigen::Vector3d(0.1, 0.1, 0.2).cwiseProduct(vb.cwiseProduct(vb.cwiseAbs()));
        return state.R * drag_b;
      }
    
      Command compute(const State& state, const Reference& ref) const {
        Command cmd;
        // Part 5.1: equations (6),(7).
        const Eigen::Vector3d ex = state.x - ref.x;
        const Eigen::Vector3d ev = state.v - ref.v;
        const Eigen::Vector3d e3 = Eigen::Vector3d::UnitZ();
    
        // Part 5.2: ROS uses upward z and +f*R*e3 thrust, unlike the paper.
        Eigen::Vector3d A = -gains.kx*ex - gains.kv*ev + m*g*e3 + m*ref.a;
        if (compensate_drag) A -= dragWorld(state);
        // With zero requested force the thrust direction is undetermined.
        const Eigen::Vector3d b3d = A.norm() > 1e-9 ? A.normalized() : e3;
        Eigen::Vector3d b1c(std::cos(ref.yaw), std::sin(ref.yaw), 0.0);
        Eigen::Vector3d b2d = b3d.cross(b1c);
        if (b2d.norm() < 1e-9) {
          // Pick a perpendicular heading if the requested heading is parallel to thrust.
          b1c = b3d.unitOrthogonal();
          b2d = b3d.cross(b1c);
        }
        b2d.normalize();
        cmd.Rd.col(0) = b2d.cross(b3d);
        cmd.Rd.col(1) = b2d;
        cmd.Rd.col(2) = b3d;
    
        // Part 5.3: the handout permits Omega_d=0 and dot(Omega_d)=0.
        const Eigen::Vector3d er =
            0.5 * vee(cmd.Rd.transpose()*state.R - state.R.transpose()*cmd.Rd);
        const Eigen::Vector3d eomega = state.omega;
    
        // Part 5.4: equations (15),(16), adapted to upward z.
        cmd.wrench(0) = A.dot(state.R.col(2));
        cmd.wrench.tail<3>() = -gains.kr*er - gains.komega*eomega
                              + state.omega.cross(J*state.omega);
    
        // Parts 5.5,5.6: invert the wrench map and preserve reversible rotor signs.
        const Eigen::Vector4d signed_squared_speeds = F2W_ * cmd.wrench;
        for (int i = 0; i < 4; ++i) {
          const double s = signed_squared_speeds(i);
          cmd.rotor_speeds(i) = std::copysign(std::sqrt(std::abs(s)), s);
        }
        return cmd;
      }
    
     private:
      Eigen::Matrix4d allocation_, F2W_;
    };
    }  // namespace controller_pkg
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/launch/traj_tracking.launch
    <launch>
      <arg name="static_pose" default="false"/>
      <arg name="rviz" default="false"/>
      <arg name="gains_file" default="$(find controller_pkg)/config/gains.yaml"/>
      <node name="traj_publisher" pkg="controller_pkg" type="traj_publisher" output="screen">
        <param name="static_pose" value="$(arg static_pose)"/>
      </node>
      <node name="controller_node" pkg="controller_pkg" type="controller_node" output="screen">
        <rosparam command="load" file="$(arg gains_file)"/>
      </node>
      <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz"
            args="-d $(find controller_pkg)/rviz/lab3.rviz"/>
    </launch>
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/package.xml
    <?xml version="1.0"?>
    <package format="2">
      <name>controller_pkg</name>
      <version>1.0.0</version>
      <description>VNAV Lab 3 geometric SE(3) quadrotor controller for TESSE.</description>
      <maintainer email="teamfullcans@example.com">Team Fullcans</maintainer>
      <license>MIT</license>
      <buildtool_depend>catkin</buildtool_depend>
      <depend>roscpp</depend>
      <depend>geometry_msgs</depend>
      <depend>nav_msgs</depend>
      <depend>trajectory_msgs</depend>
      <depend>mav_msgs</depend>
      <depend>tf2</depend>
      <depend>tf2_ros</depend>
      <depend>tf2_geometry_msgs</depend>
      <depend>tf2_eigen</depend>
      <depend>eigen</depend>
      <exec_depend>rviz</exec_depend>
    </package>
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/src/controller_node.cpp
    #include <ros/ros.h>
    #include <mav_msgs/Actuators.h>
    #include <nav_msgs/Odometry.h>
    #include <trajectory_msgs/MultiDOFJointTrajectoryPoint.h>
    #include <tf2/LinearMath/Quaternion.h>
    #include <tf2/utils.h>
    #include <tf2_eigen/tf2_eigen.h>
    #include <tf2_geometry_msgs/tf2_geometry_msgs.h>
    
    #include <controller_pkg/geometric_controller.h>
    #include <stdexcept>
    
    class controllerNode {
      ros::NodeHandle nh, pnh;
      // Part 1: retain handles for the subscriptions, publisher, and timer.
      ros::Subscriber desired_sub, current_sub;
      ros::Publisher rotor_pub;
      ros::Timer timer;
      controller_pkg::GeometricController controller;
      controller_pkg::State state;
      controller_pkg::Reference reference;
      bool have_current = false, have_desired = false;
      ros::Time current_received, desired_received;
      double hz, state_timeout, desired_timeout;
    
     public:
      controllerNode() : pnh("~") {
        // Part 6: gains have defaults and are configurable in the launch file.
        pnh.param("kx", controller.gains.kx, 6.0);
        pnh.param("kv", controller.gains.kv, 4.7);
        pnh.param("kr", controller.gains.kr, 64.0);
        pnh.param("komega", controller.gains.komega, 16.0);
        pnh.param("compensate_drag", controller.compensate_drag, false);
        pnh.param("hz", hz, 1000.0);
        pnh.param("state_timeout", state_timeout, 0.5);
        pnh.param("desired_timeout", desired_timeout, 0.5);
        for (double value : {controller.gains.kx, controller.gains.kv,
                             controller.gains.kr, controller.gains.komega,
                             hz, state_timeout, desired_timeout}) {
          if (!std::isfinite(value) || value <= 0.0)
            throw std::invalid_argument("Gains, frequency and timeouts must be positive and finite");
        }
        // Part 2: official topic names and message types; callbacks use latest state.
        desired_sub = nh.subscribe("desired_state", 1, &controllerNode::onDesiredState, this);
        current_sub = nh.subscribe("current_state", 1, &controllerNode::onCurrentState, this,
                                   ros::TransportHints().tcpNoDelay());
        rotor_pub = nh.advertise<mav_msgs::Actuators>("rotor_speed_cmds", 1);
        timer = nh.createTimer(ros::Duration(1.0/hz), &controllerNode::controlLoop, this);
        ROS_INFO("Gains kx=%g kv=%g kr=%g komega=%g; control rate=%g Hz",
                 controller.gains.kx, controller.gains.kv,
                 controller.gains.kr, controller.gains.komega, hz);
      }
    
      void onDesiredState(const trajectory_msgs::MultiDOFJointTrajectoryPoint& msg) {
        // Part 3: guard variable-length arrays before accessing element zero.
        if (msg.transforms.empty() || msg.velocities.empty() || msg.accelerations.empty()) {
          have_desired = false;
          ROS_WARN_THROTTLE(1.0, "Desired state requires a transform, velocity and acceleration");
          return;
        }
        controller_pkg::Reference next;
        tf2::fromMsg(msg.transforms[0].translation, next.x);
        tf2::fromMsg(msg.velocities[0].linear, next.v);
        tf2::fromMsg(msg.accelerations[0].linear, next.a);
        tf2::Quaternion q;
        tf2::fromMsg(msg.transforms[0].rotation, q);
        if (!next.x.allFinite() || !next.v.allFinite() || !next.a.allFinite() ||
            !std::isfinite(q.length2()) || q.length2() < 1e-12) {
          have_desired = false;
          ROS_WARN_THROTTLE(1.0, "Ignoring invalid desired state");
          return;
        }
        q.normalize();
        next.yaw = tf2::getYaw(q);
        reference = next;
        desired_received = ros::Time::now();
        have_desired = true;
      }
    
      void onCurrentState(const nav_msgs::Odometry& msg) {
        // Part 4: TESSE publishes both twist vectors in WORLD coordinates.
        // This differs from the usual Odometry child_frame_id twist convention.
        controller_pkg::State next;
        tf2::fromMsg(msg.pose.pose.position, next.x);
        tf2::fromMsg(msg.twist.twist.linear, next.v);
        Eigen::Quaterniond q;
        tf2::fromMsg(msg.pose.pose.orientation, q);
        Eigen::Vector3d omega_world;
        tf2::fromMsg(msg.twist.twist.angular, omega_world);
        if (!next.x.allFinite() || !next.v.allFinite() || !omega_world.allFinite() ||
            !q.coeffs().allFinite() || q.squaredNorm() < 1e-12) {
          have_current = false;
          ROS_WARN_THROTTLE(1.0, "Ignoring invalid current state");
          return;
        }
        next.R = q.normalized().toRotationMatrix();
        next.omega = next.R.transpose()*omega_world;
        state = next;
        current_received = ros::Time::now();
        have_current = true;
      }
    
      void controlLoop(const ros::TimerEvent&) {
        const ros::Time now = ros::Time::now();
        const double state_age = (now-current_received).toSec();
        const double desired_age = (now-desired_received).toSec();
        if (!have_current || !have_desired || state_age < 0.0 || desired_age < 0.0 ||
            state_age > state_timeout || desired_age > desired_timeout) return;
    
        // Part 5: equations, desired SO(3) attitude and signed allocation are in
        // geometric_controller.h so the same implementation can run without ROS.
        const auto cmd = controller.compute(state, reference);
        if (!cmd.rotor_speeds.allFinite()) {
          ROS_ERROR_THROTTLE(1.0, "Nonfinite rotor command suppressed");
          return;
        }
        mav_msgs::Actuators msg;
        msg.header.stamp = now;
        msg.header.frame_id = "base_link_gt";
        msg.angular_velocities.assign(cmd.rotor_speeds.data(), cmd.rotor_speeds.data()+4);
        rotor_pub.publish(msg);
      }
    };
    
    int main(int argc, char** argv) {
      ros::init(argc, argv, "controller_node");
      try {
        controllerNode node;
        ros::spin();
      } catch (const std::exception& e) {
        ROS_FATAL("Controller initialization failed: %s", e.what());
        return 1;
      }
      return 0;
    }
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/src/traj_publisher.cpp
    #include <ros/ros.h>
    #include <tf2/LinearMath/Quaternion.h>
    #include <tf2_geometry_msgs/tf2_geometry_msgs.h>
    #include <tf2_ros/transform_broadcaster.h>
    #include <trajectory_msgs/MultiDOFJointTrajectoryPoint.h>
    #include <cmath>
    
    int main(int argc, char** argv) {
      ros::init(argc, argv, "traj_publisher");
      ros::NodeHandle nh, pnh("~");
      bool static_pose;
      double radius, time_scale, height;
      pnh.param("static_pose", static_pose, false);
      pnh.param("radius", radius, 5.0);
      pnh.param("time_scale", time_scale, 2.0);
      pnh.param("height", height, 2.0);
      if (!std::isfinite(radius) || radius <= 0 || !std::isfinite(time_scale) ||
          time_scale <= 0 || !std::isfinite(height)) {
        ROS_FATAL("Invalid trajectory parameters");
        return 1;
      }
      auto pub = nh.advertise<trajectory_msgs::MultiDOFJointTrajectoryPoint>("desired_state", 1);
      tf2_ros::TransformBroadcaster br;
      ros::Rate rate(100);
      ros::Time::waitForValid();  // TESSE starts publishing /clock after initialization.
      ros::Time start = ros::Time::now();
      while (ros::ok()) {
        const ros::Time now = ros::Time::now();
        if (now < start) start = now;
        const double t = (now-start).toSec();
        const double phase = t/time_scale;
        trajectory_msgs::MultiDOFJointTrajectoryPoint msg;
        msg.transforms.resize(1);
        msg.velocities.resize(1);
        msg.accelerations.resize(1);
        auto& p = msg.transforms[0].translation;
        auto& v = msg.velocities[0].linear;
        auto& a = msg.accelerations[0].linear;
        p.z = height;
        tf2::Quaternion q;
        if (static_pose) {
          q.setRPY(0, 0, std::acos(-1.0)/4.0);
        } else {
          // Preserve the official 5 m radius, 2 s time scale circular reference.
          p.x = radius*std::sin(phase);
          p.y = radius*std::cos(phase);
          v.x = radius*std::cos(phase)/time_scale;
          v.y = -radius*std::sin(phase)/time_scale;
          a.x = -radius*std::sin(phase)/(time_scale*time_scale);
          a.y = -radius*std::cos(phase)/(time_scale*time_scale);
          q.setRPY(0, 0, -phase);
          msg.velocities[0].angular.z = -1.0/time_scale;
        }
        msg.transforms[0].rotation = tf2::toMsg(q);
        msg.time_from_start = ros::Duration(t);
        pub.publish(msg);
        geometry_msgs::TransformStamped transform;
        transform.header.stamp = now;
        transform.header.frame_id = "world";
        transform.child_frame_id = "av-desired";
        transform.transform = msg.transforms[0];
        br.sendTransform(transform);
        ros::spinOnce();
        rate.sleep();
      }
      return 0;
    }
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/deliverable_1.txt
    VNAV Lab 3 — Deliverable 1: Transformations in Practice (ROS Noetic / C++)
    
    Required headers:
      #include <tf2/LinearMath/Quaternion.h>
      #include <tf2/utils.h>
      #include <tf2_geometry_msgs/tf2_geometry_msgs.h>
      #include <tf2_eigen/tf2_eigen.h>
      #include <Eigen/Geometry>
    
    A. Message vs. tf
    
    A1. Convert quat_msg into the already-declared quat_tf:
      tf2::fromMsg(quat_msg, quat_tf);
    
    A2. Create a geometry_msgs::Quaternion from quat_tf:
      geometry_msgs::Quaternion quat_msg = tf2::toMsg(quat_tf);
    
    A3. Get the scalar (w) component:
      quat_tf.w();
      getW() is also available; the scalar component is not the quaternion norm.
    
    B. Conversion
    
    B1. Extract yaw in radians with one function call:
      double yaw = tf2::getYaw(quat_t);
    
    B2. Convert a geometry_msgs::Quaternion to an Eigen 3x3 rotation matrix:
      Eigen::Quaterniond q_eigen;
      tf2::fromMsg(quat_msg, q_eigen);
      Eigen::Matrix3d R = q_eigen.toRotationMatrix();
    
    This uses two conversion calls, assuming the message contains a unit quaternion.
    For a valid but nonunit input, call q_eigen.normalize() before toRotationMatrix().
    Reject a zero quaternion. Eigen's constructor takes (w,x,y,z), while the ROS
    message exposes fields x,y,z,w; fromMsg handles this ordering correctly.
    
    Sources:
    https://github.com/ros/geometry2/blob/noetic-devel/tf2_geometry_msgs/include/tf2_geometry_msgs/tf2_geometry_msgs.h
    https://github.com/ros/geometry2/blob/noetic-devel/tf2_eigen/include/tf2_eigen/tf2_eigen.h
    https://github.com/ros/geometry2/blob/noetic-devel/tf2/include/tf2/utils.h
    https://eigen.tuxfamily.org/dox/classEigen_1_1QuaternionBase.html

## Activity

    $ docker exec ros_noetic_lab2 bash -lc 'source /opt/ros/noetic/setup.bash; command -v catkin_make rviz; rospack find tf2_eigen; rospack find mav_msgs; ls /root/vnav_ws/src; dpkg -l | rg "texlive|ffmpeg|rviz|tf2-eigen|mav-msgs"'; curl -sSI -L --max-time 30 https://vnav.mit.edu/material/lab3.zip
    /opt/ros/noetic/bin/catkin_make
    /opt/ros/noetic/bin/rviz
    [rospack] Error: package 'tf2_eigen' not found
    [rospack] Error: package 'mav_msgs' not found
    two_drones_pkg
    bash: rg: command not found
    HTTP/1.1 200 Connection established
    
    HTTP/1.1 200 OK
    Date: Sat, 10 Oct 2026 02:20:15 GMT
    Server: Apache
    Last-Modified: Tue, 19 Sep 2023 14:38:33 GMT
    ETag: "1e53fad-605b73692ac40"
    Accept-Ranges: bytes
    Content-Length: 31801261
    Cache-Control: max-age=3600, s-maxage=3600, public
    Connection: close
    Content-Type: application/zip
    
    ✓ • 7.33s

## Activity

    $ g++ --version | head -1; df -h . /tmp; python3 -c 'import sympy as s; a,cf,cd=s.symbols("a c_f c_d",nonzero=True); F=s.Matrix([[cf]*4,[a*cf,-a*cf,-a*cf,a*cf],[a*cf,a*cf,-a*cf,-a*cf],[-cd,cd,-cd,cd]]); print("det F_a =",F.det()); F[3,2]=cd; F[3,3]=-cd; print("rank F_b =", F.rank()); print("nullspace =",F.nullspace())'
    g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/nvme0n1p2   39G   20G   18G  54% /
    /dev/nvme0n1p2   39G   20G   18G  54% /
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ModuleNotFoundError: No module named 'sympy'
    ✗ (1) • 0ms

## Activity

    $ docker exec ros_noetic_lab2 bash -lc 'apt-get update -qq && apt-get install -y --no-install-recommends ros-noetic-tf2-eigen ros-noetic-mav-msgs texlive-latex-base texlive-latex-recommended ffmpeg xvfb python3-matplotlib'
    Reading package lists...
    Building dependency tree...
    Reading state information...
    E: Unable to locate package ros-noetic-mav-msgs
    ✗ (100) • 9.19s

## Activity

    $ python3 - <<'PY'
        import numpy as np
        F=np.array([[1,1,1,1],[1,-1,-1,1],[1,1,-1,-1],[-1,1,-1,1]],dtype=float)
        print('scaled det F_a:', np.linalg.det(F))
        F[3]=[-1,1,1,-1]
        print('scaled rank F_b:',np.linalg.matrix_rank(F))
        PY
    scaled det F_a: 15.999999999999998
    scaled rank F_b: 3
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab2 bash -lc 'apt-get install -y --no-install-recommends ros-noetic-tf2-eigen texlive-latex-base texlive-latex-recommended ffmpeg xvfb python3-matplotlib'
    Reading package lists...
    Building dependency tree...
    Reading state information...
    The following additional packages will be installed:
      fonts-lmodern fonts-lyx libaom0 libasound2 libasound2-data libass9
      libasyncns0 libavc1394-0 libavcodec58 libavdevice58 libavfilter7
      libavformat58 libavresample4 libavutil56 libbluray2 libbs2b0 libcaca0
      libcdio-cdda2 libcdio-paranoia2 libcdio18 libchromaprint1 libcodec2-0.9
      libdc1394-22 libfftw3-double3 libflac8 libflite1 libfontenc1 libgme0 libgsm1
      libharfbuzz-icu0 libiec61883-0 libjack-jackd2-0 libjs-jquery libjs-jquery-ui
      libkpathsea6 liblilv-0-0 libmp3lame0 libmpg123-0 libmysofa1 libnorm1 libogg0
      libopenal-data libopenal1 libopenmpt0 libopus0 libpaper-utils libpaper1
      libpgm-5.2-0 libpostproc55 libptexenc1 libpulse0 libraw1394-11
      librubberband2 libsamplerate0 libsdl2-2.0-0 libserd-0-0 libshine3 libslang2
      libsnappy1v5 libsndfile1 libsndio7.0 libsord-0-0 libsoxr0 libspeex1
      libsratom-0-0 libssh-gcrypt-4 libswresample3 libswscale5 libsynctex2
      libteckit0 libtexlua53 libtheora0 libtwolame0 libunwind8 libusb-1.0-0
      libva-drm2 libva-x11-2 libva2 libvdpau1 libvidstab1.1 libvorbis0a
      libvorbisenc2 libvorbisfile3 libvpx6 libwavpack1 libwrap0 libx264-155
      libx265-179 libxfont2 libxkbfile1 libxmuu1 libxss1 libxv1 libxvidcore4
      libzmq5 libzvbi-common libzvbi0 python-matplotlib-data python3-cycler
      python3-kiwisolver t1utils tex-common texlive-base texlive-binaries
      ttf-bitstream-vera x11-xkb-utils xauth xdg-utils xserver-common
    Suggested packages:
      ffmpeg-doc libasound2-plugins alsa-utils libbluray-bdj libfftw3-bin
      libfftw3-dev jackd2 libjs-jquery-ui-docs libportaudio2 opus-tools pulseaudio
      libraw1394-doc serdi sndiod sordi speex python-cycler-doc dvipng
      gir1.2-gtk-3.0 ghostscript inkscape ipython3 python-matplotlib-doc
      python3-cairocffi python3-gi-cairo python3-gobject python3-scipy
      python3-tornado texlive-extra-utils texlive-latex-extra ttf-staypuft
      debhelper gv | postscript-viewer perl-tk xpdf | pdf-viewer xzdec
      texlive-latex-base-doc texlive-latex-recommended-doc texlive-luatex
      texlive-pstricks
    Recommended packages:
      alsa-ucm-conf alsa-topology-conf libaacs0 javascript-common va-driver-all
      | va-driver vdpau-driver-all | vdpau-driver python3-pil python3-tk lmodern
      dvisvgm libfile-mimeinfo-perl libnet-dbus-perl libx11-protocol-perl
      x11-utils x11-xserver-utils xfonts-base
    The following NEW packages will be installed:
      ffmpeg fonts-lmodern fonts-lyx libaom0 libasound2 libasound2-data libass9
      libasyncns0 libavc1394-0 libavcodec58 libavdevice58 libavfilter7
      libavformat58 libavresample4 libavutil56 libbluray2 libbs2b0 libcaca0
      libcdio-cdda2 libcdio-paranoia2 libcdio18 libchromaprint1 libcodec2-0.9
      libdc1394-22 libfftw3-double3 libflac8 libflite1 libfontenc1 libgme0 libgsm1
      libharfbuzz-icu0 libiec61883-0 libjack-jackd2-0 libjs-jquery libjs-jquery-ui
      libkpathsea6 liblilv-0-0 libmp3lame0 libmpg123-0 libmysofa1 libnorm1 libogg0
      libopenal-data libopenal1 libopenmpt0 libopus0 libpaper-utils libpaper1
      libpgm-5.2-0 libpostproc55 libptexenc1 libpulse0 libraw1394-11
      librubberband2 libsamplerate0 libsdl2-2.0-0 libserd-0-0 libshine3 libslang2
      libsnappy1v5 libsndfile1 libsndio7.0 libsord-0-0 libsoxr0 libspeex1
      libsratom-0-0 libssh-gcrypt-4 libswresample3 libswscale5 libsynctex2
      libteckit0 libtexlua53 libtheora0 libtwolame0 libunwind8 libusb-1.0-0
      libva-drm2 libva-x11-2 libva2 libvdpau1 libvidstab1.1 libvorbis0a
      libvorbisenc2 libvorbisfile3 libvpx6 libwavpack1 libwrap0 libx264-155
      libx265-179 libxfont2 libxkbfile1 libxmuu1 libxss1 libxv1 libxvidcore4
      libzmq5 libzvbi-common libzvbi0 python-matplotlib-data python3-cycler
      python3-kiwisolver python3-matplotlib ros-noetic-tf2-eigen t1utils
      tex-common texlive-base texlive-binaries texlive-latex-base
      texlive-latex-recommended ttf-bitstream-vera x11-xkb-utils xauth xdg-utils
      xserver-common xvfb
    0 upgraded, 115 newly installed, 0 to remove and 16 not upgraded.
    Need to get 99.4 MB of archives.
    After this operation, 290 MB of additional disk space will be used.
    Get:1 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 tex-common all 6.13 [32.7 kB]
    Get:2 http://snapshots.ros.org/noetic/final/ubuntu focal/main arm64 ros-noetic-tf2-eigen arm64 0.7.10-1focal.20250502.231937 [9708 B]
    Get:3 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libslang2 arm64 2.3.2-4 [394 kB]
    Get:4 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libusb-1.0-0 arm64 2:1.0.23-2build1 [44.5 kB]
    Get:5 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libxmuu1 arm64 2:1.1.3-0ubuntu1 [9772 B]
    Get:6 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 xauth arm64 1:1.1-0ubuntu1 [24.1 kB]
    Get:7 http://ports.ubuntu.com/ubuntu-ports focal-updates/universe arm64 libaom0 arm64 1.0.0.errata1-3+deb11u1ubuntu0.1 [825 kB]
    Get:8 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libva2 arm64 2.7.0-2 [50.0 kB]
    Get:9 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libva-drm2 arm64 2.7.0-2 [6856 B]
    Get:10 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libva-x11-2 arm64 2.7.0-2 [11.2 kB]
    Get:11 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libvdpau1 arm64 1.3-1ubuntu2 [23.3 kB]
    Get:12 http://ports.ubuntu.com/ubuntu-ports focal-updates/universe arm64 libavutil56 arm64 7:4.2.7-0ubuntu0.1 [238 kB]
    Get:13 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libcodec2-0.9 arm64 0.9.2-2 [7878 kB]
    Get:14 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libgsm1 arm64 1.0.18-2 [24.4 kB]
    Get:15 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libmp3lame0 arm64 3.100-3 [125 kB]
    Get:16 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libopus0 arm64 1.3.1-0ubuntu1 [172 kB]
    Get:17 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libshine3 arm64 3.1.1-2 [22.5 kB]
    Get:18 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libsnappy1v5 arm64 1.1.8-1build1 [16.0 kB]
    Get:19 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libspeex1 arm64 1.2~rc1.2-1.1ubuntu1.20.04.1 [45.8 kB]
    Get:20 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libsoxr0 arm64 0.1.3-2build1 [54.3 kB]
    Get:21 http://ports.ubuntu.com/ubuntu-ports focal-updates/universe arm64 libswresample3 arm64 7:4.2.7-0ubuntu0.1 [49.9 kB]
    Get:22 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libogg0 arm64 1.3.4-0ubuntu1 [22.9 kB]
    Get:23 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libtheora0 arm64 1.1.1+dfsg.1-15ubuntu2 [154 kB]
    Get:24 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libtwolame0 arm64 0.4.0-2 [45.1 kB]
    Get:25 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libvorbis0a arm64 1.3.6-2ubuntu1 [79.5 kB]
    Get:26 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libvorbisenc2 arm64 1.3.6-2ubuntu1 [70.5 kB]
    Get:27 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libvpx6 arm64 1.8.2-1ubuntu0.4 [753 kB]
    Get:28 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libwavpack1 arm64 5.2.0-1ubuntu0.1 [68.4 kB]
    Get:29 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libx264-155 arm64 2:0.155.2917+git0a84d98-2 [427 kB]
    Get:30 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libx265-179 arm64 3.2.1-1build1 [553 kB]
    Get:31 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libxvidcore4 arm64 2:1.3.7-1 [161 kB]
    Get:32 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libzvbi-common all 0.2.35-17 [32.5 kB]
    Get:33 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libzvbi0 arm64 0.2.35-17 [223 kB]
    Get:34 http://ports.ubuntu.com/ubuntu-ports focal-updates/universe arm64 libavcodec58 arm64 7:4.2.7-0ubuntu0.1 [4512 kB]
    Get:35 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libasound2-data all 1.2.2-2.1ubuntu2.5 [20.1 kB]
    Get:36 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libasound2 arm64 1.2.2-2.1ubuntu2.5 [304 kB]
    Get:37 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libraw1394-11 arm64 2.1.2-1 [26.7 kB]
    Get:38 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libavc1394-0 arm64 0.5.4-5 [14.7 kB]
    Get:39 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libass9 arm64 1:0.14.0-2 [69.5 kB]
    Get:40 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libbluray2 arm64 1:1.2.0-1 [123 kB]
    Get:41 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libchromaprint1 arm64 1.4.3-3build1 [33.6 kB]
    Get:42 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libgme0 arm64 0.6.2-1build1 [114 kB]
    Get:43 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libmpg123-0 arm64 1.25.13-1ubuntu0.2 [116 kB]
    Get:44 http://ports.ubuntu.com/ubuntu-ports focal/main arm64 libvorbisfile3 arm64 1.3.6-2ubuntu1 [15.3 kB]
    Get:45 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libopenmpt0 arm64 0.4.11-1build1 [538 kB]
    Get:46 http://ports.ubuntu.com/ubuntu-ports focal-updates/main arm64 libssh-gcrypt-4 arm64 0.9.3-2ubuntu2.5 [191 kB]
    Get:47 http://ports.ubuntu.com/ubuntu-ports focal-updates/universe arm64 libavformat58 arm64 7:4.2.7-0ubuntu0.1 [928 kB]
    Get:48 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libbs2b0 arm64 3.1.0+dfsg-2.2build1 [9548 B]
    Get:49 http://ports.ubuntu.com/ubuntu-ports focal/universe arm64 libflite1 arm64 2.1-release-3 [12.8 MB]
    ✗ (137) • 8.63s

## Activity

    file changes: Completed · 2 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/deliverable_2.tex
    \documentclass[11pt,a4paper]{article}
    \usepackage[margin=24mm]{geometry}
    \usepackage{amsmath,amssymb,graphicx,booktabs}
    \usepackage[hidelinks]{hyperref}
    \title{VNAV Lab 3: Modelling and Control of UAVs\\Deliverable 2}
    \author{Team Fullcans}
    \date{}
    \begin{document}
    \maketitle
    
    \section*{A. Structure of quadrotors}
    We use a right-handed frame with $x$ pointing right and $y$ pointing up in
    the top-view exercise figure, and $z$ pointing out of the page. This fixes
    all moment signs explicitly. The exercise figure and simulator figure use
    different rotor numbering; the matrices in this section follow the exercise
    figure, not the simulator figure.
    Let $d>0$ be the centre-to-rotor distance and $a=d/\sqrt{2}$. The rotor
    positions in the exercise figure are
    \[
     \rho_1=(-a,a,0)^T,\quad \rho_2=(-a,-a,0)^T,\quad
     \rho_3=(a,-a,0)^T,\quad \rho_4=(a,a,0)^T.
    \]
    Define $u_i=\omega_i^2\geq0$, where $\omega_i$ is the speed magnitude in
    each propeller's configured lifting direction, $c_f>0$ the lift coefficient,
    and $c_d>0$ the reaction-torque coefficient. Then
    \[
     f_i=c_fu_i,\qquad
     \rho_i\times (0,0,f_i)^T=(\rho_{iy}f_i,-\rho_{ix}f_i,0)^T.
    \]
    Counter-clockwise rotor motion produces clockwise body reaction torque,
    so rotors 1 and 3 in (a) have negative yaw torque and rotors 2 and 4 have
    positive yaw torque. With $w=(f,M_x,M_y,M_z)^T$, we obtain
    \begin{equation}
     w=F_a u,\qquad
     F_a=\begin{bmatrix}
     c_f&c_f&c_f&c_f\\
     ac_f&-ac_f&-ac_f&ac_f\\
     ac_f&ac_f&-ac_f&-ac_f\\
     -c_d&c_d&-c_d&c_d
     \end{bmatrix}.
    \end{equation}
    The four scaled rows are mutually orthogonal and
    \[
     \det F_a=16a^2c_f^3c_d=8d^2c_f^3c_d\ne0,
     \qquad \operatorname{rank}(F_a)=4.
    \]
    Thus all four wrench components can be locally adjusted independently
    around a positive-speed hover, subject to actuator limits.
    
    In configuration (b), swapping the propeller types and reversing the
    directions of rotors 3 and 4 preserves upward lift but reverses their
    yaw reaction torques. Therefore
    \begin{equation}
     F_b=\begin{bmatrix}
     c_f&c_f&c_f&c_f\\
     ac_f&-ac_f&-ac_f&ac_f\\
     ac_f&ac_f&-ac_f&-ac_f\\
     -c_d&c_d&c_d&-c_d
     \end{bmatrix}.
    \end{equation}
    Its fourth row is $-c_d/(ac_f)$ times its second row. The first three
    rows remain independent, hence
    \[
     \boxed{\operatorname{rank}(F_b)=3,\qquad
     M_z=-\frac{c_d}{ac_f}M_x.}
    \]
    For example, $F_b(1,-1,1,-1)^T=0$. A pure yaw moment at zero roll moment
    is impossible. At an instant of level hover with zero angular velocity,
    keeping the position fixed requires zero roll acceleration and therefore
    $M_x=0$, which also forces $M_z=0$. A prescribed yaw acceleration at that
    instant cannot be realized. Consequently (b) cannot track an arbitrary
    independently prescribed output trajectory $(x,y,z,\Psi)$; only trajectories
    compatible with the moment constraint may be feasible. Changing coordinate
    axes or wrench units cannot restore the missing rank.
    
    \section*{B. Control with quadratic body drag}
    Let $R\in SO(3)$ rotate body vectors into the world frame, $v$ be the
    world velocity, and $v^b=R^Tv$. Write
    \[
     D=\operatorname{diag}(0.1,0.1,0.2),\qquad
     h(v^b)=v^b\odot|v^b|,\qquad
     F_D^b=-D h(v^b),\qquad F_D^w=RF_D^b.
    \]
    Here $\odot$ means componentwise multiplication. This sign convention
    opposes motion in every axis and satisfies
    \[
     (v^b)^TF_D^b=-0.1|v_x^b|^3-0.1|v_y^b|^3-0.2|v_z^b|^3\leq0.
    \]
    With the lab's upward $z$ convention, the translational dynamics become
    \[
     m\dot v=-mg e_3+fRe_3+F_D^w,\qquad e_3=(0,0,1)^T.
    \]
    Define $e_x=x-x_d$, $e_v=v-v_d$ and command the rotor force vector
    \begin{equation}
     \boxed{A=-k_xe_x-k_ve_v+mg e_3+m\ddot x_d-\widehat F_D^w.}
    \end{equation}
    Using measured velocity and attitude, compute $R^Tv$, evaluate the
    quadratic drag law in the body frame, then rotate the result by $R$.
    Subtract this predicted world force when constructing $A$. For example,
    with $R=I$ and $v=(2,0,0)^T$, drag is $(-0.4,0,0)^T$ N, so the
    controller adds $+0.4$ N of forward force.
    
    The compensated force changes both the desired thrust magnitude and
    attitude. For $\|A\|>0$, choose
    \[
     b_{3d}=\frac{A}{\|A\|},\quad b_{1c}=(\cos\Psi_d,\sin\Psi_d,0)^T,
     \quad b_{2d}=\frac{b_{3d}\times b_{1c}}{\|b_{3d}\times b_{1c}\|},
    \]
    \[
     R_d=[\,b_{2d}\times b_{3d}\quad b_{2d}\quad b_{3d}\,],\qquad
     \boxed{f=A^TRe_3.}
    \]
    With perfect attitude tracking, $fRe_3=A$. If the drag estimate is exact,
    substitution into the dynamics gives
    \[
     m\dot e_v=-k_xe_x-k_ve_v,
    \]
    so the modelled disturbance is cancelled rather than left for feedback
    to counter through a persistent tracking error. With imperfect estimates,
    the residual disturbance is $F_D^w-\widehat F_D^w$.
    
    The geometric attitude controller retains its form:
    \[
     e_R=\tfrac12(R_d^TR-R^TR_d)^\vee,\quad
     e_\Omega=\Omega-R^TR_d\Omega_d,
    \]
    \[
     M=-k_Re_R-k_\Omega e_\Omega+\Omega\times J\Omega
     -J(\widehat\Omega R^TR_d\Omega_d-R^TR_d\dot\Omega_d).
    \]
    If the full feedforward terms are used, $\Omega_d$ and $\dot\Omega_d$ must
    come from the compensated $R_d$. The drag model supplied in the exercise
    is a force at the centre of mass; it does not specify an extra body moment.
    
    In the paper's downward $z$ convention, instead use
    $A_p=-k_xe_x-k_ve_v-mg e_3+m\ddot x_d-\widehat F_D^w$,
    $b_{3d}=-A_p/\|A_p\|$ and $f=-A_p^TRe_3$.
    The implementation provides optional drag compensation, disabled by default
    because the hypothetical exercise drag need not match the TESSE plant.
    
    \section*{References}
    \begin{enumerate}
    \item MIT VNAV, \emph{Lab 3 Exercises (2023)},
    \url{https://vnav.mit.edu/labs_2023/lab3/exercises.html}.
    \item T. Lee, M. Leok, and N. H. McClamroch, \emph{Geometric Tracking
    Control of a Quadrotor UAV on SE(3)}, CDC 2010, pp. 5420--5425,
    \url{https://mleok.science/pdf/LeLeMc2010_quadrotor.pdf}.
    \end{enumerate}
    \end{document}
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/offline_flight.cpp
    // Numerical closed-loop check using the production controller and an independent
    // rigid-body plant. This is not the Unity/TESSE simulator or RViz evidence.
    #include <controller_pkg/geometric_controller.h>
    #include <Eigen/Geometry>
    #include <algorithm>
    #include <fstream>
    #include <iomanip>
    #include <iostream>
    #include <string>
    
    using controller_pkg::Reference;
    using controller_pkg::State;
    
    Reference referenceAt(double t, bool stationary) {
      Reference r;
      const double pi = std::acos(-1.0);
      if (stationary) {
        r.x.z() = 2.0;
        r.yaw = pi/4.0;
      } else {
        r.x << 5*std::sin(t/2), 5*std::cos(t/2), 2;
        r.v << 2.5*std::cos(t/2), -2.5*std::sin(t/2), 0;
        r.a << -1.25*std::sin(t/2), -1.25*std::cos(t/2), 0;
        r.yaw = -t/2;
      }
      return r;
    }
    
    int main(int argc, char** argv) {
      const bool stationary = argc > 1 && std::string(argv[1]) == "hover";
      const double dt = argc > 2 ? std::stod(argv[2]) : 0.001;
      const bool drag = argc > 3 && std::string(argv[3]) == "drag";
      const bool compensate = argc > 4 && std::string(argv[4]) == "compensate";
      controller_pkg::GeometricController controller;
      controller.compensate_drag = compensate;
      State state;
      Eigen::Quaterniond q = Eigen::Quaterniond::Identity();
      const double period = 4*std::acos(-1.0);
      const double finish = stationary ? 20.0 : 3*period;
      double error_sq = 0, peak_error = 0, peak_speed = 0, map_error = 0;
      std::size_t samples = 0;
      std::ofstream csv("flight.csv");
      csv << "t,x,y,z,xd,yd,zd,error,yaw_error,rotor1,rotor2,rotor3,rotor4\n";
      Reference desired = referenceAt(0, stationary);
      int desired_tick = -1;
      for (int step = 0; step*dt < finish; ++step) {
        const double t = step*dt;
        // Match the actual trajectory publisher's 100 Hz sample-and-hold.
        const int tick = static_cast<int>(std::floor((t+1e-9)*100));
        if (tick != desired_tick) {
          desired = referenceAt(tick/100.0, stationary);
          desired_tick = tick;
        }
        const auto command = controller.compute(state, desired);
        if (!command.rotor_speeds.allFinite()) return 2;
        // Independently derive forces/moments from each rotor's position and spin.
        const double arm = 0.3/std::sqrt(2.0);
        const Eigen::Vector3d positions[4] = {{arm,arm,0}, {-arm,arm,0},
                                            {-arm,-arm,0}, {arm,-arm,0}};
        double thrust = 0;
        Eigen::Vector3d moment = Eigen::Vector3d::Zero();
        for (int i = 0; i < 4; ++i) {
          const double speed = command.rotor_speeds(i);
          const double s = speed*std::abs(speed);
          const double lift = 1e-3*s;
          thrust += lift;
          moment += positions[i].cross(Eigen::Vector3d(0,0,lift));
          moment.z() += (i%2 == 0 ? 1 : -1)*1e-5*s;
          peak_speed = std::max(peak_speed, std::abs(speed));
        }
        Eigen::Vector4d actual_wrench;
        actual_wrench << thrust, moment;
        map_error = std::max(map_error, (actual_wrench-command.wrench).norm());
        const auto ideal = referenceAt(t, stationary);
        const double error = (state.x-ideal.x).norm();
        const double yaw = std::atan2(state.R(1,0),state.R(0,0));
        const double yaw_error = std::atan2(std::sin(yaw-ideal.yaw),std::cos(yaw-ideal.yaw));
        if (t >= (stationary ? 15.0 : 2*period)) {
          error_sq += error*error;
          peak_error = std::max(peak_error,error);
          ++samples;
        }
        if (step%10 == 0) {
          csv << std::setprecision(10) << t << ',' << state.x.x() << ',' << state.x.y()
              << ',' << state.x.z() << ',' << ideal.x.x() << ',' << ideal.x.y() << ','
              << ideal.x.z() << ',' << error << ',' << yaw_error;
          for (int i = 0; i < 4; ++i) csv << ',' << command.rotor_speeds(i);
          csv << '\n';
        }
        Eigen::Vector3d acceleration = -9.81*Eigen::Vector3d::UnitZ()+thrust*state.R.col(2);
        if (drag) acceleration += controller_pkg::GeometricController::dragWorld(state);
        // Semi-implicit integration; quaternion exponential preserves SO(3).
        state.v += dt*acceleration;
        state.x += dt*state.v;
        state.omega += dt*(moment-state.omega.cross(state.omega));  // J=I, m=1
        const double rate = state.omega.norm();
        if (rate > 1e-12)
          q = (q*Eigen::Quaterniond(Eigen::AngleAxisd(dt*rate,state.omega/rate))).normalized();
        state.R = q.toRotationMatrix();
        if (!state.x.allFinite() || state.x.norm() > 1e4) return 3;
      }
      std::cout << std::setprecision(9)
                << "mode=" << (stationary ? "hover" : "circle") << " dt=" << dt
                << " drag=" << drag << " compensation=" << compensate << '\n'
                << "steady_rms_position_error_m=" << std::sqrt(error_sq/samples) << '\n'
                << "steady_max_position_error_m=" << peak_error << '\n'
                << "peak_abs_rotor_speed_rad_s=" << peak_speed << '\n'
                << "max_wrench_reconstruction_error=" << map_error << '\n';
      return 0;
    }

## Activity

    $ curl -fL --max-time 180 https://vnav.mit.edu/material/lab3.zip -o /tmp/vnav_lab3_simulator.zip; git clone --depth 1 https://github.com/ethz-asl/mav_comm.git /tmp/lab3_mav_comm
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    
    Cloning into '/tmp/lab3_mav_comm'...
    ✓ • 1m 58s

## Activity

    $ g++ -std=c++11 -O2 -Wall -Wextra -I/usr/include/eigen3 -Icontroller_pkg/include scripts/offline_flight.cpp -o /tmp/lab3_offline_flight; cd /tmp; /tmp/lab3_offline_flight hover; /tmp/lab3_offline_flight circle
    mode=hover dt=0.001 drag=0 compensation=0
    steady_rms_position_error_m=5.14388541e-15
    steady_max_position_error_m=7.02552583e-15
    peak_abs_rotor_speed_rad_s=1066.21918
    max_wrench_reconstruction_error=9.77022099e-13
    mode=circle dt=0.001 drag=0 compensation=0
    steady_rms_position_error_m=0.0149279388
    steady_max_position_error_m=0.0149279407
    peak_abs_rotor_speed_rad_s=678.261562
    max_wrench_reconstruction_error=3.28486758e-13
    ✓ • 1.95s

## Activity

    $ docker ps -a --format '{{.Names}}\t{{.Status}}'; docker inspect ros_noetic_lab2 --format 'oom={{.State.OOMKilled}} memory={{.HostConfig.Memory}}'; free -m; unzip -l /tmp/vnav_lab3_simulator.zip | head -25; ls /tmp/lab3_mav_comm/mav_msgs; docker exec ros_noetic_lab2 bash -lc 'dpkg -s ros-noetic-tf2-eigen; command -v pdflatex; ps aux | head -12'
    ros_noetic_lab2    Up About a minute
    ros_noetic_lab2_old    Exited (137) 23 hours ago
    oom=false memory=0
                   total        used        free      shared  buff/cache   available
    Mem:            3893        1652         432          29        2021        2241
    Swap:           3336          23        3313
    Archive:  /tmp/vnav_lab3_simulator.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
            0  2022-09-27 09:28   lab3/
         6272  2022-09-27 09:27   lab3/lab3.x86_64
            0  2022-09-27 09:27   lab3/lab3_Data/
           32  2022-09-27 09:27   lab3/lab3_Data/app.info
          342  2022-09-27 09:27   lab3/lab3_Data/boot.config
        46004  2022-09-27 09:27   lab3/lab3_Data/globalgamemanagers
        64980  2022-09-27 09:27   lab3/lab3_Data/globalgamemanagers.assets
         8968  2022-09-27 09:27   lab3/lab3_Data/level0
        20212  2022-09-27 09:27   lab3/lab3_Data/level1
            0  2022-09-27 09:27   lab3/lab3_Data/Managed/
        96256  2022-09-27 09:27   lab3/lab3_Data/Managed/Assembly-CSharp.dll
        40360  2022-09-27 09:27   lab3/lab3_Data/Managed/Assembly-CSharp.pdb
       310272  2022-09-27 09:27   lab3/lab3_Data/Managed/Mono.Security.dll
      3905024  2022-09-27 09:27   lab3/lab3_Data/Managed/mscorlib.dll
        84992  2022-09-27 09:27   lab3/lab3_Data/Managed/netstandard.dll
       247808  2022-09-27 09:27   lab3/lab3_Data/Managed/System.ComponentModel.Composition.dll
        43008  2022-09-27 09:27   lab3/lab3_Data/Managed/System.Configuration.dll
      1057792  2022-09-27 09:27   lab3/lab3_Data/Managed/System.Core.dll
      1941504  2022-09-27 09:27   lab3/lab3_Data/Managed/System.Data.dll
         6656  2022-09-27 09:27   lab3/lab3_Data/Managed/System.Diagnostics.StackTrace.dll
      2141696  2022-09-27 09:27   lab3/lab3_Data/Managed/System.dll
       184320  2022-09-27 09:27   lab3/lab3_Data/Managed/System.Drawing.dll
    CHANGELOG.rst
    CMakeLists.txt
    cmake
    include
    msg
    package.xml
    dpkg-query: package 'ros-noetic-tf2-eigen' is not installed and no information is available
    Use dpkg --info (= dpkg-deb --info) to examine archive files.
    USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root           1  0.0  0.0   3744  1732 ?        Ss   02:21   0:00 tail -f /dev/null
    root          26  0.2  1.0 278160 42800 pts/0    Ssl+ 02:21   0:00 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch two_drones_pkg two_drones.launch static:=False
    root          77  0.1  1.0 644856 41472 ?        Ssl  02:21   0:00 /usr/bin/python3 /opt/ros/noetic/bin/rosmaster --core -p 11311 -w 3 __log:=/root/.ros/log/4a704146-c451-11f1-9f6a-000c297d5730/master.log
    root          87  0.0  0.2 266772 10648 ?        Ssl  02:21   0:00 /opt/ros/noetic/lib/rosout/rosout __name:=rosout __log:=/root/.ros/log/4a704146-c451-11f1-9f6a-000c297d5730/rosout-1.log
    root          90  0.5  0.3 349972 11980 ?        Ssl  02:21   0:00 /root/vnav_ws/devel/.private/two_drones_pkg/lib/two_drones_pkg/frames_publisher_node __name:=frames_publisher_node __log:=/root/.ros/log/4a704146-c451-11f1-9f6a-000c297d5730/frames_publisher_node-2.log
    root          91  1.0  0.3 489592 12704 ?        Ssl  02:21   0:01 /root/vnav_ws/devel/.private/two_drones_pkg/lib/two_drones_pkg/plots_publisher_node __name:=plots_publisher_node __log:=/root/.ros/log/4a704146-c451-11f1-9f6a-000c297d5730/plots_publisher_node-3.log
    root          92 52.7  4.8 1458476 194024 ?      Ssl  02:21   0:59 /opt/ros/noetic/lib/rviz/rviz -d /root/vnav_ws/src/two_drones_pkg/config/default.rviz __name:=rviz __log:=/root/.ros/log/4a704146-c451-11f1-9f6a-000c297d5730/rviz-4.log
    root         127  0.0  0.0   5384  2968 ?        Ss   02:23   0:00 bash -lc dpkg -s ros-noetic-tf2-eigen; command -v pdflatex; ps aux | head -12
    root         135  0.0  0.0   7244  2720 ?        R    02:23   0:00 ps aux
    root         136  0.0  0.0   3720  1676 ?        S    02:23   0:00 head -12
    ✓ • 0ms

## Activity

    $ docker run -d --name ros_noetic_lab3 -v /home/chixin/f29xs/2026Fall_TeamFullcans/lab3:/workspace/lab3 -v /tmp/lab3_mav_comm:/opt/lab3-deps/mav_comm:ro ros_noetic_lab2_ready:local tail -f /dev/null; unzip -q /tmp/vnav_lab3_simulator.zip -d /tmp/vnav-lab3-simulator; file /tmp/vnav-lab3-simulator/lab3/lab3.x86_64; docker exec ros_noetic_lab3 bash -lc 'DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ros-noetic-tf2-eigen texlive-latex-base texlive-latex-recommended ffmpeg xvfb python3-matplotlib qemu-user-static' > /tmp/lab3-dependencies.log 2>&1
    0e71ea2ee1ecf097eae3f89606f9f4cbfad5b15451f3a26097bfb0d6ef9b62a0
    /tmp/vnav-lab3-simulator/lab3/lab3.x86_64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8c680d7fdb3aae76f4a2e9ae1a4ce6c93b4a3c8f, stripped
    ✓ • 1m 18s

## Assistant

控制算法已通过独立动力学检查：悬停稳定，圆轨迹稳态位置误差约为 1.5 cm，电机指令能重构所需力和力矩。这还不是 TESSE 的验证结果。官方模拟器是 x86_64 程序，而本机是 ARM64；我已下载模拟器，正在尝试运行。

## Activity

    $ ls /proc/sys/fs/binfmt_misc; tail -12 /tmp/lab3-dependencies.log; file /tmp/vnav-lab3-simulator/lab3/lab3.x86_64; ls -lh /tmp/vnav-lab3-simulator/lab3; cat /tmp/lab3_mav_comm/mav_msgs/package.xml; docker exec ros_noetic_lab3 bash -lc 'cat /etc/apt/sources.list; ls /etc/apt/sources.list.d'
    python3.12
    register
    status
    Setting up libavformat58:arm64 (7:4.2.7-0ubuntu0.1) ...
    Setting up libavfilter7:arm64 (7:4.2.7-0ubuntu0.1) ...
    Setting up libavdevice58:arm64 (7:4.2.7-0ubuntu0.1) ...
    Setting up ffmpeg (7:4.2.7-0ubuntu0.1) ...
    Processing triggers for mime-support (3.64ubuntu1) ...
    Processing triggers for libc-bin (2.31-0ubuntu9.17) ...
    Processing triggers for fontconfig (2.13.1-2ubuntu3) ...
    Processing triggers for tex-common (6.13) ...
    Running updmap-sys. This may take some time... done.
    Running mktexlsr /var/lib/texmf ... done.
    Building format(s) --all.
        This may take some time... done.
    /tmp/vnav-lab3-simulator/lab3/lab3.x86_64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8c680d7fdb3aae76f4a2e9ae1a4ce6c93b4a3c8f, stripped
    total 62M
    -rw-rw-r-- 1 chixin chixin 4.4K Sep 27  2022 LinuxPlayer_s.debug
    -rw-rw-r-- 1 chixin chixin  45M Sep 27  2022 UnityPlayer.so
    -rw-rw-r-- 1 chixin chixin  18M Sep 27  2022 UnityPlayer_s.debug
    -rw-rw-r-- 1 chixin chixin 6.2K Sep 27  2022 lab3.x86_64
    drwxrwxr-x 6 chixin chixin 4.0K Sep 27  2022 lab3_Data
    <package>
      <name>mav_msgs</name>
      <version>3.3.3</version>
      <description>Package containing messages for communicating with rotary wing MAVs</description>
    
      <maintainer email="brik@ethz.ch">Rik Bähnemann</maintainer>
    
      <author>Simon Lynen</author>
      <author>Markus Achtelik</author>
      <author>Pascal Gohl</author>
      <author>Sammy Omari</author>
      <author>Michael Burri</author>
      <author>Fadri Furrer</author>
      <author>Helen Oleynikova</author>
      <author>Mina Kamel</author>
      <author>Karen Bodie</author>
      <author>Rik Bähnemann</author>
    
      <license>ASL 2.0</license>
    
      <url type="website">https://github.com/ethz-asl/mav_comm</url>
      <url type="bugtracker">https://github.com/ethz-asl/mav_comm/issues</url>
    
      <buildtool_depend>catkin</buildtool_depend>
    
      <build_depend>cmake_modules</build_depend>
      <build_depend>eigen</build_depend>
      <build_depend>geometry_msgs</build_depend>
      <build_depend>message_generation</build_depend>
      <build_depend>nav_msgs</build_depend>
      <build_depend>std_msgs</build_depend>
      <build_depend>trajectory_msgs</build_depend>
    
      <run_depend>eigen</run_depend>
      <run_depend>geometry_msgs</run_depend>
      <run_depend>message_runtime</run_depend>
      <run_depend>nav_msgs</run_depend>
      <run_depend>std_msgs</run_depend>
      <run_depend>trajectory_msgs</run_depend>
    
    </package>
    # See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
    # newer versions of the distribution.
    deb http://ports.ubuntu.com/ubuntu-ports/ focal main restricted
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal main restricted
    
    ## Major bug fix updates produced after the final release of the
    ## distribution.
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-updates main restricted
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-updates main restricted
    
    ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
    ## team. Also, please note that software in universe WILL NOT receive any
    ## review or updates from the Ubuntu security team.
    deb http://ports.ubuntu.com/ubuntu-ports/ focal universe
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal universe
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-updates universe
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-updates universe
    
    ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
    ## team, and may not be under a free licence. Please satisfy yourself as to
    ## your rights to use the software. Also, please note that software in
    ## multiverse WILL NOT receive any review or updates from the Ubuntu
    ## security team.
    deb http://ports.ubuntu.com/ubuntu-ports/ focal multiverse
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal multiverse
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-updates multiverse
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-updates multiverse
    
    ## N.B. software from this repository may not have been tested as
    ## extensively as that contained in the main release, although it includes
    ## newer versions of some applications which may provide useful features.
    ## Also, please note that software in backports WILL NOT receive any review
    ## or updates from the Ubuntu security team.
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-backports main restricted universe multiverse
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-backports main restricted universe multiverse
    
    ## Uncomment the following two lines to add software from Canonical's
    ## 'partner' repository.
    ## This software is not part of Ubuntu, but is offered by Canonical and the
    ## respective vendors as a service to Ubuntu users.
    # deb http://archive.canonical.com/ubuntu focal partner
    # deb-src http://archive.canonical.com/ubuntu focal partner
    
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-security main restricted
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-security main restricted
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-security universe
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-security universe
    deb http://ports.ubuntu.com/ubuntu-ports/ focal-security multiverse
    # deb-src http://ports.ubuntu.com/ubuntu-ports/ focal-security multiverse
    ros1-snapshots.list
    ✓ • 0ms

## Activity

    $ docker cp /tmp/vnav-lab3-simulator/lab3 ros_noetic_lab3:/tmp/tesse-lab3; docker exec ros_noetic_lab3 python3 - <<'PY'
        PY
    ✓ • 556ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /opt/ros/noetic/setup.bash; mkdir -p /tmp/lab3_ws/src; ln -s /workspace/lab3/controller_pkg /tmp/lab3_ws/src/controller_pkg; ln -s /opt/lab3-deps/mav_comm/mav_msgs /tmp/lab3_ws/src/mav_msgs; cd /tmp/lab3_ws; catkin build --no-status -j2' > report/build_noetic.txt 2>&1; docker exec ros_noetic_lab3 bash -lc 'cd /workspace/lab3/report; pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex >/tmp/lab3_latex.log; pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex >>/tmp/lab3_latex.log; tail -4 /tmp/lab3_latex.log'; tail -20 report/build_noetic.txt
    l.132 \RequirePackage{letltxmacro}[2008/06/13]
                                                  ^^M
    !  ==> Fatal error occurred, no output PDF file produced!
    Transcript written on deliverable_2.log.
    -------------------------------------------------
    Workspace configuration appears valid.
    
    NOTE: Forcing CMake to run for each package.
    -------------------------------------------------
    [build] Found 2 packages in 0.0 seconds.
    [build] Updating package table.
    Starting >>> catkin_tools_prebuild
    Finished <<< catkin_tools_prebuild                [ 0.8 seconds ]
    Starting >>> mav_msgs
    Finished <<< mav_msgs                             [ 2.4 seconds ]
    Starting >>> controller_pkg
    Finished <<< controller_pkg                       [ 5.4 seconds ]
    [build] Summary: All 3 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 8.6 seconds total.
    [build] Note: Workspace packages have changed, please re-source setup files to use them.
    ✓ • 8.85s

## Activity

    $ cat ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/requirements.txt ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/package.xml; cat ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/CMakeLists.txt | head -95; rg -n 'process.*quad|quadrotor_dict|publish_odom|rotation.*dcm|tostring|fromstring' ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/*.py; tail -10 /tmp/lab3-x86-dependencies.log
    numpy>=1.16.0
    defusedxml>=0.6.0
    Pillow>=5.0.0
    enum34>=1.1.10
    scipy>=1.10.1<?xml version="1.0"?>
    <package>
      <name>tesse_ros_bridge</name>
      <version>0.0.1</version>
      <description>TESSE/ROS bridge</description>
    
      <maintainer email="mabate@mit.edu">Marcus Abate</maintainer>
      <license>MIT</license>
      <buildtool_depend>catkin</buildtool_depend>
      <buildtool_depend>catkin_simple</buildtool_depend>
    
      <!-- List dependencies to system libs and other catkin packages here. -->
      <build_depend>message_generation</build_depend>
      <build_depend>rospy</build_depend>
      <build_depend>tf</build_depend>
      <build_depend>std_msgs</build_depend>
      <build_depend>sensor_msgs</build_depend>
      <build_depend>nav_msgs</build_depend>
      <build_depend>mav_msgs</build_depend>
      <build_depend>ackermann_msgs</build_depend>
      <build_depend>cv_bridge</build_depend>
    
      <run_depend>message_runtime</run_depend>
    
    </package>
    cmake_minimum_required(VERSION 2.8.3)
    project(tesse_ros_bridge)
    
    find_package(catkin_simple REQUIRED)
    
    catkin_python_setup()
    catkin_simple()
    
    cs_install()
    # cs_install_scripts(scripts/tesse_ros_bridge.py)
    
    cs_export()
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py:56:        self.publish_odom              = rospy.get_param("~publish_odom", False)
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py:177:        if self.publish_odom:
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py:441:        if self.publish_odom:
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/utils.py:98:                game_time = float(ET.fromstring(data).find('time').text)
    Selecting previously unselected package liblz4-1:amd64.
    Preparing to unpack .../6-liblz4-1_1.9.2-2ubuntu0.20.04.1_amd64.deb ...
    Unpacking liblz4-1:amd64 (1.9.2-2ubuntu0.20.04.1) ...
    Selecting previously unselected package liblzma5:amd64.
    Preparing to unpack .../7-liblzma5_5.2.4-1ubuntu1.1_amd64.deb ...
    Unpacking liblzma5:amd64 (5.2.4-1ubuntu1.1) ...
    Setting up gcc-10-base:amd64 (10.5.0-1ubuntu1~20.04) ...
    Setting up libgcc-s1:amd64 (10.5.0-1ubuntu1~20.04) ...
    Setting up libcrypt1:amd64 (1:4.4.10-10ubuntu4) ...
    Setting up libc6:amd64 (2.31-0ubuntu9.18) ...
    ✓ • 0ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/deliverable_2.tex
    @@ -3,3 +3,3 @@
     \usepackage{amsmath,amssymb,graphicx,booktabs}
    -\usepackage[hidelinks]{hyperref}
    +\usepackage{url}
     \title{VNAV Lab 3: Modelling and Control of UAVs\\Deliverable 2}

## Activity

    $ docker exec -i ros_noetic_lab3 python3 - <<'PY'
        from pathlib import Path
        p=Path('/etc/apt/sources.list')
        p.write_text(p.read_text().replace('deb http','deb [arch=arm64] http'))
        p=Path('/etc/apt/sources.list.d/ros1-snapshots.list')
        p.write_text(p.read_text().replace('deb http','deb [arch=arm64] http'))
        Path('/etc/apt/sources.list.d/lab3-amd64.list').write_text('deb [arch=amd64] http://archive.ubuntu.com/ubuntu focal main universe\ndeb [arch=amd64] http://archive.ubuntu.com/ubuntu focal-updates main universe\ndeb [arch=amd64] http://security.ubuntu.com/ubuntu focal-security main universe\n')
        PY
        docker exec ros_noetic_lab3 bash -lc 'dpkg --add-architecture amd64; apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends libc6:amd64 libstdc++6:amd64 libgcc-s1:amd64 libx11-6:amd64 libxcursor1:amd64 libxrandr2:amd64 libxi6:amd64 libgl1:amd64 libasound2:amd64 libpulse0:amd64' > /tmp/lab3-x86-dependencies.log 2>&1
    ✓ • 27.33s

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'cd /workspace/lab3/report; pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex >/tmp/lab3_latex.log && pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex >>/tmp/lab3_latex.log; tail -4 /tmp/lab3_latex.log'; tail -6 /tmp/lab3-x86-dependencies.log; cd /tmp; /tmp/lab3_offline_flight circle 0.0005; /tmp/lab3_offline_flight circle 0.001 drag; /tmp/lab3_offline_flight circle 0.001 drag compensate
    live/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb></usr/share/texlive/t
    exmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb>
    Output written on deliverable_2.pdf (2 pages, 147529 bytes).
    Transcript written on deliverable_2.log.
    Setting up libglx-mesa0:amd64 (21.2.6-0ubuntu0.1~20.04.2) ...
    Setting up libxi6:amd64 (2:1.7.10-0ubuntu1) ...
    Setting up libglx0:amd64 (1.3.2-1~ubuntu0.20.04.2) ...
    Setting up libxcursor1:amd64 (1:1.2.0-2) ...
    Setting up libgl1:amd64 (1.3.2-1~ubuntu0.20.04.2) ...
    Processing triggers for libc-bin (2.31-0ubuntu9.17) ...
    mode=circle dt=0.0005 drag=0 compensation=0
    steady_rms_position_error_m=0.014435967
    steady_max_position_error_m=0.0144359689
    peak_abs_rotor_speed_rad_s=676.868735
    max_wrench_reconstruction_error=2.76343409e-13
    mode=circle dt=0.001 drag=1 compensation=0
    steady_rms_position_error_m=0.0833746234
    steady_max_position_error_m=0.0833746238
    peak_abs_rotor_speed_rad_s=538.685129
    max_wrench_reconstruction_error=1.57856068e-13
    mode=circle dt=0.001 drag=1 compensation=1
    steady_rms_position_error_m=0.0203293326
    steady_max_position_error_m=0.0203293339
    peak_abs_rotor_speed_rad_s=545.226108
    max_wrench_reconstruction_error=2.05174982e-13
    ✓ • 65ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'cat /tmp/lab3_qemu.log; tail -35 /tmp/lab3_unity.log; ps aux | head -10'; tail -6 /tmp/lab3-bridge-dependencies.log; ls -l report/deliverable_2.pdf; git status --short
    Unknown host IFA type: 11
    Set current directory to /tmp/tesse-lab3
    Found path: /tmp/tesse-lab3/lab3.x86_64
    Unknown host QEMU_IFLA type: 67
    Unknown host QEMU_IFLA type: 61
    Unknown host QEMU_IFLA type: 58
    Unknown host QEMU_IFLA type: 63
    Unknown host QEMU_IFLA type: 64
    Unknown host QEMU_IFLA type: 59
    Unknown host QEMU_IFLA type: 60
    Unknown host QEMU_IFLA type: 66
    Unknown host QEMU_IFLA type: 68
    Unknown host QEMU_IFLA type: 69
    Unknown host AF_SPEC type: 45
    Unknown host QEMU_IFLA type: 32830
    Unknown host QEMU_IFLA type: 67
    Unknown host QEMU_IFLA type: 61
    Unknown host QEMU_IFLA type: 58
    Unknown host QEMU_IFLA type: 63
    Unknown host QEMU_IFLA type: 64
    Unknown host QEMU_IFLA type: 59
    Unknown host QEMU_IFLA type: 60
    Unknown host QEMU_IFLA type: 66
    Unknown host QEMU_IFLA type: 68
    Unknown host QEMU_IFLA type: 69
    Unknown host QEMU_IFLA type: 32830
    Unknown host IFA type: 11
    PlayerConnection initialized network socket : 0.0.0.0 55321
    Multi-casting "[IP] 172.17.0.2 [Port] 55321 [Flags] 3 [Guid] 1935146235 [EditorId] 898826642 [Version] 1048832 [Id] LinuxPlayer(172.17.0.2) [Debug] 1 [PackageName] LinuxPlayer [ProjectName] tesse_vnav_scenes" to [225.0.0.222:54997]...
    Waiting for connection from host on [0.0.0.0:55321]...
    Remaining time:8s
    Remaining time:7s
    Remaining time:6s
    Remaining time:5s
    Remaining time:4s
    Remaining time:3s
    Remaining time:2s
    Remaining time:1s
    USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root           1  0.0  0.0   3744  1736 ?        Ss   02:25   0:00 tail -f /dev/null
    root        4387  0.0  0.0   5384  2980 ?        Ss   02:32   0:00 bash -lc cd /tmp/tesse-lab3; chmod +x lab3.x86_64; qemu-x86_64-static ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity.log >/tmp/lab3_qemu.log 2>&1
    root        4396  3.7  2.1 3769572 83880 ?       Sl   02:32   0:00 qemu-x86_64-static ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity.log
    root        4398 16.5  2.7 122592 108420 ?       Ss   02:32   0:01 apt-get install -y --no-install-recommends ros-noetic-ackermann-msgs python3-scipy python3-defusedxml python3-pil python3-pip
    root        4418 14.0  0.5  24516 21768 pts/0    Rs+  02:32   0:00 /usr/bin/dpkg --status-fd 34 --no-triggers --unpack --auto-deconfigure --recursive /tmp/apt-dpkg-install-sMSKDL
    root        4505  0.0  0.0   7772  2116 pts/0    S+   02:32   0:00 dpkg-deb --fsys-tarfile /tmp/apt-dpkg-install-sMSKDL/9-python3-scipy_1.3.3-3build1_arm64.deb
    root        4506  0.0  0.0   7772   744 pts/0    S+   02:32   0:00 dpkg-deb --fsys-tarfile /tmp/apt-dpkg-install-sMSKDL/9-python3-scipy_1.3.3-3build1_arm64.deb
    root        4507  0.0  0.2  15968 10056 pts/0    R+   02:32   0:00 dpkg-deb --fsys-tarfile /tmp/apt-dpkg-install-sMSKDL/9-python3-scipy_1.3.3-3build1_arm64.deb
    root        4508  0.0  0.0   5384  2980 ?        Ss   02:32   0:00 bash -lc cat /tmp/lab3_qemu.log; tail -35 /tmp/lab3_unity.log; ps aux | head -10
    Selecting previously unselected package ros-noetic-ackermann-msgs.
    Preparing to unpack .../8-ros-noetic-ackermann-msgs_1.0.2-1focal.20250426.031304_arm64.deb ...
    Unpacking ros-noetic-ackermann-msgs (1.0.2-1focal.20250426.031304) ...
    Selecting previously unselected package python3-scipy.
    Preparing to unpack .../9-python3-scipy_1.3.3-3build1_arm64.deb ...
    Unpacking python3-scipy (1.3.3-3build1) ...
    -rw-r--r-- 1 root root 147529 Oct 10 10:32 report/deliverable_2.pdf
    ?? ./
    ✓ • 0ms

## Activity

    $ docker exec -d ros_noetic_lab3 bash -lc 'cd /tmp/tesse-lab3; chmod +x lab3.x86_64; qemu-x86_64-static ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity.log >/tmp/lab3_qemu.log 2>&1'; docker exec ros_noetic_lab3 bash -lc 'DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ros-noetic-ackermann-msgs python3-scipy python3-defusedxml python3-pil python3-pip' > /tmp/lab3-bridge-dependencies.log 2>&1
    ✓ • 9.81s

## Assistant

完整 ROS 包已在 Noetic 容器中编译通过，数学题 PDF 也已生成。官方 TESSE 已进入启动流程；如果跨架构运行成功，我会继续验证真实模拟器中的飞行并录制 RViz 视频。

## Activity

    $ docker cp ../lab1/vnav-codes/lab3/tesse-ros-bridge ros_noetic_lab3:/opt/lab3-deps/tesse-ros-bridge; docker cp ../lab1/vnav-codes/lab3/catkin_simple ros_noetic_lab3:/opt/lab3-deps/catkin_simple; docker exec ros_noetic_lab3 bash -lc 'tail -35 /tmp/lab3_unity.log; tail -10 /tmp/lab3_qemu.log; source /opt/ros/noetic/setup.bash; ln -s /opt/lab3-deps/catkin_simple /tmp/lab3_ws/src/catkin_simple; ln -s /opt/lab3-deps/tesse-ros-bridge/ROS /tmp/lab3_ws/src/tesse_ros_bridge; cd /tmp/lab3_ws; catkin build --no-status -j2' > /tmp/lab3-bridge-build.log 2>&1; tail -22 /tmp/lab3-bridge-build.log
    Buildlisted Packages:        None
    Skiplisted Packages:         None
    -------------------------------------------------
    Workspace configuration appears valid.
    -------------------------------------------------
    [build] Found 4 packages in 0.0 seconds.
    [build] Updating package table.
    Starting >>> catkin_simple
    Starting >>> mav_msgs
    Finished <<< mav_msgs                        [ 1.2 seconds ]
    Starting >>> controller_pkg
    Finished <<< catkin_simple                   [ 1.3 seconds ]
    Starting >>> tesse_ros_bridge
    Finished <<< controller_pkg                  [ 0.9 seconds ]
    Finished <<< tesse_ros_bridge                [ 3.1 seconds ]
    [build] Summary: All 4 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 4.4 seconds total.
    [build] Note: Workspace packages have changed, please re-source setup files to use them.
    ✓ • 4.70s

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -65 /tmp/lab3_unity.log; tail -15 /tmp/lab3_qemu.log; ps -eo pid,pcpu,pmem,args | head -12'; tail -8 /tmp/lab3-bridge-dependencies.log; tail -12 /tmp/lab3-bridge-build.log; sed -n '1,130p' ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse/env.py; sed -n '410,470p' ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py
    Mono path[0] = '/tmp/tesse-lab3/lab3_Data/Managed'
    Mono config path = '/tmp/tesse-lab3/lab3_Data/MonoBleedingEdge/etc'
    PlayerConnection initialized from /tmp/tesse-lab3/lab3_Data (debug = 0)
    Unknown host QEMU_IFLA type: 67
    Unknown host QEMU_IFLA type: 61
    Unknown host QEMU_IFLA type: 58
    Unknown host QEMU_IFLA type: 63
    Unknown host QEMU_IFLA type: 64
    Unknown host QEMU_IFLA type: 59
    Unknown host QEMU_IFLA type: 60
    Unknown host QEMU_IFLA type: 66
    Unknown host QEMU_IFLA type: 68
    Unknown host QEMU_IFLA type: 69
    Unknown host AF_SPEC type: 45
    Unknown host QEMU_IFLA type: 32830
    Unknown host QEMU_IFLA type: 67
    Unknown host QEMU_IFLA type: 61
    Unknown host QEMU_IFLA type: 58
    Unknown host QEMU_IFLA type: 63
    Unknown host QEMU_IFLA type: 64
    Unknown host QEMU_IFLA type: 59
    Unknown host QEMU_IFLA type: 60
    Unknown host QEMU_IFLA type: 66
    Unknown host QEMU_IFLA type: 68
    Unknown host QEMU_IFLA type: 69
    Unknown host QEMU_IFLA type: 32830
    Unknown host IFA type: 11
    PlayerConnection initialized network socket : 0.0.0.0 55321
    Multi-casting "[IP] 172.17.0.2 [Port] 55321 [Flags] 3 [Guid] 1935146235 [EditorId] 898826642 [Version] 1048832 [Id] LinuxPlayer(172.17.0.2) [Debug] 1 [PackageName] LinuxPlayer [ProjectName] tesse_vnav_scenes" to [225.0.0.222:54997]...
    Waiting for connection from host on [0.0.0.0:55321]...
    Remaining time:8s
    Remaining time:7s
    Remaining time:6s
    Remaining time:5s
    Remaining time:4s
    Remaining time:3s
    Remaining time:2s
    Remaining time:1s
    Remaining time:0s
    Timed out. Continuing without host connection.
    Started listening to [0.0.0.0:55321]
    Starting managed debugger on port 56235
    Using monoOptions --debugger-agent=transport=dt_socket,embedding=1,server=y,suspend=n,address=0.0.0.0:56235
    * Assertion at mini-exceptions.c:2426, condition `sigaltstack (&sa, NULL) == 0' not met
    
    Caught fatal signal - signo:1952797279 code:1819047246 errno:1601073781 addr:0x495f65736961525f
    Obtained 17 stack frames.
    #0  0x000040039d000b in gsignal
    #1  0x000040039af859 in abort
    #2  0x000041a5440cc8 in mono_dl_fallback_unregister
    #3  0x000041a5451074 in monoeg_g_logv
    #4  0x000041a54511a5 in monoeg_assertion_message
    #5  0x000041a52f9c88 in mono_debugger_run_finally
    #6  0x000041a527cfdd in mono_jit_set_domain
    #7  0x000041a527d3b5 in mono_jit_set_domain
    #8  0x000041a5406817 in mono_thread_pop_appdomain_ref
    #9  0x000041a538afe8 in mono_check_corlib_version
    #10 0x000041a5282da1 in mini_get_debug_options
    #11 0x00004001bc995a in InitializeMonoFromMain(std::vector<core::basic_string<char, core::StringStorageDefault<char> >, std::allocator<core::basic_string<char, core::StringStorageDefault<char> > > > const&, core::basic_string<char, core::StringStorageDefault<char> >, core::basic_string<char, core::StringStorageDefault<char> >, int, char const**, bool)
    #12 0x00004001bd456d in LoadAndInitializeMono(std::vector<core::basic_string<char, core::StringStorageDefault<char> >, std::allocator<core::basic_string<char, core::StringStorageDefault<char> > > > const&, core::basic_string<char, core::StringStorageDefault<char> > const&, core::basic_string<char, core::StringStorageDefault<char> >, core::basic_string<char, core::StringStorageDefault<char> > const&, int, char const**, bool (*)())
    #13 0x00004001c51111 in LoadScriptingRuntime(core::basic_string<char, core::StringStorageDefault<char> > const&, core::basic_string<char, core::StringStorageDefault<char> > const&, int, char**)
    #14 0x00004001c529aa in PlayerMain(int, char**)
    #15 0x000040039b1083 in __libc_start_main
    #16 0x00000000400569 in _start
    qemu: uncaught target signal 6 (Aborted) - core dumped
    Unknown host IFA type: 11
    Set current directory to /tmp/tesse-lab3
    Found path: /tmp/tesse-lab3/lab3.x86_64
        PID %CPU %MEM COMMAND
          1  0.0  0.0 tail -f /dev/null
       5940  0.0  0.0 bash -lc tail -65 /tmp/lab3_unity.log; tail -15 /tmp/lab3_qemu.log; ps -eo pid,pcpu,pmem,args | head -12
       5950  0.0  0.0 ps -eo pid,pcpu,pmem,args
       5951  0.0  0.0 head -12
    Setting up python3-decorator (4.4.2-0ubuntu1) ...
    Setting up libimagequant0:arm64 (2.12.2-1.1) ...
    Setting up python-pip-whl (20.0.2-5ubuntu1.11) ...
    Setting up liblbfgsb0:arm64 (3.0+dfsg.3-7build1) ...
    Setting up python3-scipy (1.3.3-3build1) ...
    Setting up python3-pil:arm64 (7.0.0-4ubuntu0.9) ...
    Setting up python3-pip (20.0.2-5ubuntu1.11) ...
    Processing triggers for libc-bin (2.31-0ubuntu9.17) ...
    Starting >>> controller_pkg
    Finished <<< catkin_simple                   [ 1.3 seconds ]
    Starting >>> tesse_ros_bridge
    Finished <<< controller_pkg                  [ 0.9 seconds ]
    Finished <<< tesse_ros_bridge                [ 3.1 seconds ]
    [build] Summary: All 4 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 4.4 seconds total.
    [build] Note: Workspace packages have changed, please re-source setup files to use them.
    ###################################################################################################
    # DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
    #
    # This material is based upon work supported by the Under Secretary of Defense for Research and
    # Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions
    # or recommendations expressed in this material are those of the author(s) and do not necessarily
    # reflect the views of the Under Secretary of Defense for Research and Engineering.
    #
    # (c) 2020 Massachusetts Institute of Technology.
    #
    # MIT Proprietary, Subject to FAR52.227-11 Patent Rights - Ownership by the contractor (May 2014)
    #
    # The software/firmware is provided to you on an As-Is basis
    #
    # Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013
    # or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work
    # are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work other
    # than as specifically authorized by the U.S. Government may violate any copyrights that exist in
    # this work.
    ###################################################################################################
    
    import socket
    import struct
    
    from tesse.msgs import Interface
    from tesse.msgs import DataResponse
    
    
    class Env(object):
        def __init__(
            self,
            simulation_ip='localhost',
            own_ip='localhost',
            position_port=9000,
            metadata_port=9001,
            image_port=9002,
            step_port=9005,
            lidar_port=9006,
        ):
            self.simulation_ip = simulation_ip
            self.own_ip = own_ip
            self.position_port = position_port
            self.metadata_port = metadata_port
            self.image_port = image_port
            self.step_port = step_port
            self.lidar_port = lidar_port
    
        def get_port(self, msg):
            if msg.get_interface() == Interface.POSITION:
                port = self.position_port
            elif msg.get_interface() == Interface.METADATA:
                port = self.metadata_port
            elif msg.get_interface() == Interface.IMAGE:
                port = self.image_port
            elif msg.get_interface() == Interface.STEP:
                port = self.step_port
            elif msg.get_interface() == Interface.LIDAR:
                port = self.lidar_port
            else:
                raise ValueError("Invalid message interface: {}".format(msg.get_interface()))
    
            return port
    
    
        def send(self, msg):
            if self.get_port(msg) == self.step_port:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp socket
                s.connect((self.simulation_ip, self.get_port(msg)))
                s.send(msg.encode())
                s.recv(3)
                s.close()
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp socket
                s.sendto(msg.encode(), (self.simulation_ip, self.get_port(msg)))
                s.close()
    
    
        def request(self, msg, timeout=1):
            # setup receive socket
            recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            recv.settimeout(timeout)
            recv.bind((self.own_ip, self.get_port(msg)))
            recv.listen(1)
    
            # send request
            self.send(msg)
    
            # wait for a connection
            try:
                conn, addr = recv.accept()
                conn.setblocking(1)
            except socket.timeout:
                recv.close()
                return
    
            # get message tag
            tag = conn.recv(4).decode('utf-8')
            if tag not in ['mult', 'mlid', 'meta', 'cami', 'scni', 'obji', 'lidi']:
                conn.close()
                recv.close()
                raise ValueError('Unknown tag received {}'.format(tag))
    
            # get maximum message payload length
            if tag == 'mult' or tag == 'mlid':
                header = conn.recv(8)
                payload_length_data = struct.unpack("I", header[:4])[0]
                payload_length_meta = struct.unpack("I", header[4:])[0]
                max_payload_length = payload_length_data + payload_length_meta
            else:
                header = conn.recv(4)
                max_payload_length = struct.unpack("I", header)[0]
    
            # allocate payload buffer
            payload = bytearray(max_payload_length)
    
            # get payload
            total_bytes_read = 0
            payload_view = memoryview(payload)
            while total_bytes_read < max_payload_length:
                bytes_read = conn.recv_into(payload_view, max_payload_length - total_bytes_read)
                if bytes_read == 0:
                    break
                payload_view = payload_view[bytes_read:]
                total_bytes_read += bytes_read
            payload_view = memoryview(payload)[:total_bytes_read]
    
            # close socket
            conn.close()
            recv.close()
    
                Args:
                    data: A string or bytestring in xml format containing the
                        metadata from the simulator.
            """
            # Publish raw metadata.
            if self.publish_metadata:
                    self.metadata_pub.publish(data)
    
            # Parse metadata and process for proper use.
            metadata = tesse_ros_bridge.utils.parse_metadata(data)
            assert(self.prev_time < metadata['time'])
    
            metadata_processed = tesse_ros_bridge.utils.process_metadata(metadata,
                    self.prev_time, self.prev_vel_brh, self.prev_enu_R_brh)
    
            timestamp = rospy.Time.from_sec(metadata_processed['time'])
    
            # Publish agent ground truth transform.
            self.publish_tf(metadata_processed['transform'], timestamp)
    
            # Publish clean imu and odometry messages.
            if self.publish_imu:
                if self.use_gt_frames:
                    imu = tesse_ros_bridge.utils.metadata_to_imu(metadata_processed,
                            timestamp, self.body_frame_id_gt)
                else:
                    imu = tesse_ros_bridge.utils.metadata_to_imu(metadata_processed,
                            timestamp, self.body_frame_id)
                self.clean_imu_pub.publish(imu)
    
            if self.publish_odom:
                odom = tesse_ros_bridge.utils.metadata_to_odom(metadata_processed,
                        timestamp, self.world_frame_id, self.body_frame_id_gt)
                self.odom_pub.publish(odom)
    
            # Publish noisy imu and odometry messages:
            if self.publish_noisy_imu or self.publish_noisy_odom:
                metadata_noisy = self.noise_simulator.apply_noise_to_metadata(metadata_processed)
    
                if self.publish_noisy_imu:
                    if self.use_gt_frames:
                        imu = tesse_ros_bridge.utils.metadata_to_imu(metadata_noisy,
                                timestamp, self.body_frame_id_gt)
                    else:
                        imu = tesse_ros_bridge.utils.metadata_to_imu(metadata_noisy,
                                timestamp, self.body_frame_id)
                    self.noisy_imu_pub.publish(imu)
    
                    # Publish imu biases for debugging:
                    if self.publish_imu_noise_biases:
                        self.imu_gyro_bias_vec.header.stamp = timestamp
                        self.imu_gyro_bias_vec.vector.x = self.noise_simulator.gyroscope_bias[0]
                        self.imu_gyro_bias_vec.vector.y = self.noise_simulator.gyroscope_bias[1]
                        self.imu_gyro_bias_vec.vector.z = self.noise_simulator.gyroscope_bias[2]
                        self.imu_gyro_bias_pub.publish(self.imu_gyro_bias_vec)
    
                        self.imu_accel_bias_vec.header.stamp = timestamp
                        self.imu_accel_bias_vec.vector.x = self.noise_simulator.accelerometer_bias[0]
                        self.imu_accel_bias_vec.vector.y = self.noise_simulator.accelerometer_bias[1]
                        self.imu_accel_bias_vec.vector.z = self.noise_simulator.accelerometer_bias[2]
    ✓ • 0ms

## Activity

    Searched the web for qemu mono "sigaltstack" "2426", qemu aarch64 mono sigaltstack assertion sigaltstack sa NULL workaround

## Activity

    $ cat /tmp/vnav-lab3-simulator/lab3/lab3_Data/boot.config; docker exec -d ros_noetic_lab3 bash -lc 'cd /tmp/tesse-lab3; qemu-x86_64-static -strace ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity_strace.log >/tmp/lab3_qemu_strace.log 2>&1'; ls -l /usr/bin/qemu* 2>/dev/null; docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; python3 -c "import scipy, numpy, rospy, PIL, defusedxml; print(scipy.__version__)"; command -v pdftoppm'
    player-connection-mode=Listen
    player-connection-guid=898826642
    player-connection-debug=1
    player-connection-project-name=tesse_vnav_scenes
    player-connection-wait-timeout=-1
    player-connection-ip=10.0.0.49
    gfx-enable-gfx-jobs=
    gfx-enable-native-gfx-jobs=
    wait-for-native-debugger=0
    wait-for-managed-debugger=0
    vr-enabled=0
    hdr-display-enabled=0
    1.3.3
    ✗ (1) • 200ms

## Activity

    $ cd /tmp; apt download qemu-user-static > /tmp/lab3-new-qemu-download.log 2>&1; cat /tmp/lab3-new-qemu-download.log; docker exec ros_noetic_lab3 bash -lc 'tail -35 /tmp/lab3_qemu_strace.log'
    
    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
    
    Get:1 http://ports.ubuntu.com/ubuntu-ports noble-updates/universe arm64 qemu-user-static arm64 1:8.2.2+ds-0ubuntu1.18 [16.9 MB]
    Fetched 16.9 MB in 9s (1810 kB/s)
    5961 stat("./lab3.x86_64",0x00000040007ffb88) = 0
    5961 lstat("./lab3.x86_64",0x0000004000800098) = 0
    5961 getcwd(0x40008006a0,1024) = 16
    5961 fstat(1,0x00000040007ffd80) = 0
    5961 write(1,0x642dc0,41)Set current directory to /tmp/tesse-lab3
     = 41
    5961 write(1,0x642dc0,40)Found path: /tmp/tesse-lab3/lab3.x86_64
     = 40
    5961 stat("/tmp/tesse-lab3/lab3_Data/globalgamemanagers",0x00000040007ff878) = 0
    5961 stat("/tmp/tesse-lab3/lab3_Data/globalgamemanagers",0x00000040007ffd88) = 0
    5961 access("/tmp/tesse-lab3/lab3_Data/globalgamemanagers",F_OK) = 0
    5961 openat(-100,"/tmp/tesse-lab3/lab3_Data/boot.config",O_RDONLY) = 3
    5961 fstat(3,0x00000040008001e0) = 0
    5961 fstat(3,0x00000040008002d0) = 0
    5961 lseek(3,0,0,6299664,1,274940272160) = 0
    5961 read(3,0x63dcc0,342) = 342
    5961 lseek(3,342,0,6299664,3072,274940272160) = 342
    5961 close(3) = 0
    5961 stat("/",0x00000040007ffa58) = 0
    5961 stat("/",0x00000040007fff58) = 0
    5961 access("/",F_OK) = 0
    5961 stat("/tmp",0x00000040007ff9e8) = 0
    5961 access("/tmp",F_OK) = 0
    5961 stat("/tmp",0x00000040007ffef8) = 0
    5961 stat("/",0x00000040007ff998) = 0
    5961 stat("/",0x00000040007ffe98) = 0
    5961 access("/",F_OK) = 0
    5961 stat("/tmp",0x00000040007ff928) = 0
    5961 access("/tmp",F_OK) = 0
    5961 stat("/tmp",0x00000040007ffe38) = 0
    5961 openat(-100,"/tmp/lab3_unity_strace.log",O_RDWR|O_CREAT|O_TRUNC,0666) = 3
    5961 dup(1,44,0,274887093443,0,1) = 4
    5961 dup(2,44,0,274887093443,0,1) = 5
    5961 dup2(3,1,0,274887031653,0,1) = 1
    5961 dup2(3,2,0,274887031653,0,1)
    ✓ • 9.51s

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'grep -B4 -A4 sigaltstack /tmp/lab3_qemu_strace.log | tail -18'; cat /tmp/lab3-new-qemu-download.log; ls -lh /tmp/qemu-user-static* 2>/dev/null; docker exec ros_noetic_lab3 bash -lc 'cd /workspace/lab3/report; grep -E "Overfull|Underfull|Warning" deliverable_2.log'
    
    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
    
    Get:1 http://ports.ubuntu.com/ubuntu-ports noble-updates/universe arm64 qemu-user-static arm64 1:8.2.2+ds-0ubuntu1.18 [16.9 MB]
    Fetched 16.9 MB in 9s (1810 kB/s)
    -rw-r--r-- 1 chixin chixin 17M Jul  9 07:51 /tmp/qemu-user-static_1%3a8.2.2+ds-0ubuntu1.18_arm64.deb
    Overfull \hbox (4.30182pt too wide) in paragraph at lines 143--145
    ✓ • 0ms

## Activity

    $ dpkg-deb -x '/tmp/qemu-user-static_1%3a8.2.2+ds-0ubuntu1.18_arm64.deb' /tmp/lab3-qemu-new; docker cp /tmp/lab3-qemu-new/usr/bin/qemu-x86_64-static ros_noetic_lab3:/usr/local/bin/qemu-x86_64-static-new; docker exec -d ros_noetic_lab3 bash -lc 'cd /tmp/tesse-lab3; /usr/local/bin/qemu-x86_64-static-new ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity_new.log >/tmp/lab3_qemu_new.log 2>&1'; docker exec ros_noetic_lab3 bash -lc 'tail -4 /tmp/lab3_qemu_strace.log; ps -eo pid,pcpu,args | head -12'
    5961 dup(1,44,0,274887093443,0,1) = 4
    5961 dup(2,44,0,274887093443,0,1) = 5
    5961 dup2(3,1,0,274887031653,0,1) = 1
    5961 dup2(3,2,0,274887031653,0,1)    PID %CPU COMMAND
          1  0.0 tail -f /dev/null
       6022  0.0 bash -lc cd /tmp/tesse-lab3; /usr/local/bin/qemu-x86_64-static-new ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity_new.log >/tmp/lab3_qemu_new.log 2>&1
       6030  0.0 /usr/local/bin/qemu-x86_64-static-new ./lab3.x86_64 -batchmode -nographics -logFile /tmp/lab3_unity_new.log
       6032  0.0 bash -lc tail -4 /tmp/lab3_qemu_strace.log; ps -eo pid,pcpu,args | head -12
       6041  0.0 ps -eo pid,pcpu,args
       6042  0.0 head -12
    ✓ • 169ms

## Activity

    $ cat /home/chixin/.codex/plugins/cache/openai-curated-remote/google-drive/0.1.20/skills/google-drive/SKILL.md
    ---
    name: google-drive
    description: Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work. Use when the user wants to find, fetch, organize, share, export, copy, or delete Drive files, or summarize and edit Google Docs, Google Sheets, and Google Slides through one unified Google Drive plugin.
    ---
    
    # Google Drive
    
    Use this as the top-level router for Google file work inside the unified Google Drive plugin. Do not route the user toward separate Google Docs, Google Sheets, or Google Slides plugins.
    
    Start with Google Drive for file discovery and file lifecycle tasks, then route to narrower sibling skills only when the task becomes specific to Docs, Sheets, or Slides.
    
    ## Workflow
    
    1. Ground the target file first.
    - If the user did not provide an exact file URL or ID, use Google Drive search, recent files, folder listing, or metadata reads to identify the right file.
    - If the request starts as "find X and then update it," do the Drive discovery step first instead of guessing the target.
    
    2. Stay in the base Google Drive workflow for Drive-native tasks.
    - Use the base workflow for search, fetch, recent files, folders, sharing, copying, deleting, exporting, revision history, file moves, and other file-lifecycle work that is not primarily about editing Docs, Sheets, or Slides content.
    - For version-history requests, including "previous version," "revision history," "what changed since the last version," or "compare to the prior revision," ground the file, fetch the current content, use `list_file_revisions`, fetch the immediately previous revision or the user-named revision with `fetch_file_revision`, then compare the fetched revision against the current content. Do not say previous versions are unsupported until you have checked whether revision tools are available for the target file.
    - For file move requests, ground the source file and target folder, read the file metadata including its current parents, then use `update_file` with `addParents` for the target folder and `removeParents` for only the verified source parent or parents that should no longer contain it. Preserve unrelated parents, and verify the move by reading metadata or listing the target folder before the final response.
    - Before any export or raw-file fetch, read or reuse Drive metadata so the MIME type and Google Drive URL are known. Use `export_file` only to convert a native Google Doc, Sheet, or Slide into an explicitly requested format; it returns an authenticated file reference, not inline bytes or base64. Google limits `files.export` responses to **10 MB**; oversized exports fail rather than returning truncated content. For a larger native PDF, use `download_file(id=file_id, mime_type="application/pdf")` when the streaming action is available. It calls Google's `files.download` API and returns a top-level materializable `file_uri`. Once `download_file` is unavailable and canonical `fetch` uses that streamed download path, use `fetch(url=google_drive_url, download_raw_file=True, raw_export_mime_type="application/pdf")` instead. A native-file `fetch` that still uses `files.export` cannot bypass the 10 MB limit. For PDFs, images, ZIPs, Office files, recordings, and other stored, non-native files, use `fetch(url=google_drive_url, download_raw_file=True)`. Use only the authenticated top-level `file_uri` or materialized `workspace_path`; never request inline base64 unless an existing caller explicitly opts into bounded legacy compatibility. Use `fetch` without `download_raw_file` for bounded, best-effort readable text. Do not retry `export_file` after metadata shows a non-native MIME type.
    
    3. Route to the narrowest sibling skill that matches the file type and job.
    - Drive, Docs, Sheets, or Slides comment creation, comment replies, comment resolution, or review-by-comments: use [google-drive-comments](../google-drive-comments/SKILL.md).
    - Google Docs net-new creation, content summary, revision planning, prose rewriting, or section edits: use [google-docs](../google-docs/SKILL.md).
    - Google Sheets creation, local spreadsheet import, range inspection, table cleanup, data restructuring, formula design or repair, chart creation or repair, or batch updates: use [google-sheets](../google-sheets/SKILL.md).
    - Google Slides deck summary, content edits, new deck creation, local presentation import, visual cleanup, structural repair, or template migration: use [google-slides](../google-slides/SKILL.md).
    
    ## Routing Rules
    
    - If the request is ambiguous between Drive and a file-type surface, use the artifact itself as the tie-breaker:
      - Doc -> Docs skill
      - Sheet -> Sheets skill
      - Deck -> Slides skill
    - If the user wants to find a file and then edit it, do both in one flow: Drive for discovery, then the file-type skill for the edit.
    - If the user wants a Google Workspace outcome but has not named a file type yet, start with Drive discovery instead of asking them to choose among separate Google plugins.
    - If the user asks to create a new Google Doc, route to the Docs skill; it owns the mandatory local `.docx` -> native Google Docs import workflow and the explicit-user-override boundary. Do not create a blank Google Doc directly from this router.
    - If the user asks to import a local `.docx` into Google Docs, route to the Docs skill and use its native conversion workflow. Preserve the source file type only when the user explicitly asks for that.
    - If the user asks to create a new Google Sheet, route to the Sheets skill. The Sheets skill should prefer the `[@spreadsheets](plugin://spreadsheets@openai-primary-runtime)` plugin or `$Excel` skill to create a local `.xlsx`, then import it as native Google Sheets.
    - If the user asks to import a local `.xlsx`, `.xls`, `.ods`, `.csv`, or `.tsv` into Google Sheets, route to the Sheets skill and use native Google Sheets conversion by default. Preserve the source file type only when the user explicitly asks for that.
    - If the user asks to create a new Google Slides deck, route to the Slides skill; it owns the mandatory local `.pptx` -> native Google Slides import workflow and the explicit-user-override boundary. Do not create a blank Google Slides deck directly from this router.
    - If the user asks to import a local `.ppt`, `.pptx`, or `.odp` into Google Slides, route to the Slides skill and use its native conversion workflow. Preserve the source file type only when the user explicitly asks for that.
    - If the user asks to export or download an existing Drive file, choose the action from metadata: native Google Docs, Sheets, and Slides files use `export_file` for explicit conversions within Google's **10 MB** limit. For a larger native PDF, prefer the currently available streaming `download_file(id=file_id, mime_type="application/pdf")`; after canonical `fetch` adopts the same streamed download path and `download_file` is removed, use `fetch(url=google_drive_url, download_raw_file=True, raw_export_mime_type="application/pdf")`. Stored, non-native PDFs, images, ZIPs, CSVs, Office files, audio, and video use `fetch(url=google_drive_url, download_raw_file=True)`. Use the returned top-level `file_uri` or its authenticated, materialized `workspace_path`; do not expose inline binary, base64, or a bearer URL. Base64 is available only when an existing compatibility caller explicitly requests the bounded legacy behavior.
    
    ## Write Safety
    
    - Preserve the user's existing file organization, sharing state, and target artifact unless the request clearly asks to change them.
    - When a task can be satisfied by a file-level Drive operation alone, do not load heavier Docs, Sheets, or Slides skills.
    - For write-heavy Sheets or Slides work, read the specialized skill before the first large update so request shapes stay grounded.
    - For any file import or explicit direct create that returns a user-facing Google Workspace link, wait for the write action to complete and verify the created file with connector readback or Drive metadata readback before returning the URL. Use only a URL or id observed from the completed connector result or readback; never synthesize or predict the URL.
    
    ## Related Skills
    
    - Comments: [google-drive-comments](../google-drive-comments/SKILL.md)
    - Docs: [google-docs](../google-docs/SKILL.md)
    - Sheets: [google-sheets](../google-sheets/SKILL.md)
    - Slides: [google-slides](../google-slides/SKILL.md)
    ✓ • 0ms

## Assistant

TESSE 在旧版 QEMU 中遇到了 Mono 运行时崩溃，我正在用新版 QEMU 重试。视频上传部分会使用 Google Drive 技能；只有取得实际飞行录像后，才会写入交付链接。

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -50 /tmp/lab3_unity_new.log; tail -5 /tmp/lab3_qemu_new.log; ps -eo pid,pcpu,pmem,args | head -12'
    Mono path[0] = '/tmp/tesse-lab3/lab3_Data/Managed'
    Mono config path = '/tmp/tesse-lab3/lab3_Data/MonoBleedingEdge/etc'
    PlayerConnection initialized from /tmp/tesse-lab3/lab3_Data (debug = 0)
    PlayerConnection initialized network socket : 0.0.0.0 55108
    Multi-casting "[IP] 172.17.0.2 [Port] 55108 [Flags] 3 [Guid] 3893210951 [EditorId] 898826642 [Version] 1048832 [Id] LinuxPlayer(172.17.0.2) [Debug] 1 [PackageName] LinuxPlayer [ProjectName] tesse_vnav_scenes" to [225.0.0.222:54997]...
    Waiting for connection from host on [0.0.0.0:55108]...
    Remaining time:8s
    Remaining time:7s
    Remaining time:6s
    Remaining time:5s
    Remaining time:4s
    Remaining time:3s
    Remaining time:2s
    Remaining time:1s
    Remaining time:0s
    Timed out. Continuing without host connection.
    Started listening to [0.0.0.0:55108]
    Starting managed debugger on port 56951
    Using monoOptions --debugger-agent=transport=dt_socket,embedding=1,server=y,suspend=n,address=0.0.0.0:56951
    qemu-x86_64-static-new: QEMU internal SIGSEGV {code=MAPERR, addr=0x20}
    Set current directory to /tmp/tesse-lab3
    Found path: /tmp/tesse-lab3/lab3.x86_64
        PID %CPU %MEM COMMAND
          1  0.0  0.0 tail -f /dev/null
       6045  0.0  0.0 bash -lc tail -50 /tmp/lab3_unity_new.log; tail -5 /tmp/lab3_qemu_new.log; ps -eo pid,pcpu,pmem,args | head -12
       6055  0.0  0.0 ps -eo pid,pcpu,pmem,args
       6056  0.0  0.0 head -12
    ✓ • 0ms

## Activity

    Searched the web for site.github.com qemu UnityPlayer "QEMU internal SIGSEGV", site.github.com qemu unity MONO_THREADS_SUSPEND, site.docs.unity3d.com disable managed debugger command line player

## Activity

    $ docker exec -d ros_noetic_lab3 bash -lc 'cd /tmp/tesse-lab3; MONO_THREADS_SUSPEND=preemptive /usr/local/bin/qemu-x86_64-static-new -cpu qemu64 ./lab3.x86_64 -batchmode -nographics -disableManagedDebugger -logFile /tmp/lab3_unity_final.log >/tmp/lab3_qemu_final.log 2>&1'; docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; python3 -m pip install --no-deps /opt/lab3-deps/tesse-ros-bridge/tesse-interface >/tmp/lab3_pip.log; python3 -c "import tesse; print(tesse.__file__)"'; cp /tmp/flight.csv report/offline_circle_drag_compensated.csv
    /usr/local/lib/python3.8/dist-packages/tesse/__init__.py
    ✓ • 694ms

## Activity

    file changes: Completed · 2 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/rviz/circle.rviz
    Panels:
      - Class: rviz/Displays
        Name: Displays
      - Class: rviz/Views
        Name: Views
    Visualization Manager:
      Class: ""
      Global Options:
        Background Color: 35; 38; 45
        Fixed Frame: world
        Frame Rate: 30
      Displays:
        - Class: rviz/Grid
          Name: Ground
          Enabled: true
          Cell Size: 1
          Plane Cell Count: 20
          Color: 100; 110; 120
        - Class: rviz/TF
          Name: Desired frame
          Enabled: true
          Frame Timeout: 1
          Marker Scale: 0.7
          Show Arrows: true
          Show Axes: true
          Show Names: true
        - Class: rviz/Odometry
          Name: Actual vehicle
          Enabled: true
          Topic: /current_state
          Keep: 1
          Shape:
            Value: Axes
            Axes Length: 1
            Axes Radius: 0.07
          Position Tolerance: 0
          Angle Tolerance: 0
        - Class: rviz/Path
          Name: Actual path
          Enabled: true
          Topic: /flight/actual
          Color: 40; 210; 255
          Line Style: Lines
          Line Width: 0.05
          Buffer Length: 1
        - Class: rviz/Path
          Name: Desired circle
          Enabled: true
          Topic: /flight/desired
          Color: 255; 185; 45
          Line Style: Lines
          Line Width: 0.05
          Buffer Length: 1
        - Class: rviz/Marker
          Name: Simulation source
          Enabled: true
          Marker Topic: /flight/source
      Views:
        Current:
          Class: rviz/Orbit
          Distance: 21
          Pitch: 0.9
          Yaw: 0.7
          Focal Point:
            X: 0
            Y: 0
            Z: 1.5
          Target Frame: world
      Tools:
        - Class: rviz/Interact
        - Class: rviz/MoveCamera
    Window Geometry:
      Width: 1280
      Height: 800
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/rigid_body_demo.py
    #!/usr/bin/env python3
    """ARM-compatible ROS rigid-body demo. This is NOT the official TESSE plant.
    
    The real controller_node and traj_publisher run unchanged. A separate plant
    consumes /rotor_speed_cmds and publishes world-frame /current_state and /clock.
    Use this for local debugging when the x86_64 Unity player cannot run.
    """
    import csv
    import math
    import os
    import threading
    
    import numpy as np
    import rospy
    import tf.transformations as tr
    from geometry_msgs.msg import PoseStamped
    from mav_msgs.msg import Actuators
    from nav_msgs.msg import Odometry, Path
    from rosgraph_msgs.msg import Clock
    from visualization_msgs.msg import Marker
    
    
    def main():
        rospy.init_node("rigid_body_demo")
        output = rospy.get_param("~output", "/tmp/lab3_ros_flight.csv")
        duration = float(rospy.get_param("~duration", 42.0))
        clock = rospy.Publisher("/clock", Clock, queue_size=1)
        odom_pub = rospy.Publisher("/current_state", Odometry, queue_size=1)
        actual_pub = rospy.Publisher("/flight/actual", Path, queue_size=1)
        desired_pub = rospy.Publisher("/flight/desired", Path, queue_size=1)
        label_pub = rospy.Publisher("/flight/source", Marker, queue_size=1, latch=True)
        lock = threading.Lock()
        speeds = np.zeros(4)
        have_command = threading.Event()
    
        def on_command(msg):
            if len(msg.angular_velocities) != 4:
                return
            candidate = np.asarray(msg.angular_velocities, dtype=float)
            if not np.all(np.isfinite(candidate)):
                return
            with lock:
                speeds[:] = candidate
            have_command.set()
    
        rospy.Subscriber("/rotor_speed_cmds", Actuators, on_command, queue_size=1)
        x, v, omega = np.zeros(3), np.zeros(3), np.zeros(3)
        q = np.array([0.0, 0.0, 0.0, 1.0])
        arm = 0.3 / math.sqrt(2)
        positions = np.array([[arm, arm, 0], [-arm, arm, 0],
                              [-arm, -arm, 0], [arm, -arm, 0]])
        actual, desired = Path(), Path()
        actual.header.frame_id = desired.header.frame_id = "world"
        label = Marker()
        label.header.frame_id = "world"
        label.ns = "source"
        label.id = 0
        label.type = Marker.TEXT_VIEW_FACING
        label.action = Marker.ADD
        label.pose.position.z = 5
        label.pose.orientation.w = 1
        label.scale.z = 0.35
        label.color.r = label.color.g = label.color.b = label.color.a = 1
        label.text = "ROS rigid-body demo (not TESSE)"
        label_pub.publish(label)
        t, tick = 0.001, 0
        rows = []
        import time  # Wall time remains usable while this node supplies /clock.
        while not rospy.is_shutdown() and t < duration:
            wall_start = time.monotonic()
            stamp = rospy.Time.from_sec(t)
            clock.publish(Clock(clock=stamp))
            msg = Odometry()
            msg.header.stamp = stamp
            msg.header.frame_id = "world"
            msg.child_frame_id = "base_link_gt"
            msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z = x
            (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
             msg.pose.pose.orientation.z, msg.pose.pose.orientation.w) = q
            msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.linear.z = v
            R = tr.quaternion_matrix(q)[:3, :3]
            world_omega = R.dot(omega)
            (msg.twist.twist.angular.x, msg.twist.twist.angular.y,
             msg.twist.twist.angular.z) = world_omega
            odom_pub.publish(msg)
            if tick % 4 == 0:
                pose = PoseStamped(header=msg.header, pose=msg.pose.pose)
                actual.poses.append(pose)
                actual.header.stamp = stamp
                actual_pub.publish(actual)
            with lock:
                current_speeds = speeds.copy()
            # Rotor force and moment are computed independently of the controller's map.
            if have_command.is_set():
                squared = current_speeds * np.abs(current_speeds)
                lift = 1e-3 * squared
                forces = np.column_stack((np.zeros(4), np.zeros(4), lift))
                moment = np.cross(positions, forces).sum(axis=0)
                moment[2] += np.dot([1, -1, 1, -1], 1e-5 * squared)
                for _ in range(5):
                    R = tr.quaternion_matrix(q)[:3, :3]
                    v += 0.001 * (lift.sum()*R[:, 2] - np.array([0, 0, 9.81]))
                    x += 0.001*v
                    omega += 0.001*moment  # J=I, omega x J*omega=0.
                    speed = np.linalg.norm(omega)
                    if speed > 1e-12:
                        dq = tr.quaternion_about_axis(0.001*speed, omega/speed)
                        q = tr.quaternion_multiply(q, dq)
                        q /= np.linalg.norm(q)
            if not np.all(np.isfinite(x)) or np.linalg.norm(x) > 1e3:
                raise RuntimeError("Rigid-body demo diverged")
            if tick % 4 == 0:
                rows.append([t, *x, *current_speeds])
            tick += 1
            t += 0.005
            time.sleep(max(0, 0.005-(time.monotonic()-wall_start)))
        os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
        with open(output, "w", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["t", "x", "y", "z", "rotor1", "rotor2", "rotor3", "rotor4"])
            writer.writerows(rows)
        rospy.loginfo("Saved %s; source: independent rigid-body demo, not TESSE", output)
    
    
    if __name__ == "__main__":
        main()

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -22 /tmp/lab3_unity_final.log; tail -4 /tmp/lab3_qemu_final.log; ps -eo pid,pcpu,args | head -10'; mkdir -p controller_pkg/scripts; mv scripts/rigid_body_demo.py controller_pkg/scripts/rigid_body_demo.py
    Mono path[0] = '/tmp/tesse-lab3/lab3_Data/Managed'
    Mono config path = '/tmp/tesse-lab3/lab3_Data/MonoBleedingEdge/etc'
    PlayerConnection initialized from /tmp/tesse-lab3/lab3_Data (debug = 0)
    PlayerConnection initialized network socket : 0.0.0.0 55382
    Multi-casting "[IP] 172.17.0.2 [Port] 55382 [Flags] 3 [Guid] 511144369 [EditorId] 898826642 [Version] 1048832 [Id] LinuxPlayer(172.17.0.2) [Debug] 1 [PackageName] LinuxPlayer [ProjectName] tesse_vnav_scenes" to [225.0.0.222:54997]...
    Waiting for connection from host on [0.0.0.0:55382]...
    Remaining time:8s
    Remaining time:7s
    Remaining time:6s
    Remaining time:5s
    Remaining time:4s
    Remaining time:3s
    Remaining time:2s
    Remaining time:1s
    Remaining time:0s
    Timed out. Continuing without host connection.
    Started listening to [0.0.0.0:55382]
    Starting managed debugger on port 56369
    Using monoOptions --debugger-agent=transport=dt_socket,embedding=1,server=y,suspend=n,address=0.0.0.0:56369
    qemu-x86_64-static-new: QEMU internal SIGSEGV {code=MAPERR, addr=0x20}
    Set current directory to /tmp/tesse-lab3
    Found path: /tmp/tesse-lab3/lab3.x86_64
        PID %CPU COMMAND
          1  0.0 tail -f /dev/null
       6105  0.0 bash -lc tail -22 /tmp/lab3_unity_final.log; tail -4 /tmp/lab3_qemu_final.log; ps -eo pid,pcpu,args | head -10
       6115  0.0 ps -eo pid,pcpu,args
       6116  0.0 head -10
    ✓ • 0ms

## Assistant

官方 TESSE 在两版 QEMU 下都因运行时错误退出，目前无法在这台 ARM64 主机上验证飞行。我会保留错误日志，并用独立刚体模型检查实际 ROS 控制节点、生成清楚标注来源的 RViz 演示。题目要求的 TESSE 飞行验证仍需在兼容环境中完成。

## Activity

    file changes: Completed · 4 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/CMakeLists.txt
    @@ -24 +24,3 @@
     install(DIRECTORY launch config rviz DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
    +catkin_install_python(PROGRAMS scripts/rigid_body_demo.py
    +  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/launch/rigid_body_demo.launch
    <launch>
      <!-- Development substitute for ARM hosts. This launch does not run TESSE. -->
      <arg name="rviz" default="true"/>
      <arg name="duration" default="42.0"/>
      <arg name="output" default="/tmp/lab3_ros_flight.csv"/>
      <param name="/use_sim_time" value="true"/>
      <node name="rigid_body_demo" pkg="controller_pkg" type="rigid_body_demo.py" output="screen">
        <param name="duration" value="$(arg duration)"/>
        <param name="output" value="$(arg output)"/>
      </node>
      <include file="$(find controller_pkg)/launch/traj_tracking.launch"/>
      <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz"
            args="-d $(find controller_pkg)/rviz/circle.rviz"/>
    </launch>
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/package.xml
    @@ -19,2 +19,7 @@
       <exec_depend>rviz</exec_depend>
    +  <exec_depend>rospy</exec_depend>
    +  <exec_depend>tf</exec_depend>
    +  <exec_depend>rosgraph_msgs</exec_depend>
    +  <exec_depend>visualization_msgs</exec_depend>
    +  <exec_depend>python3-numpy</exec_depend>
     </package>
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/scripts/rigid_body_demo.py
    @@ -19,2 +19,3 @@
     from rosgraph_msgs.msg import Clock
    +from trajectory_msgs.msg import MultiDOFJointTrajectoryPoint
     from visualization_msgs.msg import Marker
    @@ -33,2 +34,4 @@
         speeds = np.zeros(4)
    +    target = np.zeros(3)
    +    target_time = [0.0]
         have_command = threading.Event()
    @@ -46,2 +49,11 @@
         rospy.Subscriber("/rotor_speed_cmds", Actuators, on_command, queue_size=1)
    +    def on_desired(msg):
    +        if not msg.transforms:
    +            return
    +        p = msg.transforms[0].translation
    +        with lock:
    +            target[:] = [p.x, p.y, p.z]
    +            target_time[0] = msg.time_from_start.to_sec()
    +    rospy.Subscriber("/desired_state", MultiDOFJointTrajectoryPoint,
    +                     on_desired, queue_size=1)
         x, v, omega = np.zeros(3), np.zeros(3), np.zeros(3)
    @@ -92,2 +104,14 @@
                 current_speeds = speeds.copy()
    +            current_target = target.copy()
    +            current_target_time = target_time[0]
    +        if tick % 4 == 0:
    +            desired_pose = PoseStamped()
    +            desired_pose.header = msg.header
    +            (desired_pose.pose.position.x, desired_pose.pose.position.y,
    +             desired_pose.pose.position.z) = current_target
    +            desired_pose.pose.orientation.w = 1
    +            desired.poses.append(desired_pose)
    +            desired.header.stamp = stamp
    +            desired_pub.publish(desired)
    +            rows.append([t, *x, *current_target, current_target_time, *current_speeds])
             # Rotor force and moment are computed independently of the controller's map.
    @@ -111,4 +135,2 @@
                 raise RuntimeError("Rigid-body demo diverged")
    -        if tick % 4 == 0:
    -            rows.append([t, *x, *current_speeds])
             tick += 1
    @@ -119,3 +141,4 @@
             writer = csv.writer(handle)
    -        writer.writerow(["t", "x", "y", "z", "rotor1", "rotor2", "rotor3", "rotor4"])
    +        writer.writerow(["t", "x", "y", "z", "xd", "yd", "zd", "trajectory_time",
    +                         "rotor1", "rotor2", "rotor3", "rotor4"])
             writer.writerows(rows)

## Activity

    $ chmod +x controller_pkg/scripts/rigid_body_demo.py; docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; cd /tmp/lab3_ws; catkin build --no-status -j2' > report/build_noetic.txt 2>&1; tail -12 report/build_noetic.txt; docker exec -d ros_noetic_lab3 bash -lc 'Xvfb :99 -screen 0 1280x800x24 >/tmp/lab3_xvfb.log 2>&1'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_ros_flight.log 2>&1'
    Finished <<< catkin_simple                   [ 0.1 seconds ]
    Finished <<< mav_msgs                        [ 0.3 seconds ]
    Starting >>> controller_pkg
    Starting >>> tesse_ros_bridge
    Finished <<< tesse_ros_bridge                [ 0.5 seconds ]
    Finished <<< controller_pkg                  [ 0.8 seconds ]
    [build] Summary: All 4 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 1.1 seconds total.
    ✓ • 1.24s

## Activity

    mcp tool: codex_apps/google_drive.get_profile({}) · Completed
    Action completed.
    structured result: {"id":"100204035725448212489","name":"Qiaosu Jia","email":"chixin114514@gmail.com","nickname":null,"picture":"https://lh3.googleusercontent.com/a/ACg8ocJQC2Z4R-zrST1LG9wwDrEJYeP-D_nFaykRoddFelkTLK9s8A=s96-c","workspace_id":null,"workspace_name":null,"workspace_picture":null}

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -25 /tmp/lab3_ros_flight.log; ls /tmp/lab3_ws/devel/lib/controller_pkg; ls -l /tmp/lab3_xvfb.log'; ls -lh report
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    controller_node
    rigid_body_demo.py
    traj_publisher
    -rw-r--r-- 1 root root 0 Oct 10 02:37 /tmp/lab3_xvfb.log
    total 716K
    -rw-rw-r-- 1 chixin chixin 1.9K Oct 10 10:37 build_noetic.txt
    -rw-r--r-- 1 root   root      8 Oct 10 10:32 deliverable_2.aux
    -rw-r--r-- 1 root   root    11K Oct 10 10:32 deliverable_2.log
    -rw-r--r-- 1 root   root   145K Oct 10 10:32 deliverable_2.pdf
    -rw-rw-r-- 1 chixin chixin 5.6K Oct 10 10:32 deliverable_2.tex
    -rw-rw-r-- 1 chixin chixin 537K Oct 10 10:35 offline_circle_drag_compensated.csv
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; rosnode list; rostopic echo -n1 /clock; tail -12 /tmp/lab3_ros_flight.log'; ls -lh report/ros_flight.csv 2>/dev/null
    /controller_node
    /rigid_body_demo
    /rosout
    /rviz
    /traj_publisher
    clock:
      secs: 31
      nsecs: 115999999
    ---
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    ✗ (2) • 1.28s

## Activity

    $ mkdir -p report/video; docker exec ros_noetic_lab3 bash -lc 'ffmpeg -hide_banner -loglevel error -f x11grab -video_size 1280x800 -framerate 20 -i :99 -t 20 -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -movflags +faststart /workspace/lab3/report/video/rviz_rigid_body_demo.mp4'
    ✓ • 20.20s

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -15 /tmp/lab3_ros_flight.log; ps -eo pid,pcpu,args | head -12'; ls -lh report/ros_flight.csv report/video/rviz_rigid_body_demo.mp4 2>/dev/null
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    [INFO] [1791599914.450294, 41.996000]: Saved /workspace/lab3/report/ros_flight.csv; source: independent rigid-body demo, not TESSE
        PID %CPU COMMAND
          1  0.0 tail -f /dev/null
       7051  0.0 bash -lc Xvfb :99 -screen 0 1280x800x24 >/tmp/lab3_xvfb.log 2>&1
       7060  1.1 Xvfb :99 -screen 0 1280x800x24
       7061  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_ros_flight.log 2>&1
       7090  0.3 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv
       7098  0.2 /usr/bin/python3 /opt/ros/noetic/bin/rosmaster --core -p 11311 -w 3 __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/master.log
       7108  0.3 /opt/ros/noetic/lib/rosout/rosout __name:=rosout __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/rosout-1.log
       7116  1.1 /tmp/lab3_ws/devel/.private/controller_pkg/lib/controller_pkg/traj_publisher __name:=traj_publisher __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/traj_publisher-3.log
       7117  2.3 /tmp/lab3_ws/devel/.private/controller_pkg/lib/controller_pkg/controller_node __name:=controller_node __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/controller_node-4.log
       7118 46.2 /opt/ros/noetic/lib/rviz/rviz -d /tmp/lab3_ws/src/controller_pkg/rviz/circle.rviz __name:=rviz __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/rviz-5.log
       7303  0.0 bash -lc tail -15 /tmp/lab3_ros_flight.log; ps -eo pid,pcpu,args | head -12
    -rw-r--r-- 1 root root 411K Oct 10 10:38 report/ros_flight.csv
    -rw-r--r-- 1 root root 1.1M Oct 10 10:38 report/video/rviz_rigid_body_demo.mp4
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'ffmpeg -hide_banner -loglevel error -ss 5 -i /workspace/lab3/report/video/rviz_rigid_body_demo.mp4 -frames:v 1 /workspace/lab3/report/video/rviz_demo_frame.png; ffprobe -v error -show_entries format=duration -of default=nw=1 /workspace/lab3/report/video/rviz_rigid_body_demo.mp4'; python3 - <<'PY'
        import numpy as np
        p=np.genfromtxt('report/ros_flight.csv', delimiter=',', names=True)
        m=p['trajectory_time']>25.2
        e=np.sqrt((p['x']-p['xd'])**2+(p['y']-p['yd'])**2+(p['z']-p['zd'])**2)
        print('real_ROS_controller_with_independent_plant')
        print('samples',len(p),'time_range',p['trajectory_time'][0],p['trajectory_time'][-1])
        print('steady_RMS_m', np.sqrt(np.mean(e[m]**2)), 'steady_max_m',max(e[m]))
        print('z_range_steady',p['z'][m].min(),p['z'][m].max())
        PY
    duration=20.000000
    real_ROS_controller_with_independent_plant
    samples 2100 time_range 0.0 41.76
    steady_RMS_m 0.033882264704726224 steady_max_m 0.055439416469619106
    z_range_steady 1.9997597389916626 1.9998384737233796
    ✓ • 187ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_demo_frame.png

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; rosnode kill /rviz'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1 rosrun rviz rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz >/tmp/lab3_rviz.log 2>&1'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; rosrun controller_pkg rigid_body_demo.py _duration:=60 _output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_demo_second.log 2>&1'
    killing /rviz
    killed
    ✓ • 247ms

## Activity

    $ docker cp ros_noetic_lab3:/tmp/lab3_unity.log report/tesse_qemu_4_startup.txt; docker cp ros_noetic_lab3:/tmp/lab3_unity_new.log report/tesse_qemu_8_startup.txt; docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; rosnode info /controller_node; rostopic info /rotor_speed_cmds' > report/ros_runtime_topics.txt; cat report/ros_runtime_topics.txt; python3 - <<'PY'
        from pathlib import Path
        p=Path('report/deliverable_2.tex')
        s=p.read_text().replace('m\\dot e_v=-k_xe_x-k_ve_v,','m\\dot e_v=-k_xe_x-k_ve_v,')
        p.write_text(s)
        PY
    --------------------------------------------------------------------------------
    Node [/controller_node]
    Publications:
     * /rosout [rosgraph_msgs/Log]
     * /rotor_speed_cmds [mav_msgs/Actuators]
    
    Subscriptions:
     * /clock [rosgraph_msgs/Clock]
     * /current_state [nav_msgs/Odometry]
     * /desired_state [trajectory_msgs/MultiDOFJointTrajectoryPoint]
    
    Services:
     * /controller_node/get_loggers
     * /controller_node/set_logger_level
    
    
    contacting node http://0e71ea2ee1ec:38755/ ...
    Pid: 7117
    Connections:
     * topic: /rosout
        * to: /rosout
        * direction: outbound (41683 - 172.17.0.2:56962) [10]
        * transport: TCPROS
     * topic: /rotor_speed_cmds
        * to: /rigid_body_demo
        * direction: outbound (41683 - 172.17.0.2:54484) [14]
        * transport: TCPROS
     * topic: /clock
        * to: /rigid_body_demo (http://0e71ea2ee1ec:33999/)
        * direction: inbound (48758 - 0e71ea2ee1ec:35363) [18]
        * transport: TCPROS
     * topic: /desired_state
        * to: /traj_publisher (http://0e71ea2ee1ec:38741/)
        * direction: inbound (34008 - 0e71ea2ee1ec:46253) [16]
        * transport: TCPROS
     * topic: /current_state
        * to: /rigid_body_demo (http://0e71ea2ee1ec:33999/)
        * direction: inbound (48766 - 0e71ea2ee1ec:35363) [19]
        * transport: TCPROS
    
    Type: mav_msgs/Actuators
    
    Publishers:
     * /controller_node (http://0e71ea2ee1ec:38755/)
    
    Subscribers:
     * /rigid_body_demo (http://0e71ea2ee1ec:33999/)
    
    
    ✓ • 613ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; python3 -c "import rospy; from rosgraph_msgs.msg import Clock; rospy.init_node(\"record_wait\"); rospy.Subscriber(\"/clock\", Clock, lambda m: rospy.signal_shutdown(\"ready\") if m.clock.to_sec() >= 28 else None); rospy.spin()"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -framerate 20 -i :99 -t 20 -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -movflags +faststart /workspace/lab3/report/video/rviz_rigid_body_demo.mp4; ffmpeg -y -hide_banner -loglevel error -ss 5 -i /workspace/lab3/report/video/rviz_rigid_body_demo.mp4 -frames:v 1 /workspace/lab3/report/video/rviz_demo_frame.png'
    ✓ • 47.96s

## Activity

    file changes: Completed · 4 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/README.md
    # Lab 3 — Quadrotor geometric control
    
    依据 [MIT VNAV 2023 Lab 3](https://vnav.mit.edu/labs_2023/lab3/exercises.html) 实现。
    
    ## 交付状态
    
    | 交付项 | 文件 | 状态 |
    | --- | --- | --- |
    | Deliverable 1：ROS 四元数转换 | `deliverable_1.txt` | 完成 |
    | Deliverable 2：旋翼布局秩分析、阻力补偿 | `report/deliverable_2.pdf`、`.tex` | 完成 |
    | Deliverable 3：完整控制器源码 | `controller_pkg/` | ROS Noetic 编译通过 |
    | 悬停、圆轨迹及阻力补偿数值验证 | `report/numerical_validation.txt` | 独立刚体模型验证，非 TESSE |
    | 真实 ROS 节点闭环运行 | `report/ros_flight.csv`、`ros_metrics.json` | 独立刚体模型驱动实际控制节点，非 TESSE |
    | RViz 演示录像 | `report/video/rviz_rigid_body_demo.mp4` | 独立模型演示，画面内明确标注来源 |
    | 官方 TESSE 飞行、最终调参及公开录像链接 | `rviz_drone_flight.txt` | **待完成**，见下方环境限制 |
    
    当前主机为 ARM64；官方安装包中的 `lab3.x86_64` 为 x86_64。
    QEMU 4.2 启动失败于 Mono 的 `sigaltstack` 断言，QEMU 8.2 失败于内部 SIGSEGV。
    失败日志保存在 `report/tesse_qemu_4_startup.txt` 和 `report/tesse_qemu_8_startup.txt`。
    因此尚不能声称在官方 TESSE 中完成了稳定飞行；独立模型录像也不能作为 TESSE 验证的证明。
    
    个人题按原题要求提交个人仓库；团队仓库提交完整 `controller_pkg` 和最终录像公开链接。
    
    ## 控制器实现
    
    - `src/controller_node.cpp`：订阅 `/desired_state` 和 `/current_state`，1000 Hz 发布 `/rotor_speed_cmds`；初始化、参数默认值、非法消息及超时检查完整。
    - `include/controller_pkg/geometric_controller.h`：位置/速度误差、期望 SO(3) 姿态、姿态反馈、陀螺项和旋翼分配。控制数学与 ROS 消息处理分离，数值验证使用同一份控制实现。
    - `src/traj_publisher.cpp`：保留官方半径 5 m、高度 2 m、时间尺度 2 s 的圆轨迹，周期为 `4*pi ≈ 12.566 s`，期望 yaw 为 `-t/2`；静态目标通过参数切换。
    - `config/gains.yaml`：`kx=6, kv=4.7, kr=64, komega=16`。这些值已在独立模型中验证，仍须在目标 TESSE 环境中复核。
    
    状态消息中的位置和线速度都按实验定义使用世界坐标。角速度转换为
    `omega_body = R.transpose() * omega_world`。这遵循 TESSE 的实验约定，与一般
    `nav_msgs/Odometry` 的 child frame twist 约定不同。
    
    采用 ROS 向上的 z 轴：
    
    ```text
    A = -kx*(x-xd) - kv*(v-vd) + m*g*e3 + m*ad
    b3d = A / ||A||
    b2d = normalize(b3d cross [cos(yawd), sin(yawd), 0])
    Rd = [b2d cross b3d, b2d, b3d]
    eR = 0.5 * vee(Rd^T*R - R^T*Rd)
    f = A dot (R*e3)
    M = -kr*eR - komega*omega_body + omega_body cross (J*omega_body)
    ```
    
    按骨架允许的简化，忽略 `Omega_d` 及其导数，因此旋转轨迹中可能有小的姿态跟踪滞后。
    零期望力和期望方向平行情形提供了确定的备用轴，避免归一化除零。
    
    官方模拟器的旋翼位置为 `(+a,+a),(-a,+a),(-a,-a),(+a,-a)`，其中 `a=d/sqrt(2)`。
    令 `s_i=omega_i*abs(omega_i)`，使用
    
    ```text
                  [ cf     cf     cf     cf   ]
    [f Mx My Mz] = [ a*cf   a*cf  -a*cf  -a*cf] s
                  [-a*cf   a*cf   a*cf  -a*cf]
                  [ cd    -cd     cd    -cd   ]
    ```
    
    上式左边按列向量理解。逆映射后对每个分量取带符号平方根，单位为 rad/s；
    保留题目模拟器允许的负转速。悬停每个旋翼转速应为 `sqrt(9.81/(4*0.001)) ≈ 49.523 rad/s`。
    个人题示意图使用另一套旋翼编号，不能直接拿其矩阵驱动模拟器。
    
    `compensate_drag:=true` 时，从 A 中减去 `R*(-D*(R^T*v)*abs(R^T*v))`；默认关闭，
    只有被控对象确实具有 Deliverable 2 给定的阻力时才应启用。
    
    ## ROS Noetic 构建
    
    在 Ubuntu 20.04 + ROS Noetic 的 catkin 工作区内执行：
    
    ```bash
    source /opt/ros/noetic/setup.bash
    sudo apt-get update
    sudo apt-get install -y python3-catkin-tools ros-noetic-tf2-eigen \
      ros-noetic-tf2-geometry-msgs ros-noetic-ackermann-msgs ros-noetic-cv-bridge \
      ros-noetic-rviz python3-numpy python3-scipy python3-defusedxml python3-pil
    
    mkdir -p ~/vnav_ws/src
    cp -r /path/to/this/lab3/controller_pkg ~/vnav_ws/src/
    cd ~/vnav_ws/src
    git clone https://github.com/ethz-asl/mav_comm.git
    
    # 官方桥接和 catkin_simple 在本仓库的 lab1/vnav-codes/lab3 内。
    cp -r /path/to/repository/lab1/vnav-codes/lab3/catkin_simple .
    cp -r /path/to/repository/lab1/vnav-codes/lab3/tesse-ros-bridge .
    cd tesse-ros-bridge/tesse-interface
    python3 -m pip install --no-deps .
    
    cd ~/vnav_ws
    catkin build
    source devel/setup.bash
    ```
    
    Python 标准库已提供 enum，无需安装 Python 2 的 enum34。上述环境使用发行版自带 NumPy、SciPy、Pillow、defusedxml。
    实际构建记录见 `report/build_noetic.txt`。
    
    当前会话创建了独立容器 `ros_noetic_lab3`，代码挂载在 `/workspace/lab3`，
    构建工作区在 `/tmp/lab3_ws`。可直接进入并复用：
    
    ```bash
    docker exec -it ros_noetic_lab3 bash
    source /tmp/lab3_ws/devel/setup.bash
    ```
    
    这些 `/tmp` 依赖和容器状态不是永久安装流程；换机器时按上面的源码构建步骤操作。
    
    ## 官方 TESSE 运行及最终交付
    
    需要能够运行 x86_64 Linux Unity Player 的环境。下载
    [官方安装包](https://vnav.mit.edu/material/lab3.zip)，解压后在不同终端运行：
    
    ```bash
    # 终端 1
    cd /path/to/simulator/lab3
    chmod +x lab3.x86_64
    ./lab3.x86_64
    
    # 终端 2；ROS 终端都先 source 工作区
    roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch
    
    # 终端 3：先观察静态目标 (0,0,2)，yaw=pi/4
    DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg traj_tracking.launch static_pose:=true rviz:=true
    ```
    
    静态跟踪稳定后，结束控制节点，按 R 重置模拟器，再启动圆轨迹：
    
    ```bash
    DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg traj_tracking.launch rviz:=true
    ```
    
    根据实际结果调整 `config/gains.yaml`。`kx,kv` 调节位置和速度反馈，`kr,komega` 调节姿态恢复和角速度阻尼。
    如有需要，按 W 启动旋翼。记录 RViz 中至少完整一圈，上传 Google Drive 或 Dropbox，
    设置为“知道链接的任何人可查看”，将实际公开链接写入 `rviz_drone_flight.txt`。
    
    ## ARM64 上的独立模型演示
    
    该演示启动实际编译的控制器和轨迹节点，由独立刚体模型读取旋翼转速并积分运动，
    在 ROS 中发布状态、仿真时钟和轨迹。**该模型没有 Unity 接触、碰撞或电机动态，不能替代 TESSE 验证。**
    
    ```bash
    source /tmp/lab3_ws/devel/setup.bash
    DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg rigid_body_demo.launch duration:=60
    ```
    
    模型会在指定时长后退出并写出 CSV，其余可视化节点用 Ctrl+C 结束。
    容器内无物理显示时可使用 `Xvfb :99 -screen 0 1280x800x24`，再设置
    `DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1`。录屏示例：
    
    ```bash
    ffmpeg -f x11grab -video_size 1280x800 -framerate 20 -i :99 -t 20 \
      -c:v libx264 -preset ultrafast -pix_fmt yuv420p -movflags +faststart rviz_demo.mp4
    ```
    
    ## 数值验证与报告再生成
    
    ```bash
    # 宿主机仅需 C++11 编译器和 Eigen；使用生产控制器头文件。
    bash scripts/validate_offline.sh > report/numerical_validation.txt
    
    # 在安装 matplotlib 的环境中，根据真实 ROS 日志生成图和指标。
    python3 scripts/plot_flight.py
    
    # LaTeX 报告
    cd report
    pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex
    pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex
    ```
    
    数值检查比较悬停、圆轨迹、较小积分步长以及有/无阻力补偿；动力学中的旋翼力矩通过
    独立的 `rho cross force` 计算，以检查控制器的电机分配符号。
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/rviz_drone_flight.txt
    PENDING — no verified public TESSE/RViz flight video link yet.
    
    The official TESSE Linux player is x86_64; this host is ARM64. It crashes under
    both QEMU 4.2 (Mono sigaltstack assertion) and QEMU 8.2 (internal SIGSEGV).
    Startup evidence is saved under report/tesse_qemu_*_startup.txt.
    
    Local development video: report/video/rviz_rigid_body_demo.mp4
    This video uses a separate rigid-body model with the actual ROS controller.
    It is explicitly labelled NOT TESSE and is not evidence of official TESSE flight.
    
    To finish the official submission: run TESSE in a compatible environment, tune
    the gains, record at least one full circular lap in RViz, upload the video to
    Google Drive or Dropbox, enable public viewing, and replace this file with the
    verified public video URL.
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/plot_flight.py
    #!/usr/bin/env python3
    """Plot recorded ROS closed-loop data; explicitly identify the plant source."""
    from pathlib import Path
    import json
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    
    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root / "report/ros_flight.csv", delimiter=",", names=True)
    steady = data["trajectory_time"] >= 8*np.pi
    errors = np.sqrt(sum((data[a]-data[b])**2 for a, b in
                         [("x", "xd"), ("y", "yd"), ("z", "zd")]))
    metrics = {
        "plant": "independent rigid-body model, NOT TESSE",
        "controller": "compiled ROS Noetic controller_node via real ROS topics",
        "steady_window_trajectory_time_s": [float(data["trajectory_time"][steady][0]),
                                             float(data["trajectory_time"][-1])],
        "steady_position_rms_m": float(np.sqrt(np.mean(errors[steady]**2))),
        "steady_position_max_m": float(np.max(errors[steady])),
        "sample_count": len(data),
    }
    (root / "report/ros_metrics.json").write_text(json.dumps(metrics, indent=2)+"\n")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(data["xd"][steady], data["yd"][steady], "--", label="Desired", color="#c17b00")
    axes[0].plot(data["x"][steady], data["y"][steady], label="Actual", color="#0075ad")
    axes[0].set(xlabel="World x (m)", ylabel="World y (m)", title="Steady circular flight")
    axes[0].axis("equal")
    axes[0].legend()
    axes[1].plot(data["trajectory_time"], errors, color="#0075ad")
    axes[1].axvline(8*np.pi, color="0.4", linestyle="--", label="Steady window starts")
    axes[1].set(xlabel="Trajectory time (s)", ylabel="Position error (m)", title="ROS closed-loop tracking")
    axes[1].legend()
    for ax in axes:
        ax.grid(alpha=0.25)
    fig.suptitle("Independent rigid-body model + actual ROS controller (not TESSE)")
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig(root / "report/ros_tracking.pdf")
    fig.savefig(root / "report/ros_tracking.png", dpi=160)
    print(json.dumps(metrics, indent=2))
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/validate_offline.sh
    #!/usr/bin/env bash
    set -euo pipefail
    lab3_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
    validation_dir=$(mktemp -d /tmp/lab3-validation.XXXXXX)
    ${CXX:-g++} -std=c++11 -O2 -Wall -Wextra \
      -I/usr/include/eigen3 -I"$lab3_root/controller_pkg/include" \
      "$lab3_root/scripts/offline_flight.cpp" -o "$validation_dir/offline_flight"
    cd "$validation_dir"
    ./offline_flight hover
    ./offline_flight circle
    cp flight.csv "$lab3_root/report/offline_circle.csv"
    ./offline_flight circle 0.0005
    ./offline_flight circle 0.001 drag
    ./offline_flight circle 0.001 drag compensate
    cp flight.csv "$lab3_root/report/offline_circle_drag_compensated.csv"
    printf 'CSV files saved under %s/report; numerical plant is not TESSE.\n' "$lab3_root"

## Activity

    $ chmod +x scripts/validate_offline.sh scripts/plot_flight.py; bash scripts/validate_offline.sh > report/numerical_validation.txt; cat report/numerical_validation.txt
    mode=hover dt=0.001 drag=0 compensation=0
    steady_rms_position_error_m=5.14388541e-15
    steady_max_position_error_m=7.02552583e-15
    peak_abs_rotor_speed_rad_s=1066.21918
    max_wrench_reconstruction_error=9.77022099e-13
    mode=circle dt=0.001 drag=0 compensation=0
    steady_rms_position_error_m=0.0149279388
    steady_max_position_error_m=0.0149279407
    peak_abs_rotor_speed_rad_s=678.261562
    max_wrench_reconstruction_error=3.28486758e-13
    mode=circle dt=0.0005 drag=0 compensation=0
    steady_rms_position_error_m=0.014435967
    steady_max_position_error_m=0.0144359689
    peak_abs_rotor_speed_rad_s=676.868735
    max_wrench_reconstruction_error=2.76343409e-13
    mode=circle dt=0.001 drag=1 compensation=0
    steady_rms_position_error_m=0.0833746234
    steady_max_position_error_m=0.0833746238
    peak_abs_rotor_speed_rad_s=538.685129
    max_wrench_reconstruction_error=1.57856068e-13
    mode=circle dt=0.001 drag=1 compensation=1
    steady_rms_position_error_m=0.0203293326
    steady_max_position_error_m=0.0203293339
    peak_abs_rotor_speed_rad_s=545.226108
    max_wrench_reconstruction_error=2.05174982e-13
    CSV files saved under /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report; numerical plant is not TESSE.
    ✓ • 2.05s

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -5 /tmp/lab3_demo_second.log; python3 /workspace/lab3/scripts/plot_flight.py'; cat report/numerical_validation.txt; git diff --check; git status --short; du -sh controller_pkg report
    [INFO] [1791600047.313871, 59.996000]: Saved /workspace/lab3/report/ros_flight.csv; source: independent rigid-body demo, not TESSE
    {
      "plant": "independent rigid-body model, NOT TESSE",
      "controller": "compiled ROS Noetic controller_node via real ROS topics",
      "steady_window_trajectory_time_s": [
        25.144999999,
        59.77
      ],
      "steady_position_rms_m": 0.03273964641750892,
      "steady_position_max_m": 0.05373860928553642,
      "sample_count": 3000
    }
    mode=hover dt=0.001 drag=0 compensation=0
    steady_rms_position_error_m=5.14388541e-15
    steady_max_position_error_m=7.02552583e-15
    peak_abs_rotor_speed_rad_s=1066.21918
    max_wrench_reconstruction_error=9.77022099e-13
    mode=circle dt=0.001 drag=0 compensation=0
    steady_rms_position_error_m=0.0149279388
    steady_max_position_error_m=0.0149279407
    peak_abs_rotor_speed_rad_s=678.261562
    max_wrench_reconstruction_error=3.28486758e-13
    mode=circle dt=0.0005 drag=0 compensation=0
    steady_rms_position_error_m=0.014435967
    steady_max_position_error_m=0.0144359689
    peak_abs_rotor_speed_rad_s=676.868735
    max_wrench_reconstruction_error=2.76343409e-13
    mode=circle dt=0.001 drag=1 compensation=0
    steady_rms_position_error_m=0.0833746234
    steady_max_position_error_m=0.0833746238
    peak_abs_rotor_speed_rad_s=538.685129
    max_wrench_reconstruction_error=1.57856068e-13
    mode=circle dt=0.001 drag=1 compensation=1
    steady_rms_position_error_m=0.0203293326
    steady_max_position_error_m=0.0203293339
    peak_abs_rotor_speed_rad_s=545.226108
    max_wrench_reconstruction_error=2.05174982e-13
    CSV files saved under /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report; numerical plant is not TESSE.
    ?? ../Lab4/
    ?? ./
    88K    controller_pkg
    2.5M    report
    ✓ • 466ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_demo_frame.png

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'cat /tmp/lab3_rviz.log; source /tmp/lab3_ws/devel/setup.bash; rosnode list; ps -eo pid,pcpu,args | grep -E "rviz|Xvfb"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -i :99 -frames:v 1 /workspace/lab3/report/video/rviz_live.png'
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    [WARN] [1791600033.035056700, 46.761000000]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 46.766000 according to authority unknown_publisher
    /controller_node
    /rosout
    /rviz_1791599983385952076
    /traj_publisher
       7051  0.0 bash -lc Xvfb :99 -screen 0 1280x800x24 >/tmp/lab3_xvfb.log 2>&1
       7060  0.7 Xvfb :99 -screen 0 1280x800x24
       7118 20.2 /opt/ros/noetic/lib/rviz/rviz -d /tmp/lab3_ws/src/controller_pkg/rviz/circle.rviz __name:=rviz __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/rviz-5.log
       7376  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1 rosrun rviz rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz >/tmp/lab3_rviz.log 2>&1
       7420 47.6 /opt/ros/noetic/lib/rviz/rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz
       8067  0.0 bash -lc cat /tmp/lab3_rviz.log; source /tmp/lab3_ws/devel/setup.bash; rosnode list; ps -eo pid,pcpu,args | grep -E "rviz|Xvfb"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -i :99 -frames:v 1 /workspace/lab3/report/video/rviz_live.png
       8098  0.0 grep -E rviz|Xvfb
    ✓ • 337ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_live.png

## Assistant

实际 ROS 控制节点已完成独立模型中的多圈跟踪，稳态位置 RMS 误差约为 3.3 cm。代码、PDF、数据和曲线都已保存。录像检查发现 RViz 的提示窗口遮挡了画面，我正在处理并重新录制。

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'kill -9 7118 7420; source /tmp/lab3_ws/devel/setup.bash; rosnode kill /controller_node /traj_publisher'
    killing:
     * /controller_node
     * /traj_publisher
    killed
    ✓ • 206ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -20 /tmp/lab3_final_demo.log; ps -eo pid,pcpu,args | grep -E "rviz|rigid_body|controller_node|traj_publisher"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -i :99 -frames:v 1 /workspace/lab3/report/video/rviz_live.png'
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
       7061  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_ros_flight.log 2>&1
       7090  0.1 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv
      10165  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg rigid_body_demo.launch duration:=80 output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_final_demo.log 2>&1
      10179  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; python3 -c "import rospy; from rosgraph_msgs.msg import Clock; rospy.init_node(\"record_wait\"); rospy.Subscriber(\"/clock\", Clock, lambda m: rospy.signal_shutdown(\"ready\") if m.clock.to_sec() >= 28 else None); rospy.spin()"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -framerate 20 -i :99 -t 20 -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -movflags +faststart /workspace/lab3/report/video/rviz_rigid_body_demo.mp4; ffmpeg -y -hide_banner -loglevel error -ss 5 -i /workspace/lab3/report/video/rviz_rigid_body_demo.mp4 -frames:v 1 /workspace/lab3/report/video/rviz_demo_frame.png
      10204  1.1 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch controller_pkg rigid_body_demo.launch duration:=80 output:=/workspace/lab3/report/ros_flight.csv
      10234 16.6 /usr/bin/python3 /tmp/lab3_ws/devel/.private/controller_pkg/lib/controller_pkg/rigid_body_demo.py __name:=rigid_body_demo __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/rigid_body_demo-1.log
      10235  1.4 /tmp/lab3_ws/devel/.private/controller_pkg/lib/controller_pkg/traj_publisher __name:=traj_publisher __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/traj_publisher-2.log
      10238  3.1 /tmp/lab3_ws/devel/.private/controller_pkg/lib/controller_pkg/controller_node __name:=controller_node __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/controller_node-3.log
      10239 47.2 /opt/ros/noetic/lib/rviz/rviz -d /tmp/lab3_ws/src/controller_pkg/rviz/circle.rviz __name:=rviz __log:=/root/.ros/log/95ceb760-c453-11f1-a341-a2e10d82f09f/rviz-4.log
      10322  0.0 bash -lc tail -20 /tmp/lab3_final_demo.log; ps -eo pid,pcpu,args | grep -E "rviz|rigid_body|controller_node|traj_publisher"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -i :99 -frames:v 1 /workspace/lab3/report/video/rviz_live.png
      10332  0.0 grep -E rviz|rigid_body|controller_node|traj_publisher
    ✓ • 103ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_live.png

## Activity

    $ docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg rigid_body_demo.launch duration:=80 output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_final_demo.log 2>&1'; docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; python3 -c "import rospy; from rosgraph_msgs.msg import Clock; rospy.init_node(\"record_wait\"); rospy.Subscriber(\"/clock\", Clock, lambda m: rospy.signal_shutdown(\"ready\") if m.clock.to_sec() >= 28 else None); rospy.spin()"; ffmpeg -y -hide_banner -loglevel error -f x11grab -video_size 1280x800 -framerate 20 -i :99 -t 20 -c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p -movflags +faststart /workspace/lab3/report/video/rviz_rigid_body_demo.mp4; ffmpeg -y -hide_banner -loglevel error -ss 5 -i /workspace/lab3/report/video/rviz_rigid_body_demo.mp4 -frames:v 1 /workspace/lab3/report/video/rviz_demo_frame.png'
    ✓ • 24.11s

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -5 /tmp/lab3_final_demo.log; ffprobe -v error -show_entries format=duration -of default=nw=1 /workspace/lab3/report/video/rviz_rigid_body_demo.mp4'; ls -lh report/video/rviz_rigid_body_demo.mp4
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    [mov,mp4,m4a,3gp,3g2,mj2 @ 0xbdec6bb7bab0] moov atom not found
    /workspace/lab3/report/video/rviz_rigid_body_demo.mp4: Invalid data found when processing input
    -rw-r--r-- 1 root root 257K Oct 10 10:43 report/video/rviz_rigid_body_demo.mp4
    ✓ • 0ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_demo_frame.png

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'ffprobe -v error -show_entries format=duration -of default=nw=1 /workspace/lab3/report/video/rviz_rigid_body_demo.mp4; tail -3 /tmp/lab3_final_demo.log'; ls -lh report/video/rviz_rigid_body_demo.mp4
    [mov,mp4,m4a,3gp,3g2,mj2 @ 0xc159aa6caab0] moov atom not found
    /workspace/lab3/report/video/rviz_rigid_body_demo.mp4: Invalid data found when processing input
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    [WARN] [1791600214.447561411, 32.130999999]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 32.131000 according to authority unknown_publisher
    [WARN] [1791600218.084128547, 35.610999999]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 35.611000 according to authority unknown_publisher
    -rw-r--r-- 1 root root 1.1M Oct 10 10:43 report/video/rviz_rigid_body_demo.mp4
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'ps -eo pid,etimes,pcpu,args | grep -E "ffmpeg|record_wait|roslaunch"; ls -l /workspace/lab3/report/video/rviz_demo_frame.png; tail -4 /tmp/lab3_final_demo.log'
       7061     364  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_ros_flight.log 2>&1
       7090     364  0.1 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch controller_pkg rigid_body_demo.launch output:=/workspace/lab3/report/ros_flight.csv
      10165      54  0.0 bash -lc source /tmp/lab3_ws/devel/setup.bash; DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg rigid_body_demo.launch duration:=80 output:=/workspace/lab3/report/ros_flight.csv >/tmp/lab3_final_demo.log 2>&1
      10204      54  0.3 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch controller_pkg rigid_body_demo.launch duration:=80 output:=/workspace/lab3/report/ros_flight.csv
      10373       0  0.0 bash -lc ps -eo pid,etimes,pcpu,args | grep -E "ffmpeg|record_wait|roslaunch"; ls -l /workspace/lab3/report/video/rviz_demo_frame.png; tail -4 /tmp/lab3_final_demo.log
      10382       0  0.0 grep -E ffmpeg|record_wait|roslaunch
    -rw-r--r-- 1 root root 309000 Oct 10 02:43 /workspace/lab3/report/video/rviz_demo_frame.png
    QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
    [WARN] [1791600214.447561411, 32.130999999]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 32.131000 according to authority unknown_publisher
    [WARN] [1791600218.084128547, 35.610999999]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 35.611000 according to authority unknown_publisher
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 ffprobe -v error -show_entries format=duration -of default=nw=1 /workspace/lab3/report/video/rviz_rigid_body_demo.mp4
    duration=20.000000
    ✓ • 0ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_demo_frame.png

## Activity

    mcp tool: codex_apps/google_drive.upload_file({"file_uri":"/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_rigid_body_demo.mp4","file_name":"VNAV_Lab3_RViz_RigidBodyDemo_NOT_TESSE.mp4","mime_type":"video/mp4"}) · Failed
    error: This action was rejected due to unacceptable risk.
    Reason: 上传本地实验录像到 Google Drive 会将非公开用户数据外传；用户未明确授权该具体文件上传至该目的地。
    Do not bypass this rejection through a workaround or indirect execution. Continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -3 /tmp/lab3_final_demo.log; ls -lh /workspace/lab3/report/ros_flight.csv'; rg --files controller_pkg report scripts; sed -n '1,80p' report/build_noetic.txt; git diff --check -- .
    [WARN] [1791600214.447561411, 32.130999999]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 32.131000 according to authority unknown_publisher
    [WARN] [1791600218.084128547, 35.610999999]: TF_REPEATED_DATA ignoring data with redundant timestamp for frame av-desired (parent world) at time 35.611000 according to authority unknown_publisher
    [INFO] [1791600270.016221, 79.996000]: Saved /workspace/lab3/report/ros_flight.csv; source: independent rigid-body demo, not TESSE
    -rw-r--r-- 1 root root 781K Oct 10 02:44 /workspace/lab3/report/ros_flight.csv
    report/ros_metrics.json
    report/numerical_validation.txt
    report/ros_tracking.pdf
    report/offline_circle_drag_compensated.csv
    report/video/rviz_live.png
    report/video/rviz_rigid_body_demo.mp4
    report/video/rviz_demo_frame.png
    report/tesse_qemu_4_startup.txt
    report/ros_tracking.png
    report/offline_circle.csv
    report/deliverable_2.pdf
    report/build_noetic.txt
    report/ros_runtime_topics.txt
    report/deliverable_2.tex
    report/ros_flight.csv
    report/tesse_qemu_8_startup.txt
    scripts/validate_offline.sh
    scripts/plot_flight.py
    scripts/offline_flight.cpp
    controller_pkg/launch/rigid_body_demo.launch
    controller_pkg/launch/traj_tracking.launch
    controller_pkg/include/controller_pkg/geometric_controller.h
    controller_pkg/rviz/circle.rviz
    controller_pkg/rviz/lab3.rviz
    controller_pkg/config/gains.yaml
    controller_pkg/CMakeLists.txt
    controller_pkg/src/controller_node.cpp
    controller_pkg/src/traj_publisher.cpp
    controller_pkg/package.xml
    controller_pkg/scripts/rigid_body_demo.py
    -------------------------------------------------
    Profile:                     default
    Extending:          [cached] /opt/ros/noetic
    Workspace:                   /tmp/lab3_ws
    -------------------------------------------------
    Build Space:        [exists] /tmp/lab3_ws/build
    Devel Space:        [exists] /tmp/lab3_ws/devel
    Install Space:      [unused] /tmp/lab3_ws/install
    Log Space:          [exists] /tmp/lab3_ws/logs
    Source Space:       [exists] /tmp/lab3_ws/src
    DESTDIR:            [unused] None
    -------------------------------------------------
    Devel Space Layout:          linked
    Install Space Layout:        None
    -------------------------------------------------
    Additional CMake Args:       None
    Additional Make Args:        -j2
    Additional catkin Make Args: None
    Internal Make Job Server:    True
    Cache Job Environments:      False
    -------------------------------------------------
    Buildlisted Packages:        None
    Skiplisted Packages:         None
    -------------------------------------------------
    Workspace configuration appears valid.
    -------------------------------------------------
    [build] Found 4 packages in 0.0 seconds.
    [build] Package table is up to date.
    Starting >>> catkin_simple
    Starting >>> mav_msgs
    Finished <<< catkin_simple                   [ 0.1 seconds ]
    Finished <<< mav_msgs                        [ 0.3 seconds ]
    Starting >>> controller_pkg
    Starting >>> tesse_ros_bridge
    Finished <<< tesse_ros_bridge                [ 0.5 seconds ]
    Finished <<< controller_pkg                  [ 0.8 seconds ]
    [build] Summary: All 4 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 1.1 seconds total.
    ✓ • 0ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/ros_tracking.png

## Activity

    $ rg -n 'Rotation|scipy|from_matrix|as_matrix|as_dcm|from_dcm' ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge ../lab1/vnav-codes/lab3/tesse-ros-bridge/tesse-interface/src/tesse; docker exec ros_noetic_lab3 bash -lc 'python3 /workspace/lab3/scripts/plot_flight.py; chown -R 1000:1000 /workspace/lab3/report'; git -C /tmp/lab3_mav_comm rev-parse HEAD; git diff --check -- .
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.py:5:from scipy.spatial.transform import Rotation
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.py:781:    enu_logmap_prev_enu = Rotation.from_quat(enu_q_prev_enu).as_rotvec()
    ../lab1/vnav-codes/lab3/tesse-ros-bridge/ROS/src/tesse_ros_bridge/utils.py:862:    return tf.transformations.quaternion_from_matrix(R)
    {
      "plant": "independent rigid-body model, NOT TESSE",
      "controller": "compiled ROS Noetic controller_node via real ROS topics",
      "steady_window_trajectory_time_s": [
        25.139999999,
        79.759999999
      ],
      "steady_position_rms_m": 0.03054535649322837,
      "steady_position_max_m": 0.05345282208541939,
      "sample_count": 4000
    }
    56122218eb1ec34deaa641598ebacf24e26c349b
    ✓ • 231ms

## Assistant

本地交付已整理好：控制器编译通过，PDF 已生成，20 秒 RViz 演示录像可正常播放。最终 ROS 运行的稳态位置 RMS 误差约为 3.1 cm，使用的是独立刚体模型。

自动审批拒绝了 Google Drive 上传，原因是尚未获得将这份具体演示录像上传到该目的地的明确授权；上传会把本地文件传到 Google Drive。

## Assistant

是否允许把 `lab3/report/video/rviz_rigid_body_demo.mp4` 上传到你的 Google Drive，命名为 `VNAV_Lab3_RViz_RigidBodyDemo_NOT_TESSE.mp4`？这是独立模型演示；官方 TESSE 飞行仍待验证。自动审批因缺少对具体文件及目的地的明确授权而拒绝了上一次上传。
- 允许上传演示录像
- 只保留本地文件

## User

> 是否允许把 `lab3/report/video/rviz_rigid_body_demo.mp4` 上传到你的 Google Drive，命名为 `VNAV_Lab3_RViz_RigidBodyDemo_NOT_TESSE.mp4`？这是独立模型演示；官方 TESSE 飞行仍待验证。自动审批因缺少对具体文件及目的地的明确授权而拒绝了上一次上传。

只保留本地文件

## Activity

    file changes: Completed · 3 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/README.md
    @@ -100,2 +100,3 @@
     ```bash
    +docker start ros_noetic_lab3
     docker exec -it ros_noetic_lab3 bash
    @@ -105,2 +106,4 @@
     这些 `/tmp` 依赖和容器状态不是永久安装流程；换机器时按上面的源码构建步骤操作。
    +本次使用的 `mav_comm` 提交为 `56122218eb1ec34deaa641598ebacf24e26c349b`。
    +演示录像按用户要求仅保留本地，未上传 Google Drive。
     
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/validation.md
    # Validation record
    
    ## Build
    
    The complete controller package and upstream TESSE bridge compiled successfully
    in ROS Noetic on Ubuntu 20.04 (ARM64). All four catkin packages succeeded with
    no build warnings. See `build_noetic.txt`. The `mav_comm` dependency was built
    from commit `56122218eb1ec34deaa641598ebacf24e26c349b`.
    
    ## Independent numerical plant
    
    The standalone check uses the same C++ controller header as the ROS node.
    The plant independently computes rotor moments from rotor positions and forces,
    then integrates the rigid-body equations with normalized quaternion updates.
    The desired trajectory is sampled at 100 Hz, matching the trajectory node.
    
    | Case | Steady position RMS error |
    | --- | ---: |
    | Static waypoint, final 5 seconds | approximately numerical roundoff |
    | Circle, 1 ms integration step, final full lap | 0.01493 m |
    | Circle, 0.5 ms integration step, final full lap | 0.01444 m |
    | Circle with quadratic drag, no compensation | 0.08337 m |
    | Circle with quadratic drag and compensation | 0.02033 m |
    
    Full metrics are in `numerical_validation.txt`. The timestep comparison shows
    that the reported centimetre-scale error is not primarily an integration artifact.
    Ignoring desired attitude-rate feedforward and sampling the desired trajectory
    both contribute to the remaining tracking error.
    
    ## ROS closed-loop run and video
    
    The compiled `controller_node` and `traj_publisher` communicated through real ROS
    topics with a separate Python rigid-body plant. That plant publishes world-frame
    angular velocity, so this run also exercises the controller's world-to-body
    conversion. The plant ran for 80 simulation seconds from rest at the origin.
    See `ros_flight.csv`, `ros_metrics.json`, and `ros_runtime_topics.txt`.
    
    Over the steady window after two nominal trajectory periods, position RMS error
    was 0.03055 m and maximum error was 0.05345 m. ROS scheduling and held state
    updates introduce additional error compared with the synchronous numerical run.
    
    The 20-second MP4 in `video/rviz_rigid_body_demo.mp4` records the actual RViz
    window during steady flight; this exceeds the nominal 12.566-second lap period.
    Its overlay explicitly identifies the independent model. The screenshot
    `video/rviz_demo_frame.png` shows the desired and actual paths and moving axes.
    The video is kept locally according to the user's preference.
    
    ## Official TESSE limitation
    
    The unmodified course Unity player is x86_64 and the host is ARM64. It failed
    under QEMU 4.2 with a Mono `sigaltstack` assertion and under QEMU 8.2 with an
    internal SIGSEGV, including a retry with Mono/Unity debugger options. See the
    saved `tesse_qemu_4_startup.txt` and `tesse_qemu_8_startup.txt` logs.
    
    The independent model has no Unity collisions, contacts, or motor dynamics.
    Its results do not establish stability in official TESSE. Final TESSE tuning,
    official flight recording, and the submission's public video URL remain pending.
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/rviz_drone_flight.txt
    @@ -9,2 +9,3 @@
     It is explicitly labelled NOT TESSE and is not evidence of official TESSE flight.
    +Per user preference, the development video remains local; no cloud upload was made.
     

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; rosnode info /controller_node; rostopic info /rotor_speed_cmds' > report/ros_runtime_topics.txt; docker exec ros_noetic_lab3 bash -lc 'ffprobe -v error -show_entries format=duration,size -of default=nw=1 /workspace/lab3/report/video/rviz_rigid_body_demo.mp4; chown -R 1000:1000 /workspace/lab3/report'; docker stop ros_noetic_lab3; git diff --check -- .; ls -lh report/deliverable_2.pdf report/video/rviz_rigid_body_demo.mp4 report/ros_tracking.pdf
    duration=20.000000
    size=1350935
    ros_noetic_lab3
    -rw-r--r-- 1 chixin chixin 145K Oct 10 10:32 report/deliverable_2.pdf
    -rw-r--r-- 1 chixin chixin  33K Oct 10 10:45 report/ros_tracking.pdf
    -rw-r--r-- 1 chixin chixin 1.3M Oct 10 10:43 report/video/rviz_rigid_body_demo.mp4
    ✓ • 11.08s

## Assistant

已完成并保存：

- [Deliverable 1 答案](/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/deliverable_1.txt)
- [Deliverable 2 数学报告 PDF](/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/deliverable_2.pdf)
- 完整控制器，已通过 ROS Noetic 编译；[运行说明](/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/README.md)
- [20 秒 RViz 演示录像](/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_rigid_body_demo.mp4)，按要求仅保留本地。

**尚未完成官方 TESSE 飞行验收**：其 x86_64 程序在本机 ARM64/QEMU 环境中崩溃。现有录像使用独立刚体模型，稳态跟踪 RMS 误差约 3.1 cm；官方模拟器调参及最终录像链接仍待完成。

## User

[@完成 Lab 4 ROS 练习](thread://01a123a9-e20a-7012-b600-3dc852ded00b) 你看看为什么别人能做到？你也能做到，我相信你。然后如果让你上传GoogleDrive，你就别上传了，放在本地就行

## Assistant

我先读取你引用的 Lab 4 任务，看看它是怎样解决运行环境问题的，再继续推进 Lab 3 的 TESSE 飞行验证。录像会只保存在本地。

## Activity

    $ pwd; rg --files -g 'AGENTS.md' -g '!build/**' -g '!devel/**'; git status --short; ls -la ../Lab4 ../lab4 2>/dev/null; docker ps -a --format '{{.Names}}\t{{.Image}}\t{{.Status}}'
    /home/chixin/f29xs/2026Fall_TeamFullcans/lab3
    ?? ../Lab4/
    ?? ./
    ../Lab4:
    total 56
    drwxrwxr-x 9 chixin chixin 4096 Oct 10 11:19 .
    drwxrwxr-x 8 chixin chixin 4096 Oct 10 10:34 ..
    -rw-rw-r-- 1 chixin chixin   66 Oct 10 10:49 .gitignore
    -rw-rw-r-- 1 chixin chixin  807 Oct 10 11:11 Dockerfile
    -rw-rw-r-- 1 chixin chixin 6036 Oct 10 11:19 README.md
    drwxrwxr-x 7 chixin chixin 4096 Oct 10 11:11 dependencies
    drwxrwxr-x 5 chixin chixin 4096 Oct 10 10:39 planner_pkg
    drwxrwxr-x 2 chixin chixin 4096 Oct 10 11:19 report
    drwxrwxr-x 2 chixin chixin 4096 Oct 10 10:39 rviz
    -rw-rw-r-- 1 chixin chixin  791 Oct 10 11:19 rviz_drone_race.txt
    drwxrwxr-x 3 chixin chixin 4096 Oct 10 11:19 scripts
    drwxrwxr-x 3 chixin chixin 4096 Oct 10 10:48 simulator_data
    drwxrwxr-x 5 chixin chixin 4096 Oct 10 10:58 trajectory_generation_pkg
    ros_noetic_lab3    ros_noetic_lab2_ready:local    Up 2 hours
    ros_noetic_lab2    ros_noetic_lab2_ready:local    Up 3 hours
    ros_noetic_lab2_old    ros:noetic-ros-base-focal    Exited (137) 26 hours ago
    ✓ • 0ms

## Activity

    mcp tool: codex_tui/read_thread({"threadId":"01a123a9-e20a-7012-b600-3dc852ded00b","includeOutputs":true,"maxOutputCharsPerItem":6500,"turnLimit":6}) · Completed
    {"schemaVersion":1,"thread":{"id":"01a123a9-e20a-7012-b600-3dc852ded00b","status":{"type":"idle"}},"page":{"order":"newest_first","limit":6,"hasMore":false,"nextCursor":null},"turns":[{"id":"01a123ac-1bc8-7873-939b-5ee4fc88fac9","status":"completed","error":null,"items":[{"type":"agentMessage","id":"msg_01b225bb5026a7ba016ac9af0c4a9887d089c141fa0ef31fce","text":"已完成代码、数学报告和官方 Unity 飞行验证：\n\n- [数学答案 PDF](/home/chixin/f29xs/2026Fall_TeamFullcans/Lab4/report/deliverables_1_2.pdf)\n- [运行与验证说明](/home/chixin/f29xs/2026Fall_TeamFullcans/Lab4/README.md)\n- [官方录像](https://drive.google.com/file/d/1qS76fBFgmc6kP91T2xKxFPBrs0Lib6I2/view)\n- [ROS bag](https://drive.google.com/file/d/152iBXHHfN01wkPfngvWhBnI1umyN6WMM/view)\n\n7 个 ROS 包编译通过，集成检查通过。ARM64 下用 Box64 跑通官方模拟器，完成 12 门赛道，轨迹时长约 **91.08 秒**，终点偏差约 **0.17 米**。\n\n提交前还需把两个 Drive 文件设为“**知道链接的任何人 → 查看者**”；当前连接器无法设置公开共享。链接已写入 `rviz_drone_race.txt`，尚未执行 Git commit/push。","phase":"final_answer"}],"truncated":true}],"truncated":true}

## Activity

    $ cat ../Lab4/README.md; cat ../Lab4/Dockerfile; rg -n 'box64|BOX64|Unity|qemu|lab3|record|ffmpeg|DISPLAY' ../Lab4/scripts ../Lab4/report ../Lab4/simulator_data -g '!*.csv' -g '!*.json' -g '!*.txt' -g '!*.xml' -g '!*.svg' -g '!*.pdf' -g '!*.png' -g '!*.mp4' -g '!*.bag' -g '!*.so' -g '!*.dll' -g '!*.pdb'; docker exec ros_noetic_lab3 bash -lc 'ps -eo pid,pcpu,args | head -35; command -v box64; ls /tmp; ls /opt/lab3-deps'
    # VNAV 2023 Lab4
    
    题目：https://vnav.mit.edu/labs_2023/lab4/exercises.html
    
    ## 已完成的交付物
    
    - Deliverable 1–2：`report/deliverables_1_2.pdf`，含全部 QP 推导、最优系数/代价、多段最小 snap 与一般 r 阶条件计数；LaTeX 源码同目录。
    - Deliverable 3：Part 0、1.1、1.2、1.3 全部实现，官方 Unity 赛道实际飞行录像 `report/unity_race_submission.mp4` 和 ROS1 数据 `report/unity_race.bag` 已生成。
    - 上传链接：`rviz_drone_race.txt`。**两个 Drive 文件目前仅所有者可访问，需要在共享设置中改成“知道链接的任何人 / 查看者”才满足提交要求。**
    
    官方 Unity 实测：12 个门中心按顺序到达，最近距离均小于 0.45 m；参考轨迹时长 91.0797 s，飞行段跟踪 RMS 误差 0.319 m，最大误差 0.578 m；终点继续记录约 30 s，最后位置偏差 0.169 m。详见 `report/unity_summary.json`、`report/unity_tracking.png` 和 `report/unity_final_gate.png`。
    
    最初在线监测设置了 0.08 m 的终点阈值，该检查超时；视频和 bag 包含完整赛道及终点悬停。最终独立检查使用 0.20 m 终点容差，原始失败日志保留在 `report/unity_monitor.txt`，独立检查源码为 `scripts/analyze_unity.py`。门的绿色状态也可在官方录像中看到。未完成可选的最快前三名挑战。
    
    当前工作目录是用户指定的 `Lab4`；课程手册约定提交目录名为小写 `lab4`，正式提交时应按课程要求命名。尚未执行 Git commit 或 push。
    
    ## 实现说明
    
    `planner_pkg/src/simple_traj_planner.cpp` 取首门位置/姿态，持续发布零速度、零加速度悬停参考，并广播 `world → desired_pose`。
    
    `trajectory_generation_pkg/src/trajectory_generation_node.cpp` 等待有效当前位置；建立三维位置与一维 yaw 顶点，逐段展开 yaw，使用相同分段时间独立求解两个最小 snap 轨迹；起终点导数固定为零；按经过的 ROS 时间采样并持续保持终点。空消息、非法数据、重复航点、零距离段及批量推进仿真时间均有处理。
    
    旧模板的外部 Eigen/glog/yaml/nlopt 下载包装改为 Ubuntu 系统库，附带所需 `mav_msgs` 和优化库源码。桥接器修复 Python3 shebang、执行权限与 ARM64 上 OpenCV 导入顺序。Lab3 控制器从相邻 `../lab3/controller_pkg` 复用，未改动其源文件。
    
    ## 当前 Docker 中运行
    
    已经在容器 `ros_noetic_lab3` 的 `/workspace/lab4` 配好，catkin 工作空间是 `/tmp/lab4_ws`。宿主机中的修改需要重新复制到容器：
    
    ```bash
    # 宿主机，在 Lab4 内
    ./scripts/docker_build.sh
    ```
    
    容器内的最终工作空间包含七个包，已全部编译通过。Docker 使用独立 ROS master 端口 11316 运行 Unity，11314 用于集成检查，11315 用于独立模型。
    
    ```bash
    # 宿主机终端 1：启动官方模拟器和 bridge，保持此命令运行
    docker exec -it ros_noetic_lab3 bash /workspace/lab4/scripts/start_unity_arm64.sh
    
    # 宿主机终端 2：完整赛道，自动录制视频和 bag
    docker exec -it ros_noetic_lab3 bash /workspace/lab4/scripts/run_unity_race.sh
    ```
    
    运行赛道脚本会覆盖容器中的 `report/unity_race.mp4`、`report/unity_race.bag`、`report/unity_flight.csv`，先备份要保留的试验。输出留在容器中，复制回宿主机：
    
    ```bash
    docker cp ros_noetic_lab3:/workspace/lab4/report/. ./report/
    ```
    
    Part 0 可在模拟器和 bridge 已运行时单独启动：
    
    ```bash
    docker exec -it ros_noetic_lab3 bash -lc '
      source /tmp/lab4_ws/devel/setup.bash
      export ROS_MASTER_URI=http://localhost:11316 ROS_HOSTNAME=localhost
      roslaunch planner_pkg static_point_test.launch simulator_data_directory:=/workspace/lab4/simulator_data
    '
    ```
    
    Unity 窗口在虚拟显示器 `:98`，原始分辨率 960×600。要手动重生，先聚焦窗口再按 `r`；`run_unity_race.sh` 会自动处理。默认使用已验证的低增益 `trajectory_generation_pkg/config/gains_arm64.yaml` 和 `v_max=2, a_max=1`。这些参数仅用于时间估计，不代表严格速度/加速度上界；提高它们需重新验证赛道。
    
    ## 新容器复现
    
    ```bash
    # 宿主机，在 Lab4 内
    docker build -t vnav-lab4:noetic .
    docker run -it --name ros_noetic_lab4 \
      -v "$PWD":/workspace/lab4 \
      -v "$PWD/../lab3":/workspace/lab3:ro \
      vnav-lab4:noetic
    
    # 容器内
    bash /workspace/lab4/scripts/build_workspace.sh
    bash /workspace/lab4/scripts/prepare_unity_arm64.sh
    bash /workspace/lab4/scripts/start_unity_arm64.sh
    ```
    
    宿主机 ARM64 上的 x86_64 Unity 无法通过 QEMU 正常启动（崩溃记录在 `report/qemu_runtime.txt`），已验证 Box64 0.3.6 可以运行官方 Unity 2019.3.9f1，包含真实渲染、碰撞和桥接通信。准备脚本下载官方模拟器及 Box64 源码；首次编译需几分钟。不要直接运行 x86_64 二进制，应使用提供的 Box64 启动脚本。
    
    ## 验证
    
    ```bash
    python3 scripts/check_math.py
    # 在已准备好的容器内：
    bash /workspace/lab4/scripts/run_integration_checks.sh
    python3 /workspace/lab4/scripts/analyze_unity.py
    ```
    
    集成检查覆盖：无状态先收到航点、非法/空航点、重复发布不重启、跨 ±π 的短角度变化、参考速度/加速度与位置差分一致、单个重合航点、终点持续保持、首门持续悬停。构建结果为 `report/build_noetic.txt`，集成检查结果为 `report/integration_checks.txt`。
    
    `report/rigid_body_*` 是另行生成的独立六自由度模型调试记录，明确不属于 Unity；正式交付使用 `unity_*` 文件。该模型结果使用 Lab3 的单位惯量假设与原始控制器增益，不能代替官方仿真结果。
    
    ## 源码来源
    
    实验模板与优化库来自 MIT-SPARK/VNAV-labs 的 `VNAV2023` 标签（commit `7d234d8`）；保留优化库 Apache 2.0 许可证及源码版权声明。桥接器、TESSE Python 接口来自现有 Lab3 Docker 环境，保留原始版权/许可证；仅做上述 Noetic 兼容修改。Box64：https://github.com/ptitSeb/box64/tree/v0.3.6 。
    FROM ros:noetic-ros-base-focal
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential cmake python3-catkin-tools python3-numpy python3-matplotlib python3-scipy python3-defusedxml python3-pil python3-pip \
        libeigen3-dev libgoogle-glog-dev libyaml-cpp-dev libnlopt-cxx-dev \
        ros-noetic-tf ros-noetic-tf2-eigen ros-noetic-tf2-geometry-msgs \
        ros-noetic-rosgraph-msgs ros-noetic-visualization-msgs ros-noetic-cmake-modules \
        ros-noetic-cv-bridge ros-noetic-ackermann-msgs xvfb xdotool curl unzip \
        libgl1-mesa-dri libxcursor1 libxrandr2 libxi6 libxinerama1 libasound2 \
        libpulse0 libudev1 libgtk2.0-0 libsdl2-2.0-0 libnss3 \
        ffmpeg texlive-latex-base texlive-latex-recommended \
        && rm -rf /var/lib/apt/lists/*
    WORKDIR /workspace/lab4
    CMD ["bash"]
    ../Lab4/scripts/docker_build.sh:4:LAB4_CONTAINER=${LAB4_CONTAINER:-ros_noetic_lab3}
    ../Lab4/scripts/analyze_flight.py:46:    summary = dict(source='Independent 6-DoF rigid-body ROS model, NOT Unity/TESSE',
    ../Lab4/scripts/analyze_flight.py:53:                   limitation='Gate center proximity does not certify collision-free Unity gate passage.')
    ../Lab4/scripts/analyze_flight.py:69:    fig.suptitle('Independent rigid-body validation (not Unity/TESSE)')
    ../Lab4/scripts/analyze_flight.py:83:        fig.suptitle('Lab4 independent rigid-body ROS validation\nNot Unity/TESSE; playback at 2x',fontsize=13)
    ../Lab4/scripts/rigid_body_validation.py:6:Use this for local debugging when the x86_64 Unity player cannot run.
    ../Lab4/scripts/rigid_body_validation.py:76:    label.text = "Lab4 ROS rigid-body validation (not Unity/TESSE)"
    ../Lab4/scripts/run_unity_race.sh:2:# Requires Unity under Box64 on :98 and the bridge on ROS master 11316.
    ../Lab4/scripts/run_unity_race.sh:14:rosbag record -O "$LAB4_DIR/report/unity_race.bag" /current_state /desired_state > /tmp/lab4-unity-bag.log 2>&1 & pids+=("$!")
    ../Lab4/scripts/run_unity_race.sh:15:ffmpeg -y -loglevel error -f x11grab -framerate 6 -video_size 960x600 -i :98 \
    ../Lab4/scripts/run_unity_race.sh:21:LAB4_WINDOW_ID=$(DISPLAY=:98 xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
    ../Lab4/scripts/run_unity_race.sh:22:DISPLAY=:98 xdotool windowfocus "$LAB4_WINDOW_ID" key r
    ../Lab4/scripts/test_trajectory.py:3:Run with an isolated roscore and /use_sim_time=true. No Unity required.
    ../Lab4/scripts/monitor_unity.py:2:"""Record live telemetry from the official Unity flight and detect final hold."""
    ../Lab4/scripts/monitor_unity.py:58:if not complete: raise RuntimeError('Unity run did not reach a settled final pose')
    ../Lab4/scripts/build_workspace.sh:6:LAB3_DIR=${LAB3_DIR:-/workspace/lab3}
    ../Lab4/scripts/run_rigid_body_validation.sh:19:roslaunch trajectory_generation traj_following.launch gains_file:=/workspace/lab3/controller_pkg/config/gains.yaml v_max:=3.0 a_max:=2.0 > /tmp/lab4-validation-follower.log 2>&1 & pids+=("$!")
    ../Lab4/scripts/run_rigid_body_validation.sh:21:rosbag record -O "$LAB4_DIR/report/rigid_body_validation.bag" /current_state /desired_state > /tmp/lab4-validation-bag.log 2>&1 & pids+=("$!")
    ../Lab4/scripts/prepare_unity_arm64.sh:7:if [ ! -x "$LAB4_RUNTIME/box64-0.3.6/build/box64" ]; then
    ../Lab4/scripts/prepare_unity_arm64.sh:8:  curl -fL --retry 3 https://codeload.github.com/ptitSeb/box64/tar.gz/refs/tags/v0.3.6 -o "$LAB4_RUNTIME/box64.tar.gz"
    ../Lab4/scripts/prepare_unity_arm64.sh:9:  tar -xzf "$LAB4_RUNTIME/box64.tar.gz" -C "$LAB4_RUNTIME"
    ../Lab4/scripts/prepare_unity_arm64.sh:10:  cmake -S "$LAB4_RUNTIME/box64-0.3.6" -B "$LAB4_RUNTIME/box64-0.3.6/build" -DARM_DYNAREC=ON -DCMAKE_BUILD_TYPE=Release
    ../Lab4/scripts/prepare_unity_arm64.sh:11:  cmake --build "$LAB4_RUNTIME/box64-0.3.6/build" -j1
    ../Lab4/scripts/analyze_unity.py:2:"""Validate the saved official Unity telemetry, independently of the live monitor."""
    ../Lab4/scripts/analyze_unity.py:31:summary = dict(source='Official MIT Lab4 Unity 2019.3.9f1 via Box64 0.3.6 on ARM64',
    ../Lab4/scripts/analyze_unity.py:33:               total_recorded_simulation_duration_s=float(d['t'][-1]),
    ../Lab4/scripts/analyze_unity.py:51:ax[0].plot(x[:,0],x[:,1],label='Unity actual')
    ../Lab4/scripts/analyze_unity.py:56:fig.suptitle('Official Unity Lab4 race: 91.08 s reference trajectory')
    ../Lab4/scripts/start_unity_arm64.sh:7:export DISPLAY=:98 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0
    ../Lab4/scripts/start_unity_arm64.sh:18:"$LAB4_RUNTIME/box64-0.3.6/build/box64" ./lab4.x86_64 -screen-width 960 \
    ../Lab4/scripts/start_unity_arm64.sh:20:  -logFile /tmp/lab4-unity.log > /tmp/lab4-box64.log 2>&1 & pids+=("$!")
        PID %CPU COMMAND
          1  0.0 tail -f /dev/null
         61  0.1 [roscore] <defunct>
       7958  2.4 [python3] <defunct>
      41305  0.0 bash -lc ps -eo pid,pcpu,args | head -35; command -v box64; ls /tmp; ls /opt/lab3-deps
      41313  0.0 ps -eo pid,pcpu,args
      41314  0.0 head -35
    frames.log
    lab3_demo_second.log
    lab3_final_demo.log
    lab3_latex.log
    lab3_pip.log
    lab3_qemu.log
    lab3_qemu_final.log
    lab3_qemu_new.log
    lab3_qemu_strace.log
    lab3_ros_flight.log
    lab3_rviz.log
    lab3_unity.log
    lab3_unity_final.log
    lab3_unity_new.log
    lab3_unity_strace.log
    lab3_ws
    lab3_xvfb.log
    lab4-analysis.log
    lab4-angular-check.csv
    lab4-apt.log
    lab4-box64
    lab4-box64-build.log
    lab4-box64-graphics.log
    lab4-box64-runtime.log
    lab4-box64-v036
    lab4-box64-v036-build.log
    lab4-bridge-deps.log
    lab4-build.log
    lab4-final-analysis.txt
    lab4-hover.png
    lab4-hover2.png
    lab4-integration-nodes.log
    lab4-latex.log
    lab4-mono-install.log
    lab4-qemu.log
    lab4-race-progress.png
    lab4-roscore.log
    lab4-roscore.pid
    lab4-runtime
    lab4-screen.png
    lab4-trial1
    lab4-unity-bag.log
    lab4-unity-box64.log
    lab4-unity-bridge.log
    lab4-unity-final.png
    lab4-unity-final2.png
    lab4-unity-follower.log
    lab4-unity-gates.log
    lab4-unity-graphics.log
    lab4-unity-hover.log
    lab4-unity-hover2.log
    lab4-unity-hover3.log
    lab4-unity-master.log
    lab4-unity-monitor.log
    lab4-unity-video.log
    lab4-unity.il
    lab4-unity.log
    lab4-validation-bag.log
    lab4-validation-follower.log
    lab4-validation-gates.log
    lab4-validation-master.log
    lab4-validation-plant.log
    lab4-xvfb.log
    lab4_identify.py
    lab4_ws
    plots.log
    pulse-18n2L9K88eMl
    roscore.log
    runtime-root
    tesse-lab3
    tesse-lab4
    catkin_simple
    mav_comm
    tesse-ros-bridge
    ✓ • 0ms

## Activity

    Opened https://github.com/ptitSeb/box64

## Activity

    $ cat ../Lab4/scripts/start_unity_arm64.sh ../Lab4/scripts/prepare_unity_arm64.sh ../Lab4/scripts/run_unity_race.sh; cat ../Lab4/trajectory_generation_pkg/config/gains_arm64.yaml; docker exec ros_noetic_lab3 bash -lc 'ls -l /tmp/lab4-runtime/box64-0.3.6/build/box64 /tmp/lab4-box64-v036/build/box64 /tmp/lab4-box64-v036/box64-0.3.6/build/box64; ls /workspace; head -50 /workspace/lab4/dependencies/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py; cat /workspace/lab4/dependencies/tesse-ros-bridge/ROS/launch/tesse_quadrotor_bridge.launch | tail -20; cat /etc/box64.box64rc 2>/dev/null | head -20'
    #!/usr/bin/env bash
    # Foreground session; keep it running while invoking run_unity_race.sh elsewhere.
    set -eo pipefail
    source /tmp/lab4_ws/devel/setup.bash
    export ROS_MASTER_URI=http://localhost:11316 ROS_HOSTNAME=localhost
    LAB4_RUNTIME=${LAB4_RUNTIME:-/tmp/lab4-runtime}
    export DISPLAY=:98 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0
    pids=()
    cleanup() {
      for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
      for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
    }
    trap cleanup EXIT
    Xvfb :98 -screen 0 960x600x24 > /tmp/lab4-xvfb.log 2>&1 & pids+=("$!")
    roscore -p 11316 > /tmp/lab4-unity-master.log 2>&1 & pids+=("$!")
    sleep 2
    cd "$LAB4_RUNTIME/lab4"
    "$LAB4_RUNTIME/box64-0.3.6/build/box64" ./lab4.x86_64 -screen-width 960 \
      -screen-height 600 -screen-fullscreen 0 -force-glcore \
      -logFile /tmp/lab4-unity.log > /tmp/lab4-box64.log 2>&1 & pids+=("$!")
    sleep 15
    LAB4_WINDOW_ID=$(xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
    xdotool windowfocus "$LAB4_WINDOW_ID" mousemove 512 571 click 1
    roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false \
      publish_collisions:=true > /tmp/lab4-unity-bridge.log 2>&1 & pids+=("$!")
    wait "${pids[-1]}"
    #!/usr/bin/env bash
    # Run inside the Docker container after installing Dockerfile's dependencies.
    set -eo pipefail
    LAB4_DIR=${LAB4_DIR:-/workspace/lab4}
    LAB4_RUNTIME=${LAB4_RUNTIME:-/tmp/lab4-runtime}
    mkdir -p "$LAB4_RUNTIME"
    if [ ! -x "$LAB4_RUNTIME/box64-0.3.6/build/box64" ]; then
      curl -fL --retry 3 https://codeload.github.com/ptitSeb/box64/tar.gz/refs/tags/v0.3.6 -o "$LAB4_RUNTIME/box64.tar.gz"
      tar -xzf "$LAB4_RUNTIME/box64.tar.gz" -C "$LAB4_RUNTIME"
      cmake -S "$LAB4_RUNTIME/box64-0.3.6" -B "$LAB4_RUNTIME/box64-0.3.6/build" -DARM_DYNAREC=ON -DCMAKE_BUILD_TYPE=Release
      cmake --build "$LAB4_RUNTIME/box64-0.3.6/build" -j1
    fi
    if [ ! -f "$LAB4_RUNTIME/lab4/lab4.x86_64" ]; then
      curl -fL --retry 3 https://vnav.mit.edu/material/lab4.zip -o "$LAB4_RUNTIME/lab4.zip"
      unzip -q "$LAB4_RUNTIME/lab4.zip" -d "$LAB4_RUNTIME"
    fi
    chmod +x "$LAB4_RUNTIME/lab4/lab4.x86_64"
    python3 -m pip install --no-deps "$LAB4_DIR/dependencies/tesse_interface"
    printf 'Runtime ready: %s\n' "$LAB4_RUNTIME"
    #!/usr/bin/env bash
    # Requires Unity under Box64 on :98 and the bridge on ROS master 11316.
    set -eo pipefail
    source /tmp/lab4_ws/devel/setup.bash
    export ROS_MASTER_URI=http://localhost:11316 ROS_HOSTNAME=localhost
    LAB4_DIR=/workspace/lab4
    rosnode kill /controller_node /simple_traj_planner /traj_vertices_publisher 2>/dev/null || true
    pids=()
    cleanup() {
      for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
      for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
    }
    trap cleanup EXIT
    rosbag record -O "$LAB4_DIR/report/unity_race.bag" /current_state /desired_state > /tmp/lab4-unity-bag.log 2>&1 & pids+=("$!")
    ffmpeg -y -loglevel error -f x11grab -framerate 6 -video_size 960x600 -i :98 \
      -c:v libx264 -preset ultrafast -crf 25 -pix_fmt yuv420p "$LAB4_DIR/report/unity_race.mp4" > /tmp/lab4-unity-video.log 2>&1 & pids+=("$!")
    roslaunch trajectory_generation traj_following.launch \
      gains_file:="$LAB4_DIR/trajectory_generation_pkg/config/gains_arm64.yaml" \
      v_max:=2.0 a_max:=1.0 > /tmp/lab4-unity-follower.log 2>&1 & pids+=("$!")
    sleep 2
    LAB4_WINDOW_ID=$(DISPLAY=:98 xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
    DISPLAY=:98 xdotool windowfocus "$LAB4_WINDOW_ID" key r
    sleep 1
    roslaunch planner_pkg traj_gen.launch simulator_data_directory:="$LAB4_DIR/simulator_data" > /tmp/lab4-unity-gates.log 2>&1 & pids+=("$!")
    python3 "$LAB4_DIR/scripts/monitor_unity.py" > /tmp/lab4-unity-monitor.log 2>&1
    # Tuned on the official Lab4 Unity simulator under Box64 (4-6 fps).
    # The bridge applies commands at Unity update boundaries; high Lab3 attitude
    # gains become unstable when several physics ticks share one stale command.
    # Unity also uses inertia diag(0.1,0.1,0.2) in its own body axes; the Lab3
    # handout model uses I. These lower torque gains accommodate that difference.
    kx: 1.2
    kv: 2.0
    kr: 1.2
    komega: 0.7
    hz: 200.0
    state_timeout: 1.0
    desired_timeout: 1.0
    compensate_drag: false
    -rwxr-xr-x 1 root root 26973768 Oct 10 02:51 /tmp/lab4-box64-v036/build/box64
    -rwxr-xr-x 1 root root 26973768 Oct 10 02:51 /tmp/lab4-runtime/box64-0.3.6/build/box64
    ls: cannot access '/tmp/lab4-box64-v036/box64-0.3.6/build/box64': No such file or directory
    Lab2
    lab3
    lab4
    head: cannot open '/workspace/lab4/dependencies/tesse-ros-bridge/ROS/src/tesse_ros_bridge/tesse_ros_node.py' for reading: No such file or directory
    cat: /workspace/lab4/dependencies/tesse-ros-bridge/ROS/launch/tesse_quadrotor_bridge.launch: No such file or directory
    ✓ • 0ms

## Assistant

差别找到了：Lab 4 用 Box64 0.3.6 跑通了官方 Unity 模拟器。我之前在 QEMU 失败后就停止尝试，结论下得过早。现在复用这套运行办法，并针对模拟器重新调参、录制 Lab 3 的正式飞行视频。

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'ls /workspace/lab4/dependencies; readlink -f /tmp/lab4_ws/src/tesse_ros_bridge; ls /tmp/lab4-runtime/lab4; cat /tmp/lab4-runtime/lab4/lab4_Data/app.info; cat /tmp/tesse-lab3/lab3_Data/app.info; command -v monodis xdotool; source /tmp/lab4_ws/devel/setup.bash; rospack find tesse_ros_bridge; head -40 /tmp/lab4-unity-bridge.log; cat /tmp/lab4-angular-check.csv | head -6; ls /workspace/lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge'
    catkin_simple
    mav_msgs
    mav_trajectory_generation
    tesse_interface
    tesse_ros_bridge
    /workspace/lab4/dependencies/tesse_ros_bridge
    LinuxPlayer_s.debug
    UnityPlayer.so
    UnityPlayer_s.debug
    lab4.x86_64
    lab4_Data
    DefaultCompany
    tesse_vnav_scenesDefaultCompany
    tesse_vnav_scenes/usr/bin/monodis
    /usr/bin/xdotool
    /tmp/lab4_ws/src/tesse_ros_bridge
    ... logging to /root/.ros/log/c3c910aa-c455-11f1-9a23-e2e6d9d83e81/roslaunch-0e71ea2ee1ec-7909.log
    Checking log directory for disk usage. This may take a while.
    Press Ctrl-C to interrupt
    Done checking log file disk usage. Usage is <1GB.
    
    started roslaunch server http://localhost:39341/
    
    SUMMARY
    ========
    
    PARAMETERS
     * /rosdistro: noetic
     * /rosversion: 1.17.4
     * /tesse/tesse_ros_bridge/accelerometer_bias_correlation_time: 500
     * /tesse/tesse_ros_bridge/accelerometer_bias_random_walk: 0.003
     * /tesse/tesse_ros_bridge/accelerometer_bias_random_walk_mu: 0.0
     * /tesse/tesse_ros_bridge/accelerometer_noise_density: 0.002
     * /tesse/tesse_ros_bridge/accelerometer_noise_density_mu: 0.0
     * /tesse/tesse_ros_bridge/body_frame_id: base_link
     * /tesse/tesse_ros_bridge/body_frame_id_gt: base_link_gt
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/camera_id: depth_cam
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/compression: False
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/far_draw_dist: 200
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/frame_id: left_cam
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/height: 480
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/near_draw_dist: -0.05
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/num_channels: 1
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/pos_x: -0.05
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/pos_y: 0.0
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/pos_z: 0.0
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/quat_w: 1.0
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/quat_x: 0.0
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/quat_y: 0.0
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/quat_z: 0.0
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/vertical_fov: 60
     * /tesse/tesse_ros_bridge/camera_params/DEPTH/width: 720
     * /tesse/tesse_ros_bridge/camera_params/GRY_LEFT/camera_id: left_cam
     * /tesse/tesse_ros_bridge/camera_params/GRY_LEFT/compression: False
     * /tesse/tesse_ros_bridge/camera_params/GRY_LEFT/frame_id: left_cam
     * /tesse/tesse_ros_bridge/camera_params/GRY_LEFT/num_channels: 1
    # t,wx_reported,wy_reported,wz_reported,wx_dR,wy_dR,wz_dR
    4.966000000000000227e+02,-0.000000000000000000e+00,-0.000000000000000000e+00,-0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00
    4.966200000000000045e+02,-0.000000000000000000e+00,-0.000000000000000000e+00,-0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00
    4.966399999989999969e+02,-0.000000000000000000e+00,-0.000000000000000000e+00,-0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00
    4.966600000000000250e+02,-0.000000000000000000e+00,-0.000000000000000000e+00,-0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00
    4.966800000000000068e+02,-0.000000000000000000e+00,-0.000000000000000000e+00,-0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00
    __init__.py
    noise_simulator.py
    quadrotor_control_interface.py
    tesse_ros_node.py
    utils.py
    ✓ • 1ms

## Activity

    $ cat ../Lab4/scripts/analyze_unity.py | head -85; rg -n 'angular|quaternion|cv2|numpy|shebang' ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py 2>/dev/null | head -30; sed -n '1,180p' controller_pkg/include/controller_pkg/geometric_controller.h
    #!/usr/bin/env python3
    """Validate the saved official Unity telemetry, independently of the live monitor."""
    import csv
    import json
    import os
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root,'report')
    d = np.genfromtxt(os.path.join(out,'unity_flight.csv'),delimiter=',',names=True)
    x = np.column_stack([d[k] for k in ['x','y','z']])
    ref = np.column_stack([d[k] for k in ['xd','yd','zd']])
    gates = []
    for row in csv.reader(open(os.path.join(root,'simulator_data/StreamingAssets/vnav-2020-lab4_static_tfs.csv'))):
        if row and row[0].startswith('red_square_drone_door'):
            i = int(row[0].split('(')[1].rstrip(')')) if '(' in row[0] else 0
            gates.append((i,np.array([float(row[1]),float(row[3]),float(row[2])])))
    gates = sorted(gates)
    visits = []
    previous = -1
    for i,g in gates:
        dist = np.linalg.norm(x-g,axis=1)
        j = int(dist.argmin())
        assert j > previous, 'Gates must be visited in the correct order'
        previous = j
        visits.append(dict(gate=i,time_s=float(d['t'][j]),min_center_distance_m=float(dist[j])))
    error = np.linalg.norm(x-ref,axis=1)
    active = d['trajectory_time'] < d['trajectory_time'].max()-.01
    summary = dict(source='Official MIT Lab4 Unity 2019.3.9f1 via Box64 0.3.6 on ARM64',
                   trajectory_duration_s=float(d['trajectory_time'].max()),
                   total_recorded_simulation_duration_s=float(d['t'][-1]),
                   gate_count=len(gates),gate_center_visits=visits,
                   rms_tracking_error_m=float(np.sqrt(np.mean(error[active]**2))),
                   max_tracking_error_m=float(error[active].max()),
                   final_position_error_m=float(np.linalg.norm(x[-1]-gates[-1][1])),
                   final_hold_s=float(d['t'][-1]-d['t'][np.flatnonzero(~active)[0]]),
                   terminal_tolerance_m=.2,
                   note='Gate passage is also visible as green gates in unity_race_submission.mp4. '
                        'The original live monitor demanded 0.08m and timed out; '
                        'this offline check uses the documented 0.20m hover tolerance.')
    assert len(gates)==12 and max(v['min_center_distance_m'] for v in visits)<.6
    assert summary['final_position_error_m'] < summary['terminal_tolerance_m']
    assert summary['final_hold_s'] > 10
    summary['verification']='PASS: 12 ordered gate-center visits, full trajectory, terminal hold within 0.20m'
    with open(os.path.join(out,'unity_summary.json'),'w') as f:json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))
    fig,ax = plt.subplots(1,2,figsize=(11,4.5))
    ax[0].plot(ref[:,0],ref[:,1],'--',label='Desired')
    ax[0].plot(x[:,0],x[:,1],label='Unity actual')
    xyz=np.array([g for _,g in gates]);ax[0].scatter(xyz[:,0],xyz[:,1],marker='s',label='Gate centers')
    for i,g in gates:ax[0].annotate(str(i),g[:2],xytext=(4,4),textcoords='offset points')
    ax[0].set(xlabel='World x [m]',ylabel='World y [m]',title='12 gates in order');ax[0].axis('equal');ax[0].legend();ax[0].grid(alpha=.25)
    ax[1].plot(d['t'],error);ax[1].set(xlabel='Simulation time [s]',ylabel='Position error [m]',title='Tracking and final hover');ax[1].grid(alpha=.25)
    fig.suptitle('Official Unity Lab4 race: 91.08 s reference trajectory')
    fig.tight_layout(rect=(0,0,1,.93));fig.savefig(os.path.join(out,'unity_tracking.png'),dpi=160)
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:3:import numpy as np
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:19:import cv2  # Initialize OpenCV before cv_bridge on ARM64 Noetic.
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:346:            Twist messages for both linear and angular 'velocities'. These
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:356:        torque_z = msg.angular.z
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:384:        # TODO(marcus): We really want to convert to numpy 4x4 and compose!
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:393:        quat = tf.transformations.quaternion_multiply([-qx, -qz, -qy, qw],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:513:                    img_msg = self.cv_bridge.cv2_to_imgmsg(
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:517:                    img_msg = self.cv_bridge.cv2_to_imgmsg(
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:520:                    img_msg = self.cv_bridge.cv2_to_imgmsg(
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:559:                                              obj['quaternion'],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:730:            static_tf_cam.transform.rotation    = Quaternion(cam_data['quaternion'][0],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:731:                                                             cam_data['quaternion'][1],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:732:                                                             cam_data['quaternion'][2],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:733:                                                             cam_data['quaternion'][3])
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:881:        scan_ts.transform.rotation = Quaternion(lidar_data['quaternion'][0],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:882:                                                lidar_data['quaternion'][1],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:883:                                                lidar_data['quaternion'][2],
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:884:                                                lidar_data['quaternion'][3])
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:1050:                cur_tf: A 4x4 numpy matrix containing the transformation from
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py:1057:        quat = tesse_ros_bridge.utils.get_quaternion(cur_tf)
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:2:import numpy as np
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:24:            'quaternion': Agent rotation in world frame as a list.
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:26:            'ang_vel': Agent angular velocity in body frame as a list.
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:28:            'ang_accel': Agent angular acceleration in body frame as a list.
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:42:    d['quaternion'] = [float(root[1].attrib['x']),
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:81:                'quaternion': A list of floats representing the camera's
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:115:    brh_T_cam = tf.transformations.quaternion_matrix(quat)
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:121:    d['quaternion'] = get_quaternion(bros_T_cam)
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:141:                'quaternion': A list of floats representing the lidar's
    ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py:173:    blh_T_lidar = tf.transformations.quaternion_matrix(quat)
    #pragma once
    
    #include <Eigen/Dense>
    #include <cmath>
    
    namespace controller_pkg {
    
    struct State {
      Eigen::Vector3d x = Eigen::Vector3d::Zero();
      Eigen::Vector3d v = Eigen::Vector3d::Zero();
      Eigen::Matrix3d R = Eigen::Matrix3d::Identity();  // body -> world
      Eigen::Vector3d omega = Eigen::Vector3d::Zero();  // body frame
    };
    
    struct Reference {
      Eigen::Vector3d x = Eigen::Vector3d::Zero();
      Eigen::Vector3d v = Eigen::Vector3d::Zero();
      Eigen::Vector3d a = Eigen::Vector3d::Zero();
      double yaw = 0.0;
    };
    
    struct Gains {
      double kx = 6.0;
      double kv = 4.7;
      double kr = 64.0;
      double komega = 16.0;
    };
    
    struct Command {
      Eigen::Matrix3d Rd;
      Eigen::Vector4d wrench;  // thrust, body Mx, My, Mz
      Eigen::Vector4d rotor_speeds;  // signed rad/s, rotor order 1,2,3,4
    };
    
    // Lab 3 simulator constants; do not substitute real drone coefficients.
    class GeometricController {
     public:
      Gains gains;
      bool compensate_drag = false;
      const double m = 1.0, g = 9.81, d = 0.3, cf = 1e-3, cd = 1e-5;
      const Eigen::Matrix3d J = Eigen::Matrix3d::Identity();
    
      GeometricController() {
        // rho1=(+a,+a,0), rho2=(-a,+a,0), rho3=(-a,-a,0), rho4=(+a,-a,0).
        // rho x (0,0,cf*s): Mx=y*cf*s, My=-x*cf*s.
        // TESSE yaw signs: +,-,+,-. s_i = omega_i*abs(omega_i).
        const double a = d / std::sqrt(2.0);
        allocation_ << cf, cf, cf, cf,
                       a*cf, a*cf, -a*cf, -a*cf,
                       -a*cf, a*cf, a*cf, -a*cf,
                       cd, -cd, cd, -cd;
        F2W_ = allocation_.inverse();
      }
    
      const Eigen::Matrix4d& allocation() const { return allocation_; }
    
      static Eigen::Vector3d vee(const Eigen::Matrix3d& S) {
        return Eigen::Vector3d(S(2,1), S(0,2), S(1,0));
      }
    
      static Eigen::Vector3d dragWorld(const State& state) {
        const Eigen::Vector3d vb = state.R.transpose() * state.v;
        const Eigen::Vector3d drag_b =
            -Eigen::Vector3d(0.1, 0.1, 0.2).cwiseProduct(vb.cwiseProduct(vb.cwiseAbs()));
        return state.R * drag_b;
      }
    
      Command compute(const State& state, const Reference& ref) const {
        Command cmd;
        // Part 5.1: equations (6),(7).
        const Eigen::Vector3d ex = state.x - ref.x;
        const Eigen::Vector3d ev = state.v - ref.v;
        const Eigen::Vector3d e3 = Eigen::Vector3d::UnitZ();
    
        // Part 5.2: ROS uses upward z and +f*R*e3 thrust, unlike the paper.
        Eigen::Vector3d A = -gains.kx*ex - gains.kv*ev + m*g*e3 + m*ref.a;
        if (compensate_drag) A -= dragWorld(state);
        // With zero requested force the thrust direction is undetermined.
        const Eigen::Vector3d b3d = A.norm() > 1e-9 ? A.normalized() : e3;
        Eigen::Vector3d b1c(std::cos(ref.yaw), std::sin(ref.yaw), 0.0);
        Eigen::Vector3d b2d = b3d.cross(b1c);
        if (b2d.norm() < 1e-9) {
          // Pick a perpendicular heading if the requested heading is parallel to thrust.
          b1c = b3d.unitOrthogonal();
          b2d = b3d.cross(b1c);
        }
        b2d.normalize();
        cmd.Rd.col(0) = b2d.cross(b3d);
        cmd.Rd.col(1) = b2d;
        cmd.Rd.col(2) = b3d;
    
        // Part 5.3: the handout permits Omega_d=0 and dot(Omega_d)=0.
        const Eigen::Vector3d er =
            0.5 * vee(cmd.Rd.transpose()*state.R - state.R.transpose()*cmd.Rd);
        const Eigen::Vector3d eomega = state.omega;
    
        // Part 5.4: equations (15),(16), adapted to upward z.
        cmd.wrench(0) = A.dot(state.R.col(2));
        cmd.wrench.tail<3>() = -gains.kr*er - gains.komega*eomega
                              + state.omega.cross(J*state.omega);
    
        // Parts 5.5,5.6: invert the wrench map and preserve reversible rotor signs.
        const Eigen::Vector4d signed_squared_speeds = F2W_ * cmd.wrench;
        for (int i = 0; i < 4; ++i) {
          const double s = signed_squared_speeds(i);
          cmd.rotor_speeds(i) = std::copysign(std::sqrt(std::abs(s)), s);
        }
        return cmd;
      }
    
     private:
      Eigen::Matrix4d allocation_, F2W_;
    };
    }  // namespace controller_pkg
    ✓ • 0ms

## Activity

    $ docker exec -i ros_noetic_lab3 python3 - <<'PY'
        from pathlib import Path
        import difflib
        for f in ['tesse_ros_node.py','quadrotor_control_interface.py','utils.py']:
            a=Path('/opt/lab3-deps/tesse-ros-bridge/ROS/src/tesse_ros_bridge')/f
            b=Path('/workspace/lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge')/f
            print(''.join(difflib.unified_diff(a.read_text().splitlines(True),b.read_text().splitlines(True),fromfile='old/'+f,tofile='working/'+f)))
        PY
        docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roscore -p 11317 >/tmp/lab3-unity-master.log 2>&1'
        docker exec -d ros_noetic_lab3 bash -lc 'Xvfb :97 -screen 0 960x600x24 >/tmp/lab3-unity-xvfb.log 2>&1'
        docker exec -d ros_noetic_lab3 bash -lc 'cd /tmp/tesse-lab3; DISPLAY=:97 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0 /tmp/lab4-runtime/box64-0.3.6/build/box64 ./lab3.x86_64 -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile /tmp/lab3-unity-box64.log >/tmp/lab3-box64.log 2>&1'
    
    
    
    ✓ • 55ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -18 /tmp/lab3-unity-box64.log; tail -8 /tmp/lab3-box64.log; DISPLAY=:97 xdotool search --onlyvisible --name tesse_vnav_scenes; ffmpeg -y -loglevel error -f x11grab -video_size 960x600 -i :97 -frames:v 1 /workspace/lab3/report/video/unity_startup.png'
    
    Metadata request listener started...
    UnityEngine.DebugLogHandler:Internal_Log(LogType, LogOption, String, Object)
    UnityEngine.DebugLogHandler:LogFormat(LogType, Object, String, Object[])
    UnityEngine.Logger:Log(LogType, Object)
    UnityEngine.Debug:Log(Object)
    UnityEngine.MonoBehaviour:print(Object)
    tesse.tesse_metadata_interface:met_request_listener() (at C:\Users\j_shi\code\tesse_vnav_scenes\Assets\tesse-core\Scripts\Interfaces\tesse_metadata_interface.cs:176)
    System.Threading.ThreadHelper:ThreadStart_Context(Object)
    System.Threading.ExecutionContext:RunInternal(ExecutionContext, ContextCallback, Object, Boolean)
    System.Threading.ExecutionContext:Run(ExecutionContext, ContextCallback, Object, Boolean)
    System.Threading.ExecutionContext:Run(ExecutionContext, ContextCallback, Object)
    System.Threading.ThreadHelper:ThreadStart()
    
    (Filename: C Line: 0)
    
    Setting up 1 worker threads for Enlighten.
      Thread -> id: e90ed98fef50 -> priority: 1
    Set current directory to /tmp/tesse-lab3
    Found path: /tmp/tesse-lab3/lab3.x86_64
    2097166
    ✓ • 174ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/unity_startup.png

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'DISPLAY=:97 xdotool windowfocus 2097166 mousemove 512 571 click 1; source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; rosparam set /use_sim_time true'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true >/tmp/lab3-unity-bridge.log 2>&1'; docker exec ros_noetic_lab3 bash -lc 'monodis --output=/tmp/lab3-unity.il /tmp/tesse-lab3/lab3_Data/Managed/Assembly-CSharp.dll; grep -n -E "inertiaTensor|thrustCoeff|liftCoeff|Quadrotor|quadrotor_control" /tmp/lab3-unity.il | head -25'
    130:  .class public auto ansi beforefieldinit QuadrotorDynamics
    162:      IL_000f:  ldfld int32 QuadrotorDynamics::port
    164:      IL_0019:  stfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics::udp_client
    181:    } // end of method QuadrotorDynamics::Connect
    192:    IL_0002:  call instance void class QuadrotorDynamics::Connect()
    197:    IL_000f:  stfld unsigned int8[] QuadrotorDynamics::timestamp
    200:    IL_0016:  stfld bool QuadrotorDynamics::timestamp_valid
    204:    IL_0022:  stfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics::rb
    206:    } // end of method QuadrotorDynamics::Start
    231:    IL_000f:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics::udp_client
    247:    IL_0033:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics::udp_client
    249:    IL_0039:  ldflda class [System]System.Net.IPEndPoint QuadrotorDynamics::ip_endpoint
    254:    IL_0046:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics::udp_client
    277:    IL_006e:  ldfld unsigned int8[] QuadrotorDynamics::timestamp
    283:    IL_007c:  stfld bool QuadrotorDynamics::timestamp_valid
    336:    } // end of method QuadrotorDynamics::GrabPose
    347:    IL_0002:  ldfld class [UnityEngine.CoreModule]UnityEngine.GameObject QuadrotorDynamics::vehicle
    362:    IL_0021:  ldfld class [UnityEngine.CoreModule]UnityEngine.GameObject QuadrotorDynamics::vehicle
    380:    } // end of method QuadrotorDynamics::SetVehiclePose
    475:    } // end of method QuadrotorDynamics::MatrixTranspose
    615:    } // end of method QuadrotorDynamics::MatrixSubtraction
    935:    } // end of method QuadrotorDynamics::MatrixMultiplication
    1034:    } // end of method QuadrotorDynamics::MatrixVectorMultiplication
    1071:    } // end of method QuadrotorDynamics::VectorVectorMultiplication
    1184:    } // end of method QuadrotorDynamics::MatrixScalarMultiplication
    ✓ • 398ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'grep -n -E "inertiaTensor|1.000000|0.1|0.2|c_f|c_d|mass|Init|FixedUpdate|Update" /tmp/lab3-unity.il | head -65; source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; rostopic echo -n1 /current_state; tail -4 /tmp/lab3-unity-bridge.log'; cat ../Lab4/scripts/monitor_unity.py | head -105
    62:        // Method begins at RVA 0x2050
    66:    IL_0001:  ldc.i4.1
    67:    IL_0002:  call void class [UnityEngine.CoreModule]UnityEngine.Cursor::set_visible(bool)
    76:        // Method begins at RVA 0x205a
    80:    IL_0001:  call instance void class [UnityEngine.CoreModule]UnityEngine.MonoBehaviour::'.ctor'()
    94:           instance default void Update ()  cil managed
    96:        // Method begins at RVA 0x2063
    97:    // Code size 31 (0x1f)
    100:    IL_0001:  ldarg.0
    101:    IL_0002:  call instance class [UnityEngine.CoreModule]UnityEngine.Transform class [UnityEngine.CoreModule]UnityEngine.Component::get_transform()
    105:    IL_0012:  call float32 class [UnityEngine.CoreModule]UnityEngine.Time::get_deltaTime()
    106:    IL_0017:  mul
    107:    IL_0018:  callvirt instance void class [UnityEngine.CoreModule]UnityEngine.Transform::Rotate(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, float32)
    108:    IL_001d:  nop
    109:    IL_001e:  ret
    110:    } // end of method PropellersRotate::Update
    116:        // Method begins at RVA 0x2083
    117:    // Code size 19 (0x13)
    120:    IL_0001:  ldc.r4 1000.
    124:    IL_0011:  nop
    125:    IL_0012:  ret
    143:    .field private static literal  int32 STAMP_LENGTH = int32(0x00000002)
    149:        // Method begins at RVA 0x2098
    156:      IL_0001:  nop
    157:      IL_0002:  ldstr "Pose Grabber Setting Up Connection"
    163:      IL_0014:  newobj instance void class [System]System.Net.Sockets.UdpClient::'.ctor'(int32)
    164:      IL_0019:  stfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics::udp_client
    165:      IL_001e:  nop
    166:      IL_001f:  leave.s IL_0032
    170:      IL_0021:  stloc.0
    171:      IL_0022:  nop
    172:      IL_0023:  ldloc.0
    173:      IL_0024:  callvirt instance string class [mscorlib]System.Exception::get_Message()
    174:      IL_0029:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
    175:      IL_002e:  nop
    176:      IL_002f:  nop
    177:      IL_0030:  leave.s IL_0032
    180:    IL_0032:  ret
    187:        // Method begins at RVA 0x20e8
    188:    // Code size 40 (0x28)
    191:    IL_0001:  ldarg.0
    192:    IL_0002:  call instance void class QuadrotorDynamics::Connect()
    198:    IL_0014:  ldarg.0
    199:    IL_0015:  ldc.i4.0
    200:    IL_0016:  stfld bool QuadrotorDynamics::timestamp_valid
    201:    IL_001b:  ldarg.0
    202:    IL_001c:  ldarg.0
    203:    IL_001d:  call instance !!0 class [UnityEngine.CoreModule]UnityEngine.Component::GetComponent<class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody> ()
    204:    IL_0022:  stfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics::rb
    205:    IL_0027:  ret
    212:        // Method begins at RVA 0x2114
    225:    IL_0001:  ldnull
    226:    IL_0002:  stloc.0
    232:    IL_0014:  callvirt instance int32 class [System]System.Net.Sockets.UdpClient::get_Available()
    233:    IL_0019:  ldc.i4.0
    234:    IL_001a:  cgt
    235:    IL_001c:  stloc.1
    236:    IL_001d:  ldloc.1
    237:    IL_001e:  brfalse IL_00c2
    239:    IL_0023:  nop
    240:    IL_0024:  ldstr "UDP client available"
    241:    IL_0029:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
    242:    IL_002e:  nop
    243:    IL_002f:  br.s IL_0045
    245:    IL_0031:  nop
    header:
      seq: 1
      stamp:
        secs: 40
        nsecs: 460000000
      frame_id: "world"
    child_frame_id: "base_link_gt"
    pose:
      pose:
        position:
          x: 0.003100869
          y: -0.2411913
          z: 0.700026
        orientation:
          x: -4.74156e-05
          y: -6.335822e-05
          z: -0.3973999
          w: 0.9176456
      covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    twist:
      twist:
        linear:
          x: 0.0
          y: 0.0
          z: 0.0
        angular:
          x: -0.0
          y: -0.0
          z: -0.0
      covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ---
    NODES
      /tesse/
        quadrotor_control_interface (tesse_ros_bridge/quadrotor_control_interface.py)
        tesse_ros_bridge (tesse_ros_bridge/tesse_ros_node.py)
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
    ✓ • 1.30s

## Activity

    file changes: Completed · 2 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/config/gains_unity.yaml
    # Official Unity / Box64 tuning; low rendered frame rates hold motor commands.
    # Keep the handout's model constants; tune the feedback on the actual plant.
    kx: 2.0
    kv: 2.4
    kr: 1.8
    komega: 0.7
    hz: 200.0
    state_timeout: 1.0
    desired_timeout: 1.0
    compensate_drag: false
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/monitor_unity.py
    #!/usr/bin/env python3
    """Record live official TESSE telemetry and publish paths for the RViz video."""
    import argparse
    import csv
    import json
    import math
    import threading
    import time
    from pathlib import Path as FilePath
    
    import numpy as np
    import rospy
    from geometry_msgs.msg import PoseStamped
    from mav_msgs.msg import Actuators
    from nav_msgs.msg import Odometry, Path
    from trajectory_msgs.msg import MultiDOFJointTrajectoryPoint
    from visualization_msgs.msg import Marker
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--duration", type=float, default=50.0)
    parser.add_argument("--wall-timeout", type=float, default=300.0)
    args = parser.parse_args()
    rospy.init_node("lab3_unity_monitor", anonymous=True)
    lock = threading.Lock()
    rows = []
    reference = None
    rotors = [0.0]*4
    actual_path, desired_path = Path(), Path()
    actual_path.header.frame_id = desired_path.header.frame_id = "world"
    actual_pub = rospy.Publisher("/flight/actual", Path, queue_size=1)
    desired_pub = rospy.Publisher("/flight/desired", Path, queue_size=1)
    source_pub = rospy.Publisher("/flight/source", Marker, queue_size=1, latch=True)
    last_path_t = -1.0
    
    def yaw(q):
        return math.atan2(2*(q.w*q.z+q.x*q.y), 1-2*(q.y*q.y+q.z*q.z))
    
    def on_reference(msg):
        global reference
        if not msg.transforms:
            return
        with lock:
            reference = msg
    
    def on_rotors(msg):
        global rotors
        if len(msg.angular_velocities) == 4:
            with lock:
                rotors = list(msg.angular_velocities)
    
    def on_state(msg):
        global last_path_t
        with lock:
            if reference is None:
                return
            ref = reference
            speed = list(rotors)
            target = ref.transforms[0]
            p = msg.pose.pose.position
            pd = target.translation
            w = msg.twist.twist.angular
            stamp = msg.header.stamp.to_sec()
            rows.append([stamp, ref.time_from_start.to_sec(), p.x,p.y,p.z,
                         pd.x,pd.y,pd.z,yaw(msg.pose.pose.orientation),yaw(target.rotation),
                         w.x,w.y,w.z,*speed])
            if stamp-last_path_t < 0.1:
                return
            last_path_t = stamp
            actual_path.header.stamp = desired_path.header.stamp = msg.header.stamp
            actual_path.poses.append(PoseStamped(header=msg.header,pose=msg.pose.pose))
            desired = PoseStamped()
            desired.header = msg.header
            desired.pose.position.x,desired.pose.position.y,desired.pose.position.z = pd.x,pd.y,pd.z
            desired.pose.orientation = target.rotation
            desired_path.poses.append(desired)
            actual_path.poses = actual_path.poses[-1200:]
            desired_path.poses = desired_path.poses[-1200:]
            actual_pub.publish(actual_path)
            desired_pub.publish(desired_path)
    
    rospy.Subscriber("/desired_state",MultiDOFJointTrajectoryPoint,on_reference,queue_size=1)
    rospy.Subscriber("/rotor_speed_cmds",Actuators,on_rotors,queue_size=1)
    rospy.Subscriber("/current_state",Odometry,on_state,queue_size=100)
    marker = Marker()
    marker.header.frame_id = "world"
    marker.type = Marker.TEXT_VIEW_FACING
    marker.action = Marker.ADD
    marker.pose.position.z = 5
    marker.pose.orientation.w = 1
    marker.scale.z = 0.35
    marker.color.r = marker.color.g = marker.color.b = marker.color.a = 1
    marker.text = "Official MIT Lab3 TESSE / Box64"
    source_pub.publish(marker)
    started = time.monotonic()
    next_progress = 0
    complete = False
    try:
        while not rospy.is_shutdown() and time.monotonic()-started < args.wall_timeout:
            with lock:
                latest = rows[-1] if rows else None
            if latest and latest[1] >= next_progress:
                error = np.linalg.norm(np.array(latest[2:5])-latest[5:8])
                print("trajectory t=%.2f s, position=%s, error=%.3f m" %
                      (latest[1],latest[2:5],error),flush=True)
                next_progress += 5
            if latest and latest[1] >= args.duration:
                complete = True
                break
            time.sleep(0.1)
    finally:
        with lock:
            data = np.asarray(rows)
        path = FilePath(args.output)
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("w",newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["t","trajectory_time","x","y","z","xd","yd","zd",
                             "yaw","yawd","wx_world","wy_world","wz_world",
                             "rotor1","rotor2","rotor3","rotor4"])
            writer.writerows(data)
        if len(data):
            error = np.linalg.norm(data[:,2:5]-data[:,5:8],axis=1)
            steady = data[:,1] >= min(2*4*math.pi,args.duration/2)
            summary = dict(source="Official MIT Lab3 Unity/TESSE via Box64 0.3.6",
                           complete_duration=complete, samples=len(data),
                           trajectory_duration_s=float(data[-1,1]),
                           steady_position_rms_m=float(np.sqrt(np.mean(error[steady]**2))) if steady.any() else None,
                           steady_position_max_m=float(error[steady].max()) if steady.any() else None,
                           final_position_error_m=float(error[-1]))
            path.with_suffix(".json").write_text(json.dumps(summary,indent=2)+"\n")
            print(json.dumps(summary,indent=2),flush=True)
    if not complete:
        raise SystemExit("Did not record the requested trajectory duration")

## Activity

    $ mkdir -p report/trials; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; python3 /workspace/lab3/scripts/monitor_unity.py --output /workspace/lab3/report/trials/unity_hover.csv --duration 25 >/tmp/lab3-unity-hover-monitor.log 2>&1'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roslaunch controller_pkg traj_tracking.launch static_pose:=true gains_file:=/workspace/lab3/controller_pkg/config/gains_unity.yaml >/tmp/lab3-unity-hover-controller.log 2>&1'
    ✓ • 205ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -7 /tmp/lab3-unity-hover-monitor.log; tail -8 /tmp/lab3-unity-hover-controller.log; grep -n -E "inertiaTensor|QuadrotorDynamics::Init|QuadrotorDynamics::FixedUpdate|QuadrotorDynamics::Update|ldc.r4 0.1|ldc.r4 0.2" /tmp/lab3-unity.il | tail -35'; cat ../Lab4/scripts/build_workspace.sh; head -25 ../Lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/quadrotor_control_interface.py; ls -lh ../Lab4/dependencies/tesse_ros_bridge
    trajectory t=0.00 s, position=[0.003100869, -0.2411913, 0.700026], error=1.322 m
    trajectory t=5.04 s, position=[-0.0006714537, 0.00639488, 1.737266], error=0.263 m
    trajectory t=10.02 s, position=[0.007488999, 0.007923074, 1.737346], error=0.263 m
    1392:    IL_01f8:  ldc.r4 0.10000000149011612
    1827:    } // end of method QuadrotorDynamics::Update
    1874:    } // end of method QuadrotorDynamics::FixedUpdate
    1978:    IL_002d:  ldc.r4 0.10000000149011612
    1979:    IL_0032:  ldc.r4 0.10000000149011612
    1980:    IL_0037:  ldc.r4 0.20000000298023224
    1982:    IL_0041:  callvirt instance void class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody::set_inertiaTensor(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
    5344:    IL_0014:  ldc.r4 0.10000000149011612
    5401:    IL_0052:  ldc.r4 0.20000000298023224
    5804:    IL_02bd:  ldc.r4 0.10000000149011612
    5817:    IL_02e1:  ldc.r4 0.10000000149011612
    7892:    IL_0013:  ldc.r4 0.10000000149011612
    7893:    IL_0018:  ldc.r4 0.10000000149011612
    7894:    IL_001d:  ldc.r4 0.20000000298023224
    7896:    IL_0027:  callvirt instance void class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody::set_inertiaTensor(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
    #!/usr/bin/env bash
    # Inside Docker; keep outputs outside the source repository.
    set -eo pipefail
    source /opt/ros/noetic/setup.bash
    LAB4_DIR=${LAB4_DIR:-/workspace/lab4}
    LAB3_DIR=${LAB3_DIR:-/workspace/lab3}
    LAB4_WS=${LAB4_WS:-/tmp/lab4_ws}
    mkdir -p "$LAB4_WS/src"
    for pkg in planner_pkg trajectory_generation_pkg; do
      ln -sfn "$LAB4_DIR/$pkg" "$LAB4_WS/src/$pkg"
    done
    for pkg in mav_trajectory_generation mav_msgs catkin_simple tesse_ros_bridge; do
      ln -sfn "$LAB4_DIR/dependencies/$pkg" "$LAB4_WS/src/$pkg"
    done
    ln -sfn "$LAB3_DIR/controller_pkg" "$LAB4_WS/src/controller_pkg"
    cd "$LAB4_WS"
    catkin build -j2 --no-status --cmake-args -DCMAKE_BUILD_TYPE=Release
    #!/usr/bin/env python3
    
    import numpy as np
    import copy
    
    import rospy
    import tf
    import tf2_ros
    from std_msgs.msg import Header, String
    from sensor_msgs.msg import Image as ImageMsg
    from sensor_msgs.msg import Imu, CameraInfo
    from sensor_msgs.msg import LaserScan
    from nav_msgs.msg import Odometry
    from mav_msgs.msg import Actuators
    from geometry_msgs.msg import (
        Pose,
        PoseStamped,
        Point,
        PointStamped,
        TransformStamped,
        Quaternion,
        Twist,
        PoseWithCovarianceStamped,
        Vector3Stamped,
    )
    total 32K
    -rw-rw-r-- 1 chixin chixin  218 Sep 20 11:05 CMakeLists.txt
    drwxrwxr-x 2 chixin chixin 4.0K Sep 20 11:05 launch
    drwxrwxr-x 2 chixin chixin 4.0K Sep 20 11:05 msg
    -rw-rw-r-- 1 chixin chixin  829 Sep 20 11:05 package.xml
    drwxrwxr-x 2 chixin chixin 4.0K Sep 20 11:05 params
    -rw-rw-r-- 1 chixin chixin  453 Sep 20 11:05 setup.py
    drwxrwxr-x 4 chixin chixin 4.0K Sep 20 11:05 src
    drwxrwxr-x 2 chixin chixin 4.0K Sep 20 11:05 srv
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'sed -n "1220,1450p" /tmp/lab3-unity.il; sed -n "1930,2015p" /tmp/lab3-unity.il; tail -6 /tmp/lab3-unity-hover-monitor.log'
            float32[0...,0...]    V_26,
            float32[0...,0...]    V_27,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector3    V_28,
            float32[0...,0...]    V_29,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector3    V_30,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector3    V_31,
            float32[0...,0...]    V_32,
            float32    V_33,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector3    V_34,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector4    V_35,
            bool    V_36,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector4    V_37)
        IL_0000:  nop
        IL_0001:  ldarg.2
        IL_0002:  callvirt instance float32 class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody::get_mass()
        IL_0007:  stloc.0
        IL_0008:  ldc.r4 9.8100004196166992
        IL_000d:  stloc.1
        IL_000e:  ldc.r4 10.
        IL_0013:  stloc.2
        IL_0014:  ldc.r4 12.
        IL_0019:  stloc.3
        IL_001a:  ldc.r4 18.
        IL_001f:  stloc.s 4
        IL_0021:  ldc.r4 -3.5
        IL_0026:  stloc.s 5
        IL_0028:  ldarg.2
        IL_0029:  callvirt instance class [UnityEngine.CoreModule]UnityEngine.Transform class [UnityEngine.CoreModule]UnityEngine.Component::get_transform()
        IL_002e:  callvirt instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 class [UnityEngine.CoreModule]UnityEngine.Transform::get_position()
        IL_0033:  stloc.s 6
        IL_0035:  ldloca.s 7
        IL_0037:  ldloc.s 6
        IL_0039:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::x
        IL_003e:  ldloc.s 6
        IL_0040:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::z
        IL_0045:  ldloc.s 6
        IL_0047:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::y
        IL_004c:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0051:  ldarg.2
        IL_0052:  callvirt instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody::get_velocity()
        IL_0057:  stloc.s 8
        IL_0059:  ldloca.s 8
        IL_005b:  ldloc.s 8
        IL_005d:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::x
        IL_0062:  ldloc.s 8
        IL_0064:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::z
        IL_0069:  ldloc.s 8
        IL_006b:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::y
        IL_0070:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0075:  ldarg.2
        IL_0076:  callvirt instance class [UnityEngine.CoreModule]UnityEngine.Transform class [UnityEngine.CoreModule]UnityEngine.Component::get_transform()
        IL_007b:  callvirt instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 class [UnityEngine.CoreModule]UnityEngine.Transform::get_eulerAngles()
        IL_0080:  stloc.s 9
        IL_0082:  ldloca.s 9
        IL_0084:  ldloc.s 9
        IL_0086:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::x
        IL_008b:  neg
        IL_008c:  ldc.r4 180.
        IL_0091:  div
        IL_0092:  ldc.r4 3.1415927410125732
        IL_0097:  mul
        IL_0098:  ldloc.s 9
        IL_009a:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::z
        IL_009f:  neg
        IL_00a0:  ldc.r4 180.
        IL_00a5:  div
        IL_00a6:  ldc.r4 3.1415927410125732
        IL_00ab:  mul
        IL_00ac:  ldloc.s 9
        IL_00ae:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::y
        IL_00b3:  neg
        IL_00b4:  ldc.r4 180.
        IL_00b9:  div
        IL_00ba:  ldc.r4 3.1415927410125732
        IL_00bf:  mul
        IL_00c0:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_00c5:  ldloca.s 10
        IL_00c7:  ldarg.1
        IL_00c8:  ldc.i4.0
        IL_00c9:  ldelem.r4
        IL_00ca:  ldarg.1
        IL_00cb:  ldc.i4.1
        IL_00cc:  ldelem.r4
        IL_00cd:  ldarg.1
        IL_00ce:  ldc.i4.2
        IL_00cf:  ldelem.r4
        IL_00d0:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_00d5:  ldloca.s 11
        IL_00d7:  ldc.r4 0.
        IL_00dc:  ldc.r4 0.
        IL_00e1:  ldc.r4 0.
        IL_00e6:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_00eb:  ldloca.s 12
        IL_00ed:  ldc.r4 0.
        IL_00f2:  ldc.r4 0.
        IL_00f7:  ldc.r4 0.
        IL_00fc:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0101:  ldloca.s 13
        IL_0103:  ldc.r4 0.
        IL_0108:  ldc.r4 0.
        IL_010d:  ldc.r4 0.
        IL_0112:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0117:  ldloca.s 14
        IL_0119:  ldc.r4 0.
        IL_011e:  ldc.r4 0.
        IL_0123:  ldc.r4 0.
        IL_0128:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_012d:  ldloc.s 7
        IL_012f:  ldloc.s 10
        IL_0131:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0136:  stloc.s 15
        IL_0138:  ldloc.s 8
        IL_013a:  ldloc.s 11
        IL_013c:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0141:  stloc.s 16
        IL_0143:  ldloca.s 17
        IL_0145:  ldc.r4 1.
        IL_014a:  ldc.r4 0.
        IL_014f:  ldc.r4 0.
        IL_0154:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0159:  ldloc.2
        IL_015a:  neg
        IL_015b:  ldloc.s 15
        IL_015d:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0162:  ldloc.3
        IL_0163:  ldloc.s 16
        IL_0165:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_016a:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_016f:  ldloc.0
        IL_0170:  ldloc.1
        IL_0171:  mul
        IL_0172:  ldc.r4 0.
        IL_0177:  ldc.r4 0.
        IL_017c:  ldc.r4 -1.
        IL_0181:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0186:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_018b:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0190:  ldloc.0
        IL_0191:  ldloc.s 12
        IL_0193:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0198:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Addition(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_019d:  stloc.s 18
        IL_019f:  ldloca.s 18
        IL_01a1:  call instance float32 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::get_magnitude()
        IL_01a6:  ldc.r4 0.
        IL_01ab:  clt
        IL_01ad:  stloc.s 36
        IL_01af:  ldloc.s 36
        IL_01b1:  brfalse.s IL_020a
    
        IL_01b3:  nop
        IL_01b4:  ldloc.2
        IL_01b5:  neg
        IL_01b6:  ldloc.s 15
        IL_01b8:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01bd:  ldloc.3
        IL_01be:  ldloc.s 16
        IL_01c0:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01c5:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01ca:  ldloc.0
        IL_01cb:  ldloc.1
        IL_01cc:  mul
        IL_01cd:  ldc.r4 0.
        IL_01d2:  ldc.r4 0.
        IL_01d7:  ldc.r4 -1.
        IL_01dc:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_01e1:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01e6:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01eb:  ldloc.0
        IL_01ec:  ldloc.s 12
        IL_01ee:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01f3:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Addition(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_01f8:  ldc.r4 0.10000000149011612
        IL_01fd:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Division(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, float32)
        IL_0202:  stloc.s 19
        IL_0204:  nop
        IL_0205:  br IL_02a4
    
        IL_020a:  nop
        IL_020b:  ldloc.2
        IL_020c:  neg
        IL_020d:  ldloc.s 15
        IL_020f:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0214:  ldloc.3
        IL_0215:  ldloc.s 16
        IL_0217:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_021c:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0221:  ldloc.0
        IL_0222:  ldloc.1
        IL_0223:  mul
        IL_0224:  ldc.r4 0.
        IL_0229:  ldc.r4 0.
        IL_022e:  ldc.r4 -1.
        IL_0233:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0238:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_023d:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0242:  ldloc.0
        IL_0243:  ldloc.s 12
        IL_0245:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_024a:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Addition(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_024f:  stloc.s 18
        IL_0251:  ldloc.2
        IL_0252:  neg
        IL_0253:  ldloc.s 15
        IL_0255:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_025a:  ldloc.3
        IL_025b:  ldloc.s 16
        IL_025d:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0262:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0267:  ldloc.0
        IL_0268:  ldloc.1
        IL_0269:  mul
        IL_026a:  ldc.r4 0.
        IL_026f:  ldc.r4 0.
        IL_0274:  ldc.r4 -1.
        IL_0279:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_027e:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0283:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Subtraction(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0288:  ldloc.0
        IL_0289:  ldloc.s 12
        IL_028b:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Multiply(float32, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0290:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Addition(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0295:  ldloca.s 18
        IL_0297:  call instance float32 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::get_magnitude()
        IL_029c:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::op_Division(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, float32)
        IL_02a1:  stloc.s 19
        IL_02a3:  nop
        IL_02a4:  ldloc.s 19
        IL_02a6:  ldloc.s 17
        IL_02a8:  call valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::Cross(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3, valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_02ad:  stloc.s 20
          IL_000c:  nop
          IL_000d:  ldarg.0
          IL_000e:  ldarg.0
          IL_000f:  ldfld int32 QuadrotorDynamics_w::port
          IL_0014:  newobj instance void class [System]System.Net.Sockets.UdpClient::'.ctor'(int32)
          IL_0019:  stfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics_w::udp_client
          IL_001e:  nop
          IL_001f:  leave.s IL_0032
    
        } // end .try 0
        catch class [mscorlib]System.Exception { // 0
          IL_0021:  stloc.0
          IL_0022:  nop
          IL_0023:  ldloc.0
          IL_0024:  callvirt instance string class [mscorlib]System.Exception::get_Message()
          IL_0029:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
          IL_002e:  nop
          IL_002f:  nop
          IL_0030:  leave.s IL_0032
    
        } // end handler 0
        IL_0032:  ret
        } // end of method QuadrotorDynamics_w::Connect
    
        // method line 20
        .method private hidebysig
               instance default void Start ()  cil managed
        {
            // Method begins at RVA 0x2f64
        // Code size 72 (0x48)
        .maxstack 4
        IL_0000:  nop
        IL_0001:  ldarg.0
        IL_0002:  call instance void class QuadrotorDynamics_w::Connect()
        IL_0007:  nop
        IL_0008:  ldarg.0
        IL_0009:  ldc.i4.0
        IL_000a:  newarr [netstandard]System.Byte
        IL_000f:  stfld unsigned int8[] QuadrotorDynamics_w::timestamp
        IL_0014:  ldarg.0
        IL_0015:  ldc.i4.0
        IL_0016:  stfld bool QuadrotorDynamics_w::timestamp_valid
        IL_001b:  ldarg.0
        IL_001c:  ldarg.0
        IL_001d:  call instance !!0 class [UnityEngine.CoreModule]UnityEngine.Component::GetComponent<class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody> ()
        IL_0022:  stfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics_w::rb
        IL_0027:  ldarg.0
        IL_0028:  ldfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics_w::rb
        IL_002d:  ldc.r4 0.10000000149011612
        IL_0032:  ldc.r4 0.10000000149011612
        IL_0037:  ldc.r4 0.20000000298023224
        IL_003c:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0041:  callvirt instance void class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody::set_inertiaTensor(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_0046:  nop
        IL_0047:  ret
        } // end of method QuadrotorDynamics_w::Start
    
        // method line 21
        .method private hidebysig
               instance default float32[] GrabW ()  cil managed
        {
            // Method begins at RVA 0x2fb8
        // Code size 212 (0xd4)
        .maxstack 5
        .locals init (
            unsigned int8[]    V_0,
            bool    V_1,
            float32[]    V_2,
            bool    V_3,
            bool    V_4,
            int32    V_5,
            bool    V_6,
            float32[]    V_7)
        IL_0000:  nop
        IL_0001:  ldnull
        IL_0002:  stloc.0
        IL_0003:  ldstr "Trying to grab pose"
        IL_0008:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
        IL_000d:  nop
        IL_000e:  ldarg.0
        IL_000f:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics_w::udp_client
        IL_0014:  callvirt instance int32 class [System]System.Net.Sockets.UdpClient::get_Available()
        IL_0019:  ldc.i4.0
        IL_001a:  cgt
        IL_001c:  stloc.1
        IL_001d:  ldloc.1
    trajectory t=0.00 s, position=[0.003100869, -0.2411913, 0.700026], error=1.322 m
    trajectory t=5.04 s, position=[-0.0006714537, 0.00639488, 1.737266], error=0.263 m
    trajectory t=10.02 s, position=[0.007488999, 0.007923074, 1.737346], error=0.263 m
    trajectory t=15.04 s, position=[-0.003645568, -0.00362614, 1.845511], error=0.155 m
    trajectory t=20.00 s, position=[-0.0009833416, -0.0009845786, 1.644164], error=0.356 m
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'grep "^  .class" /tmp/lab3-unity.il | head -35; grep -n "class.*QuadrotorDynamics_" /tmp/lab3-unity.il | head -15; sed -n "7700,7940p" /tmp/lab3-unity.il; tail -10 /tmp/lab3-unity-hover-monitor.log'
      .class public auto ansi beforefieldinit CursorScript
      .class public auto ansi beforefieldinit PropellersRotate
      .class public auto ansi beforefieldinit QuadrotorDynamics
      .class public auto ansi beforefieldinit QuadrotorDynamics_w
      .class public auto ansi beforefieldinit QuitScript
      .class public auto ansi beforefieldinit StatePublisher
      .class public auto ansi beforefieldinit camera_parameters
      .class public auto ansi beforefieldinit depth_camera_effect
      .class public auto ansi beforefieldinit instance_segmentation
      .class public auto ansi beforefieldinit lidar_parameters
      .class public auto ansi beforefieldinit object_segmentation
      .class public auto ansi beforefieldinit tesse_fps_counter
      .class public auto ansi beforefieldinit simple_tesse_controller
      .class public auto ansi beforefieldinit simple_tesse_hover_controller
      .class public auto ansi beforefieldinit tesse_car_controller
      .class public auto ansi abstract beforefieldinit tesse_controller_base
      .class public auto ansi beforefieldinit tesse_quadrotor_controller
      .class public auto ansi beforefieldinit tesse_image_interface
      .class nested private sequential ansi sealed beforefieldinit img_requested
      .class public auto ansi beforefieldinit tesse_lidar_interface
      .class nested private sequential ansi sealed beforefieldinit scan_requested
      .class public auto ansi beforefieldinit tesse_metadata_interface
      .class nested private auto ansi sealed beforefieldinit '<>c__DisplayClass15_0'
      .class nested private auto ansi sealed beforefieldinit '<>c__DisplayClass16_0'
      .class public auto ansi beforefieldinit tesse_position_interface
      .class nested private auto ansi sealed beforefieldinit '<unload_current_scene>d__66'
      .class nested private auto ansi sealed beforefieldinit '<update_segmentation>d__67'
      .class nested private auto ansi sealed beforefieldinit '<update_static_tf_csv>d__68'
      .class public auto ansi beforefieldinit SpawnObject
      .class public auto ansi abstract sealed beforefieldinit Geometry
      .class public auto ansi abstract sealed beforefieldinit LinAlg
      .class public auto ansi abstract beforefieldinit SpawnObjectParameters
      .class nested private auto ansi sealed beforefieldinit '<getID>d__7'
      .class public auto ansi beforefieldinit tesse_base
      .class public auto ansi beforefieldinit tesse_command_line_parser
    1897:  .class public auto ansi beforefieldinit QuadrotorDynamics_w
    1935:      IL_0019:  stfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics_w::udp_client
    1963:    IL_0002:  call instance void class QuadrotorDynamics_w::Connect()
    1975:    IL_0022:  stfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics_w::rb
    1977:    IL_0028:  ldfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics_w::rb
    2010:    IL_000f:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics_w::udp_client
    2026:    IL_0033:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics_w::udp_client
    2028:    IL_0039:  ldflda class [System]System.Net.IPEndPoint QuadrotorDynamics_w::ip_endpoint
    2033:    IL_0046:  ldfld class [System]System.Net.Sockets.UdpClient QuadrotorDynamics_w::udp_client
    2586:    IL_0003:  call instance float32[] class QuadrotorDynamics_w::GrabW()
    2608:    IL_0036:  call instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector4 class QuadrotorDynamics_w::Dynamics(valuetype [UnityEngine.CoreModule]UnityEngine.Vector4)
    2611:    IL_003d:  ldfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics_w::rb
    2622:    IL_0060:  ldfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody QuadrotorDynamics_w::rb
    2625:    IL_006f:  call instance float32[0...,0...] class QuadrotorDynamics_w::GetRotationMatrix(valuetype [UnityEngine.CoreModule]UnityEngine.Quaternion)
    2641:    IL_0094:  call instance valuetype [UnityEngine.CoreModule]UnityEngine.Vector3 class QuadrotorDynamics_w::MatrixVectorMultiplication(float32[0...,0...], valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
          IL_0029:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
          IL_002e:  nop
          IL_002f:  nop
          IL_0030:  leave.s IL_0032
    
        } // end handler 0
        IL_0032:  ret
        } // end of method tesse_quadrotor_controller::Connect
    
        // method line 114
        .method private hidebysig
               instance default valuetype [UnityEngine.CoreModule]UnityEngine.Vector4 GetWrench (valuetype [UnityEngine.CoreModule]UnityEngine.Vector4 w)  cil managed
        {
            // Method begins at RVA 0x5bd0
        // Code size 327 (0x147)
        .maxstack 6
        .locals init (
            float32    V_0,
            float32    V_1,
            float32    V_2,
            float32    V_3,
            float32    V_4,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector3    V_5,
            float32    V_6,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector3    V_7,
            valuetype [UnityEngine.CoreModule]UnityEngine.Vector4    V_8)
        IL_0000:  nop
        IL_0001:  ldarg.0
        IL_0002:  ldfld float32 tesse.tesse_quadrotor_controller::c_f
        IL_0007:  ldarg.1
        IL_0008:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::x
        IL_000d:  mul
        IL_000e:  ldarg.1
        IL_000f:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::x
        IL_0014:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_0019:  mul
        IL_001a:  stloc.0
        IL_001b:  ldarg.0
        IL_001c:  ldfld float32 tesse.tesse_quadrotor_controller::c_f
        IL_0021:  ldarg.1
        IL_0022:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::y
        IL_0027:  mul
        IL_0028:  ldarg.1
        IL_0029:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::y
        IL_002e:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_0033:  mul
        IL_0034:  stloc.1
        IL_0035:  ldarg.0
        IL_0036:  ldfld float32 tesse.tesse_quadrotor_controller::c_f
        IL_003b:  ldarg.1
        IL_003c:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::z
        IL_0041:  mul
        IL_0042:  ldarg.1
        IL_0043:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::z
        IL_0048:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_004d:  mul
        IL_004e:  stloc.2
        IL_004f:  ldarg.0
        IL_0050:  ldfld float32 tesse.tesse_quadrotor_controller::c_f
        IL_0055:  ldarg.1
        IL_0056:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::w
        IL_005b:  mul
        IL_005c:  ldarg.1
        IL_005d:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::w
        IL_0062:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_0067:  mul
        IL_0068:  stloc.3
        IL_0069:  ldloc.0
        IL_006a:  ldloc.1
        IL_006b:  add
        IL_006c:  ldloc.2
        IL_006d:  add
        IL_006e:  ldloc.3
        IL_006f:  add
        IL_0070:  stloc.s 4
        IL_0072:  ldloca.s 5
        IL_0074:  ldc.r4 0.
        IL_0079:  ldarg.0
        IL_007a:  ldfld float32 tesse.tesse_quadrotor_controller::c_d
        IL_007f:  ldarg.1
        IL_0080:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::x
        IL_0085:  ldarg.1
        IL_0086:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::x
        IL_008b:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_0090:  mul
        IL_0091:  neg
        IL_0092:  ldarg.1
        IL_0093:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::y
        IL_0098:  ldarg.1
        IL_0099:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::y
        IL_009e:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_00a3:  mul
        IL_00a4:  add
        IL_00a5:  ldarg.1
        IL_00a6:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::z
        IL_00ab:  ldarg.1
        IL_00ac:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::z
        IL_00b1:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_00b6:  mul
        IL_00b7:  sub
        IL_00b8:  ldarg.1
        IL_00b9:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::w
        IL_00be:  ldarg.1
        IL_00bf:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector4::w
        IL_00c4:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Abs(float32)
        IL_00c9:  mul
        IL_00ca:  add
        IL_00cb:  mul
        IL_00cc:  ldc.r4 0.
        IL_00d1:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_00d6:  ldarg.0
        IL_00d7:  ldfld float32 tesse.tesse_quadrotor_controller::arm_length
        IL_00dc:  ldc.r4 2.
        IL_00e1:  call float32 valuetype [UnityEngine.CoreModule]UnityEngine.Mathf::Sqrt(float32)
        IL_00e6:  div
        IL_00e7:  stloc.s 6
        IL_00e9:  ldloca.s 7
        IL_00eb:  ldloc.s 6
        IL_00ed:  neg
        IL_00ee:  ldloc.0
        IL_00ef:  ldloc.1
        IL_00f0:  add
        IL_00f1:  ldloc.2
        IL_00f2:  sub
        IL_00f3:  ldloc.3
        IL_00f4:  sub
        IL_00f5:  mul
        IL_00f6:  ldc.r4 0.
        IL_00fb:  ldloc.s 6
        IL_00fd:  neg
        IL_00fe:  ldloc.0
        IL_00ff:  neg
        IL_0100:  ldloc.1
        IL_0101:  add
        IL_0102:  ldloc.2
        IL_0103:  add
        IL_0104:  ldloc.3
        IL_0105:  sub
        IL_0106:  mul
        IL_0107:  call instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_010c:  ldloc.s 4
        IL_010e:  ldloc.s 7
        IL_0110:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::x
        IL_0115:  ldloc.s 5
        IL_0117:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::x
        IL_011c:  add
        IL_011d:  ldloc.s 7
        IL_011f:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::y
        IL_0124:  ldloc.s 5
        IL_0126:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::y
        IL_012b:  add
        IL_012c:  ldloc.s 7
        IL_012e:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::z
        IL_0133:  ldloc.s 5
        IL_0135:  ldfld float32 [UnityEngine.CoreModule]UnityEngine.Vector3::z
        IL_013a:  add
        IL_013b:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector4::'.ctor'(float32, float32, float32, float32)
        IL_0140:  stloc.s 8
        IL_0142:  br.s IL_0144
    
        IL_0144:  ldloc.s 8
        IL_0146:  ret
        } // end of method tesse_quadrotor_controller::GetWrench
    
        // method line 115
        .method private hidebysig
               instance default void Awake ()  cil managed
        {
            // Method begins at RVA 0x513a
        // Code size 9 (0x9)
        .maxstack 8
        IL_0000:  nop
        IL_0001:  ldarg.0
        IL_0002:  call instance void class tesse.tesse_controller_base::Awake()
        IL_0007:  nop
        IL_0008:  ret
        } // end of method tesse_quadrotor_controller::Awake
    
        // method line 116
        .method private hidebysig
               instance default void Start ()  cil managed
        {
            // Method begins at RVA 0x5d23
        // Code size 46 (0x2e)
        .maxstack 8
        IL_0000:  nop
        IL_0001:  ldarg.0
        IL_0002:  ldarg.0
        IL_0003:  call instance !!0 class [UnityEngine.CoreModule]UnityEngine.Component::GetComponent<class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody> ()
        IL_0008:  stfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody tesse.tesse_quadrotor_controller::rigidBody
        IL_000d:  ldarg.0
        IL_000e:  ldfld class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody tesse.tesse_quadrotor_controller::rigidBody
        IL_0013:  ldc.r4 0.10000000149011612
        IL_0018:  ldc.r4 0.10000000149011612
        IL_001d:  ldc.r4 0.20000000298023224
        IL_0022:  newobj instance void valuetype [UnityEngine.CoreModule]UnityEngine.Vector3::'.ctor'(float32, float32, float32)
        IL_0027:  callvirt instance void class [UnityEngine.PhysicsModule]UnityEngine.Rigidbody::set_inertiaTensor(valuetype [UnityEngine.CoreModule]UnityEngine.Vector3)
        IL_002c:  nop
        IL_002d:  ret
        } // end of method tesse_quadrotor_controller::Start
    
        // method line 117
        .method private hidebysig
               instance default float32[] GrabW ()  cil managed
        {
            // Method begins at RVA 0x5d54
        // Code size 212 (0xd4)
        .maxstack 5
        .locals init (
            unsigned int8[]    V_0,
            bool    V_1,
            float32[]    V_2,
            bool    V_3,
            bool    V_4,
            int32    V_5,
            bool    V_6,
            float32[]    V_7)
        IL_0000:  nop
        IL_0001:  ldnull
        IL_0002:  stloc.0
        IL_0003:  ldstr "Trying to grab pose"
        IL_0008:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
        IL_000d:  nop
        IL_000e:  ldarg.0
        IL_000f:  ldfld class [System]System.Net.Sockets.UdpClient tesse.tesse_quadrotor_controller::udp_client
        IL_0014:  callvirt instance int32 class [System]System.Net.Sockets.UdpClient::get_Available()
        IL_0019:  ldc.i4.0
        IL_001a:  cgt
        IL_001c:  stloc.1
        IL_001d:  ldloc.1
        IL_001e:  brfalse IL_00c0
    
        IL_0023:  nop
        IL_0024:  ldstr "UDP client available"
        IL_0029:  call void class [UnityEngine.CoreModule]UnityEngine.Debug::Log(object)
        IL_002e:  nop
        IL_002f:  br.s IL_0045
    
        IL_0031:  nop
        IL_0032:  ldarg.0
        IL_0033:  ldfld class [System]System.Net.Sockets.UdpClient tesse.tesse_quadrotor_controller::udp_client
    trajectory t=25.04 s, position=[-0.0222484, -0.02224858, 1.805749], error=0.197 m
    {
      "source": "Official MIT Lab3 Unity/TESSE via Box64 0.3.6",
      "complete_duration": true,
      "samples": 1254,
      "trajectory_duration_s": 25.039999999,
      "steady_position_rms_m": 0.24516090982344205,
      "steady_position_max_m": 0.3720797437132154,
      "final_position_error_m": 0.19678272692382423
    }
    ✓ • 0ms

## Activity

    $ python3 - <<'PY'
        import numpy as np
        p=np.genfromtxt('report/trials/unity_hover.csv',delimiter=',',names=True)
        s=np.column_stack([p['rotor'+str(i)] for i in range(1,5)])
        m=p['trajectory_time']>10
        f=.001*np.sum(s*np.abs(s),axis=1)
        print('mean z',p['z'][m].mean(),'force',f[m].mean(),'rotors',np.mean(s[m],axis=0),'mean yaw',p['yaw'][m].mean())
        print('z_std',p['z'][m].std(),'force std',f[m].std())
        PY
        docker exec ros_noetic_lab3 bash -lc 'sed -n "8490,8545p" /tmp/lab3-unity.il; grep -n "tesse_quadrotor_controller::.ctor" /tmp/lab3-unity.il; source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; rosnode kill /controller_node /traj_publisher'
    mean z 1.773078275132275 force 10.243559017085264 rotors [50.58820384 50.61213548 50.61214676 50.58842394] mean yaw 0.7853988832667983
    z_std 0.05855124099802181 force std 0.19618790532372485
        .field  private  class tesse.tesse_metadata_interface tmi
        .field  private  unsigned int32 mult_image_tag
    
        // method line 123
        .method private hidebysig
               instance default void Start ()  cil managed
        {
            // Method begins at RVA 0x6158
        // Code size 206 (0xce)
        .maxstack 3
        .locals init (
            unsigned int8[]    V_0,
            bool    V_1,
            class [UnityEngine.CoreModule]UnityEngine.Camera[]    V_2,
            int32    V_3,
            class [UnityEngine.CoreModule]UnityEngine.Camera    V_4)
        IL_0000:  nop
        IL_0001:  ldarg.0
        IL_0002:  call instance void class tesse.tesse_base::Start()
        IL_0007:  nop
        IL_0008:  ldarg.0
        IL_0009:  ldarg.0
        IL_000a:  ldfld class tesse.tesse_command_line_parser tesse.tesse_base::cla_parser
        IL_000f:  ldfld int32 tesse.tesse_command_line_parser::img_listen_port
        IL_0014:  stfld int32 tesse.tesse_image_interface::img_listen_port
        IL_0019:  ldarg.0
        IL_001a:  ldarg.0
        IL_001b:  ldfld class tesse.tesse_command_line_parser tesse.tesse_base::cla_parser
        IL_0020:  ldfld int32 tesse.tesse_command_line_parser::img_send_port
        IL_0025:  stfld int32 tesse.tesse_image_interface::img_send_port
        IL_002a:  ldarg.0
        IL_002b:  ldarg.0
        IL_002c:  ldfld class tesse.tesse_command_line_parser tesse.tesse_base::cla_parser
        IL_0031:  ldfld string tesse.tesse_command_line_parser::host_ip_address
        IL_0036:  stfld string tesse.tesse_image_interface::host_ip_address
        IL_003b:  ldarg.0
        IL_003c:  ldarg.0
        IL_003d:  ldftn instance void class tesse.tesse_image_interface::'<Start>b__33_0'()
        IL_0043:  newobj instance void class [mscorlib]System.Threading.ThreadStart::'.ctor'(object, native int)
        IL_0048:  newobj instance void class [mscorlib]System.Threading.Thread::'.ctor'(class [mscorlib]System.Threading.ThreadStart)
        IL_004d:  stfld class [mscorlib]System.Threading.Thread tesse.tesse_image_interface::img_request_thread
        IL_0052:  ldarg.0
        IL_0053:  ldfld class [mscorlib]System.Threading.Thread tesse.tesse_image_interface::img_request_thread
        IL_0058:  callvirt instance void class [mscorlib]System.Threading.Thread::Start()
        IL_005d:  nop
        IL_005e:  ldarg.0
        IL_005f:  ldc.i4.1
        IL_0060:  stfld bool tesse.tesse_image_interface::img_request_running
        IL_0065:  ldarg.0
        IL_0066:  ldfld class [mscorlib]System.Collections.Generic.List`1<class [UnityEngine.CoreModule]UnityEngine.Camera> tesse.tesse_image_interface::agent_cameras
        IL_006b:  callvirt instance int32 class [mscorlib]System.Collections.Generic.List`1<class [UnityEngine.CoreModule]UnityEngine.Camera>::get_Count()
        IL_0070:  ldc.i4.0
        IL_0071:  ceq
        IL_0073:  stloc.1
        IL_0074:  ldloc.1
        IL_0075:  brfalse.s IL_00a4
    8445:    } // end of method tesse_quadrotor_controller::.ctor
    killing:
     * /controller_node
     * /traj_publisher
    killed
    ✓ • 732ms

## Activity

    $ docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; python3 /workspace/lab3/scripts/monitor_unity.py --output /workspace/lab3/report/trials/unity_circle_initial.csv --duration 40 >/tmp/lab3-unity-circle-monitor.log 2>&1'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roslaunch controller_pkg traj_tracking.launch gains_file:=/workspace/lab3/controller_pkg/config/gains_unity.yaml >/tmp/lab3-unity-circle-controller.log 2>&1'
    ✓ • 57ms

## Assistant

官方 Lab 3 模拟器已经通过 Box64 正常启动，ROS 桥接也已接通。无人机完成了悬停验证，现在正在跟踪题目原定的 5 米半径圆轨迹；我会根据实测误差继续调整参数。

## Activity

    $ docker exec -d ros_noetic_lab3 bash -lc 'Xvfb :96 -screen 0 1280x800x24 >/tmp/lab3-official-rviz-xvfb.log 2>&1'; docker exec -d ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost DISPLAY=:96 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1; rosrun rviz rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz >/tmp/lab3-official-rviz.log 2>&1'; docker exec ros_noetic_lab3 bash -lc 'tail -8 /tmp/lab3-unity-circle-monitor.log; sed -n "8400,8448p" /tmp/lab3-unity.il'; df -h .
    trajectory t=0.10 s, position=[0.3539814, 0.3533833, 0.7000261], error=4.820 m
    trajectory t=5.02 s, position=[2.923585, -4.236206, 1.683187], error=0.376 m
    trajectory t=10.10 s, position=[-4.684399, 1.656921, 1.839516], error=0.164 m
    trajectory t=15.00 s, position=[4.76716, 1.65496, 1.800396], error=0.228 m
            // Method begins at RVA 0x60c0
        // Code size 138 (0x8a)
        .maxstack 2
        IL_0000:  ldarg.0
        IL_0001:  ldstr "localhost"
        IL_0006:  stfld string tesse.tesse_quadrotor_controller::host
        IL_000b:  ldarg.0
        IL_000c:  ldc.i4 12346
        IL_0011:  stfld int32 tesse.tesse_quadrotor_controller::port
        IL_0016:  ldarg.0
        IL_0017:  ldc.r4 0.0010000000474974513
        IL_001c:  stfld float32 tesse.tesse_quadrotor_controller::c_f
        IL_0021:  ldarg.0
        IL_0022:  ldc.r4 9.9999997473787516e-06
        IL_0027:  stfld float32 tesse.tesse_quadrotor_controller::c_d
        IL_002c:  ldarg.0
        IL_002d:  ldc.r4 0.30000001192092896
        IL_0032:  stfld float32 tesse.tesse_quadrotor_controller::arm_length
        IL_0037:  ldarg.0
        IL_0038:  ldc.i4.4
        IL_0039:  newarr [netstandard]System.Single
        IL_003e:  stfld float32[] tesse.tesse_quadrotor_controller::w_
        IL_0043:  ldarg.0
        IL_0044:  ldc.i4.0
        IL_0045:  stfld bool tesse.tesse_quadrotor_controller::prop_is_pressed
        IL_004a:  ldarg.0
        IL_004b:  ldc.r4 500.
        IL_0050:  stfld float32 tesse.tesse_quadrotor_controller::max_prop_speed
        IL_0055:  ldarg.0
        IL_0056:  ldc.r4 0.
        IL_005b:  stfld float32 tesse.tesse_quadrotor_controller::min_prop_speed
        IL_0060:  ldarg.0
        IL_0061:  ldc.r4 50.
        IL_0066:  stfld float32 tesse.tesse_quadrotor_controller::prop_accel
        IL_006b:  ldarg.0
        IL_006c:  ldc.r4 2.
        IL_0071:  stfld float32 tesse.tesse_quadrotor_controller::spawn_height
        IL_0076:  ldarg.0
        IL_0077:  ldc.i4.4
        IL_0078:  newarr [netstandard]System.Single
        IL_007d:  stfld float32[] tesse.tesse_quadrotor_controller::'<propSpeeds>k__BackingField'
        IL_0082:  ldarg.0
        IL_0083:  call instance void class tesse.tesse_controller_base::'.ctor'()
        IL_0088:  nop
        IL_0089:  ret
        } // end of method tesse_quadrotor_controller::.ctor
    
        .property instance float32[] propSpeeds ()
        {
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/nvme0n1p2   39G   23G   15G  61% /
    ✓ • 432ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -16 /tmp/lab3-unity-circle-monitor.log; ffmpeg -y -loglevel error -f x11grab -video_size 1280x800 -i :96 -frames:v 1 /workspace/lab3/report/video/rviz_unity_trial.png'
    trajectory t=10.10 s, position=[-4.684399, 1.656921, 1.839516], error=0.164 m
    trajectory t=15.00 s, position=[4.76716, 1.65496, 1.800396], error=0.228 m
    trajectory t=20.00 s, position=[-2.817459, -4.207043, 1.818422], error=0.206 m
    trajectory t=25.02 s, position=[-0.2363272, 5.0449, 1.841014], error=0.174 m
    trajectory t=30.10 s, position=[3.035283, -4.053452, 1.823361], error=0.203 m
    trajectory t=35.12 s, position=[-4.855436, 1.48009, 1.746881], error=0.274 m
    trajectory t=40.00 s, position=[4.655701, 1.976437, 1.768604], error=0.257 m
    {
      "source": "Official MIT Lab3 Unity/TESSE via Box64 0.3.6",
      "complete_duration": true,
      "samples": 1999,
      "trajectory_duration_s": 40.0,
      "steady_position_rms_m": 0.2710110012866323,
      "steady_position_max_m": 0.44628792343177226,
      "final_position_error_m": 0.256735462226358
    }
    ✓ • 204ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_unity_trial.png

## Activity

    • Context compacted

## Activity

    $ cat controller_pkg/config/gains_unity.yaml && sed -n '1,220p' scripts/monitor_unity.py && cat controller_pkg/launch/traj_tracking.launch && sed -n '1,200p' README.md
    # Official Unity / Box64 tuning; low rendered frame rates hold motor commands.
    # Keep the handout's model constants; tune the feedback on the actual plant.
    kx: 2.0
    kv: 2.4
    kr: 1.8
    komega: 0.7
    hz: 200.0
    state_timeout: 1.0
    desired_timeout: 1.0
    compensate_drag: false
    #!/usr/bin/env python3
    """Record live official TESSE telemetry and publish paths for the RViz video."""
    import argparse
    import csv
    import json
    import math
    import threading
    import time
    from pathlib import Path as FilePath
    
    import numpy as np
    import rospy
    from geometry_msgs.msg import PoseStamped
    from mav_msgs.msg import Actuators
    from nav_msgs.msg import Odometry, Path
    from trajectory_msgs.msg import MultiDOFJointTrajectoryPoint
    from visualization_msgs.msg import Marker
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--duration", type=float, default=50.0)
    parser.add_argument("--wall-timeout", type=float, default=300.0)
    args = parser.parse_args()
    rospy.init_node("lab3_unity_monitor", anonymous=True)
    lock = threading.Lock()
    rows = []
    reference = None
    rotors = [0.0]*4
    actual_path, desired_path = Path(), Path()
    actual_path.header.frame_id = desired_path.header.frame_id = "world"
    actual_pub = rospy.Publisher("/flight/actual", Path, queue_size=1)
    desired_pub = rospy.Publisher("/flight/desired", Path, queue_size=1)
    source_pub = rospy.Publisher("/flight/source", Marker, queue_size=1, latch=True)
    last_path_t = -1.0
    
    def yaw(q):
        return math.atan2(2*(q.w*q.z+q.x*q.y), 1-2*(q.y*q.y+q.z*q.z))
    
    def on_reference(msg):
        global reference
        if not msg.transforms:
            return
        with lock:
            reference = msg
    
    def on_rotors(msg):
        global rotors
        if len(msg.angular_velocities) == 4:
            with lock:
                rotors = list(msg.angular_velocities)
    
    def on_state(msg):
        global last_path_t
        with lock:
            if reference is None:
                return
            ref = reference
            speed = list(rotors)
            target = ref.transforms[0]
            p = msg.pose.pose.position
            pd = target.translation
            w = msg.twist.twist.angular
            stamp = msg.header.stamp.to_sec()
            rows.append([stamp, ref.time_from_start.to_sec(), p.x,p.y,p.z,
                         pd.x,pd.y,pd.z,yaw(msg.pose.pose.orientation),yaw(target.rotation),
                         w.x,w.y,w.z,*speed])
            if stamp-last_path_t < 0.1:
                return
            last_path_t = stamp
            actual_path.header.stamp = desired_path.header.stamp = msg.header.stamp
            actual_path.poses.append(PoseStamped(header=msg.header,pose=msg.pose.pose))
            desired = PoseStamped()
            desired.header = msg.header
            desired.pose.position.x,desired.pose.position.y,desired.pose.position.z = pd.x,pd.y,pd.z
            desired.pose.orientation = target.rotation
            desired_path.poses.append(desired)
            actual_path.poses = actual_path.poses[-1200:]
            desired_path.poses = desired_path.poses[-1200:]
            actual_pub.publish(actual_path)
            desired_pub.publish(desired_path)
    
    rospy.Subscriber("/desired_state",MultiDOFJointTrajectoryPoint,on_reference,queue_size=1)
    rospy.Subscriber("/rotor_speed_cmds",Actuators,on_rotors,queue_size=1)
    rospy.Subscriber("/current_state",Odometry,on_state,queue_size=100)
    marker = Marker()
    marker.header.frame_id = "world"
    marker.type = Marker.TEXT_VIEW_FACING
    marker.action = Marker.ADD
    marker.pose.position.z = 5
    marker.pose.orientation.w = 1
    marker.scale.z = 0.35
    marker.color.r = marker.color.g = marker.color.b = marker.color.a = 1
    marker.text = "Official MIT Lab3 TESSE / Box64"
    source_pub.publish(marker)
    started = time.monotonic()
    next_progress = 0
    complete = False
    try:
        while not rospy.is_shutdown() and time.monotonic()-started < args.wall_timeout:
            with lock:
                latest = rows[-1] if rows else None
            if latest and latest[1] >= next_progress:
                error = np.linalg.norm(np.array(latest[2:5])-latest[5:8])
                print("trajectory t=%.2f s, position=%s, error=%.3f m" %
                      (latest[1],latest[2:5],error),flush=True)
                next_progress += 5
            if latest and latest[1] >= args.duration:
                complete = True
                break
            time.sleep(0.1)
    finally:
        with lock:
            data = np.asarray(rows)
        path = FilePath(args.output)
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("w",newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["t","trajectory_time","x","y","z","xd","yd","zd",
                             "yaw","yawd","wx_world","wy_world","wz_world",
                             "rotor1","rotor2","rotor3","rotor4"])
            writer.writerows(data)
        if len(data):
            error = np.linalg.norm(data[:,2:5]-data[:,5:8],axis=1)
            steady = data[:,1] >= min(2*4*math.pi,args.duration/2)
            summary = dict(source="Official MIT Lab3 Unity/TESSE via Box64 0.3.6",
                           complete_duration=complete, samples=len(data),
                           trajectory_duration_s=float(data[-1,1]),
                           steady_position_rms_m=float(np.sqrt(np.mean(error[steady]**2))) if steady.any() else None,
                           steady_position_max_m=float(error[steady].max()) if steady.any() else None,
                           final_position_error_m=float(error[-1]))
            path.with_suffix(".json").write_text(json.dumps(summary,indent=2)+"\n")
            print(json.dumps(summary,indent=2),flush=True)
    if not complete:
        raise SystemExit("Did not record the requested trajectory duration")
    <launch>
      <arg name="static_pose" default="false"/>
      <arg name="rviz" default="false"/>
      <arg name="gains_file" default="$(find controller_pkg)/config/gains.yaml"/>
      <node name="traj_publisher" pkg="controller_pkg" type="traj_publisher" output="screen">
        <param name="static_pose" value="$(arg static_pose)"/>
      </node>
      <node name="controller_node" pkg="controller_pkg" type="controller_node" output="screen">
        <rosparam command="load" file="$(arg gains_file)"/>
      </node>
      <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz"
            args="-d $(find controller_pkg)/rviz/lab3.rviz"/>
    </launch>
    # Lab 3 — Quadrotor geometric control
    
    依据 [MIT VNAV 2023 Lab 3](https://vnav.mit.edu/labs_2023/lab3/exercises.html) 实现。
    
    ## 交付状态
    
    | 交付项 | 文件 | 状态 |
    | --- | --- | --- |
    | Deliverable 1：ROS 四元数转换 | `deliverable_1.txt` | 完成 |
    | Deliverable 2：旋翼布局秩分析、阻力补偿 | `report/deliverable_2.pdf`、`.tex` | 完成 |
    | Deliverable 3：完整控制器源码 | `controller_pkg/` | ROS Noetic 编译通过 |
    | 悬停、圆轨迹及阻力补偿数值验证 | `report/numerical_validation.txt` | 独立刚体模型验证，非 TESSE |
    | 真实 ROS 节点闭环运行 | `report/ros_flight.csv`、`ros_metrics.json` | 独立刚体模型驱动实际控制节点，非 TESSE |
    | RViz 演示录像 | `report/video/rviz_rigid_body_demo.mp4` | 独立模型演示，画面内明确标注来源 |
    | 官方 TESSE 飞行、最终调参及公开录像链接 | `rviz_drone_flight.txt` | **待完成**，见下方环境限制 |
    
    当前主机为 ARM64；官方安装包中的 `lab3.x86_64` 为 x86_64。
    QEMU 4.2 启动失败于 Mono 的 `sigaltstack` 断言，QEMU 8.2 失败于内部 SIGSEGV。
    失败日志保存在 `report/tesse_qemu_4_startup.txt` 和 `report/tesse_qemu_8_startup.txt`。
    因此尚不能声称在官方 TESSE 中完成了稳定飞行；独立模型录像也不能作为 TESSE 验证的证明。
    
    个人题按原题要求提交个人仓库；团队仓库提交完整 `controller_pkg` 和最终录像公开链接。
    
    ## 控制器实现
    
    - `src/controller_node.cpp`：订阅 `/desired_state` 和 `/current_state`，1000 Hz 发布 `/rotor_speed_cmds`；初始化、参数默认值、非法消息及超时检查完整。
    - `include/controller_pkg/geometric_controller.h`：位置/速度误差、期望 SO(3) 姿态、姿态反馈、陀螺项和旋翼分配。控制数学与 ROS 消息处理分离，数值验证使用同一份控制实现。
    - `src/traj_publisher.cpp`：保留官方半径 5 m、高度 2 m、时间尺度 2 s 的圆轨迹，周期为 `4*pi ≈ 12.566 s`，期望 yaw 为 `-t/2`；静态目标通过参数切换。
    - `config/gains.yaml`：`kx=6, kv=4.7, kr=64, komega=16`。这些值已在独立模型中验证，仍须在目标 TESSE 环境中复核。
    
    状态消息中的位置和线速度都按实验定义使用世界坐标。角速度转换为
    `omega_body = R.transpose() * omega_world`。这遵循 TESSE 的实验约定，与一般
    `nav_msgs/Odometry` 的 child frame twist 约定不同。
    
    采用 ROS 向上的 z 轴：
    
    ```text
    A = -kx*(x-xd) - kv*(v-vd) + m*g*e3 + m*ad
    b3d = A / ||A||
    b2d = normalize(b3d cross [cos(yawd), sin(yawd), 0])
    Rd = [b2d cross b3d, b2d, b3d]
    eR = 0.5 * vee(Rd^T*R - R^T*Rd)
    f = A dot (R*e3)
    M = -kr*eR - komega*omega_body + omega_body cross (J*omega_body)
    ```
    
    按骨架允许的简化，忽略 `Omega_d` 及其导数，因此旋转轨迹中可能有小的姿态跟踪滞后。
    零期望力和期望方向平行情形提供了确定的备用轴，避免归一化除零。
    
    官方模拟器的旋翼位置为 `(+a,+a),(-a,+a),(-a,-a),(+a,-a)`，其中 `a=d/sqrt(2)`。
    令 `s_i=omega_i*abs(omega_i)`，使用
    
    ```text
                  [ cf     cf     cf     cf   ]
    [f Mx My Mz] = [ a*cf   a*cf  -a*cf  -a*cf] s
                  [-a*cf   a*cf   a*cf  -a*cf]
                  [ cd    -cd     cd    -cd   ]
    ```
    
    上式左边按列向量理解。逆映射后对每个分量取带符号平方根，单位为 rad/s；
    保留题目模拟器允许的负转速。悬停每个旋翼转速应为 `sqrt(9.81/(4*0.001)) ≈ 49.523 rad/s`。
    个人题示意图使用另一套旋翼编号，不能直接拿其矩阵驱动模拟器。
    
    `compensate_drag:=true` 时，从 A 中减去 `R*(-D*(R^T*v)*abs(R^T*v))`；默认关闭，
    只有被控对象确实具有 Deliverable 2 给定的阻力时才应启用。
    
    ## ROS Noetic 构建
    
    在 Ubuntu 20.04 + ROS Noetic 的 catkin 工作区内执行：
    
    ```bash
    source /opt/ros/noetic/setup.bash
    sudo apt-get update
    sudo apt-get install -y python3-catkin-tools ros-noetic-tf2-eigen \
      ros-noetic-tf2-geometry-msgs ros-noetic-ackermann-msgs ros-noetic-cv-bridge \
      ros-noetic-rviz python3-numpy python3-scipy python3-defusedxml python3-pil
    
    mkdir -p ~/vnav_ws/src
    cp -r /path/to/this/lab3/controller_pkg ~/vnav_ws/src/
    cd ~/vnav_ws/src
    git clone https://github.com/ethz-asl/mav_comm.git
    
    # 官方桥接和 catkin_simple 在本仓库的 lab1/vnav-codes/lab3 内。
    cp -r /path/to/repository/lab1/vnav-codes/lab3/catkin_simple .
    cp -r /path/to/repository/lab1/vnav-codes/lab3/tesse-ros-bridge .
    cd tesse-ros-bridge/tesse-interface
    python3 -m pip install --no-deps .
    
    cd ~/vnav_ws
    catkin build
    source devel/setup.bash
    ```
    
    Python 标准库已提供 enum，无需安装 Python 2 的 enum34。上述环境使用发行版自带 NumPy、SciPy、Pillow、defusedxml。
    实际构建记录见 `report/build_noetic.txt`。
    
    当前会话创建了独立容器 `ros_noetic_lab3`，代码挂载在 `/workspace/lab3`，
    构建工作区在 `/tmp/lab3_ws`。可直接进入并复用：
    
    ```bash
    docker start ros_noetic_lab3
    docker exec -it ros_noetic_lab3 bash
    source /tmp/lab3_ws/devel/setup.bash
    ```
    
    这些 `/tmp` 依赖和容器状态不是永久安装流程；换机器时按上面的源码构建步骤操作。
    本次使用的 `mav_comm` 提交为 `56122218eb1ec34deaa641598ebacf24e26c349b`。
    演示录像按用户要求仅保留本地，未上传 Google Drive。
    
    ## 官方 TESSE 运行及最终交付
    
    需要能够运行 x86_64 Linux Unity Player 的环境。下载
    [官方安装包](https://vnav.mit.edu/material/lab3.zip)，解压后在不同终端运行：
    
    ```bash
    # 终端 1
    cd /path/to/simulator/lab3
    chmod +x lab3.x86_64
    ./lab3.x86_64
    
    # 终端 2；ROS 终端都先 source 工作区
    roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch
    
    # 终端 3：先观察静态目标 (0,0,2)，yaw=pi/4
    DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg traj_tracking.launch static_pose:=true rviz:=true
    ```
    
    静态跟踪稳定后，结束控制节点，按 R 重置模拟器，再启动圆轨迹：
    
    ```bash
    DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg traj_tracking.launch rviz:=true
    ```
    
    根据实际结果调整 `config/gains.yaml`。`kx,kv` 调节位置和速度反馈，`kr,komega` 调节姿态恢复和角速度阻尼。
    如有需要，按 W 启动旋翼。记录 RViz 中至少完整一圈，上传 Google Drive 或 Dropbox，
    设置为“知道链接的任何人可查看”，将实际公开链接写入 `rviz_drone_flight.txt`。
    
    ## ARM64 上的独立模型演示
    
    该演示启动实际编译的控制器和轨迹节点，由独立刚体模型读取旋翼转速并积分运动，
    在 ROS 中发布状态、仿真时钟和轨迹。**该模型没有 Unity 接触、碰撞或电机动态，不能替代 TESSE 验证。**
    
    ```bash
    source /tmp/lab3_ws/devel/setup.bash
    DISABLE_ROS1_EOL_WARNINGS=1 roslaunch controller_pkg rigid_body_demo.launch duration:=60
    ```
    
    模型会在指定时长后退出并写出 CSV，其余可视化节点用 Ctrl+C 结束。
    容器内无物理显示时可使用 `Xvfb :99 -screen 0 1280x800x24`，再设置
    `DISPLAY=:99 LIBGL_ALWAYS_SOFTWARE=1`。录屏示例：
    
    ```bash
    ffmpeg -f x11grab -video_size 1280x800 -framerate 20 -i :99 -t 20 \
      -c:v libx264 -preset ultrafast -pix_fmt yuv420p -movflags +faststart rviz_demo.mp4
    ```
    
    ## 数值验证与报告再生成
    
    ```bash
    # 宿主机仅需 C++11 编译器和 Eigen；使用生产控制器头文件。
    bash scripts/validate_offline.sh > report/numerical_validation.txt
    
    # 在安装 matplotlib 的环境中，根据真实 ROS 日志生成图和指标。
    python3 scripts/plot_flight.py
    
    # LaTeX 报告
    cd report
    pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex
    pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex
    ```
    
    数值检查比较悬停、圆轨迹、较小积分步长以及有/无阻力补偿；动力学中的旋翼力矩通过
    独立的 `rho cross force` 计算，以检查控制器的电机分配符号。
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; rosnode list; ps -eo pid,args | rg "monitor_unity|traj_tracking|ffmpeg|lab3.x86"'
    /controller_node
    /lab3_official_rviz
    /rosout
    /tesse/quadrotor_control_interface
    /tesse/tesse_ros_bridge
    /traj_publisher
    bash: rg: command not found
    ✗ (127) • 672ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/config/gains_unity.yaml
    @@ -2,6 +2,6 @@
     # Keep the handout's model constants; tune the feedback on the actual plant.
    -kx: 2.0
    -kv: 2.4
    -kr: 1.8
    -komega: 0.7
    +kx: 4.0
    +kv: 3.0
    +kr: 2.4
    +komega: 0.6
     hz: 200.0

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost DISABLE_ROS1_EOL_WARNINGS=1; rosnode kill /controller_node /traj_publisher; nohup python3 /workspace/lab3/scripts/monitor_unity.py --output /workspace/lab3/report/trials/unity_circle_tuned.csv --duration 40 >/tmp/lab3-circle-tuned-monitor.log 2>&1 </dev/null & nohup roslaunch controller_pkg traj_tracking.launch gains_file:=/workspace/lab3/controller_pkg/config/gains_unity.yaml >/tmp/lab3-circle-tuned.log 2>&1 </dev/null &'
    killing:
     * /controller_node
     * /traj_publisher
    killed
    ✓ • 560ms

## Activity

    $ du -sh ../Lab4/dependencies/*; ls scripts; cat report/validation.md; cat ../Lab4/scripts/start_tesse_box64.sh; cat ../Lab4/docker/Dockerfile.arm64
    40K    ../Lab4/dependencies/catkin_simple
    132K    ../Lab4/dependencies/mav_msgs
    376K    ../Lab4/dependencies/mav_trajectory_generation
    76K    ../Lab4/dependencies/tesse_interface
    236K    ../Lab4/dependencies/tesse_ros_bridge
    monitor_unity.py
    offline_flight.cpp
    plot_flight.py
    validate_offline.sh
    # Validation record
    
    ## Build
    
    The complete controller package and upstream TESSE bridge compiled successfully
    in ROS Noetic on Ubuntu 20.04 (ARM64). All four catkin packages succeeded with
    no build warnings. See `build_noetic.txt`. The `mav_comm` dependency was built
    from commit `56122218eb1ec34deaa641598ebacf24e26c349b`.
    
    ## Independent numerical plant
    
    The standalone check uses the same C++ controller header as the ROS node.
    The plant independently computes rotor moments from rotor positions and forces,
    then integrates the rigid-body equations with normalized quaternion updates.
    The desired trajectory is sampled at 100 Hz, matching the trajectory node.
    
    | Case | Steady position RMS error |
    | --- | ---: |
    | Static waypoint, final 5 seconds | approximately numerical roundoff |
    | Circle, 1 ms integration step, final full lap | 0.01493 m |
    | Circle, 0.5 ms integration step, final full lap | 0.01444 m |
    | Circle with quadratic drag, no compensation | 0.08337 m |
    | Circle with quadratic drag and compensation | 0.02033 m |
    
    Full metrics are in `numerical_validation.txt`. The timestep comparison shows
    that the reported centimetre-scale error is not primarily an integration artifact.
    Ignoring desired attitude-rate feedforward and sampling the desired trajectory
    both contribute to the remaining tracking error.
    
    ## ROS closed-loop run and video
    
    The compiled `controller_node` and `traj_publisher` communicated through real ROS
    topics with a separate Python rigid-body plant. That plant publishes world-frame
    angular velocity, so this run also exercises the controller's world-to-body
    conversion. The plant ran for 80 simulation seconds from rest at the origin.
    See `ros_flight.csv`, `ros_metrics.json`, and `ros_runtime_topics.txt`.
    
    Over the steady window after two nominal trajectory periods, position RMS error
    was 0.03055 m and maximum error was 0.05345 m. ROS scheduling and held state
    updates introduce additional error compared with the synchronous numerical run.
    
    The 20-second MP4 in `video/rviz_rigid_body_demo.mp4` records the actual RViz
    window during steady flight; this exceeds the nominal 12.566-second lap period.
    Its overlay explicitly identifies the independent model. The screenshot
    `video/rviz_demo_frame.png` shows the desired and actual paths and moving axes.
    The video is kept locally according to the user's preference.
    
    ## Official TESSE limitation
    
    The unmodified course Unity player is x86_64 and the host is ARM64. It failed
    under QEMU 4.2 with a Mono `sigaltstack` assertion and under QEMU 8.2 with an
    internal SIGSEGV, including a retry with Mono/Unity debugger options. See the
    saved `tesse_qemu_4_startup.txt` and `tesse_qemu_8_startup.txt` logs.
    
    The independent model has no Unity collisions, contacts, or motor dynamics.
    Its results do not establish stability in official TESSE. Final TESSE tuning,
    official flight recording, and the submission's public video URL remain pending.
    cat: ../Lab4/scripts/start_tesse_box64.sh: No such file or directory
    cat: ../Lab4/docker/Dockerfile.arm64: No such file or directory
    ✗ (1) • 0ms

## Activity

    $ rg --files ../Lab4 | rg '(scripts/|Dockerfile|README|requirements|setup.py|LICENSE)' ; cat ../Lab4/Dockerfile; cat ../Lab4/dependencies/tesse_interface/setup.py; cat controller_pkg/rviz/circle.rviz; docker exec ros_noetic_lab3 tail -10 /tmp/lab3-circle-tuned-monitor.log
    ../Lab4/README.md
    ../Lab4/Dockerfile
    ../Lab4/scripts/docker_build.sh
    ../Lab4/scripts/rigid_body_validation.py
    ../Lab4/scripts/run_unity_race.sh
    ../Lab4/scripts/monitor_unity.py
    ../Lab4/scripts/run_rigid_body_validation.sh
    ../Lab4/scripts/prepare_unity_arm64.sh
    ../Lab4/scripts/start_unity_arm64.sh
    ../Lab4/scripts/check_math.py
    ../Lab4/scripts/analyze_flight.py
    ../Lab4/scripts/test_trajectory.py
    ../Lab4/scripts/build_workspace.sh
    ../Lab4/scripts/analyze_unity.py
    ../Lab4/scripts/run_integration_checks.sh
    ../Lab4/dependencies/tesse_interface/README.md
    ../Lab4/dependencies/tesse_interface/LICENSE
    ../Lab4/dependencies/tesse_interface/setup.py
    ../Lab4/dependencies/tesse_ros_bridge/src/key_teleop/LICENSE
    ../Lab4/dependencies/tesse_ros_bridge/setup.py
    ../Lab4/dependencies/mav_trajectory_generation/LICENSE
    ../Lab4/dependencies/catkin_simple/README.md
    FROM ros:noetic-ros-base-focal
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential cmake python3-catkin-tools python3-numpy python3-matplotlib python3-scipy python3-defusedxml python3-pil python3-pip \
        libeigen3-dev libgoogle-glog-dev libyaml-cpp-dev libnlopt-cxx-dev \
        ros-noetic-tf ros-noetic-tf2-eigen ros-noetic-tf2-geometry-msgs \
        ros-noetic-rosgraph-msgs ros-noetic-visualization-msgs ros-noetic-cmake-modules \
        ros-noetic-cv-bridge ros-noetic-ackermann-msgs xvfb xdotool curl unzip \
        libgl1-mesa-dri libxcursor1 libxrandr2 libxi6 libxinerama1 libasound2 \
        libpulse0 libudev1 libgtk2.0-0 libsdl2-2.0-0 libnss3 \
        ffmpeg texlive-latex-base texlive-latex-recommended \
        && rm -rf /var/lib/apt/lists/*
    WORKDIR /workspace/lab4
    CMD ["bash"]
    ###################################################################################################
    # DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
    #
    # This material is based upon work supported by the Under Secretary of Defense for Research and
    # Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions
    # or recommendations expressed in this material are those of the author(s) and do not necessarily
    # reflect the views of the Under Secretary of Defense for Research and Engineering.
    #
    # (c) 2019 Massachusetts Institute of Technology.
    #
    # MIT Proprietary, Subject to FAR52.227-11 Patent Rights - Ownership by the contractor (May 2014)
    #
    # The software/firmware is provided to you on an As-Is basis
    #
    # Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013
    # or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work
    # are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work other
    # than as specifically authorized by the U.S. Government may violate any copyrights that exist in
    # this work.
    ###################################################################################################
    
    from setuptools import setup, find_packages
    
    setup(
        name='tesse',
        version='0.1.2',
        description='TESSE python interface',
        packages=find_packages('src'),
        # tell setuptools that all packages will be under the 'src' directory
        # and nowhere else
        package_dir={'': 'src'},
        install_requires=['numpy >= 1.16.0', 'defusedxml >= 0.6.0', 'Pillow >= 5.0.0', 'enum34 >= 1.1.10',],
    )
    Panels:
      - Class: rviz/Displays
        Name: Displays
      - Class: rviz/Views
        Name: Views
    Visualization Manager:
      Class: ""
      Global Options:
        Background Color: 35; 38; 45
        Fixed Frame: world
        Frame Rate: 30
      Displays:
        - Class: rviz/Grid
          Name: Ground
          Enabled: true
          Cell Size: 1
          Plane Cell Count: 20
          Color: 100; 110; 120
        - Class: rviz/TF
          Name: Desired frame
          Enabled: true
          Frame Timeout: 1
          Marker Scale: 0.7
          Show Arrows: true
          Show Axes: true
          Show Names: true
        - Class: rviz/Odometry
          Name: Actual vehicle
          Enabled: true
          Topic: /current_state
          Keep: 1
          Shape:
            Value: Axes
            Axes Length: 1
            Axes Radius: 0.07
          Position Tolerance: 0
          Angle Tolerance: 0
        - Class: rviz/Path
          Name: Actual path
          Enabled: true
          Topic: /flight/actual
          Color: 40; 210; 255
          Line Style: Lines
          Line Width: 0.05
          Buffer Length: 1
        - Class: rviz/Path
          Name: Desired circle
          Enabled: true
          Topic: /flight/desired
          Color: 255; 185; 45
          Line Style: Lines
          Line Width: 0.05
          Buffer Length: 1
        - Class: rviz/Marker
          Name: Simulation source
          Enabled: true
          Marker Topic: /flight/source
      Views:
        Current:
          Class: rviz/Orbit
          Distance: 21
          Pitch: 0.9
          Yaw: 0.7
          Focal Point:
            X: 0
            Y: 0
            Z: 1.5
          Target Frame: world
      Tools:
        - Class: rviz/Interact
        - Class: rviz/MoveCamera
    Window Geometry:
      Width: 1280
      Height: 800
    trajectory t=0.00 s, position=[-3.871332, -3.697889, 0.7612246], error=9.601 m
    trajectory t=5.08 s, position=[2.905204, -5.032321, 1.276382], error=1.165 m
    trajectory t=10.12 s, position=[-4.724346, 1.098959, 1.232789], error=0.977 m
    ✓ • 0ms

## Activity

    Opened https://vnav.mit.edu/labs_2023/lab3/exercises.html

## Assistant

圆轨迹已经跑通。较强的反馈参数反而增大了误差，我会保留实测更稳定的参数，并把正式 RViz 录像、飞行数据和复现步骤一起保存到本地。

## Activity

    $ cat ../Lab4/scripts/prepare_unity_arm64.sh; cat ../Lab4/scripts/start_unity_arm64.sh; cat ../Lab4/scripts/build_workspace.sh; cat .gitignore; docker exec ros_noetic_lab3 tail -8 /tmp/lab3-circle-tuned-monitor.log
    #!/usr/bin/env bash
    # Run inside the Docker container after installing Dockerfile's dependencies.
    set -eo pipefail
    LAB4_DIR=${LAB4_DIR:-/workspace/lab4}
    LAB4_RUNTIME=${LAB4_RUNTIME:-/tmp/lab4-runtime}
    mkdir -p "$LAB4_RUNTIME"
    if [ ! -x "$LAB4_RUNTIME/box64-0.3.6/build/box64" ]; then
      curl -fL --retry 3 https://codeload.github.com/ptitSeb/box64/tar.gz/refs/tags/v0.3.6 -o "$LAB4_RUNTIME/box64.tar.gz"
      tar -xzf "$LAB4_RUNTIME/box64.tar.gz" -C "$LAB4_RUNTIME"
      cmake -S "$LAB4_RUNTIME/box64-0.3.6" -B "$LAB4_RUNTIME/box64-0.3.6/build" -DARM_DYNAREC=ON -DCMAKE_BUILD_TYPE=Release
      cmake --build "$LAB4_RUNTIME/box64-0.3.6/build" -j1
    fi
    if [ ! -f "$LAB4_RUNTIME/lab4/lab4.x86_64" ]; then
      curl -fL --retry 3 https://vnav.mit.edu/material/lab4.zip -o "$LAB4_RUNTIME/lab4.zip"
      unzip -q "$LAB4_RUNTIME/lab4.zip" -d "$LAB4_RUNTIME"
    fi
    chmod +x "$LAB4_RUNTIME/lab4/lab4.x86_64"
    python3 -m pip install --no-deps "$LAB4_DIR/dependencies/tesse_interface"
    printf 'Runtime ready: %s\n' "$LAB4_RUNTIME"
    #!/usr/bin/env bash
    # Foreground session; keep it running while invoking run_unity_race.sh elsewhere.
    set -eo pipefail
    source /tmp/lab4_ws/devel/setup.bash
    export ROS_MASTER_URI=http://localhost:11316 ROS_HOSTNAME=localhost
    LAB4_RUNTIME=${LAB4_RUNTIME:-/tmp/lab4-runtime}
    export DISPLAY=:98 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0
    pids=()
    cleanup() {
      for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
      for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
    }
    trap cleanup EXIT
    Xvfb :98 -screen 0 960x600x24 > /tmp/lab4-xvfb.log 2>&1 & pids+=("$!")
    roscore -p 11316 > /tmp/lab4-unity-master.log 2>&1 & pids+=("$!")
    sleep 2
    cd "$LAB4_RUNTIME/lab4"
    "$LAB4_RUNTIME/box64-0.3.6/build/box64" ./lab4.x86_64 -screen-width 960 \
      -screen-height 600 -screen-fullscreen 0 -force-glcore \
      -logFile /tmp/lab4-unity.log > /tmp/lab4-box64.log 2>&1 & pids+=("$!")
    sleep 15
    LAB4_WINDOW_ID=$(xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
    xdotool windowfocus "$LAB4_WINDOW_ID" mousemove 512 571 click 1
    roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false \
      publish_collisions:=true > /tmp/lab4-unity-bridge.log 2>&1 & pids+=("$!")
    wait "${pids[-1]}"
    #!/usr/bin/env bash
    # Inside Docker; keep outputs outside the source repository.
    set -eo pipefail
    source /opt/ros/noetic/setup.bash
    LAB4_DIR=${LAB4_DIR:-/workspace/lab4}
    LAB3_DIR=${LAB3_DIR:-/workspace/lab3}
    LAB4_WS=${LAB4_WS:-/tmp/lab4_ws}
    mkdir -p "$LAB4_WS/src"
    for pkg in planner_pkg trajectory_generation_pkg; do
      ln -sfn "$LAB4_DIR/$pkg" "$LAB4_WS/src/$pkg"
    done
    for pkg in mav_trajectory_generation mav_msgs catkin_simple tesse_ros_bridge; do
      ln -sfn "$LAB4_DIR/dependencies/$pkg" "$LAB4_WS/src/$pkg"
    done
    ln -sfn "$LAB3_DIR/controller_pkg" "$LAB4_WS/src/controller_pkg"
    cd "$LAB4_WS"
    catkin build -j2 --no-status --cmake-args -DCMAKE_BUILD_TYPE=Release
    .venv/
    build/
    devel/
    logs/
    report/*.aux
    report/*.log
    report/*.out
    report/*.toc
    *.bag
    trajectory t=0.00 s, position=[-3.871332, -3.697889, 0.7612246], error=9.601 m
    trajectory t=5.08 s, position=[2.905204, -5.032321, 1.276382], error=1.165 m
    trajectory t=10.12 s, position=[-4.724346, 1.098959, 1.232789], error=0.977 m
    trajectory t=15.04 s, position=[4.478967, 1.565768, 1.323175], error=0.723 m
    trajectory t=20.00 s, position=[-3.618035, -4.323619, 1.492089], error=1.040 m
    trajectory t=25.02 s, position=[-0.8487715, 4.680742, 1.316833], error=0.941 m
    ✓ • 0ms

## Activity

    $ mkdir -p dependencies; cp -a ../Lab4/dependencies/catkin_simple ../Lab4/dependencies/mav_msgs ../Lab4/dependencies/tesse_interface ../Lab4/dependencies/tesse_ros_bridge dependencies/; rg --files dependencies | head -35; cat controller_pkg/package.xml; docker exec ros_noetic_lab3 ls -l /tmp/lab3_ws/src
    dependencies/mav_msgs/include/mav_msgs/eigen_mav_msgs.h
    dependencies/mav_msgs/include/mav_msgs/default_values.h
    dependencies/mav_msgs/include/mav_msgs/common.h
    dependencies/mav_msgs/include/mav_msgs/default_topics.h
    dependencies/mav_msgs/include/mav_msgs/conversions.h
    dependencies/mav_msgs/msg/RateThrust.msg
    dependencies/mav_msgs/msg/TorqueThrust.msg
    dependencies/mav_msgs/msg/GpsWaypoint.msg
    dependencies/mav_msgs/msg/AttitudeThrust.msg
    dependencies/mav_msgs/msg/RollPitchYawrateThrust.msg
    dependencies/mav_msgs/msg/Actuators.msg
    dependencies/mav_msgs/msg/FilteredSensorData.msg
    dependencies/mav_msgs/msg/Status.msg
    dependencies/mav_msgs/cmake/export_flags.cmake
    dependencies/mav_msgs/CHANGELOG.rst
    dependencies/mav_msgs/CMakeLists.txt
    dependencies/mav_msgs/package.xml
    dependencies/catkin_simple/README.md
    dependencies/catkin_simple/cmake/catkin_simple-extras.cmake.em
    dependencies/catkin_simple/CMakeLists.txt
    dependencies/catkin_simple/package.xml
    dependencies/tesse_ros_bridge/srv/RepositionRequestService.srv
    dependencies/tesse_ros_bridge/srv/ObjectSpawnRequestService.srv
    dependencies/tesse_ros_bridge/srv/SceneRequestService.srv
    dependencies/tesse_ros_bridge/launch/tesse_quadrotor_bridge.launch
    dependencies/tesse_ros_bridge/launch/play_traj.launch
    dependencies/tesse_ros_bridge/launch/record_traj.launch
    dependencies/tesse_ros_bridge/launch/tesse_bridge.launch
    dependencies/tesse_ros_bridge/launch/maps.launch
    dependencies/tesse_ros_bridge/msg/CollisionStats.msg
    dependencies/tesse_ros_bridge/CMakeLists.txt
    dependencies/tesse_ros_bridge/params/map_tfs.yaml
    dependencies/tesse_ros_bridge/params/noise_model.yaml
    dependencies/tesse_ros_bridge/params/tesse_agent_params.yaml
    dependencies/tesse_ros_bridge/params/camera_params.yaml
    <?xml version="1.0"?>
    <package format="2">
      <name>controller_pkg</name>
      <version>1.0.0</version>
      <description>VNAV Lab 3 geometric SE(3) quadrotor controller for TESSE.</description>
      <maintainer email="teamfullcans@example.com">Team Fullcans</maintainer>
      <license>MIT</license>
      <buildtool_depend>catkin</buildtool_depend>
      <depend>roscpp</depend>
      <depend>geometry_msgs</depend>
      <depend>nav_msgs</depend>
      <depend>trajectory_msgs</depend>
      <depend>mav_msgs</depend>
      <depend>tf2</depend>
      <depend>tf2_ros</depend>
      <depend>tf2_geometry_msgs</depend>
      <depend>tf2_eigen</depend>
      <depend>eigen</depend>
      <exec_depend>rviz</exec_depend>
      <exec_depend>rospy</exec_depend>
      <exec_depend>tf</exec_depend>
      <exec_depend>rosgraph_msgs</exec_depend>
      <exec_depend>visualization_msgs</exec_depend>
      <exec_depend>python3-numpy</exec_depend>
    </package>
    total 0
    lrwxrwxrwx 1 root root 28 Oct 10 02:33 catkin_simple -> /opt/lab3-deps/catkin_simple
    lrwxrwxrwx 1 root root 30 Oct 10 02:31 controller_pkg -> /workspace/lab3/controller_pkg
    lrwxrwxrwx 1 root root 32 Oct 10 02:31 mav_msgs -> /opt/lab3-deps/mav_comm/mav_msgs
    lrwxrwxrwx 1 root root 35 Oct 10 02:33 tesse_ros_bridge -> /opt/lab3-deps/tesse-ros-bridge/ROS
    ✓ • 73ms

## Activity

    file changes: Completed · 6 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/Dockerfile
    FROM ros:noetic-ros-base-focal
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential cmake python3-catkin-tools python3-numpy python3-matplotlib \
        python3-scipy python3-defusedxml python3-pil python3-pip libeigen3-dev \
        ros-noetic-tf ros-noetic-tf2-eigen ros-noetic-tf2-geometry-msgs \
        ros-noetic-rosgraph-msgs ros-noetic-visualization-msgs ros-noetic-cmake-modules \
        ros-noetic-cv-bridge ros-noetic-ackermann-msgs ros-noetic-rviz \
        xvfb xdotool curl unzip ffmpeg libgl1-mesa-dri libxcursor1 libxrandr2 \
        libxi6 libxinerama1 libasound2 libpulse0 libudev1 libgtk2.0-0 \
        libsdl2-2.0-0 libnss3 texlive-latex-base texlive-latex-recommended \
        && rm -rf /var/lib/apt/lists/*
    WORKDIR /workspace/lab3
    CMD ["bash"]
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/config/gains_unity.yaml
    @@ -2,6 +2,6 @@
     # Keep the handout's model constants; tune the feedback on the actual plant.
    -kx: 4.0
    -kv: 3.0
    -kr: 2.4
    -komega: 0.6
    +kx: 2.0
    +kv: 2.4
    +kr: 1.8
    +komega: 0.7
     hz: 200.0
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/launch/traj_tracking.launch
    @@ -3,3 +3,3 @@
       <arg name="rviz" default="false"/>
    -  <arg name="gains_file" default="$(find controller_pkg)/config/gains.yaml"/>
    +  <arg name="gains_file" default="$(find controller_pkg)/config/gains_unity.yaml"/>
       <node name="traj_publisher" pkg="controller_pkg" type="traj_publisher" output="screen">
    @@ -11,3 +11,3 @@
       <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz"
    -        args="-d $(find controller_pkg)/rviz/lab3.rviz"/>
    +        args="-d $(find controller_pkg)/rviz/circle.rviz"/>
     </launch>
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/dependencies/README.md
    # Runtime dependencies
    
    Copied from the working local Lab4 dependency snapshots; these are the course
    TESSE ROS bridge/interface, catkin_simple, and ETH mav_msgs. Original copyright
    headers and available licenses are retained. The source snapshots are included
    so this lab builds without the Lab4 directory or a changing upstream branch.
    
    The bridge has the Python 3 compatibility fixes used by Lab4: executable Python
    3 entrypoints and `import cv2` before `cv_bridge` (required on this ARM64 system).
    The interface is installed with `pip --no-deps`; Python 3 provides `enum`, while
    the Docker image supplies NumPy, Pillow and defusedxml. Do not install enum34.
    
    Upstream projects: https://github.com/MIT-TESSE/tesse-ros-bridge,
    https://github.com/MIT-TESSE/tesse-interface,
    https://github.com/catkin/catkin_simple,
    https://github.com/ethz-asl/mav_comm.
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/build_workspace.sh
    #!/usr/bin/env bash
    set -eo pipefail
    source /opt/ros/noetic/setup.bash
    LAB3_DIR=${LAB3_DIR:-/workspace/lab3}
    LAB3_WS=${LAB3_WS:-/tmp/lab3_unity_ws}
    mkdir -p "$LAB3_WS/src"
    ln -sfn "$LAB3_DIR/controller_pkg" "$LAB3_WS/src/controller_pkg"
    for pkg in catkin_simple mav_msgs tesse_ros_bridge; do
      ln -sfn "$LAB3_DIR/dependencies/$pkg" "$LAB3_WS/src/$pkg"
    done
    python3 -m pip install --no-deps "$LAB3_DIR/dependencies/tesse_interface"
    cd "$LAB3_WS"
    catkin build -j2 --no-status --cmake-args -DCMAKE_BUILD_TYPE=Release
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/prepare_unity_arm64.sh
    #!/usr/bin/env bash
    # Inside the ARM64 Noetic container. The official Unity files stay unmodified.
    set -eo pipefail
    LAB3_RUNTIME=${LAB3_RUNTIME:-/tmp/lab3-runtime}
    mkdir -p "$LAB3_RUNTIME"
    if [ ! -x "$LAB3_RUNTIME/box64-0.3.6/build/box64" ]; then
      curl -fL --retry 3 https://codeload.github.com/ptitSeb/box64/tar.gz/refs/tags/v0.3.6 -o "$LAB3_RUNTIME/box64.tar.gz"
      tar -xzf "$LAB3_RUNTIME/box64.tar.gz" -C "$LAB3_RUNTIME"
      cmake -S "$LAB3_RUNTIME/box64-0.3.6" -B "$LAB3_RUNTIME/box64-0.3.6/build" -DARM_DYNAREC=ON -DCMAKE_BUILD_TYPE=Release
      cmake --build "$LAB3_RUNTIME/box64-0.3.6/build" -j1
    fi
    if [ ! -f "$LAB3_RUNTIME/lab3/lab3.x86_64" ]; then
      curl -fL --retry 3 https://vnav.mit.edu/material/lab3.zip -o "$LAB3_RUNTIME/lab3.zip"
      unzip -q "$LAB3_RUNTIME/lab3.zip" -d "$LAB3_RUNTIME"
    fi
    chmod +x "$LAB3_RUNTIME/lab3/lab3.x86_64"
    printf 'Runtime ready: %s\n' "$LAB3_RUNTIME"

## Activity

    file changes: Completed · 3 changes
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/analyze_unity.py
    #!/usr/bin/env python3
    """Analyze official TESSE telemetry; independent-model data is never read."""
    import json
    from pathlib import Path
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    
    root = Path(__file__).resolve().parents[1]
    data = np.genfromtxt(root/"report/unity_flight.csv", delimiter=",", names=True)
    t = data["trajectory_time"]
    p = np.column_stack([data[n] for n in ("x","y","z")])
    pd = np.column_stack([data[n] for n in ("xd","yd","zd")])
    error = np.linalg.norm(p-pd, axis=1)
    steady = t >= 8*np.pi  # exclude the first two nominal laps
    phase = np.unwrap(np.arctan2(p[steady,0], p[steady,1]))
    laps = float((phase[-1]-phase[0])/(2*np.pi))
    summary = {
        "source": "Unmodified official MIT Lab3 Unity/TESSE; Box64 0.3.6 on ARM64",
        "trajectory": "x=5*sin(t/2), y=5*cos(t/2), z=2, yaw=-t/2",
        "gains": {"kx":2.0,"kv":2.4,"kr":1.8,"komega":0.7,"hz":200},
        "samples":len(t), "trajectory_duration_s":float(t[-1]),
        "steady_start_s":float(8*np.pi), "observed_steady_laps":laps,
        "steady_position_rms_m":float(np.sqrt(np.mean(error[steady]**2))),
        "steady_position_max_m":float(error[steady].max()),
        "steady_altitude_min_m":float(p[steady,2].min()),
        "steady_altitude_max_m":float(p[steady,2].max()),
        "steady_radial_rms_m":float(np.sqrt(np.mean((np.linalg.norm(p[steady,:2],axis=1)-5)**2))),
        "all_values_finite":bool(np.isfinite(p).all() and np.isfinite(error).all()),
    }
    summary["flight_completed"] = bool(laps >= 1 and t[-1] >= 55 and summary["all_values_finite"])
    (root/"report/unity_metrics.json").write_text(json.dumps(summary,indent=2)+"\n")
    fig, ax = plt.subplots(2,2,figsize=(11,8))
    ax[0,0].plot(pd[:,0],pd[:,1],"--",label="Desired")
    ax[0,0].plot(p[:,0],p[:,1],label="Official TESSE")
    ax[0,0].set(xlabel="x [m]",ylabel="y [m]",aspect="equal",title="Circular trajectory")
    ax[0,0].legend()
    ax[0,1].plot(t,p[:,2],label="Actual z")
    ax[0,1].plot(t,pd[:,2],"--",label="Desired z")
    ax[0,1].set(xlabel="Trajectory time [s]",ylabel="Height [m]")
    ax[0,1].legend()
    ax[1,0].plot(t,error)
    ax[1,0].set(xlabel="Trajectory time [s]",ylabel="Position error [m]")
    ax[1,0].axvline(8*np.pi,color="gray",ls="--",label="Steady window starts")
    ax[1,0].legend()
    ax[1,1].plot(t[steady],(phase-phase[0])/(2*np.pi))
    ax[1,1].set(xlabel="Trajectory time [s]",ylabel="Observed turns",title="Actual position phase")
    for a in ax.flat:
        a.grid(alpha=.25)
    fig.suptitle("MIT VNAV Lab3 — official Unity/TESSE flight")
    fig.tight_layout()
    fig.savefig(root/"report/unity_tracking.pdf")
    fig.savefig(root/"report/unity_tracking.png",dpi=150)
    print(json.dumps(summary,indent=2))
    if not summary["flight_completed"]:
        raise SystemExit("Official flight did not include a complete steady circle")
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/run_unity_flight.sh
    #!/usr/bin/env bash
    # Uses the live official simulator started by start_unity_arm64.sh.
    set -eo pipefail
    LAB3_DIR=${LAB3_DIR:-/workspace/lab3}
    LAB3_WS=${LAB3_WS:-/tmp/lab3_unity_ws}
    source "$LAB3_WS/devel/setup.bash"
    export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost
    export DISABLE_ROS1_EOL_WARNINGS=1 LIBGL_ALWAYS_SOFTWARE=1
    mkdir -p "$LAB3_DIR/report/video"
    pids=()
    cleanup() {
      for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
      for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
    }
    trap cleanup EXIT
    # Only these two Lab3 nodes are restarted. The runtime and other masters stay up.
    rosnode kill /controller_node /traj_publisher 2>/dev/null || true
    python3 "$LAB3_DIR/scripts/monitor_unity.py" \
      --output "$LAB3_DIR/report/unity_flight.csv" --duration 55 --wall-timeout 600 \
      > /tmp/lab3-final-monitor.log 2>&1 & monitor_pid=$!; pids+=("$monitor_pid")
    rosbag record -O "$LAB3_DIR/report/unity_flight.bag" \
      /clock /current_state /desired_state /rotor_speed_cmds /flight/actual \
      /flight/desired /flight/source /tesse/collisions \
      >/tmp/lab3-final-bag.log 2>&1 & pids+=("$!")
    if [ "${LAB3_REUSE_RVIZ:-0}" != 1 ]; then
      Xvfb :96 -screen 0 1280x800x24 >/tmp/lab3-official-rviz-xvfb.log 2>&1 & pids+=("$!")
      sleep 1
      DISPLAY=:96 rosrun rviz rviz -d "$LAB3_DIR/controller_pkg/rviz/circle.rviz" \
        __name:=lab3_official_rviz >/tmp/lab3-official-rviz.log 2>&1 & pids+=("$!")
      sleep 5
    fi
    ffmpeg -y -f x11grab -video_size 1280x800 -framerate 8 -i :96 \
      -c:v libx264 -threads 1 -preset ultrafast -crf 23 -pix_fmt yuv420p \
      -movflags +faststart "$LAB3_DIR/report/video/rviz_official_tesse.mp4" \
      >/tmp/lab3-final-ffmpeg.log 2>&1 & pids+=("$!")
    roslaunch controller_pkg traj_tracking.launch \
      >/tmp/lab3-final-controller.log 2>&1 & pids+=("$!")
    wait "$monitor_pid"
    # The EXIT trap closes MP4 and rosbag cleanly.
    Add: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/start_unity_arm64.sh
    #!/usr/bin/env bash
    # Foreground runtime session. Run run_unity_flight.sh in another terminal.
    set -eo pipefail
    LAB3_WS=${LAB3_WS:-/tmp/lab3_unity_ws}
    LAB3_RUNTIME=${LAB3_RUNTIME:-/tmp/lab3-runtime}
    source "$LAB3_WS/devel/setup.bash"
    export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost
    export DISPLAY=:97 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0
    pids=()
    cleanup() {
      for pid in "${pids[@]}"; do kill -INT "$pid" 2>/dev/null || true; done
      for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
    }
    trap cleanup EXIT
    Xvfb :97 -screen 0 960x600x24 >/tmp/lab3-unity-xvfb.log 2>&1 & pids+=("$!")
    roscore -p 11317 >/tmp/lab3-unity-master.log 2>&1 & pids+=("$!")
    sleep 2
    cd "$LAB3_RUNTIME/lab3"
    "$LAB3_RUNTIME/box64-0.3.6/build/box64" ./lab3.x86_64 \
      -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore \
      -logFile /tmp/lab3-unity-box64.log >/tmp/lab3-box64.log 2>&1 & pids+=("$!")
    sleep 15
    # Close Unity's startup audio-error console on the headless X server.
    LAB3_WINDOW_ID=$(xdotool search --onlyvisible --name tesse_vnav_scenes | head -n1)
    xdotool windowfocus "$LAB3_WINDOW_ID" mousemove 512 571 click 1
    roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false \
      publish_collisions:=true >/tmp/lab3-unity-bridge.log 2>&1 & pids+=("$!")
    wait "${pids[-1]}"

## Activity

    $ docker exec ros_noetic_lab3 tail -18 /tmp/lab3-circle-tuned-monitor.log; docker exec ros_noetic_lab3 bash -lc 'LAB3_WS=/tmp/lab3_ws LAB3_REUSE_RVIZ=1 nohup bash /workspace/lab3/scripts/run_unity_flight.sh >/tmp/lab3-final-session.log 2>&1 </dev/null &'
    trajectory t=0.00 s, position=[-3.871332, -3.697889, 0.7612246], error=9.601 m
    trajectory t=5.08 s, position=[2.905204, -5.032321, 1.276382], error=1.165 m
    trajectory t=10.12 s, position=[-4.724346, 1.098959, 1.232789], error=0.977 m
    trajectory t=15.04 s, position=[4.478967, 1.565768, 1.323175], error=0.723 m
    trajectory t=20.00 s, position=[-3.618035, -4.323619, 1.492089], error=1.040 m
    trajectory t=25.02 s, position=[-0.8487715, 4.680742, 1.316833], error=0.941 m
    trajectory t=30.00 s, position=[3.157432, -3.870821, 1.364176], error=0.647 m
    trajectory t=35.04 s, position=[-5.325789, 1.805494, 1.430291], error=0.959 m
    trajectory t=40.18 s, position=[3.998294, 2.110539, 1.450472], error=1.037 m
    {
      "source": "Official MIT Lab3 Unity/TESSE via Box64 0.3.6",
      "complete_duration": true,
      "samples": 2008,
      "trajectory_duration_s": 40.180000001,
      "steady_position_rms_m": 0.8970293306680099,
      "steady_position_max_m": 1.3129845825655257,
      "final_position_error_m": 1.0371284524351434
    }
    ✓ • 353ms

## Activity

    $ docker exec ros_noetic_lab3 tail -12 /tmp/lab3-final-monitor.log; cat controller_pkg/launch/rigid_body_demo.launch; cat deliverable_1.txt; sed -n '1,220p' report/deliverable_2.tex; rg --files dependencies --hidden | rg '(__pycache__|\.pyc|\.git/|egg-info)'
    trajectory t=0.08 s, position=[1.880263, 4.118707, 0.8651562], error=2.209 m
    trajectory t=5.04 s, position=[2.144054, 4.066453, 0.8595815], error=8.247 m
    trajectory t=10.02 s, position=[1.650895, 4.140183, 0.7371824], error=7.078 m
    trajectory t=15.08 s, position=[4.356316, 1.501668, 1.397928], error=0.724 m
    <launch>
      <!-- Development substitute for ARM hosts. This launch does not run TESSE. -->
      <arg name="rviz" default="true"/>
      <arg name="duration" default="42.0"/>
      <arg name="output" default="/tmp/lab3_ros_flight.csv"/>
      <param name="/use_sim_time" value="true"/>
      <node name="rigid_body_demo" pkg="controller_pkg" type="rigid_body_demo.py" output="screen">
        <param name="duration" value="$(arg duration)"/>
        <param name="output" value="$(arg output)"/>
      </node>
      <include file="$(find controller_pkg)/launch/traj_tracking.launch"/>
      <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz"
            args="-d $(find controller_pkg)/rviz/circle.rviz"/>
    </launch>
    VNAV Lab 3 — Deliverable 1: Transformations in Practice (ROS Noetic / C++)
    
    Required headers:
      #include <tf2/LinearMath/Quaternion.h>
      #include <tf2/utils.h>
      #include <tf2_geometry_msgs/tf2_geometry_msgs.h>
      #include <tf2_eigen/tf2_eigen.h>
      #include <Eigen/Geometry>
    
    A. Message vs. tf
    
    A1. Convert quat_msg into the already-declared quat_tf:
      tf2::fromMsg(quat_msg, quat_tf);
    
    A2. Create a geometry_msgs::Quaternion from quat_tf:
      geometry_msgs::Quaternion quat_msg = tf2::toMsg(quat_tf);
    
    A3. Get the scalar (w) component:
      quat_tf.w();
      getW() is also available; the scalar component is not the quaternion norm.
    
    B. Conversion
    
    B1. Extract yaw in radians with one function call:
      double yaw = tf2::getYaw(quat_t);
    
    B2. Convert a geometry_msgs::Quaternion to an Eigen 3x3 rotation matrix:
      Eigen::Quaterniond q_eigen;
      tf2::fromMsg(quat_msg, q_eigen);
      Eigen::Matrix3d R = q_eigen.toRotationMatrix();
    
    This uses two conversion calls, assuming the message contains a unit quaternion.
    For a valid but nonunit input, call q_eigen.normalize() before toRotationMatrix().
    Reject a zero quaternion. Eigen's constructor takes (w,x,y,z), while the ROS
    message exposes fields x,y,z,w; fromMsg handles this ordering correctly.
    
    Sources:
    https://github.com/ros/geometry2/blob/noetic-devel/tf2_geometry_msgs/include/tf2_geometry_msgs/tf2_geometry_msgs.h
    https://github.com/ros/geometry2/blob/noetic-devel/tf2_eigen/include/tf2_eigen/tf2_eigen.h
    https://github.com/ros/geometry2/blob/noetic-devel/tf2/include/tf2/utils.h
    https://eigen.tuxfamily.org/dox/classEigen_1_1QuaternionBase.html
    \documentclass[11pt,a4paper]{article}
    \usepackage[margin=24mm]{geometry}
    \usepackage{amsmath,amssymb,graphicx,booktabs}
    \usepackage{url}
    \title{VNAV Lab 3: Modelling and Control of UAVs\\Deliverable 2}
    \author{Team Fullcans}
    \date{}
    \begin{document}
    \maketitle
    
    \section*{A. Structure of quadrotors}
    We use a right-handed frame with $x$ pointing right and $y$ pointing up in
    the top-view exercise figure, and $z$ pointing out of the page. This fixes
    all moment signs explicitly. The exercise figure and simulator figure use
    different rotor numbering; the matrices in this section follow the exercise
    figure, not the simulator figure.
    Let $d>0$ be the centre-to-rotor distance and $a=d/\sqrt{2}$. The rotor
    positions in the exercise figure are
    \[
     \rho_1=(-a,a,0)^T,\quad \rho_2=(-a,-a,0)^T,\quad
     \rho_3=(a,-a,0)^T,\quad \rho_4=(a,a,0)^T.
    \]
    Define $u_i=\omega_i^2\geq0$, where $\omega_i$ is the speed magnitude in
    each propeller's configured lifting direction, $c_f>0$ the lift coefficient,
    and $c_d>0$ the reaction-torque coefficient. Then
    \[
     f_i=c_fu_i,\qquad
     \rho_i\times (0,0,f_i)^T=(\rho_{iy}f_i,-\rho_{ix}f_i,0)^T.
    \]
    Counter-clockwise rotor motion produces clockwise body reaction torque,
    so rotors 1 and 3 in (a) have negative yaw torque and rotors 2 and 4 have
    positive yaw torque. With $w=(f,M_x,M_y,M_z)^T$, we obtain
    \begin{equation}
     w=F_a u,\qquad
     F_a=\begin{bmatrix}
     c_f&c_f&c_f&c_f\\
     ac_f&-ac_f&-ac_f&ac_f\\
     ac_f&ac_f&-ac_f&-ac_f\\
     -c_d&c_d&-c_d&c_d
     \end{bmatrix}.
    \end{equation}
    The four scaled rows are mutually orthogonal and
    \[
     \det F_a=16a^2c_f^3c_d=8d^2c_f^3c_d\ne0,
     \qquad \operatorname{rank}(F_a)=4.
    \]
    Thus all four wrench components can be locally adjusted independently
    around a positive-speed hover, subject to actuator limits.
    
    In configuration (b), swapping the propeller types and reversing the
    directions of rotors 3 and 4 preserves upward lift but reverses their
    yaw reaction torques. Therefore
    \begin{equation}
     F_b=\begin{bmatrix}
     c_f&c_f&c_f&c_f\\
     ac_f&-ac_f&-ac_f&ac_f\\
     ac_f&ac_f&-ac_f&-ac_f\\
     -c_d&c_d&c_d&-c_d
     \end{bmatrix}.
    \end{equation}
    Its fourth row is $-c_d/(ac_f)$ times its second row. The first three
    rows remain independent, hence
    \[
     \boxed{\operatorname{rank}(F_b)=3,\qquad
     M_z=-\frac{c_d}{ac_f}M_x.}
    \]
    For example, $F_b(1,-1,1,-1)^T=0$. A pure yaw moment at zero roll moment
    is impossible. At an instant of level hover with zero angular velocity,
    keeping the position fixed requires zero roll acceleration and therefore
    $M_x=0$, which also forces $M_z=0$. A prescribed yaw acceleration at that
    instant cannot be realized. Consequently (b) cannot track an arbitrary
    independently prescribed output trajectory $(x,y,z,\Psi)$; only trajectories
    compatible with the moment constraint may be feasible. Changing coordinate
    axes or wrench units cannot restore the missing rank.
    
    \section*{B. Control with quadratic body drag}
    Let $R\in SO(3)$ rotate body vectors into the world frame, $v$ be the
    world velocity, and $v^b=R^Tv$. Write
    \[
     D=\operatorname{diag}(0.1,0.1,0.2),\qquad
     h(v^b)=v^b\odot|v^b|,\qquad
     F_D^b=-D h(v^b),\qquad F_D^w=RF_D^b.
    \]
    Here $\odot$ means componentwise multiplication. This sign convention
    opposes motion in every axis and satisfies
    \[
     (v^b)^TF_D^b=-0.1|v_x^b|^3-0.1|v_y^b|^3-0.2|v_z^b|^3\leq0.
    \]
    With the lab's upward $z$ convention, the translational dynamics become
    \[
     m\dot v=-mg e_3+fRe_3+F_D^w,\qquad e_3=(0,0,1)^T.
    \]
    Define $e_x=x-x_d$, $e_v=v-v_d$ and command the rotor force vector
    \begin{equation}
     \boxed{A=-k_xe_x-k_ve_v+mg e_3+m\ddot x_d-\widehat F_D^w.}
    \end{equation}
    Using measured velocity and attitude, compute $R^Tv$, evaluate the
    quadratic drag law in the body frame, then rotate the result by $R$.
    Subtract this predicted world force when constructing $A$. For example,
    with $R=I$ and $v=(2,0,0)^T$, drag is $(-0.4,0,0)^T$ N, so the
    controller adds $+0.4$ N of forward force.
    
    The compensated force changes both the desired thrust magnitude and
    attitude. For $\|A\|>0$, choose
    \[
     b_{3d}=\frac{A}{\|A\|},\quad b_{1c}=(\cos\Psi_d,\sin\Psi_d,0)^T,
     \quad b_{2d}=\frac{b_{3d}\times b_{1c}}{\|b_{3d}\times b_{1c}\|},
    \]
    \[
     R_d=[\,b_{2d}\times b_{3d}\quad b_{2d}\quad b_{3d}\,],\qquad
     \boxed{f=A^TRe_3.}
    \]
    With perfect attitude tracking, $fRe_3=A$. If the drag estimate is exact,
    substitution into the dynamics gives
    \[
     m\dot e_v=-k_xe_x-k_ve_v,
    \]
    so the modelled disturbance is cancelled rather than left for feedback
    to counter through a persistent tracking error. With imperfect estimates,
    the residual disturbance is $F_D^w-\widehat F_D^w$.
    
    The geometric attitude controller retains its form:
    \[
     e_R=\tfrac12(R_d^TR-R^TR_d)^\vee,\quad
     e_\Omega=\Omega-R^TR_d\Omega_d,
    \]
    \[
     M=-k_Re_R-k_\Omega e_\Omega+\Omega\times J\Omega
     -J(\widehat\Omega R^TR_d\Omega_d-R^TR_d\dot\Omega_d).
    \]
    If the full feedforward terms are used, $\Omega_d$ and $\dot\Omega_d$ must
    come from the compensated $R_d$. The drag model supplied in the exercise
    is a force at the centre of mass; it does not specify an extra body moment.
    
    In the paper's downward $z$ convention, instead use
    $A_p=-k_xe_x-k_ve_v-mg e_3+m\ddot x_d-\widehat F_D^w$,
    $b_{3d}=-A_p/\|A_p\|$ and $f=-A_p^TRe_3$.
    The implementation provides optional drag compensation, disabled by default
    because the hypothetical exercise drag need not match the TESSE plant.
    
    \section*{References}
    \begin{enumerate}
    \item MIT VNAV, \emph{Lab 3 Exercises (2023)},
    \url{https://vnav.mit.edu/labs_2023/lab3/exercises.html}.
    \item T. Lee, M. Leok, and N. H. McClamroch, \emph{Geometric Tracking
    Control of a Quadrotor UAV on SE(3)}, CDC 2010, pp. 5420--5425,
    \url{https://mleok.science/pdf/LeLeMc2010_quadrotor.pdf}.
    \end{enumerate}
    \end{document}
    ✗ (1) • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317; rosparam get /controller_node; tail -12 /tmp/lab3-final-monitor.log; tail -20 /tmp/lab3-final-controller.log; tail -5 /tmp/lab3-final-ffmpeg.log'
    compensate_drag: false
    desired_timeout: 1.0
    hz: 200.0
    komega: 0.7
    kr: 1.8
    kv: 2.4
    kx: 2.0
    state_timeout: 1.0
    
    trajectory t=0.08 s, position=[1.880263, 4.118707, 0.8651562], error=2.209 m
    trajectory t=5.04 s, position=[2.144054, 4.066453, 0.8595815], error=8.247 m
    trajectory t=10.02 s, position=[1.650895, 4.140183, 0.7371824], error=7.078 m
    trajectory t=15.08 s, position=[4.356316, 1.501668, 1.397928], error=0.724 m
    trajectory t=20.08 s, position=[-2.941879, -4.0562, 1.673159], error=0.333 m
    trajectory t=25.08 s, position=[0.009259093, 5.07272, 1.750036], error=0.297 m
        Metadata:
          encoder         : Lavc58.54.100 libx264
        Side data:
          cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: -1
    frame=    7 fps=0.0 q=11.0 size=       0kB time=00:00:00.62 bitrate=   0.6kbits/s speed=1.14x
    ✓ • 322ms

## Activity

    $ tail -22 report/build_unity_noetic.txt; docker exec ros_noetic_lab3 tail -8 /tmp/lab3-final-monitor.log; rg --files --hidden dependencies | rg '(LICENSE|COPYING|\.gitignore)'
    Processing /workspace/lab3/dependencies/tesse_interface
    Building wheels for collected packages: tesse
      Building wheel for tesse (setup.py): started
      Building wheel for tesse (setup.py): finished with status 'done'
      Created wheel for tesse: filename=tesse-0.1.2-py3-none-any.whl size=16022 sha256=76f31a9b9bd30831ac0f7be3bae8ad54b0570b959ecf213f8592a97af08e03f4
      Stored in directory: /tmp/pip-ephem-wheel-cache-odyu0xeu/wheels/4e/7d/76/740f2c90a936588adbc6bc6acbf386cb7fef1101efe361536a
    Successfully built tesse
    Installing collected packages: tesse
      Attempting uninstall: tesse
        Found existing installation: tesse 0.1.2
        Uninstalling tesse-0.1.2:
          Successfully uninstalled tesse-0.1.2
    Successfully installed tesse-0.1.2
    trajectory t=5.04 s, position=[2.144054, 4.066453, 0.8595815], error=8.247 m
    trajectory t=10.02 s, position=[1.650895, 4.140183, 0.7371824], error=7.078 m
    trajectory t=15.08 s, position=[4.356316, 1.501668, 1.397928], error=0.724 m
    trajectory t=20.08 s, position=[-2.941879, -4.0562, 1.673159], error=0.333 m
    trajectory t=25.08 s, position=[0.009259093, 5.07272, 1.750036], error=0.297 m
    trajectory t=30.08 s, position=[3.156888, -4.020423, 1.799021], error=0.230 m
    trajectory t=35.06 s, position=[-4.918502, 1.259744, 1.66949], error=0.339 m
    trajectory t=40.08 s, position=[4.723901, 1.820639, 1.789008], error=0.229 m
    dependencies/tesse_interface/LICENSE
    dependencies/tesse_ros_bridge/src/key_teleop/LICENSE
    dependencies/catkin_simple/.gitignore
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 bash /workspace/lab3/scripts/build_workspace.sh >report/build_unity_noetic.txt 2>&1
    ✓ • 33.20s

## Activity

    file changes: Completed · 2 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/.gitignore
    @@ -9 +9,5 @@
     *.bag
    +*.bag.active
    +__pycache__/
    +*.pyc
    +*.egg-info/
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/launch/rigid_body_demo.launch
    @@ -10,3 +10,5 @@
       </node>
    -  <include file="$(find controller_pkg)/launch/traj_tracking.launch"/>
    +  <include file="$(find controller_pkg)/launch/traj_tracking.launch">
    +    <arg name="gains_file" value="$(find controller_pkg)/config/gains.yaml"/>
    +  </include>
       <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz"

## Assistant

正式录制已进入稳定飞行段，目前位置误差约 0.2～0.35 米。录像同步保存了官方模拟器的状态、目标轨迹和旋翼命令，之后可以回放核对；实验依赖也已整理进 Lab 3，便于独立复现。

## User

继续

## Assistant

我继续检查录像是否完整、整理飞行指标，并更新本地交付说明。刚才工具的自动审批服务因额度限制中断了操作；已启动的录制进程可能仍在运行，我先确认结果。

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'tail -18 /tmp/lab3-final-monitor.log; tail -8 /tmp/lab3-final-session.log; ps -eo pid,args | grep -E "catkin|make|cc1plus|run_unity_flight|ffmpeg" | head -15'; du -sh report/video/* report/unity*; tail -28 report/build_unity_noetic.txt
    trajectory t=15.08 s, position=[4.356316, 1.501668, 1.397928], error=0.724 m
    trajectory t=20.08 s, position=[-2.941879, -4.0562, 1.673159], error=0.333 m
    trajectory t=25.08 s, position=[0.009259093, 5.07272, 1.750036], error=0.297 m
    trajectory t=30.08 s, position=[3.156888, -4.020423, 1.799021], error=0.230 m
    trajectory t=35.06 s, position=[-4.918502, 1.259744, 1.66949], error=0.339 m
    trajectory t=40.08 s, position=[4.723901, 1.820639, 1.789008], error=0.229 m
    trajectory t=45.04 s, position=[-2.684226, -4.308162, 1.769798], error=0.281 m
    trajectory t=50.08 s, position=[-0.3761803, 5.071409, 1.744871], error=0.285 m
    trajectory t=55.02 s, position=[3.474039, -3.734323, 1.722597], error=0.305 m
    {
      "source": "Official MIT Lab3 Unity/TESSE via Box64 0.3.6",
      "complete_duration": true,
      "samples": 2752,
      "trajectory_duration_s": 55.019999999,
      "steady_position_rms_m": 0.30630605599350413,
      "steady_position_max_m": 0.5845453007436116,
      "final_position_error_m": 0.30461954372209715
    }
    killing:
     * /controller_node
     * /traj_publisher
    killed
     209097 bash -lc tail -18 /tmp/lab3-final-monitor.log; tail -8 /tmp/lab3-final-session.log; ps -eo pid,args | grep -E "catkin|make|cc1plus|run_unity_flight|ffmpeg" | head -15
     209109 grep -E catkin|make|cc1plus|run_unity_flight|ffmpeg
    304K    report/video/rviz_demo_frame.png
    112K    report/video/rviz_live.png
    2.0M    report/video/rviz_official_tesse.mp4
    1.3M    report/video/rviz_rigid_body_demo.mp4
    112K    report/video/rviz_unity_trial.png
    156K    report/video/unity_startup.png
    21M    report/unity_flight.bag
    636K    report/unity_flight.csv
    4.0K    report/unity_flight.json
    Cache Job Environments:      False
    -------------------------------------------------------
    Buildlisted Packages:        None
    Skiplisted Packages:         None
    -------------------------------------------------------
    Workspace configuration appears valid.
    
    NOTE: Forcing CMake to run for each package.
    -------------------------------------------------------
    [build] Found 4 packages in 0.0 seconds.
    [build] Updating package table.
    Starting >>> catkin_tools_prebuild
    Finished <<< catkin_tools_prebuild                [ 2.5 seconds ]
    Starting >>> catkin_simple
    Starting >>> mav_msgs
    Finished <<< catkin_simple                        [ 2.8 seconds ]
    Finished <<< mav_msgs                             [ 7.3 seconds ]
    Starting >>> controller_pkg
    Starting >>> tesse_ros_bridge
    Finished <<< tesse_ros_bridge                     [ 9.8 seconds ]
    Finished <<< controller_pkg                       [ 20.2 seconds ]
    [build] Summary: All 5 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 30.1 seconds total.
    [build] Note: Workspace packages have changed, please re-source setup files to use them.
    ✓ • 114ms

## Activity

    $ docker exec ros_noetic_lab3 python3 /workspace/lab3/scripts/analyze_unity.py; docker exec ros_noetic_lab3 ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,r_frame_rate,codec_name -of json /workspace/lab3/report/video/rviz_official_tesse.mp4; docker exec ros_noetic_lab3 ffmpeg -y -loglevel error -ss 40 -i /workspace/lab3/report/video/rviz_official_tesse.mp4 -frames:v 1 /workspace/lab3/report/video/rviz_official_frame.png; docker exec ros_noetic_lab3 bash -lc 'source /tmp/lab3_unity_ws/devel/setup.bash; rosbag info /workspace/lab3/report/unity_flight.bag' > report/unity_bag_info.txt; sed -n '1,230p' controller_pkg/include/controller_pkg/geometric_controller.h
    {
      "source": "Unmodified official MIT Lab3 Unity/TESSE; Box64 0.3.6 on ARM64",
      "trajectory": "x=5*sin(t/2), y=5*cos(t/2), z=2, yaw=-t/2",
      "gains": {
        "kx": 2.0,
        "kv": 2.4,
        "kr": 1.8,
        "komega": 0.7,
        "hz": 200
      },
      "samples": 2752,
      "trajectory_duration_s": 55.019999999,
      "steady_start_s": 25.132741228718345,
      "observed_steady_laps": 2.3755648711366417,
      "steady_position_rms_m": 0.30630605599350413,
      "steady_position_max_m": 0.5845453007436116,
      "steady_altitude_min_m": 1.559839,
      "steady_altitude_max_m": 1.863796,
      "steady_radial_rms_m": 0.08292571660246979,
      "all_values_finite": true,
      "flight_completed": true
    }
    {
        "programs": [
    
        ],
        "streams": [
            {
                "codec_name": "h264",
                "width": 1280,
                "height": 800,
                "r_frame_rate": "8/1"
            }
        ],
        "format": {
            "duration": "57.125000",
            "size": "2044741"
        }
    }
    #pragma once
    
    #include <Eigen/Dense>
    #include <cmath>
    
    namespace controller_pkg {
    
    struct State {
      Eigen::Vector3d x = Eigen::Vector3d::Zero();
      Eigen::Vector3d v = Eigen::Vector3d::Zero();
      Eigen::Matrix3d R = Eigen::Matrix3d::Identity();  // body -> world
      Eigen::Vector3d omega = Eigen::Vector3d::Zero();  // body frame
    };
    
    struct Reference {
      Eigen::Vector3d x = Eigen::Vector3d::Zero();
      Eigen::Vector3d v = Eigen::Vector3d::Zero();
      Eigen::Vector3d a = Eigen::Vector3d::Zero();
      double yaw = 0.0;
    };
    
    struct Gains {
      double kx = 6.0;
      double kv = 4.7;
      double kr = 64.0;
      double komega = 16.0;
    };
    
    struct Command {
      Eigen::Matrix3d Rd;
      Eigen::Vector4d wrench;  // thrust, body Mx, My, Mz
      Eigen::Vector4d rotor_speeds;  // signed rad/s, rotor order 1,2,3,4
    };
    
    // Lab 3 simulator constants; do not substitute real drone coefficients.
    class GeometricController {
     public:
      Gains gains;
      bool compensate_drag = false;
      const double m = 1.0, g = 9.81, d = 0.3, cf = 1e-3, cd = 1e-5;
      const Eigen::Matrix3d J = Eigen::Matrix3d::Identity();
    
      GeometricController() {
        // rho1=(+a,+a,0), rho2=(-a,+a,0), rho3=(-a,-a,0), rho4=(+a,-a,0).
        // rho x (0,0,cf*s): Mx=y*cf*s, My=-x*cf*s.
        // TESSE yaw signs: +,-,+,-. s_i = omega_i*abs(omega_i).
        const double a = d / std::sqrt(2.0);
        allocation_ << cf, cf, cf, cf,
                       a*cf, a*cf, -a*cf, -a*cf,
                       -a*cf, a*cf, a*cf, -a*cf,
                       cd, -cd, cd, -cd;
        F2W_ = allocation_.inverse();
      }
    
      const Eigen::Matrix4d& allocation() const { return allocation_; }
    
      static Eigen::Vector3d vee(const Eigen::Matrix3d& S) {
        return Eigen::Vector3d(S(2,1), S(0,2), S(1,0));
      }
    
      static Eigen::Vector3d dragWorld(const State& state) {
        const Eigen::Vector3d vb = state.R.transpose() * state.v;
        const Eigen::Vector3d drag_b =
            -Eigen::Vector3d(0.1, 0.1, 0.2).cwiseProduct(vb.cwiseProduct(vb.cwiseAbs()));
        return state.R * drag_b;
      }
    
      Command compute(const State& state, const Reference& ref) const {
        Command cmd;
        // Part 5.1: equations (6),(7).
        const Eigen::Vector3d ex = state.x - ref.x;
        const Eigen::Vector3d ev = state.v - ref.v;
        const Eigen::Vector3d e3 = Eigen::Vector3d::UnitZ();
    
        // Part 5.2: ROS uses upward z and +f*R*e3 thrust, unlike the paper.
        Eigen::Vector3d A = -gains.kx*ex - gains.kv*ev + m*g*e3 + m*ref.a;
        if (compensate_drag) A -= dragWorld(state);
        // With zero requested force the thrust direction is undetermined.
        const Eigen::Vector3d b3d = A.norm() > 1e-9 ? A.normalized() : e3;
        Eigen::Vector3d b1c(std::cos(ref.yaw), std::sin(ref.yaw), 0.0);
        Eigen::Vector3d b2d = b3d.cross(b1c);
        if (b2d.norm() < 1e-9) {
          // Pick a perpendicular heading if the requested heading is parallel to thrust.
          b1c = b3d.unitOrthogonal();
          b2d = b3d.cross(b1c);
        }
        b2d.normalize();
        cmd.Rd.col(0) = b2d.cross(b3d);
        cmd.Rd.col(1) = b2d;
        cmd.Rd.col(2) = b3d;
    
        // Part 5.3: the handout permits Omega_d=0 and dot(Omega_d)=0.
        const Eigen::Vector3d er =
            0.5 * vee(cmd.Rd.transpose()*state.R - state.R.transpose()*cmd.Rd);
        const Eigen::Vector3d eomega = state.omega;
    
        // Part 5.4: equations (15),(16), adapted to upward z.
        cmd.wrench(0) = A.dot(state.R.col(2));
        cmd.wrench.tail<3>() = -gains.kr*er - gains.komega*eomega
                              + state.omega.cross(J*state.omega);
    
        // Parts 5.5,5.6: invert the wrench map and preserve reversible rotor signs.
        const Eigen::Vector4d signed_squared_speeds = F2W_ * cmd.wrench;
        for (int i = 0; i < 4; ++i) {
          const double s = signed_squared_speeds(i);
          cmd.rotor_speeds(i) = std::copysign(std::sqrt(std::abs(s)), s);
        }
        return cmd;
      }
    
     private:
      Eigen::Matrix4d allocation_, F2W_;
    };
    }  // namespace controller_pkg
    ✓ • 3.22s

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_official_frame.png

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/unity_tracking.png

## Activity

    $ cat report/unity_bag_info.txt; sed -n '1,220p' controller_pkg/src/controller_node.cpp; git status --short; ls -l scripts dependencies/tesse_ros_bridge/src/tesse_ros_bridge/*node*
    path:        /workspace/lab3/report/unity_flight.bag
    version:     2.0
    duration:    56.4s
    start:       Jan 01 1970 00:08:20.56 (500.56)
    end:         Jan 01 1970 00:09:16.96 (556.96)
    size:        20.9 MB
    messages:    10487
    compression: none [28/28 chunks]
    types:       mav_msgs/Actuators                           [25741daf38ed25442e3a66a855ee8d9c]
                 nav_msgs/Odometry                            [cd5e73d190d741a2f92e81eda573aca7]
                 nav_msgs/Path                                [6227e2b7e9cce15051f669a5e197bbf7]
                 rosgraph_msgs/Clock                          [a9c97c1d230cfc112e270351a944ee47]
                 trajectory_msgs/MultiDOFJointTrajectoryPoint [3ebe08d1abd5b65862d50e09430db776]
                 visualization_msgs/Marker                    [4048c9de2a16f4ae8e0538085ebf1b97]
    topics:      /clock              1374 msgs    : rosgraph_msgs/Clock
                 /current_state      2821 msgs    : nav_msgs/Odometry
                 /desired_state      2614 msgs    : trajectory_msgs/MultiDOFJointTrajectoryPoint
                 /flight/actual       484 msgs    : nav_msgs/Path
                 /flight/desired      487 msgs    : nav_msgs/Path
                 /flight/source         1 msg     : visualization_msgs/Marker
                 /rotor_speed_cmds   2706 msgs    : mav_msgs/Actuators
    #include <ros/ros.h>
    #include <mav_msgs/Actuators.h>
    #include <nav_msgs/Odometry.h>
    #include <trajectory_msgs/MultiDOFJointTrajectoryPoint.h>
    #include <tf2/LinearMath/Quaternion.h>
    #include <tf2/utils.h>
    #include <tf2_eigen/tf2_eigen.h>
    #include <tf2_geometry_msgs/tf2_geometry_msgs.h>
    
    #include <controller_pkg/geometric_controller.h>
    #include <stdexcept>
    
    class controllerNode {
      ros::NodeHandle nh, pnh;
      // Part 1: retain handles for the subscriptions, publisher, and timer.
      ros::Subscriber desired_sub, current_sub;
      ros::Publisher rotor_pub;
      ros::Timer timer;
      controller_pkg::GeometricController controller;
      controller_pkg::State state;
      controller_pkg::Reference reference;
      bool have_current = false, have_desired = false;
      ros::Time current_received, desired_received;
      double hz, state_timeout, desired_timeout;
    
     public:
      controllerNode() : pnh("~") {
        // Part 6: gains have defaults and are configurable in the launch file.
        pnh.param("kx", controller.gains.kx, 6.0);
        pnh.param("kv", controller.gains.kv, 4.7);
        pnh.param("kr", controller.gains.kr, 64.0);
        pnh.param("komega", controller.gains.komega, 16.0);
        pnh.param("compensate_drag", controller.compensate_drag, false);
        pnh.param("hz", hz, 1000.0);
        pnh.param("state_timeout", state_timeout, 0.5);
        pnh.param("desired_timeout", desired_timeout, 0.5);
        for (double value : {controller.gains.kx, controller.gains.kv,
                             controller.gains.kr, controller.gains.komega,
                             hz, state_timeout, desired_timeout}) {
          if (!std::isfinite(value) || value <= 0.0)
            throw std::invalid_argument("Gains, frequency and timeouts must be positive and finite");
        }
        // Part 2: official topic names and message types; callbacks use latest state.
        desired_sub = nh.subscribe("desired_state", 1, &controllerNode::onDesiredState, this);
        current_sub = nh.subscribe("current_state", 1, &controllerNode::onCurrentState, this,
                                   ros::TransportHints().tcpNoDelay());
        rotor_pub = nh.advertise<mav_msgs::Actuators>("rotor_speed_cmds", 1);
        timer = nh.createTimer(ros::Duration(1.0/hz), &controllerNode::controlLoop, this);
        ROS_INFO("Gains kx=%g kv=%g kr=%g komega=%g; control rate=%g Hz",
                 controller.gains.kx, controller.gains.kv,
                 controller.gains.kr, controller.gains.komega, hz);
      }
    
      void onDesiredState(const trajectory_msgs::MultiDOFJointTrajectoryPoint& msg) {
        // Part 3: guard variable-length arrays before accessing element zero.
        if (msg.transforms.empty() || msg.velocities.empty() || msg.accelerations.empty()) {
          have_desired = false;
          ROS_WARN_THROTTLE(1.0, "Desired state requires a transform, velocity and acceleration");
          return;
        }
        controller_pkg::Reference next;
        tf2::fromMsg(msg.transforms[0].translation, next.x);
        tf2::fromMsg(msg.velocities[0].linear, next.v);
        tf2::fromMsg(msg.accelerations[0].linear, next.a);
        tf2::Quaternion q;
        tf2::fromMsg(msg.transforms[0].rotation, q);
        if (!next.x.allFinite() || !next.v.allFinite() || !next.a.allFinite() ||
            !std::isfinite(q.length2()) || q.length2() < 1e-12) {
          have_desired = false;
          ROS_WARN_THROTTLE(1.0, "Ignoring invalid desired state");
          return;
        }
        q.normalize();
        next.yaw = tf2::getYaw(q);
        reference = next;
        desired_received = ros::Time::now();
        have_desired = true;
      }
    
      void onCurrentState(const nav_msgs::Odometry& msg) {
        // Part 4: TESSE publishes both twist vectors in WORLD coordinates.
        // This differs from the usual Odometry child_frame_id twist convention.
        controller_pkg::State next;
        tf2::fromMsg(msg.pose.pose.position, next.x);
        tf2::fromMsg(msg.twist.twist.linear, next.v);
        Eigen::Quaterniond q;
        tf2::fromMsg(msg.pose.pose.orientation, q);
        Eigen::Vector3d omega_world;
        tf2::fromMsg(msg.twist.twist.angular, omega_world);
        if (!next.x.allFinite() || !next.v.allFinite() || !omega_world.allFinite() ||
            !q.coeffs().allFinite() || q.squaredNorm() < 1e-12) {
          have_current = false;
          ROS_WARN_THROTTLE(1.0, "Ignoring invalid current state");
          return;
        }
        next.R = q.normalized().toRotationMatrix();
        next.omega = next.R.transpose()*omega_world;
        state = next;
        current_received = ros::Time::now();
        have_current = true;
      }
    
      void controlLoop(const ros::TimerEvent&) {
        const ros::Time now = ros::Time::now();
        const double state_age = (now-current_received).toSec();
        const double desired_age = (now-desired_received).toSec();
        if (!have_current || !have_desired || state_age < 0.0 || desired_age < 0.0 ||
            state_age > state_timeout || desired_age > desired_timeout) return;
    
        // Part 5: equations, desired SO(3) attitude and signed allocation are in
        // geometric_controller.h so the same implementation can run without ROS.
        const auto cmd = controller.compute(state, reference);
        if (!cmd.rotor_speeds.allFinite()) {
          ROS_ERROR_THROTTLE(1.0, "Nonfinite rotor command suppressed");
          return;
        }
        mav_msgs::Actuators msg;
        msg.header.stamp = now;
        msg.header.frame_id = "base_link_gt";
        msg.angular_velocities.assign(cmd.rotor_speeds.data(), cmd.rotor_speeds.data()+4);
        rotor_pub.publish(msg);
      }
    };
    
    int main(int argc, char** argv) {
      ros::init(argc, argv, "controller_node");
      try {
        controllerNode node;
        ros::spin();
      } catch (const std::exception& e) {
        ROS_FATAL("Controller initialization failed: %s", e.what());
        return 1;
      }
      return 0;
    }
    ?? ../Lab4/
    ?? ./
    -rwxrwxr-x 1 chixin chixin 46119 Oct 10 10:56 dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py
    
    scripts:
    total 44
    -rw-rw-r-- 1 chixin chixin 2745 Oct 10 13:02 analyze_unity.py
    -rw-rw-r-- 1 chixin chixin  514 Oct 10 13:01 build_workspace.sh
    -rw-rw-r-- 1 chixin chixin 5282 Oct 10 12:55 monitor_unity.py
    -rw-rw-r-- 1 chixin chixin 4797 Oct 10 10:22 offline_flight.cpp
    -rwxrwxr-x 1 chixin chixin 1989 Oct 10 10:41 plot_flight.py
    -rw-rw-r-- 1 chixin chixin  886 Oct 10 13:01 prepare_unity_arm64.sh
    -rw-rw-r-- 1 chixin chixin 1883 Oct 10 13:02 run_unity_flight.sh
    -rw-rw-r-- 1 chixin chixin 1319 Oct 10 13:02 start_unity_arm64.sh
    -rwxrwxr-x 1 chixin chixin  728 Oct 10 10:41 validate_offline.sh
    ✓ • 49ms

## Assistant

正式飞行和录像已完成：记录了 55 秒轨迹，稳定段实际绕行 2.38 圈，位置均方根误差为 0.306 米。独立工作区也已编译通过；我正在整理最终录像和报告，文件全部保留在本地。

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/analyze_unity.py
    @@ -51,3 +51,3 @@
     fig.suptitle("MIT VNAV Lab3 — official Unity/TESSE flight")
    -fig.tight_layout()
    +fig.tight_layout(rect=(0,0,1,.95))
     fig.savefig(root/"report/unity_tracking.pdf")

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'cp /workspace/lab3/report/video/rviz_official_tesse.mp4 /workspace/lab3/report/video/rviz_official_tesse_full.mp4; ffmpeg -y -loglevel error -ss 30 -i /workspace/lab3/report/video/rviz_official_tesse_full.mp4 -c:v libx264 -threads 1 -preset fast -crf 20 -pix_fmt yuv420p -movflags +faststart /workspace/lab3/report/video/rviz_official_tesse.mp4; ffmpeg -y -loglevel error -ss 8 -i /workspace/lab3/report/video/rviz_official_tesse.mp4 -frames:v 1 /workspace/lab3/report/video/rviz_official_frame.png; python3 /workspace/lab3/scripts/analyze_unity.py; ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,r_frame_rate,codec_name -of json /workspace/lab3/report/video/rviz_official_tesse.mp4 > /workspace/lab3/report/video/rviz_official_metadata.json; cp /tmp/lab3-final-monitor.log /workspace/lab3/report/unity_runtime.txt; cp /tmp/lab3-unity-box64.log /workspace/lab3/report/unity_startup.txt; sha256sum /tmp/tesse-lab3/lab3.x86_64; if [ -f /opt/lab3-deps/mav_comm/LICENSE ]; then cp /opt/lab3-deps/mav_comm/LICENSE /workspace/lab3/dependencies/mav_msgs/LICENSE; fi'; sha256sum /tmp/vnav_lab3_simulator.zip; chmod +x scripts/*unity*.sh scripts/build_workspace.sh scripts/analyze_unity.py scripts/monitor_unity.py
    {
      "source": "Unmodified official MIT Lab3 Unity/TESSE; Box64 0.3.6 on ARM64",
      "trajectory": "x=5*sin(t/2), y=5*cos(t/2), z=2, yaw=-t/2",
      "gains": {
        "kx": 2.0,
        "kv": 2.4,
        "kr": 1.8,
        "komega": 0.7,
        "hz": 200
      },
      "samples": 2752,
      "trajectory_duration_s": 55.019999999,
      "steady_start_s": 25.132741228718345,
      "observed_steady_laps": 2.3755648711366417,
      "steady_position_rms_m": 0.30630605599350413,
      "steady_position_max_m": 0.5845453007436116,
      "steady_altitude_min_m": 1.559839,
      "steady_altitude_max_m": 1.863796,
      "steady_radial_rms_m": 0.08292571660246979,
      "all_values_finite": true,
      "flight_completed": true
    }
    fc275e71f90659bbc2b9e066696ebb842d69579238b8969178ac3396007e51e4  /tmp/tesse-lab3/lab3.x86_64
    63569062b7d33265faad4b525e247c6e01fc5052b01d6c4f6e4c756cc968c25e  /tmp/vnav_lab3_simulator.zip
    ✓ • 5.69s

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/scripts/run_unity_flight.sh
    @@ -33,3 +33,3 @@
       -c:v libx264 -threads 1 -preset ultrafast -crf 23 -pix_fmt yuv420p \
    -  -movflags +faststart "$LAB3_DIR/report/video/rviz_official_tesse.mp4" \
    +  -movflags +faststart "$LAB3_DIR/report/video/rviz_official_tesse_full.mp4" \
       >/tmp/lab3-final-ffmpeg.log 2>&1 & pids+=("$!")
    @@ -38,2 +38,9 @@
     wait "$monitor_pid"
    -# The EXIT trap closes MP4 and rosbag cleanly.
    +# Close MP4 and rosbag before extracting the steady flight segment.
    +cleanup
    +pids=()
    +ffmpeg -y -loglevel error -ss 30 \
    +  -i "$LAB3_DIR/report/video/rviz_official_tesse_full.mp4" \
    +  -c:v libx264 -threads 1 -preset fast -crf 20 -pix_fmt yuv420p \
    +  -movflags +faststart "$LAB3_DIR/report/video/rviz_official_tesse.mp4"
    +python3 "$LAB3_DIR/scripts/analyze_unity.py"

## Activity

    $ python3 - <<'PY'
        from pathlib import Path
        Path('README.md').write_text('''# Lab 3 — Quadrotor geometric control
        
        依据 [MIT VNAV 2023 Lab 3](https://vnav.mit.edu/labs_2023/lab3/exercises.html) 完成。
        已在本机 ARM64 Docker / ROS Noetic 中，通过 **Box64 0.3.6 运行未修改的官方
        Lab 3 Unity/TESSE 模拟器**，完成悬停、调参和圆轨迹飞行。
        
        ## 本地交付
        
        | 交付项 | 文件 |
        | --- | --- |
        | Deliverable 1：ROS 四元数转换 | [deliverable_1.txt](deliverable_1.txt) |
        | Deliverable 2：旋翼布局秩分析、阻力补偿 | [PDF](report/deliverable_2.pdf)、[LaTeX](report/deliverable_2.tex) |
        | Deliverable 3：完整控制器源码 | [controller_pkg](controller_pkg/) |
        | 官方 TESSE 的 RViz 飞行录像 | [rviz_official_tesse.mp4](report/video/rviz_official_tesse.mp4) |
        | 完整原始录像，含起飞过渡段 | [rviz_official_tesse_full.mp4](report/video/rviz_official_tesse_full.mp4) |
        | 官方飞行轨迹、指标和说明 | [图表 PDF](report/unity_tracking.pdf)、[指标 JSON](report/unity_metrics.json)、[验证说明](report/validation.md) |
        | 官方原始飞行数据 | [CSV](report/unity_flight.csv)、`report/unity_flight.bag` |
        | 题目要求的录像说明文件 | [rviz_drone_flight.txt](rviz_drone_flight.txt) |
        
        **按用户要求，所有文件只保留在本地，未上传 Google Drive / Dropbox。**
        题目原本要求的公开链接已在说明文件中替换成本地录像路径；未执行远程提交或推送。
        
        ## 官方飞行结果
        
        原定轨迹保持为 `x=5*sin(t/2), y=5*cos(t/2), z=2, yaw=-t/2`，
        半径 5 米，周期 `4*pi ≈ 12.566` 秒。
        
        | 项目 | 实测结果 |
        | --- | ---: |
        | 总轨迹时间 | 55.02 s |
        | 稳定统计窗口 | 25.133–55.02 s，排除前两个名义周期 |
        | 稳定段实际绕行 | 2.376 圈，由实际位置相位累计计算 |
        | 稳定段三维位置 RMS 误差 | 0.3063 m |
        | 稳定段最大三维位置误差 | 0.5845 m |
        | 稳定段半径 RMS 误差 | 0.0829 m |
        | 稳定段高度范围 | 1.560–1.864 m，目标 2 m |
        
        最终参数为 `kx=2, kv=2.4, kr=1.8, komega=0.7`，控制定时器配置为 200 Hz。
        由于模拟器状态发布和容器调度，实际消息频率会低于定时器配置。
        本控制器采用题目允许的简化，忽略期望角速度前馈；仍存在高度偏差，未声称精确零误差。
        
        正式录像为 1280×800、8 fps，长 27.125 秒，从完整录像的第 30 秒开始截取，
        保持原始播放速度，覆盖超过一整圈稳定飞行。完整录像长 57.125 秒。
        画面内的来源标记说明状态来自官方 MIT Lab 3 TESSE。
        
        ## 本机直接复用
        
        已有容器 `ros_noetic_lab3`，Lab 3 挂载到 `/workspace/lab3`。
        自包含工作区 `/tmp/lab3_unity_ws` 已编译通过，见 [构建日志](report/build_unity_noetic.txt)。
        Box64 和模拟器属于容器内运行时文件，重建容器后需重新准备。
        
        ```bash
        docker start ros_noetic_lab3
        docker exec -it ros_noetic_lab3 bash
        cd /workspace/lab3
        bash scripts/build_workspace.sh
        bash scripts/prepare_unity_arm64.sh
        
        # 终端 1：保持运行，包含 roscore、Unity 和 ROS 桥接
        bash scripts/start_unity_arm64.sh
        
        # 终端 2：同一容器内，启动控制器、RViz、录屏及飞行数据记录
        bash /workspace/lab3/scripts/run_unity_flight.sh
        ```
        
        脚本使用 ROS master `11317`、Unity 显示 `:97`、RViz 显示 `:96`。
        同一网络中一次仅运行一个 TESSE 实例，避免其固定 UDP 端口冲突。
        若已存在旧的 Lab 3 运行会话，先结束其进程再运行启动脚本。
        本次任务结束时已停止本次实验进程，保留共用容器供其他实验使用。
        
        ## 从 Dockerfile 重新搭建
        
        在 ARM64 主机上，从本目录运行：
        
        ```bash
        docker build -t vnav-lab3-noetic .
        docker run --name vnav_lab3 --shm-size=1g -it -v "$PWD:/workspace/lab3" vnav-lab3-noetic
        ```
        
        然后在容器内依次执行上述 build、prepare、start 脚本；另开宿主机终端，
        执行 `docker exec -it vnav_lab3 bash`，再运行 flight 脚本。
        新容器的所有包来自本目录 `dependencies/`，无需 Lab 4 工作区。
        Dockerfile 已包含编译、RViz、Xvfb、FFmpeg 和 Python 依赖。
        Box64 固定使用 0.3.6，下载并构建；Unity 来自
        [官方 lab3.zip](https://vnav.mit.edu/material/lab3.zip)。
        
        已有 x86_64 Noetic 环境时，也可构建同一工作区，直接启动官方 `lab3.x86_64`，
        再启动 `tesse_quadrotor_bridge.launch` 和 `traj_tracking.launch`，无需 Box64。
        
        ## 控制器实现
        
        - `src/controller_node.cpp`：ROS 订阅、参数、消息校验、超时检查和电机命令发布。
        - `include/controller_pkg/geometric_controller.h`：位置反馈、SO(3) 姿态误差、力矩和旋翼分配。
        - `src/traj_publisher.cpp`：官方圆轨迹及精确解析速度、加速度；`static_pose:=true` 切换悬停。
        - `config/gains_unity.yaml`：官方 TESSE 最终参数，也是标准启动文件默认值。
        - `config/gains.yaml`：早期独立模型的参数，仅供独立模型实验使用。
        
        采用 ROS 向上 z 轴，`R` 从机体转到世界坐标：
        
        ```text
        A = -kx*(x-xd) - kv*(v-vd) + m*g*e3 + m*ad
        b3d = A / ||A||
        b2d = normalize(b3d cross [cos(yawd), sin(yawd), 0])
        Rd = [b2d cross b3d, b2d, b3d]
        eR = 0.5 * vee(Rd^T*R - R^T*Rd)
        f = A dot (R*e3)
        M = -kr*eR - komega*omega_body + omega_body cross (J*omega_body)
        ```
        
        TESSE 的状态角速度按题目约定为世界坐标，因此先计算
        `omega_body = R.transpose()*omega_world`。
        保留骨架参数 `m=1, d=0.3, cf=0.001, cd=0.00001, J=I`。
        官方 Unity 内部的惯量并非单位阵；最终增益是在真实模拟器中调出的。
        
        令 `a=d/sqrt(2)`、`s_i=omega_i*abs(omega_i)`，模拟器旋翼分配为：
        
        ```text
                      [ cf     cf     cf     cf   ]
        [f Mx My Mz] = [ a*cf   a*cf  -a*cf  -a*cf] s
                      [-a*cf   a*cf   a*cf  -a*cf]
                      [ cd    -cd     cd    -cd   ]
        ```
        
        左边为列向量；求逆后取带符号平方根，输出 rad/s。
        个人题图与模拟器图的旋翼编号不同，报告各自按对应图定义。
        阻力补偿可通过 `compensate_drag` 开启，官方飞行默认关闭。
        
        ## 数据回放和报告再生成
        
        ```bash
        source /tmp/lab3_unity_ws/devel/setup.bash
        python3 scripts/analyze_unity.py
        
        # 独立终端启动 roscore，停止实时控制和模拟器后回放：
        rosparam set /use_sim_time true
        rosrun rviz rviz -d controller_pkg/rviz/circle.rviz
        # 另一个同 ROS master 的终端：
        rosbag play --clock report/unity_flight.bag
        
        # 数学报告
        cd report
        pdflatex -interaction=nonstopmode -halt-on-error deliverable_2.tex
        ```
        
        `report/unity_metrics.json` 和 `unity_tracking.pdf` 只读取官方飞行 CSV。
        原始 bag 保留在本地，因体积原因由 `.gitignore` 排除；CSV、图表和录像可正常提交。
        
        ## 早期独立模型记录
        
        `scripts/validate_offline.sh`、`controller_pkg/scripts/rigid_body_demo.py`、
        `report/numerical_validation.txt`、`report/ros_metrics.json` 及
        `report/video/rviz_rigid_body_demo.mp4` 来自独立刚体模型，用于检查数学实现。
        它们不包含 Unity 接触、电机动态，指标不能与官方飞行混用。
        QEMU 4.2 / 8.2 的失败日志也保留；本次改用 Lab 4 已验证的 Box64 0.3.6
        解决了 x86_64 Unity 在 ARM64 上运行的问题。
        ''')
        Path('rviz_drone_flight.txt').write_text('''VNAV Lab 3 — Official TESSE / RViz circular flight
        
        Local video (user explicitly requested local files only):
        report/video/rviz_official_tesse.mp4
        
        Complete original recording, including initial transient:
        report/video/rviz_official_tesse_full.mp4
        
        The official MIT Lab3 Unity player ran unmodified through Box64 0.3.6 in an
        ARM64 ROS Noetic Docker container. The controller tracked the original 5 m
        radius, 2 m target-height circle with period 4*pi seconds.
        
        The primary video is an unaccelerated 27.125 s RViz screen recording excerpt
        starting at 30 s in the complete 57.125 s recording. It includes more than
        one complete stable circular flight. The full telemetry contains 55.02 s
        of trajectory time and 2.376 observed turns after the first two periods;
        steady position RMS error is 0.3063 m.
        
        Evidence: report/unity_flight.csv, report/unity_flight.bag,
        report/unity_metrics.json, report/unity_tracking.pdf, report/validation.md.
        
        No Google Drive or Dropbox upload was performed. The course's public-link
        requirement is replaced with this local path according to the user's request.
        ''')
        Path('report/validation.md').write_text('''# Lab 3 validation record
        
        ## Official Unity/TESSE flight — completed
        
        The unmodified [MIT Lab3 Unity player](https://vnav.mit.edu/material/lab3.zip)
        ran in the ARM64 ROS Noetic container via **Box64 0.3.6**. The successful local
        Lab4 task identified this runtime; previous QEMU failures did not establish
        that official TESSE was impossible on this host.
        
        Source identifiers:
        
        - Official ZIP SHA-256: `63569062b7d33265faad4b525e247c6e01fc5052b01d6c4f6e4c756cc968c25e`.
        - `lab3.x86_64` SHA-256: `fc275e71f90659bbc2b9e066696ebb842d69579238b8969178ac3396007e51e4`.
        - Box64 tag: `v0.3.6` from `ptitSeb/box64`.
        - Official startup log: `unity_startup.txt`.
        
        The actual controller and trajectory publisher communicated through the TESSE
        ROS bridge with Unity. No independent dynamics node was used in this run.
        The trajectory remained `x=5*sin(t/2), y=5*cos(t/2), z=2, yaw=-t/2`, with period
        `4*pi` s. A 25 s static hover was checked before circular tuning; its data are
        in `trials/unity_hover.csv`. Circle trials are also retained.
        
        ### Tuning and measured result
        
        | Gains (kx, kv, kr, komega) | Circle RMS position error | Action |
        | --- | ---: | --- |
        | 2, 2.4, 1.8, 0.7 | 0.2710 m, initial trial's last 20 s | selected |
        | 4, 3, 2.4, 0.6 | 0.8970 m, stronger-gain trial's last 20 s | rejected |
        | 2, 2.4, 1.8, 0.7 | 0.3063 m, final recorded run after two periods | final default |
        
        The final run contains 2,752 state samples over 55.02 trajectory seconds.
        After excluding the first two nominal periods (25.1327 s), the actual position
        phase `unwrap(atan2(x,y))` advances by **2.3756 turns**. This measures the
        vehicle's observed path rather than counting requested trajectory periods.
        
        | Final steady-window metric | Value |
        | --- | ---: |
        | Three-dimensional position RMS error | 0.306306 m |
        | Maximum three-dimensional position error | 0.584545 m |
        | Radial RMS error | 0.082926 m |
        | Actual height range | 1.559839–1.863796 m |
        | Target height | 2 m |
        
        Feedback is stable and completes repeated circles, with a remaining height
        offset. Desired attitude-rate feedforward is omitted as permitted by the
        exercise. The handout's unit inertia is retained in the controller; the actual
        Unity inertia differs. These results demonstrate bounded circular tracking,
        not zero error or a proof of stability for all initial conditions.
        
        The configured control timer is 200 Hz; received state and transmitted motor
        message rates in this software-rendered container are lower. Error is evaluated
        against the latest received desired-state message at each state callback;
        asynchronous transport can contribute to the measurement.
        
        ### Video and raw evidence
        
        - `video/rviz_official_tesse_full.mp4`: complete 57.125 s, 1280×800, H.264,
          8 fps, actual RViz screen capture.
        - `video/rviz_official_tesse.mp4`: 27.125 s excerpt beginning at wall-video time
          30 s; original playback speed; more than one steady circular flight.
        - `video/rviz_official_frame.png`: frame extracted from the final excerpt.
        - `unity_flight.csv`: measured states, latest references and motor commands.
        - `unity_flight.bag`: original ROS messages, 56.4 s, 10,487 messages; local only.
        - `unity_bag_info.txt`: topic and message inventory.
        - `unity_metrics.json`, `unity_tracking.pdf` / `.png`: generated by
          `scripts/analyze_unity.py` exclusively from official telemetry.
        - `unity_runtime.txt`: monitor progress and completion record.
        
        The recording label identifies the official MIT Lab3 TESSE source. MP4
        metadata was inspected and video frames were visually checked. All videos
        and data remain local at the user's explicit request; no public URL is created.
        
        ## Build
        
        The controller, catkin_simple, mav_msgs and vendored TESSE bridge compiled
        successfully in the self-contained `/tmp/lab3_unity_ws` workspace. All four
        source packages plus catkin's prebuild package succeeded with no warnings.
        See `build_unity_noetic.txt`. Dependencies now live in `lab3/dependencies/`;
        the new workspace has no Lab4 package links. The earlier Noetic build log is
        also retained as `build_noetic.txt`.
        
        The Python bridge uses Python 3 entrypoints and imports cv2 before cv_bridge,
        which avoids an ARM64 import crash. The TESSE interface is installed without
        the obsolete enum34 dependency; Python 3 already supplies enum.
        
        ## Independent numerical plant — separate diagnostic evidence
        
        Earlier numerical checks use the same C++ controller header, with an independent
        rigid-body plant. Rotor moments are computed from positions and forces, then
        integrated with quaternion normalization. They use the original high gains
        for that model, not the final official Unity gains.
        
        | Case | Steady position RMS error |
        | --- | ---: |
        | Static waypoint, final 5 s | approximately roundoff |
        | Circle, 1 ms integration step | 0.01493 m |
        | Circle, 0.5 ms integration step | 0.01444 m |
        | Circle with quadratic drag, no compensation | 0.08337 m |
        | Circle with quadratic drag compensation | 0.02033 m |
        
        Full details: `numerical_validation.txt`. A separate actual-ROS-node run with
        the independent plant produced 0.03055 m steady RMS over 80 simulation seconds;
        see `ros_flight.csv` and `ros_metrics.json`. Its 20 s recording is explicitly
        named `video/rviz_rigid_body_demo.mp4`. It has no Unity contacts or motor
        dynamics and must not be presented as official TESSE evidence.
        
        QEMU 4.2 and 8.2 startup failures remain in `tesse_qemu_4_startup.txt` and
        `tesse_qemu_8_startup.txt` for history. Box64 resolved the runtime issue.
        ''')
        PY
    ✓ • 0ms

## Activity

    $ docker exec ros_noetic_lab3 ps -eo pid,ppid,args | rg '(:96|:97|11317|tesse-lab3|lab3-official|lab3_official|tesse_quadrotor_bridge|quadrotor_control_interface|tesse_ros_node|/rosout|/rosmaster)' ; rg -n 'PENDING|待完成|尚不能|remain pending|上传 Google|public video URL' README.md rviz_drone_flight.txt report/validation.md; cat report/video/rviz_official_metadata.json; ls -lh report/deliverable_2.pdf report/unity_tracking.pdf; docker exec ros_noetic_lab3 bash -lc 'bash -n /workspace/lab3/scripts/build_workspace.sh /workspace/lab3/scripts/prepare_unity_arm64.sh /workspace/lab3/scripts/start_unity_arm64.sh /workspace/lab3/scripts/run_unity_flight.sh; ls -l /tmp/lab3_unity_ws/src; ls -l /opt/lab3-deps/mav_comm/LICENSE*'
      41376       0 bash -lc source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roscore -p 11317 >/tmp/lab3-unity-master.log 2>&1
      41390       0 bash -lc Xvfb :97 -screen 0 960x600x24 >/tmp/lab3-unity-xvfb.log 2>&1
      41402   41390 Xvfb :97 -screen 0 960x600x24
      41403       0 bash -lc cd /tmp/tesse-lab3; DISPLAY=:97 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0 /tmp/lab4-runtime/box64-0.3.6/build/box64 ./lab3.x86_64 -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile /tmp/lab3-unity-box64.log >/tmp/lab3-box64.log 2>&1
      41421   41376 /usr/bin/python3 /opt/ros/noetic/bin/roscore -p 11317
      41442   41421 /usr/bin/python3 /opt/ros/noetic/bin/rosmaster --core -p 11317 -w 3 __log:=/root/.ros/log/8dc15290-c466-11f1-8a6d-e2e6d9d83e81/master.log
      41461   41421 /opt/ros/noetic/lib/rosout/rosout __name:=rosout __log:=/root/.ros/log/8dc15290-c466-11f1-8a6d-e2e6d9d83e81/rosout-1.log
      41544       0 bash -lc source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true >/tmp/lab3-unity-bridge.log 2>&1
      41580   41544 /usr/bin/python3 /opt/ros/noetic/bin/roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true
      41596   41580 python3 /workspace/lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py imu/clean/imu:=imu/clean/imu imu/noisy/imu:=imu/noisy/imu imu/noisy/biases/gyro:=imu/noisy/biases/gyro imu/noisy/biases/accel:=imu/noisy/biases/accel odom:=/current_state left_cam/rgb/image_raw:=left_cam/rgb/image_raw left_cam/mono/image_raw:=left_cam/mono/image_raw right_cam/image_raw:=right_cam/image_raw seg_cam/rgb/image_raw:=seg_cam/rgb/image_raw depth_cam/mono/image_raw:=depth_cam/mono/image_raw left_cam/camera_info:=left_cam/camera_info right_cam/camera_info:=right_cam/camera_info seg_cam/camera_info:=seg_cam/camera_info depth_cam/camera_info:=depth_cam/camera_info lidar/front_lidar/scan:=lidar/front_lidar/scan lidar/rear_lidar/scan:=lidar/rear_lidar/scan __name:=tesse_ros_bridge __log:=/root/.ros/log/8dc15290-c466-11f1-8a6d-e2e6d9d83e81/tesse-tesse_ros_bridge-1.log
      41597   41580 python3 /workspace/lab4/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/quadrotor_control_interface.py quadrotor_control/rotor_speed_cmds:=/rotor_speed_cmds __name:=quadrotor_control_interface __log:=/root/.ros/log/8dc15290-c466-11f1-8a6d-e2e6d9d83e81/tesse-quadrotor_control_interface-2.log
      46130       0 bash -lc Xvfb :96 -screen 0 1280x800x24 >/tmp/lab3-official-rviz-xvfb.log 2>&1
      46140   46130 Xvfb :96 -screen 0 1280x800x24
      46141       0 bash -lc source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost DISPLAY=:96 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1; rosrun rviz rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz >/tmp/lab3-official-rviz.log 2>&1
      46170   46141 /opt/ros/noetic/lib/rviz/rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz
    README.md:20:**按用户要求，所有文件只保留在本地，未上传 Google Drive / Dropbox。**
    {
        "programs": [
    
        ],
        "streams": [
            {
                "codec_name": "h264",
                "width": 1280,
                "height": 800,
                "r_frame_rate": "8/1"
            }
        ],
        "format": {
            "duration": "27.125000",
            "size": "420049"
        }
    }
    -rw-r--r-- 1 chixin chixin 145K Oct 10 10:32 report/deliverable_2.pdf
    -rw-r--r-- 1 root   root    57K Oct 10 15:23 report/unity_tracking.pdf
    total 0
    lrwxrwxrwx 1 root root 42 Oct 10 05:02 catkin_simple -> /workspace/lab3/dependencies/catkin_simple
    lrwxrwxrwx 1 root root 30 Oct 10 05:02 controller_pkg -> /workspace/lab3/controller_pkg
    lrwxrwxrwx 1 root root 37 Oct 10 05:02 mav_msgs -> /workspace/lab3/dependencies/mav_msgs
    lrwxrwxrwx 1 root root 45 Oct 10 05:02 tesse_ros_bridge -> /workspace/lab3/dependencies/tesse_ros_bridge
    ls: cannot access '/opt/lab3-deps/mav_comm/LICENSE*': No such file or directory
    ✗ (2) • 80ms

## Activity

    Viewed image /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_official_frame.png

## Activity

    $ docker exec ros_noetic_lab3 ps -eo pid,ppid,args | rg '(lab3|box64|Unity)'; docker inspect ros_noetic_lab3 --format '{{.Config.Image}} {{.HostConfig.ShmSize}}'; sed -n '1,70p' dependencies/tesse_ros_bridge/launch/tesse_quadrotor_bridge.launch; sed -n '1,35p' dependencies/mav_msgs/include/mav_msgs/common.h; du -sh .
      41376       0 bash -lc source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roscore -p 11317 >/tmp/lab3-unity-master.log 2>&1
      41390       0 bash -lc Xvfb :97 -screen 0 960x600x24 >/tmp/lab3-unity-xvfb.log 2>&1
      41403       0 bash -lc cd /tmp/tesse-lab3; DISPLAY=:97 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0 /tmp/lab4-runtime/box64-0.3.6/build/box64 ./lab3.x86_64 -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile /tmp/lab3-unity-box64.log >/tmp/lab3-box64.log 2>&1
      41420   41403 ./lab3.x86_64 -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile /tmp/lab3-unity-box64.log
      41544       0 bash -lc source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true >/tmp/lab3-unity-bridge.log 2>&1
      46130       0 bash -lc Xvfb :96 -screen 0 1280x800x24 >/tmp/lab3-official-rviz-xvfb.log 2>&1
      46141       0 bash -lc source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost DISPLAY=:96 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1; rosrun rviz rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz >/tmp/lab3-official-rviz.log 2>&1
      46170   46141 /opt/ros/noetic/lib/rviz/rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz
    ros_noetic_lab2_ready:local 67108864
    <!--
         Use RVIZ for visualization.
    -->
    <launch>
      <arg name="ns"                   default="tesse"/>
      <arg name="teleop"               default="false"/>
      <arg name="drive_with_ackermann" default="false"/>
      <arg name="params_dir"           default="$(find tesse_ros_bridge)/params"/>
      <arg name="use_gt_frames"        default="true"/>
      <arg name="enable_step_mode"     default="false"/>
    
      <!-- Network arguments -->
      <arg name="sim_ip"                default="127.0.0.1"/>
      <arg name="self_ip"               default="127.0.0.1"/>
      <arg name="use_broadcast"         default="true"/>
    
      <!-- Specify data to publish -->
      <!-- `publish_stereo_gry` toggles between publishing as mono8 (true) or rgb8 (false) \
            for both left/right stereo cameras -->
      <arg name="publish_clock"             default="true"/>
      <arg name="publish_metadata"          default="false"/>
      <arg name="publish_collisions"        default="false"/>
    
      <arg name="publish_imu"               default="true"/>
      <arg name="publish_odom"              default="true"/>
      <arg name="publish_noisy_imu"         default="false"/>
      <arg name="publish_imu_noise_biases"  default="false"/>
      <arg name="publish_noisy_odom"        default="false"/>
    
      <arg name="publish_stereo_rgb"        default="false"/>
      <arg name="publish_stereo_gry"        default="false"/>
      <arg name="publish_segmentation"      default="false"/>
      <arg name="publish_depth"             default="false"/>
      <arg name="publish_third_pov"         default="false"/>
    
      <arg name="publish_front_lidar"       default="false"/>
      <arg name="publish_rear_lidar"        default="false"/>
    
      <!-- Sanity check argument -->
      <arg name="stereo_baseline"      default="0.10"/>
    
      <!-- Sim arguments -->
      <!-- NOTE: `use_sim_time` should always be true for tesse! -->
      <arg name="use_sim_time"          default="true"/>
      <arg name="frame_rate"            default="20.0"/>
      <arg name="imu_rate"              default="200"/>
      <arg name="scan_rate"             default="40.0"/>
      <arg name="enable_collision"      default="true"/>
      <arg name="initial_scene"         default="1"/>
    
      <!-- Reference frame arguments -->
      <arg name="world_frame_id"        default="world"/>
      <arg name="map_frame_id"          default="map"/>
      <arg name="body_frame_id"         default="base_link"/>
      <arg name="body_frame_id_gt"      default="base_link_gt"/>
    
      <!-- If use_sim, simulator will publish -->
      <param name="/use_sim_time" value="$(arg use_sim_time)"/>
    
      <!-- Map servers -->
      <!-- <include file="$(find tesse_ros_bridge)/launch/maps.launch"/> -->
    
      <!-- Launch tesse ROS Bridge Node -->
      <node ns="$(arg ns)" name="tesse_ros_bridge" pkg="tesse_ros_bridge"
            type="tesse_ros_node.py" output="screen">
        <!-- Topics -->
        <remap from="imu/clean/imu"          to="imu/clean/imu"/>
        <remap from="imu/noisy/imu"          to="imu/noisy/imu"/>
        <remap from="imu/noisy/biases/gyro"  to="imu/noisy/biases/gyro"/>
        <remap from="imu/noisy/biases/accel" to="imu/noisy/biases/accel"/>
    /*
     * Copyright 2015 Fadri Furrer, ASL, ETH Zurich, Switzerland
     * Copyright 2015 Michael Burri, ASL, ETH Zurich, Switzerland
     * Copyright 2015 Markus Achtelik, ASL, ETH Zurich, Switzerland
     * Copyright 2015 Helen Oleynikova, ASL, ETH Zurich, Switzerland
     * Copyright 2015 Mina Kamel, ASL, ETH Zurich, Switzerland
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *     http://www.apache.org/licenses/LICENSE-2.0
    
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    // Common conversion functions between geometry messages, Eigen types, and yaw.
    
    #ifndef MAV_MSGS_COMMON_H
    #define MAV_MSGS_COMMON_H
    
    #include <geometry_msgs/Point.h>
    #include <geometry_msgs/Quaternion.h>
    #include <geometry_msgs/Vector3.h>
    #include <Eigen/Geometry>
    #include <boost/algorithm/clamp.hpp>
    
    namespace mav_msgs {
    
    const double kSmallValueCheck = 1.e-6;
    const double kNumNanosecondsPerSecond = 1.e9;
    31M    .
    ✓ • 0ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /home/chixin/f29xs/2026Fall_TeamFullcans/lab3/controller_pkg/include/controller_pkg/geometric_controller.h
    @@ -34,3 +34,3 @@
     
    -// Lab 3 simulator constants; do not substitute real drone coefficients.
    +// Lab 3 skeleton model constants; Unity's internal inertia may differ.
     class GeometricController {

## Activity

    $ docker exec ros_noetic_lab3 bash -lc 'kill -INT 41580 46170; kill -TERM 41420; kill -INT 41421' ; docker exec ros_noetic_lab3 bash -lc 'kill -TERM 41402 46140' ; docker exec ros_noetic_lab3 ps -eo pid,ppid,args | rg '(lab3.x86_64|11317|lab3_official_rviz|Xvfb :9[67])' ; git diff --check -- .; cat report/unity_metrics.json; ls -lh report/video/rviz_official*
      41376       0 bash -lc source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roscore -p 11317 >/tmp/lab3-unity-master.log 2>&1
      41403       0 bash -lc cd /tmp/tesse-lab3; DISPLAY=:97 LIBGL_ALWAYS_SOFTWARE=1 BOX64_LOG=0 /tmp/lab4-runtime/box64-0.3.6/build/box64 ./lab3.x86_64 -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile /tmp/lab3-unity-box64.log >/tmp/lab3-box64.log 2>&1
      41420   41403 ./lab3.x86_64 -screen-width 960 -screen-height 600 -screen-fullscreen 0 -force-glcore -logFile /tmp/lab3-unity-box64.log
      41421   41376 /usr/bin/python3 /opt/ros/noetic/bin/roscore -p 11317
      41442   41421 /usr/bin/python3 /opt/ros/noetic/bin/rosmaster --core -p 11317 -w 3 __log:=/root/.ros/log/8dc15290-c466-11f1-8a6d-e2e6d9d83e81/master.log
      41544       0 bash -lc source /tmp/lab4_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost; roslaunch tesse_ros_bridge tesse_quadrotor_bridge.launch publish_imu:=false publish_collisions:=true >/tmp/lab3-unity-bridge.log 2>&1
      46141       0 bash -lc source /tmp/lab3_ws/devel/setup.bash; export ROS_MASTER_URI=http://localhost:11317 ROS_HOSTNAME=localhost DISPLAY=:96 LIBGL_ALWAYS_SOFTWARE=1 DISABLE_ROS1_EOL_WARNINGS=1; rosrun rviz rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz >/tmp/lab3-official-rviz.log 2>&1
      46170   46141 /opt/ros/noetic/lib/rviz/rviz -d /workspace/lab3/controller_pkg/rviz/circle.rviz __name:=lab3_official_rviz
    {
      "source": "Unmodified official MIT Lab3 Unity/TESSE; Box64 0.3.6 on ARM64",
      "trajectory": "x=5*sin(t/2), y=5*cos(t/2), z=2, yaw=-t/2",
      "gains": {
        "kx": 2.0,
        "kv": 2.4,
        "kr": 1.8,
        "komega": 0.7,
        "hz": 200
      },
      "samples": 2752,
      "trajectory_duration_s": 55.019999999,
      "steady_start_s": 25.132741228718345,
      "observed_steady_laps": 2.3755648711366417,
      "steady_position_rms_m": 0.30630605599350413,
      "steady_position_max_m": 0.5845453007436116,
      "steady_altitude_min_m": 1.559839,
      "steady_altitude_max_m": 1.863796,
      "steady_radial_rms_m": 0.08292571660246979,
      "all_values_finite": true,
      "flight_completed": true
    }
    -rw-r--r-- 1 root root 292K Oct 10 15:23 report/video/rviz_official_frame.png
    -rw-r--r-- 1 root root  276 Oct 10 15:23 report/video/rviz_official_metadata.json
    -rw-r--r-- 1 root root 411K Oct 10 15:23 report/video/rviz_official_tesse.mp4
    -rw-r--r-- 1 root root 2.0M Oct 10 15:23 report/video/rviz_official_tesse_full.mp4
    ✓ • 413ms

## Activity

    $ docker exec ros_noetic_lab3 ps -eo pid,ppid,args | rg '(lab3.x86_64|11317|lab3_official_rviz|Xvfb :9[67])' ; python3 - <<'PY'
        import os, subprocess
        subprocess.run(['docker','exec','ros_noetic_lab3','chown','-R',f'{os.getuid()}:{os.getgid()}','/workspace/lab3/report'],check=True)
        PY
        rg -n 'wait|cleanup|full.mp4' scripts/run_unity_flight.sh; tail -8 report/build_unity_noetic.txt
    11:cleanup() {
    13:  for pid in "${pids[@]}"; do wait "$pid" 2>/dev/null || true; done
    15:trap cleanup EXIT
    34:  -movflags +faststart "$LAB3_DIR/report/video/rviz_official_tesse_full.mp4" \
    38:wait "$monitor_pid"
    40:cleanup
    43:  -i "$LAB3_DIR/report/video/rviz_official_tesse_full.mp4" \
    Finished <<< controller_pkg                       [ 20.2 seconds ]
    [build] Summary: All 5 packages succeeded!
    [build] Ignored: None.
    [build] Warnings: None.
    [build] Abandoned: No packages were abandoned.
    [build] Failed: No packages failed.
    [build] Runtime: 30.1 seconds total.
    [build] Note: Workspace packages have changed, please re-source setup files to use them.
    ✓ • 0ms

## Assistant

已完成。这次复用 Lab 4 的 **Box64 0.3.6**，成功运行官方 TESSE；之前在 QEMU 失败后停止尝试，确实过早。

- 官方飞行记录 55 秒，稳定段完成 **2.38 圈**，位置 RMS 误差 **0.306 米**，仍有高度偏差。
- 控制器和实验依赖编译通过，书面答案已完成。
- [正式飞行录像](/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/report/video/rviz_official_tesse.mp4)
- [完整交付与复现说明](/home/chixin/f29xs/2026Fall_TeamFullcans/lab3/README.md)

**全部保留在本地，没有上传 Google Drive。**

## User

我已经git完了，请你commit一下

## Assistant

我先检查暂存区和改动范围，然后提交 Lab 3 的文件。

## Activity

    $ git status --short; git diff --cached --stat; git log -4 --oneline; git rev-parse --show-toplevel; rg --files -g AGENTS.md -g '!dependencies/**' /home/chixin/f29xs /tmp 2>/dev/null | head -30
    A  .gitignore
    A  Dockerfile
    A  README.md
    A  controller_pkg/CMakeLists.txt
    A  controller_pkg/config/gains.yaml
    A  controller_pkg/config/gains_unity.yaml
    A  controller_pkg/include/controller_pkg/geometric_controller.h
    A  controller_pkg/launch/rigid_body_demo.launch
    A  controller_pkg/launch/traj_tracking.launch
    A  controller_pkg/package.xml
    A  controller_pkg/rviz/circle.rviz
    A  controller_pkg/rviz/lab3.rviz
    A  controller_pkg/scripts/rigid_body_demo.py
    A  controller_pkg/src/controller_node.cpp
    A  controller_pkg/src/traj_publisher.cpp
    A  deliverable_1.txt
    A  dependencies/README.md
    A  dependencies/catkin_simple/.gitignore
    A  dependencies/catkin_simple/CMakeLists.txt
    A  dependencies/catkin_simple/README.md
    A  dependencies/catkin_simple/cmake/catkin_simple-extras.cmake.em
    A  dependencies/catkin_simple/package.xml
    A  dependencies/mav_msgs/CHANGELOG.rst
    A  dependencies/mav_msgs/CMakeLists.txt
    A  dependencies/mav_msgs/cmake/export_flags.cmake
    A  dependencies/mav_msgs/include/mav_msgs/common.h
    A  dependencies/mav_msgs/include/mav_msgs/conversions.h
    A  dependencies/mav_msgs/include/mav_msgs/default_topics.h
    A  dependencies/mav_msgs/include/mav_msgs/default_values.h
    A  dependencies/mav_msgs/include/mav_msgs/eigen_mav_msgs.h
    A  dependencies/mav_msgs/msg/Actuators.msg
    A  dependencies/mav_msgs/msg/AttitudeThrust.msg
    A  dependencies/mav_msgs/msg/FilteredSensorData.msg
    A  dependencies/mav_msgs/msg/GpsWaypoint.msg
    A  dependencies/mav_msgs/msg/RateThrust.msg
    A  dependencies/mav_msgs/msg/RollPitchYawrateThrust.msg
    A  dependencies/mav_msgs/msg/Status.msg
    A  dependencies/mav_msgs/msg/TorqueThrust.msg
    A  dependencies/mav_msgs/package.xml
    A  dependencies/tesse_interface/LICENSE
    A  dependencies/tesse_interface/README.md
    A  dependencies/tesse_interface/setup.cfg
    A  dependencies/tesse_interface/setup.py
    A  dependencies/tesse_interface/src/tesse/__init__.py
    A  dependencies/tesse_interface/src/tesse/env.py
    A  dependencies/tesse_interface/src/tesse/msgs.py
    A  dependencies/tesse_interface/src/tesse/utils.py
    A  dependencies/tesse_ros_bridge/CMakeLists.txt
    A  dependencies/tesse_ros_bridge/launch/maps.launch
    A  dependencies/tesse_ros_bridge/launch/play_traj.launch
    A  dependencies/tesse_ros_bridge/launch/record_traj.launch
    A  dependencies/tesse_ros_bridge/launch/tesse_bridge.launch
    A  dependencies/tesse_ros_bridge/launch/tesse_quadrotor_bridge.launch
    A  dependencies/tesse_ros_bridge/msg/CollisionStats.msg
    A  dependencies/tesse_ros_bridge/package.xml
    A  dependencies/tesse_ros_bridge/params/camera_params.yaml
    A  dependencies/tesse_ros_bridge/params/lidar_params.yaml
    A  dependencies/tesse_ros_bridge/params/map_tfs.yaml
    A  dependencies/tesse_ros_bridge/params/noise_model.yaml
    A  dependencies/tesse_ros_bridge/params/object_spawn_params.yaml
    A  dependencies/tesse_ros_bridge/params/tesse_agent_params.yaml
    A  dependencies/tesse_ros_bridge/setup.py
    A  dependencies/tesse_ros_bridge/src/key_teleop/LICENSE
    A  dependencies/tesse_ros_bridge/src/key_teleop/key_teleop.py
    A  dependencies/tesse_ros_bridge/src/tesse_ros_bridge/__init__.py
    A  dependencies/tesse_ros_bridge/src/tesse_ros_bridge/noise_simulator.py
    A  dependencies/tesse_ros_bridge/src/tesse_ros_bridge/quadrotor_control_interface.py
    A  dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py
    A  dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py
    A  dependencies/tesse_ros_bridge/srv/ObjectSpawnRequestService.srv
    A  dependencies/tesse_ros_bridge/srv/RepositionRequestService.srv
    A  dependencies/tesse_ros_bridge/srv/SceneRequestService.srv
    A  report/build_noetic.txt
    A  report/build_unity_noetic.txt
    A  report/deliverable_2.pdf
    A  report/deliverable_2.tex
    A  report/numerical_validation.txt
    A  report/offline_circle.csv
    A  report/offline_circle_drag_compensated.csv
    A  report/ros_flight.csv
    A  report/ros_metrics.json
    A  report/ros_runtime_topics.txt
    A  report/ros_tracking.pdf
    A  report/ros_tracking.png
    A  report/tesse_qemu_4_startup.txt
    A  report/tesse_qemu_8_startup.txt
    A  report/trials/unity_circle_initial.csv
    A  report/trials/unity_circle_initial.json
    A  report/trials/unity_circle_tuned.csv
    A  report/trials/unity_circle_tuned.json
    A  report/trials/unity_hover.csv
    A  report/trials/unity_hover.json
    A  report/unity_bag_info.txt
    A  report/unity_flight.csv
    A  report/unity_flight.json
    A  report/unity_metrics.json
    A  report/unity_runtime.txt
    A  report/unity_startup.txt
    A  report/unity_tracking.pdf
    A  report/unity_tracking.png
    A  report/validation.md
    A  report/video/rviz_demo_frame.png
    A  report/video/rviz_live.png
    A  report/video/rviz_official_frame.png
    A  report/video/rviz_official_metadata.json
    A  report/video/rviz_official_tesse.mp4
    A  report/video/rviz_official_tesse_full.mp4
    A  report/video/rviz_rigid_body_demo.mp4
    A  report/video/rviz_unity_trial.png
    A  report/video/unity_startup.png
    A  rviz_drone_flight.txt
    A  scripts/analyze_unity.py
    A  scripts/build_workspace.sh
    A  scripts/monitor_unity.py
    A  scripts/offline_flight.cpp
    A  scripts/plot_flight.py
    A  scripts/prepare_unity_arm64.sh
    A  scripts/run_unity_flight.sh
    A  scripts/start_unity_arm64.sh
    A  scripts/validate_offline.sh
     lab3/.gitignore                                    |   13 +
     lab3/Dockerfile                                    |   13 +
     lab3/README.md                                     |  155 +
     lab3/controller_pkg/CMakeLists.txt                 |   26 +
     lab3/controller_pkg/config/gains.yaml              |   11 +
     lab3/controller_pkg/config/gains_unity.yaml        |   10 +
     .../include/controller_pkg/geometric_controller.h  |  114 +
     lab3/controller_pkg/launch/rigid_body_demo.launch  |   16 +
     lab3/controller_pkg/launch/traj_tracking.launch    |   13 +
     lab3/controller_pkg/package.xml                    |   25 +
     lab3/controller_pkg/rviz/circle.rviz               |   74 +
     lab3/controller_pkg/rviz/lab3.rviz                 |  256 ++
     lab3/controller_pkg/scripts/rigid_body_demo.py     |  149 +
     lab3/controller_pkg/src/controller_node.cpp        |  135 +
     lab3/controller_pkg/src/traj_publisher.cpp         |   67 +
     lab3/deliverable_1.txt                             |   41 +
     lab3/dependencies/README.md                        |   16 +
     lab3/dependencies/catkin_simple/.gitignore         |    1 +
     lab3/dependencies/catkin_simple/CMakeLists.txt     |    9 +
     lab3/dependencies/catkin_simple/README.md          |  123 +
     .../cmake/catkin_simple-extras.cmake.em            |  226 ++
     lab3/dependencies/catkin_simple/package.xml        |   17 +
     lab3/dependencies/mav_msgs/CHANGELOG.rst           |   60 +
     lab3/dependencies/mav_msgs/CMakeLists.txt          |   44 +
     .../dependencies/mav_msgs/cmake/export_flags.cmake |    2 +
     .../mav_msgs/include/mav_msgs/common.h             |  362 ++
     .../mav_msgs/include/mav_msgs/conversions.h        |  582 +++
     .../mav_msgs/include/mav_msgs/default_topics.h     |   71 +
     .../mav_msgs/include/mav_msgs/default_values.h     |   33 +
     .../mav_msgs/include/mav_msgs/eigen_mav_msgs.h     |  349 ++
     lab3/dependencies/mav_msgs/msg/Actuators.msg       |    9 +
     lab3/dependencies/mav_msgs/msg/AttitudeThrust.msg  |    7 +
     .../mav_msgs/msg/FilteredSensorData.msg            |    6 +
     lab3/dependencies/mav_msgs/msg/GpsWaypoint.msg     |    8 +
     lab3/dependencies/mav_msgs/msg/RateThrust.msg      |   12 +
     .../mav_msgs/msg/RollPitchYawrateThrust.msg        |   23 +
     lab3/dependencies/mav_msgs/msg/Status.msg          |   29 +
     lab3/dependencies/mav_msgs/msg/TorqueThrust.msg    |   12 +
     lab3/dependencies/mav_msgs/package.xml             |   41 +
     lab3/dependencies/tesse_interface/LICENSE          |  339 ++
     lab3/dependencies/tesse_interface/README.md        |   36 +
     lab3/dependencies/tesse_interface/setup.cfg        |   52 +
     lab3/dependencies/tesse_interface/setup.py         |   33 +
     .../tesse_interface/src/tesse/__init__.py          |    0
     lab3/dependencies/tesse_interface/src/tesse/env.py |  148 +
     .../dependencies/tesse_interface/src/tesse/msgs.py |  470 +++
     .../tesse_interface/src/tesse/utils.py             |  107 +
     lab3/dependencies/tesse_ros_bridge/CMakeLists.txt  |   12 +
     .../tesse_ros_bridge/launch/maps.launch            |    9 +
     .../tesse_ros_bridge/launch/play_traj.launch       |   42 +
     .../tesse_ros_bridge/launch/record_traj.launch     |   45 +
     .../tesse_ros_bridge/launch/tesse_bridge.launch    |  161 +
     .../launch/tesse_quadrotor_bridge.launch           |  151 +
     .../tesse_ros_bridge/msg/CollisionStats.msg        |    8 +
     lab3/dependencies/tesse_ros_bridge/package.xml     |   25 +
     .../tesse_ros_bridge/params/camera_params.yaml     |  118 +
     .../tesse_ros_bridge/params/lidar_params.yaml      |   35 +
     .../tesse_ros_bridge/params/map_tfs.yaml           |   20 +
     .../tesse_ros_bridge/params/noise_model.yaml       |   24 +
     .../params/object_spawn_params.yaml                |  357 ++
     .../params/tesse_agent_params.yaml                 |   48 +
     lab3/dependencies/tesse_ros_bridge/setup.py        |   15 +
     .../tesse_ros_bridge/src/key_teleop/LICENSE        |   23 +
     .../tesse_ros_bridge/src/key_teleop/key_teleop.py  |  319 ++
     .../src/tesse_ros_bridge/__init__.py               |   28 +
     .../src/tesse_ros_bridge/noise_simulator.py        |  174 +
     .../quadrotor_control_interface.py                 |   98 +
     .../src/tesse_ros_bridge/tesse_ros_node.py         | 1066 ++++++
     .../tesse_ros_bridge/src/tesse_ros_bridge/utils.py |  862 +++++
     .../srv/ObjectSpawnRequestService.srv              |   10 +
     .../srv/RepositionRequestService.srv               |    8 +
     .../tesse_ros_bridge/srv/SceneRequestService.srv   |    8 +
     lab3/report/build_noetic.txt                       |   42 +
     lab3/report/build_unity_noetic.txt                 |   61 +
     lab3/report/deliverable_2.pdf                      |  Bin 0 -> 147529 bytes
     lab3/report/deliverable_2.tex                      |  149 +
     lab3/report/numerical_validation.txt               |   26 +
     lab3/report/offline_circle.csv                     | 3771 ++++++++++++++++++
     lab3/report/offline_circle_drag_compensated.csv    | 3771 ++++++++++++++++++
     lab3/report/ros_flight.csv                         | 4001 ++++++++++++++++++++
     lab3/report/ros_metrics.json                       |   11 +
     lab3/report/ros_runtime_topics.txt                 |   36 +
     lab3/report/ros_tracking.pdf                       |  Bin 0 -> 33610 bytes
     lab3/report/ros_tracking.png                       |  Bin 0 -> 90078 bytes
     lab3/report/tesse_qemu_4_startup.txt               |   65 +
     lab3/report/tesse_qemu_8_startup.txt               |   20 +
     lab3/report/trials/unity_circle_initial.csv        | 2000 ++++++++++
     lab3/report/trials/unity_circle_initial.json       |    9 +
     lab3/report/trials/unity_circle_tuned.csv          | 2009 ++++++++++
     lab3/report/trials/unity_circle_tuned.json         |    9 +
     lab3/report/trials/unity_hover.csv                 | 1255 ++++++
     lab3/report/trials/unity_hover.json                |    9 +
     lab3/report/unity_bag_info.txt                     |   21 +
     lab3/report/unity_flight.csv                       | 2753 ++++++++++++++
     lab3/report/unity_flight.json                      |    9 +
     lab3/report/unity_metrics.json                     |   22 +
     lab3/report/unity_runtime.txt                      |   21 +
     lab3/report/unity_startup.txt                      |  361 ++
     lab3/report/unity_tracking.pdf                     |  Bin 0 -> 57374 bytes
     lab3/report/unity_tracking.png                     |  Bin 0 -> 167087 bytes
     lab3/report/validation.md                          |  108 +
     lab3/report/video/rviz_demo_frame.png              |  Bin 0 -> 309000 bytes
     lab3/report/video/rviz_live.png                    |  Bin 0 -> 111387 bytes
     lab3/report/video/rviz_official_frame.png          |  Bin 0 -> 298666 bytes
     lab3/report/video/rviz_official_metadata.json      |   17 +
     lab3/report/video/rviz_official_tesse.mp4          |  Bin 0 -> 420049 bytes
     lab3/report/video/rviz_official_tesse_full.mp4     |  Bin 0 -> 2044741 bytes
     lab3/report/video/rviz_rigid_body_demo.mp4         |  Bin 0 -> 1350935 bytes
     lab3/report/video/rviz_unity_trial.png             |  Bin 0 -> 114182 bytes
     lab3/report/video/unity_startup.png                |  Bin 0 -> 156456 bytes
     lab3/rviz_drone_flight.txt                         |   23 +
     lab3/scripts/analyze_unity.py                      |   57 +
     lab3/scripts/build_workspace.sh                    |   13 +
     lab3/scripts/monitor_unity.py                      |  134 +
     lab3/scripts/offline_flight.cpp                    |  110 +
     lab3/scripts/plot_flight.py                        |   41 +
     lab3/scripts/prepare_unity_arm64.sh                |   17 +
     lab3/scripts/run_unity_flight.sh                   |   46 +
     lab3/scripts/start_unity_arm64.sh                  |   28 +
     lab3/scripts/validate_offline.sh                   |   16 +
     120 files changed, 29052 insertions(+)
    f681092 Complete VNAV Lab 4 trajectory optimization and drone racing
    fcf1ec5 feat:nothing
    6f1e7c2 feat: betteren report
    8839e7a Update report.pdf and 7 more
    /home/chixin/f29xs/2026Fall_TeamFullcans
    /tmp/box64-main/AGENTS.md
    ✓ • 0ms

## Activity

    $ git commit -m "Complete VNAV Lab 3 geometric control and official TESSE flight"
    [main 6ad442c] Complete VNAV Lab 3 geometric control and official TESSE flight
     120 files changed, 29052 insertions(+)
     create mode 100644 lab3/.gitignore
     create mode 100644 lab3/Dockerfile
     create mode 100644 lab3/README.md
     create mode 100644 lab3/controller_pkg/CMakeLists.txt
     create mode 100644 lab3/controller_pkg/config/gains.yaml
     create mode 100644 lab3/controller_pkg/config/gains_unity.yaml
     create mode 100644 lab3/controller_pkg/include/controller_pkg/geometric_controller.h
     create mode 100644 lab3/controller_pkg/launch/rigid_body_demo.launch
     create mode 100644 lab3/controller_pkg/launch/traj_tracking.launch
     create mode 100644 lab3/controller_pkg/package.xml
     create mode 100644 lab3/controller_pkg/rviz/circle.rviz
     create mode 100644 lab3/controller_pkg/rviz/lab3.rviz
     create mode 100755 lab3/controller_pkg/scripts/rigid_body_demo.py
     create mode 100644 lab3/controller_pkg/src/controller_node.cpp
     create mode 100644 lab3/controller_pkg/src/traj_publisher.cpp
     create mode 100644 lab3/deliverable_1.txt
     create mode 100644 lab3/dependencies/README.md
     create mode 100644 lab3/dependencies/catkin_simple/.gitignore
     create mode 100644 lab3/dependencies/catkin_simple/CMakeLists.txt
     create mode 100644 lab3/dependencies/catkin_simple/README.md
     create mode 100644 lab3/dependencies/catkin_simple/cmake/catkin_simple-extras.cmake.em
     create mode 100644 lab3/dependencies/catkin_simple/package.xml
     create mode 100644 lab3/dependencies/mav_msgs/CHANGELOG.rst
     create mode 100644 lab3/dependencies/mav_msgs/CMakeLists.txt
     create mode 100644 lab3/dependencies/mav_msgs/cmake/export_flags.cmake
     create mode 100644 lab3/dependencies/mav_msgs/include/mav_msgs/common.h
     create mode 100644 lab3/dependencies/mav_msgs/include/mav_msgs/conversions.h
     create mode 100644 lab3/dependencies/mav_msgs/include/mav_msgs/default_topics.h
     create mode 100644 lab3/dependencies/mav_msgs/include/mav_msgs/default_values.h
     create mode 100644 lab3/dependencies/mav_msgs/include/mav_msgs/eigen_mav_msgs.h
     create mode 100644 lab3/dependencies/mav_msgs/msg/Actuators.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/AttitudeThrust.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/FilteredSensorData.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/GpsWaypoint.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/RateThrust.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/RollPitchYawrateThrust.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/Status.msg
     create mode 100644 lab3/dependencies/mav_msgs/msg/TorqueThrust.msg
     create mode 100644 lab3/dependencies/mav_msgs/package.xml
     create mode 100644 lab3/dependencies/tesse_interface/LICENSE
     create mode 100644 lab3/dependencies/tesse_interface/README.md
     create mode 100644 lab3/dependencies/tesse_interface/setup.cfg
     create mode 100644 lab3/dependencies/tesse_interface/setup.py
     create mode 100644 lab3/dependencies/tesse_interface/src/tesse/__init__.py
     create mode 100644 lab3/dependencies/tesse_interface/src/tesse/env.py
     create mode 100644 lab3/dependencies/tesse_interface/src/tesse/msgs.py
     create mode 100644 lab3/dependencies/tesse_interface/src/tesse/utils.py
     create mode 100644 lab3/dependencies/tesse_ros_bridge/CMakeLists.txt
     create mode 100644 lab3/dependencies/tesse_ros_bridge/launch/maps.launch
     create mode 100644 lab3/dependencies/tesse_ros_bridge/launch/play_traj.launch
     create mode 100644 lab3/dependencies/tesse_ros_bridge/launch/record_traj.launch
     create mode 100644 lab3/dependencies/tesse_ros_bridge/launch/tesse_bridge.launch
     create mode 100644 lab3/dependencies/tesse_ros_bridge/launch/tesse_quadrotor_bridge.launch
     create mode 100644 lab3/dependencies/tesse_ros_bridge/msg/CollisionStats.msg
     create mode 100644 lab3/dependencies/tesse_ros_bridge/package.xml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/params/camera_params.yaml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/params/lidar_params.yaml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/params/map_tfs.yaml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/params/noise_model.yaml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/params/object_spawn_params.yaml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/params/tesse_agent_params.yaml
     create mode 100644 lab3/dependencies/tesse_ros_bridge/setup.py
     create mode 100644 lab3/dependencies/tesse_ros_bridge/src/key_teleop/LICENSE
     create mode 100644 lab3/dependencies/tesse_ros_bridge/src/key_teleop/key_teleop.py
     create mode 100644 lab3/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/__init__.py
     create mode 100644 lab3/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/noise_simulator.py
     create mode 100755 lab3/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/quadrotor_control_interface.py
     create mode 100755 lab3/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/tesse_ros_node.py
     create mode 100644 lab3/dependencies/tesse_ros_bridge/src/tesse_ros_bridge/utils.py
     create mode 100644 lab3/dependencies/tesse_ros_bridge/srv/ObjectSpawnRequestService.srv
     create mode 100644 lab3/dependencies/tesse_ros_bridge/srv/RepositionRequestService.srv
     create mode 100644 lab3/dependencies/tesse_ros_bridge/srv/SceneRequestService.srv
     create mode 100644 lab3/report/build_noetic.txt
     create mode 100644 lab3/report/build_unity_noetic.txt
     create mode 100644 lab3/report/deliverable_2.pdf
     create mode 100644 lab3/report/deliverable_2.tex
     create mode 100644 lab3/report/numerical_validation.txt
     create mode 100644 lab3/report/offline_circle.csv
     create mode 100644 lab3/report/offline_circle_drag_compensated.csv
     create mode 100644 lab3/report/ros_flight.csv
     create mode 100644 lab3/report/ros_metrics.json
     create mode 100644 lab3/report/ros_runtime_topics.txt
     create mode 100644 lab3/report/ros_tracking.pdf
     create mode 100644 lab3/report/ros_tracking.png
     create mode 100644 lab3/report/tesse_qemu_4_startup.txt
     create mode 100644 lab3/report/tesse_qemu_8_startup.txt
     create mode 100644 lab3/report/trials/unity_circle_initial.csv
     create mode 100644 lab3/report/trials/unity_circle_initial.json
     create mode 100644 lab3/report/trials/unity_circle_tuned.csv
     create mode 100644 lab3/report/trials/unity_circle_tuned.json
     create mode 100644 lab3/report/trials/unity_hover.csv
     create mode 100644 lab3/report/trials/unity_hover.json
     create mode 100644 lab3/report/unity_bag_info.txt
     create mode 100644 lab3/report/unity_flight.csv
     create mode 100644 lab3/report/unity_flight.json
     create mode 100644 lab3/report/unity_metrics.json
     create mode 100644 lab3/report/unity_runtime.txt
     create mode 100644 lab3/report/unity_startup.txt
     create mode 100644 lab3/report/unity_tracking.pdf
     create mode 100644 lab3/report/unity_tracking.png
     create mode 100644 lab3/report/validation.md
     create mode 100644 lab3/report/video/rviz_demo_frame.png
     create mode 100644 lab3/report/video/rviz_live.png
     create mode 100644 lab3/report/video/rviz_official_frame.png
     create mode 100644 lab3/report/video/rviz_official_metadata.json
     create mode 100644 lab3/report/video/rviz_official_tesse.mp4
     create mode 100644 lab3/report/video/rviz_official_tesse_full.mp4
     create mode 100644 lab3/report/video/rviz_rigid_body_demo.mp4
     create mode 100644 lab3/report/video/rviz_unity_trial.png
     create mode 100644 lab3/report/video/unity_startup.png
     create mode 100644 lab3/rviz_drone_flight.txt
     create mode 100755 lab3/scripts/analyze_unity.py
     create mode 100755 lab3/scripts/build_workspace.sh
     create mode 100755 lab3/scripts/monitor_unity.py
     create mode 100644 lab3/scripts/offline_flight.cpp
     create mode 100755 lab3/scripts/plot_flight.py
     create mode 100755 lab3/scripts/prepare_unity_arm64.sh
     create mode 100755 lab3/scripts/run_unity_flight.sh
     create mode 100755 lab3/scripts/start_unity_arm64.sh
     create mode 100755 lab3/scripts/validate_offline.sh
    ✓ • 0ms

## Activity

    $ git status --short; git log -1 --format='%h %s'
    6ad442c Complete VNAV Lab 3 geometric control and official TESSE flight
    ✓ • 0ms

## Assistant

已提交：`6ad442c`

提交信息：`Complete VNAV Lab 3 geometric control and official TESSE flight`

工作区干净，尚未 push。
