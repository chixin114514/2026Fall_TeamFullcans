#include <ros/ros.h>
#include <geometry_msgs/TransformStamped.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_ros/transform_broadcaster.h>

#include <cmath>

class FramesPublisherNode {
 private:
  ros::NodeHandle nh;
  ros::Time startup_time;
  ros::Timer heartbeat;
  tf2_ros::TransformBroadcaster transform_broadcaster;

 public:
  FramesPublisherNode() {
    startup_time = ros::Time::now();
    heartbeat = nh.createTimer(
        ros::Duration(0.02), &FramesPublisherNode::onPublish, this);
  }

  void onPublish(const ros::TimerEvent&) {
    const double time = (ros::Time::now() - startup_time).toSec();
    const ros::Time stamp = ros::Time::now();

    geometry_msgs::TransformStamped world_to_av1;
    geometry_msgs::TransformStamped world_to_av2;

    world_to_av1.header.stamp = stamp;
    world_to_av1.header.frame_id = "world";
    world_to_av1.child_frame_id = "av1";
    world_to_av1.transform.translation.x = std::cos(time);
    world_to_av1.transform.translation.y = std::sin(time);
    world_to_av1.transform.translation.z = 0.0;

    // yaw = time makes y_1 tangent to [cos(t), sin(t), 0].
    // roll = pitch = 0 keeps z_1 parallel to z_world.
    tf2::Quaternion av1_orientation;
    av1_orientation.setRPY(0.0, 0.0, time);
    world_to_av1.transform.rotation.x = av1_orientation.x();
    world_to_av1.transform.rotation.y = av1_orientation.y();
    world_to_av1.transform.rotation.z = av1_orientation.z();
    world_to_av1.transform.rotation.w = av1_orientation.w();

    world_to_av2.header.stamp = stamp;
    world_to_av2.header.frame_id = "world";
    world_to_av2.child_frame_id = "av2";
    world_to_av2.transform.translation.x = std::sin(time);
    world_to_av2.transform.translation.y = 0.0;
    world_to_av2.transform.translation.z = std::cos(2.0 * time);
    // AV2 has no rotation relative to the world frame.
    world_to_av2.transform.rotation.w = 1.0;

    transform_broadcaster.sendTransform(world_to_av1);
    transform_broadcaster.sendTransform(world_to_av2);
  }
};

int main(int argc, char** argv) {
  ros::init(argc, argv, "frames_publisher_node");
  FramesPublisherNode node;
  ros::spin();
  return 0;
}
