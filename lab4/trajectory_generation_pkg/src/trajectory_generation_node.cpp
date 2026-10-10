#include <geometry_msgs/PoseArray.h>
#include <nav_msgs/Odometry.h>
#include <ros/ros.h>
#include <trajectory_msgs/MultiDOFJointTrajectoryPoint.h>
#include <mav_trajectory_generation/polynomial_optimization_linear.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_datatypes.h>
#include <algorithm>
#include <cmath>
#include <stdexcept>

class WaypointFollower {
  ros::Subscriber current_state_sub_, vertices_sub_;
  ros::Publisher desired_pub_;
  ros::Timer timer_;
  tf::TransformBroadcaster broadcaster_;
  Eigen::Vector3d x_ = Eigen::Vector3d::Zero();
  double yaw_ = 0.0;
  bool have_state_ = false;
  ros::Time state_received_, start_time_, last_publish_;
  geometry_msgs::PoseArray pending_;
  mav_trajectory_generation::Trajectory trajectory_, yaw_trajectory_;
  double v_max_, a_max_, time_scale_, min_segment_time_, state_timeout_;

  // Part 1.1: record the world position and heading before planning.
  void onCurrentState(const nav_msgs::Odometry& msg) {
    const auto& p = msg.pose.pose.position;
    tf::Quaternion q;
    tf::quaternionMsgToTF(msg.pose.pose.orientation, q);
    Eigen::Vector3d next(p.x, p.y, p.z);
    if (!next.allFinite() || !std::isfinite(q.length2()) || q.length2() < 1e-12) return;
    x_ = next;
    yaw_ = tf::getYaw(q.normalized());
    have_state_ = true;
    state_received_ = ros::Time::now();
    if (trajectory_.empty() && !pending_.poses.empty()) generate(pending_);
  }

  void onWaypoints(const geometry_msgs::PoseArray& msg) {
    if (!trajectory_.empty()) return;  // The publisher repeats this message at 5 Hz.
    if (msg.poses.empty()) {
      ROS_WARN("Empty waypoint list ignored");
      return;
    }
    for (const auto& pose : msg.poses) {
      const auto& p = pose.position;
      tf::Quaternion q;
      tf::quaternionMsgToTF(pose.orientation, q);
      if (!std::isfinite(p.x) || !std::isfinite(p.y) || !std::isfinite(p.z) ||
          !std::isfinite(q.length2()) || q.length2() < 1e-12) {
        ROS_ERROR("Invalid waypoint list ignored");
        return;
      }
    }
    pending_ = msg;
    if (have_state_ && (ros::Time::now() - state_received_).toSec() <= state_timeout_)
      generate(pending_);
  }

  // Part 1.2: optimize xyz and unwrapped yaw with identical segment times.
  void generate(const geometry_msgs::PoseArray& msg) {
    using namespace mav_trajectory_generation;
    using namespace mav_trajectory_generation::derivative_order;
    const int D = 3, N = 10;
    Vertex::Vector vertices, yaw_vertices;
    Vertex start(D), start_yaw(1);
    start.makeStartOrEnd(x_, SNAP);
    start_yaw.makeStartOrEnd(yaw_, SNAP);
    vertices.push_back(start);
    yaw_vertices.push_back(start_yaw);
    double last_yaw = yaw_;
    for (size_t i = 0; i < msg.poses.size(); ++i) {
      const auto& pose = msg.poses[i];
      const Eigen::Vector3d position(pose.position.x, pose.position.y, pose.position.z);
      Vertex vertex(D), yaw_vertex(1);
      tf::Quaternion q;
      tf::quaternionMsgToTF(pose.orientation, q);
      const double raw_yaw = tf::getYaw(q.normalized());
      const double yaw = last_yaw + std::atan2(std::sin(raw_yaw - last_yaw),
                                              std::cos(raw_yaw - last_yaw));
      if (i + 1 == msg.poses.size()) {
        vertex.makeStartOrEnd(position, SNAP);
        yaw_vertex.makeStartOrEnd(yaw, SNAP);
      } else {
        vertex.addConstraint(POSITION, position);
        yaw_vertex.addConstraint(ORIENTATION, yaw);
      }
      vertices.push_back(vertex);
      yaw_vertices.push_back(yaw_vertex);
      last_yaw = yaw;
    }
    auto times = estimateSegmentTimes(vertices, v_max_, a_max_);
    for (double& time : times) time = std::max(min_segment_time_, time * time_scale_);
    PolynomialOptimization<N> opt(D), yaw_opt(1);
    if (!opt.setupFromVertices(vertices, times, SNAP) || !opt.solveLinear() ||
        !yaw_opt.setupFromVertices(yaw_vertices, times, SNAP) || !yaw_opt.solveLinear()) {
      ROS_ERROR("Trajectory optimization failed");
      return;
    }
    opt.getTrajectory(&trajectory_);
    yaw_opt.getTrajectory(&yaw_trajectory_);
    start_time_ = ros::Time::now();
    ROS_INFO("Generated trajectory: %zu gates, %.3f s", msg.poses.size(), trajectory_.getMaxTime());
  }

