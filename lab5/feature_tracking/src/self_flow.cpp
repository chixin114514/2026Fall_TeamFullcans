/*
 * @file self_flow.cpp
 * Feel free to edit any part of this file!
 */
#include <memory>
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

#include <opencv2/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/video/tracking.hpp>

using namespace std;

// If non-empty, every visualization frame is written here (for the video).
static std::string frames_dir;
static bool show = true;

/** Color-code a dense flow field: hue = direction, value = magnitude
 *  (normalized by `max_magnitude` pixels, saturating above it). */
cv::Mat flowToColor(const cv::Mat &flow, float max_magnitude) {
  cv::Mat flow_xy[2], magnitude, angle;
  cv::split(flow, flow_xy);
  cv::cartToPolar(flow_xy[0], flow_xy[1], magnitude, angle, true);
  cv::Mat hsv_planes[3];
  hsv_planes[0] = angle * 0.5f;  // OpenCV 8-bit hue is in [0, 180)
  hsv_planes[1] = cv::Mat::ones(angle.size(), CV_32F) * 255.0f;
  hsv_planes[2] = cv::min(magnitude * (255.0f / max_magnitude), 255.0f);
  cv::Mat hsv, hsv8, bgr;
  cv::merge(hsv_planes, 3, hsv);
  hsv.convertTo(hsv8, CV_8UC3);
  cv::cvtColor(hsv8, bgr, cv::COLOR_HSV2BGR);
  return bgr;
}

/** imageCallback This function is called when a new image is published. */
void imageCallback(const sensor_msgs::ImageConstPtr &msg) {
  try {
    // Convert ROS msg type to OpenCV image type.
    cv::Mat image = cv_bridge::toCvShare(msg, "bgr8")->image;

    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    //  DELIVERABLE 8 | Optical Flow
    // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    //
    // LK tracker estimates the optical flow for sparse points in the image.
    // Alternatively, dense approaches try to estimate the optical flow for the whole image.
    // Try to calculate your own optical flow using Farneback’s algorithm (see OpenCV documentation).
    //
    // ~~~~ begin solution
    static cv::Mat prev_gray;
    static unsigned int frame_id = 0;
    cv::Mat gray;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
    if (prev_gray.empty()) {
      prev_gray = gray;
      return;
    }

    // 3-level pyramid (scale 0.5), 15x15 averaging window, 3 iterations,
    // polynomial expansion on 5x5 neighbourhoods with sigma 1.2.
    cv::Mat flow;
    cv::calcOpticalFlowFarneback(prev_gray, gray, flow, 0.5, 3, 15, 3, 5, 1.2, 0);

    // Left: image with a sparse grid of flow arrows; right: dense color code.
    cv::Mat arrows = image.clone();
    static constexpr int kStep = 16;
    for (int y = kStep / 2; y < flow.rows; y += kStep) {
      for (int x = kStep / 2; x < flow.cols; x += kStep) {
        const cv::Point2f f = flow.at<cv::Point2f>(y, x);
        const cv::Point p(x, y);
        const cv::Point q(cvRound(x + 2.0f * f.x), cvRound(y + 2.0f * f.y));
        cv::line(arrows, p, q, cv::Scalar(0, 255, 0), 1, cv::LINE_AA);
        cv::circle(arrows, p, 1, cv::Scalar(0, 255, 0), -1);
      }
    }
    cv::Mat vis;
    cv::hconcat(arrows, flowToColor(flow, 10.0f), vis);

    if (!frames_dir.empty()) {
      char name[64];
      std::snprintf(name, sizeof(name), "/frame_%06u.png", frame_id);
      cv::imwrite(frames_dir + name, vis);
    }
    ++frame_id;
    if (show) {
      cv::imshow("view", vis);
      cv::waitKey(1);
    }
    prev_gray = gray;
    // ~~~~ end solution

  } catch (cv_bridge::Exception &e) {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
}

/**
 * @function main
 * @brief Main function
 */
int main(int argc, char **argv) {
  ros::init(argc, argv, "optical_flow");
  ros::NodeHandle local_nh("~");
  frames_dir = local_nh.param<std::string>("frames_dir", "");
  show = local_nh.param<bool>("show", true);

  if (show) cv::namedWindow("view", cv::WINDOW_NORMAL);
  image_transport::ImageTransport it(local_nh);
  image_transport::Subscriber sub = it.subscribe("/images_topic", 2000, imageCallback);

  ros::spin();
  if (show) cv::destroyWindow("view");
  return EXIT_SUCCESS;
}
