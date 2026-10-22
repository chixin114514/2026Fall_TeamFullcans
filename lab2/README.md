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