  // Part 1.3: sample elapsed ROS time and keep holding the final rest pose.
  void publish(const ros::TimerEvent&) {
    if (trajectory_.empty()) return;
    const auto now = ros::Time::now();
    if (now == last_publish_) return;
    last_publish_ = now;
    using namespace mav_trajectory_generation::derivative_order;
    const double t = std::max(0.0, std::min((ros::Time::now() - start_time_).toSec(),
                                          trajectory_.getMaxTime()));
    const Eigen::Vector3d p = trajectory_.evaluate(t, POSITION);
    const Eigen::Vector3d v = trajectory_.evaluate(t, VELOCITY);
    const Eigen::Vector3d a = trajectory_.evaluate(t, ACCELERATION);
    const double yaw = yaw_trajectory_.evaluate(t, ORIENTATION)(0);
    trajectory_msgs::MultiDOFJointTrajectoryPoint point;
    point.time_from_start = ros::Duration(t);
    point.transforms.resize(1);
    point.velocities.resize(1);
    point.accelerations.resize(1);
    auto& transform = point.transforms[0];
    transform.translation.x = p.x(); transform.translation.y = p.y(); transform.translation.z = p.z();
    transform.rotation = tf::createQuaternionMsgFromYaw(yaw);
    point.velocities[0].linear.x = v.x();
    point.velocities[0].linear.y = v.y();
    point.velocities[0].linear.z = v.z();
    point.velocities[0].angular.z = yaw_trajectory_.evaluate(t, VELOCITY)(0);
    point.accelerations[0].linear.x = a.x();
    point.accelerations[0].linear.y = a.y();
    point.accelerations[0].linear.z = a.z();
    point.accelerations[0].angular.z = yaw_trajectory_.evaluate(t, ACCELERATION)(0);
    desired_pub_.publish(point);
    tf::Transform tf_pose;
    tf::transformMsgToTF(transform, tf_pose);
    broadcaster_.sendTransform(tf::StampedTransform(tf_pose, ros::Time::now(), "world", "desired_pose"));
    ROS_INFO_THROTTLE(2.0, "Trajectory %.1f%%", 100.0 * t / trajectory_.getMaxTime());
  }
 public:
  explicit WaypointFollower(ros::NodeHandle& nh) {
    ros::NodeHandle pnh("~");
    double hz;
    pnh.param("v_max", v_max_, 3.0);
    pnh.param("a_max", a_max_, 2.0);
    pnh.param("time_scale", time_scale_, 1.0);
    pnh.param("min_segment_time", min_segment_time_, 0.5);
    pnh.param("state_timeout", state_timeout_, 0.5);
    pnh.param("publish_rate", hz, 100.0);
    for (double value : {v_max_, a_max_, time_scale_, min_segment_time_, state_timeout_, hz})
      if (!std::isfinite(value) || value <= 0) throw std::invalid_argument("Trajectory parameters must be positive and finite");
    current_state_sub_ = nh.subscribe("current_state", 1, &WaypointFollower::onCurrentState, this);
    vertices_sub_ = nh.subscribe("desired_traj_vertices", 1, &WaypointFollower::onWaypoints, this);
    desired_pub_ = nh.advertise<trajectory_msgs::MultiDOFJointTrajectoryPoint>("desired_state", 1);
    timer_ = nh.createTimer(ros::Duration(1.0 / hz), &WaypointFollower::publish, this);
  }
};
int main(int argc, char** argv) {
  ros::init(argc, argv, "trajectory_generation_node");
  ros::NodeHandle nh;
  try { WaypointFollower follower(nh); ros::spin(); }
  catch (const std::exception& e) { ROS_FATAL("%s", e.what()); return 1; }
}
