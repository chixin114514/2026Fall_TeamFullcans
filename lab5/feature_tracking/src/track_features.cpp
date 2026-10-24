/*
 * @file track_features.cpp
 * @brief Track features from frame to frame.
 */

#include <stdio.h>
#include <iostream>
#include <memory>

#include <glog/logging.h>

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include "feature_tracker.h"
#include "sift_feature_tracker.h"
#include "surf_feature_tracker.h"
#include "orb_feature_tracker.h"
#include "fast_feature_tracker.h"
#include "lk_feature_tracker.h"

using namespace std;
using namespace cv::xfeatures2d;

/** imageCallback This function is called when a new image is published.
 * For the first part of the assignment (working with a pair of images), you
 * can ignore this function.
 * @brief Tracks features from frame to frame using images received via a ROS
 *  topic.
 */
void imageCallback(const sensor_msgs::ImageConstPtr &msg,
                   std::shared_ptr <FeatureTracker> feature_tracker) {
  try {
    // Convert ROS msg type to OpenCV image type.
    cv::Mat image = cv_bridge::toCvShare(msg, "bgr8")->image;

    // toCvShare does not own the pixels once msg is released, so keep a deep
    // copy as the previous frame. The first frame has nothing to match with.
    static cv::Mat prev_image;
    if (!prev_image.empty()) {
      feature_tracker->trackFeatures(image, prev_image);
    }
    prev_image = image.clone();
  } catch (cv_bridge::Exception &e) {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
}

/**
 * @brief Callback for LKtracker
 *  You may find this function helpful as LKFeatureTracker does not inherit from
 *  the FeatureTracker base clase
 */
void lkImageCallback(const sensor_msgs::ImageConstPtr &msg,
                     std::shared_ptr<LKFeatureTracker> lk_tracker) {
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // ~~~~ begin solution
  try {
    lk_tracker->trackFeatures(cv_bridge::toCvShare(msg, "bgr8")->image);
  } catch (cv_bridge::Exception &e) {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
  // ~~~~ end solution
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
}

/** You do not need to modify this function
 * @function retrieveImages
 * @brief Retrieves a pair of images using ROS params
 */
bool retrieveImages(const ros::NodeHandle &nh,
                    cv::Mat *img_1,
                    cv::Mat *img_2) {
  CHECK_NOTNULL(img_1);
  CHECK_NOTNULL(img_2);
  std::string img1_path;
  if (nh.getParam("img1_path", img1_path)) {
    ROS_INFO("Got param: %s", img1_path.c_str());
  } else {
    ROS_FATAL("Failed to get param 'img1_path'");
    return false;
  }

  std::string img2_path;
  if (nh.getParam("img2_path", img2_path)) {
    ROS_INFO("Got param: %s", img2_path.c_str());
  } else {
    ROS_FATAL("Failed to get param 'img2_path'");
    return false;
  }

  *img_1 = imread(img1_path, cv::IMREAD_GRAYSCALE);
  *img_2 = imread(img2_path, cv::IMREAD_GRAYSCALE);
  if (!img_1->data || !img_2->data) {
    ROS_FATAL(" --(!) Error reading images ");
    return false;
  }

  return true;
}

/**
 * @function main
 * @brief Entry point of the program
 */
int main(int argc,
         char **argv) {
  ros::init(argc, argv, "keypoint_trackers");
  ros::NodeHandle local_nh("~");

  int const mode = local_nh.param<int>("mode", 0);
  std::string const descriptor = local_nh.param<std::string>("descriptor", "");
  // Output options (empty = disabled), see FeatureTracker::setOutput.
  std::string const output_dir = local_nh.param<std::string>("output_dir", "");
  std::string const stats_csv = local_nh.param<std::string>("stats_csv", "");
  std::string const frames_dir = local_nh.param<std::string>("frames_dir", "");
  int const save_frame = local_nh.param<int>("save_frame", -1);
  bool const show = local_nh.param<bool>("show", true);

  std::shared_ptr<FeatureTracker> feature_tracker;
  std::shared_ptr<LKFeatureTracker> lk_tracker;
  if (descriptor == "SIFT") {
    ///////////////////// SIFT ///////////////////////////////////////////////////
    feature_tracker.reset(new SiftFeatureTracker(
        local_nh.param<int>("sift_nfeatures", 0),
        local_nh.param<double>("sift_contrast_threshold", 0.04)));
    // (TODO) Implement the functions in SiftFeatureTracker
  } else if (descriptor == "SURF") { // Try for different feature trackers!
    // /////////////////// SURF ///////////////////////////////////////////////////
    feature_tracker.reset(new SurfFeatureTracker(
        local_nh.param<double>("surf_hessian_threshold", 100.0)));
    // (TODO) Implement the functions in SurfFeatureTracker
  } else if (descriptor == "ORB") {
    ///////////////////// ORB ////////////////////////////////////////////////////
    feature_tracker.reset(new OrbFeatureTracker(
        local_nh.param<int>("orb_nfeatures", 500),
        local_nh.param<int>("orb_nlevels", 1)));
    // (TODO) Implement the functions in OrbFeatureTracker
  } else if (descriptor == "FAST") {
    ///////////////////// FAST ///////////////////////////////////////////////////
    feature_tracker.reset(new FastFeatureTracker(
        local_nh.param<int>("fast_threshold", 10)));
    // (TODO) Implement the functions in FastFeatureTracker
  } else if (descriptor == "LK") {
    ///////////////////// Lucas-Kanade ///////////////////////////////////////////////////
    lk_tracker.reset(new LKFeatureTracker());
    lk_tracker->setCornerParams(local_nh.param<int>("lk_max_corners", 500),
                                local_nh.param<double>("lk_quality_level", 0.01),
                                local_nh.param<double>("lk_min_distance", 10.0));
    lk_tracker->setOutput(output_dir, stats_csv, frames_dir, save_frame, show);
    // (TODO) Implement the functions in LKFeatureTracker
  } else {
    ROS_ERROR("Unknown descriptor %s", descriptor.c_str());
    return EXIT_FAILURE;
  }

  if (feature_tracker) {
    feature_tracker->setOutput(mode == 0, output_dir, stats_csv,
                               frames_dir, save_frame, show);
    feature_tracker->setRatioThreshold(local_nh.param<double>("ratio", 0.8));
    feature_tracker->setUseBruteForceMatcher(local_nh.param<bool>("bf_matcher", true));
  }

  if (mode == 0) { // Process images
    if (!feature_tracker) {
      ROS_ERROR("Cannot use descriptor \"%s\" for images", descriptor.c_str());
      return EXIT_FAILURE;
    }

    // Retrieve images using the path stored in ROS params.
    cv::Mat img_1, img_2;
    if (!retrieveImages(local_nh, &img_1, &img_2)) {
      ROS_ERROR("Failed to retrieve images");
      return EXIT_FAILURE;
    }
    feature_tracker->trackFeatures(img_1, img_2);
    // Optional extra runs, only to average the timing (figures are not
    // shown/saved again; the FLANN results can differ slightly per run).
    int const repeat = local_nh.param<int>("repeat", 1);
    if (repeat > 1) {
      feature_tracker->setOutput(false, "", "", "", -1, false);
      for (int i = 1; i < repeat && ros::ok(); ++i) {
        feature_tracker->trackFeatures(img_1, img_2);
      }
    }
  } else if (mode == 1) {
    ///////////////////// TODO ///////////////////////////////////////////////////
    ///
    /// Feel free to modify as needed for LK method!
    ///
    /// Try to use a video sequence and track features from frame to frame.
    /// Compute at the same time an average of the statistics mentioned in the
    /// handout.

    image_transport::ImageTransport it(local_nh);
    auto callback = [feature_tracker, lk_tracker, descriptor](const sensor_msgs::ImageConstPtr &msg) {
      if (descriptor == "LK") {
        lkImageCallback(msg, lk_tracker);
      } else {
        imageCallback(msg, feature_tracker);
      }
    };
    image_transport::Subscriber sub = it.subscribe("/images_topic", 1000, callback);
    ros::spin();
  } else {
    ROS_ERROR("Unrecognized mode argument");
    return EXIT_FAILURE;
  }

  if (feature_tracker) feature_tracker->printStats();
  if (lk_tracker) lk_tracker->printStats();

  return EXIT_SUCCESS;
}
