#include <geometry_msgs/Point.h>
#include <geometry_msgs/TransformStamped.h>
#include <ros/ros.h>
#include <tf2_ros/transform_listener.h>
#include <visualization_msgs/MarkerArray.h>

#include <list>
#include <string>

class PlotsPublisherNode {
 private:
  ros::Time startup_time;
  ros::Timer heartbeat;
  ros::NodeHandle nh;
  ros::Publisher markers_pub;
  // Buffer must be constructed before the listener that uses it.
  tf2_ros::Buffer tf_buffer;
  tf2_ros::TransformListener tf_listener;
  int num_trails;

  class TrajTrail {
   private:
    PlotsPublisherNode* parent;
    std::list<geometry_msgs::Point> poses;
    std::string ref_frame;
    std::string dest_frame;
    std::size_t buffer_size;
    visualization_msgs::Marker marker_out;

    void update() {
      geometry_msgs::TransformStamped transform;
      try {
        // lookupTransform(target, source, time) returns the source pose in
        // the target frame. This is exactly the requested dest-in-ref pose.
        transform = parent->tf_buffer.lookupTransform(
            ref_frame, dest_frame, ros::Time(0));

        while (poses.size() >= buffer_size) {
          poses.pop_front();
        }

        geometry_msgs::Point point;
        point.x = transform.transform.translation.x;
        point.y = transform.transform.translation.y;
        point.z = transform.transform.translation.z;
        poses.push_back(point);
      } catch (const tf2::TransformException& ex) {
        ROS_WARN_THROTTLE(1.0, "Transform lookup failed: %s", ex.what());
      }
    }

   public:
    TrajTrail() : parent(nullptr), buffer_size(1) {}

    TrajTrail(PlotsPublisherNode* parent_, const std::string& ref_frame_,
              const std::string& dest_frame_, std::size_t buffer_size_ = 160)
        : parent(parent_),
          ref_frame(ref_frame_),
          dest_frame(dest_frame_),
          buffer_size(buffer_size_) {
      if (buffer_size == 0) {
        ROS_ERROR("Invalid trail buffer size; defaulting to 10");
        buffer_size = 10;
      }

      marker_out.header.frame_id = ref_frame;
      marker_out.ns = "trails";
      marker_out.id = parent->num_trails++;
      marker_out.type = visualization_msgs::Marker::LINE_STRIP;
      marker_out.action = visualization_msgs::Marker::ADD;
      marker_out.pose.orientation.w = 1.0;
      marker_out.color.a = 0.8;
      marker_out.scale.x = 0.02;
      marker_out.lifetime = ros::Duration(1.0);
    }

    void setColor(float red, float green, float blue) {
      marker_out.color.r = red;
      marker_out.color.g = green;
      marker_out.color.b = blue;
    }

    void setNamespace(const std::string& name_space) {
      marker_out.ns = name_space;
    }

    void setDashed() { marker_out.type = visualization_msgs::Marker::LINE_LIST; }

    visualization_msgs::Marker getMarker() {
      update();
      marker_out.header.stamp = ros::Time::now();
      marker_out.points.clear();
      for (const auto& pose : poses) {
        marker_out.points.push_back(pose);
      }

      // LINE_LIST consumes points in pairs. Drop the last point if necessary.
      if (marker_out.type == visualization_msgs::Marker::LINE_LIST &&
          marker_out.points.size() % 2 != 0) {
        marker_out.points.pop_back();
      }
      return marker_out;
    }
  };

  TrajTrail av1trail;
  TrajTrail av2trail;
  TrajTrail av2trail_relative;

 public:
  PlotsPublisherNode()
      : tf_listener(tf_buffer), num_trails(0) {
    startup_time = ros::Time::now();
    markers_pub = nh.advertise<visualization_msgs::MarkerArray>("visuals", 1);
    heartbeat = nh.createTimer(
        ros::Duration(0.02), &PlotsPublisherNode::onPublish, this);

    av1trail = TrajTrail(this, "world", "av1", 300);
    av1trail.setColor(0.25f, 0.52f, 1.0f);
    av1trail.setNamespace("Trail av1-world");

    av2trail = TrajTrail(this, "world", "av2", 300);
    av2trail.setColor(0.8f, 0.4f, 0.26f);
    av2trail.setNamespace("Trail av2-world");

    av2trail_relative = TrajTrail(this, "av1", "av2", 160);
    av2trail_relative.setDashed();
    av2trail_relative.setColor(0.8f, 0.4f, 0.26f);
    av2trail_relative.setNamespace("Trail av2-av1");

    ROS_INFO("Waiting for av1 and av2 transforms to be broadcast...");
    ros::Rate wait_rate(100.0);
    while (ros::ok()) {
      const bool av1_present =
          tf_buffer.canTransform("av1", "world", ros::Time(0));
      const bool av2_present =
          tf_buffer.canTransform("av2", "world", ros::Time(0));
      if (av1_present && av2_present) {
        ROS_INFO("Necessary frames are present, starting visualization.");
        break;
      }
      wait_rate.sleep();
    }
  }

  void onPublish(const ros::TimerEvent&) {
    visualization_msgs::MarkerArray visuals;
    visuals.markers.resize(2);

    visualization_msgs::Marker& av1 = visuals.markers[0];
    av1.header.frame_id = "av1";
    av1.ns = "AVs";
    av1.id = 0;
    av1.header.stamp = ros::Time::now();
    av1.type = visualization_msgs::Marker::MESH_RESOURCE;
    av1.mesh_resource = "package://two_drones_pkg/mesh/quadrotor.dae";
    av1.action = visualization_msgs::Marker::ADD;
    av1.pose.orientation.w = 1.0;
    av1.scale.x = av1.scale.y = av1.scale.z = 1.0;
    av1.color.r = 0.25;
    av1.color.g = 0.52;
    av1.color.b = 1.0;
    av1.color.a = 1.0;
    av1.lifetime = ros::Duration(1.0);

    visualization_msgs::Marker& av2 = visuals.markers[1];
    av2 = av1;
    av2.header.frame_id = "av2";
    av2.id = 1;
    av2.color.r = 0.8;
    av2.color.g = 0.4;
    av2.color.b = 0.26;

    visuals.markers.push_back(av1trail.getMarker());
    visuals.markers.push_back(av2trail.getMarker());
    visuals.markers.push_back(av2trail_relative.getMarker());
    markers_pub.publish(visuals);
  }
};

int main(int argc, char** argv) {
  ros::init(argc, argv, "plots_publisher_node");
  PlotsPublisherNode node;
  ros::spin();
  return 0;
}
