/*
 * @file pose_estimation.cpp
 * @brief Estimates the pose from frame to frame.
 */


#include <stdio.h>
#include <iostream>
#include <fstream>
#include <memory>
#include <deque>
#include <iomanip>
#include <limits>
#include <chrono>
#include <cmath>

#include <gflags/gflags.h>
#include <glog/logging.h>

#include <ros/ros.h>
#include <message_filters/subscriber.h>
#include <message_filters/synchronizer.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <image_transport/image_transport.h>
#include <image_transport/subscriber_filter.h>
#include <sensor_msgs/image_encodings.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/CameraInfo.h>
#include <geometry_msgs/PoseStamped.h>
#include <tf/tf.h>
#include <tf/transform_datatypes.h>
#include <tf_conversions/tf_eigen.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>

#include <Eigen/Eigen>

#include <opencv2/core.hpp>
#include <opencv2/calib3d.hpp>
#include <opencv2/core/eigen.hpp>

// OpenGV
#include <opengv/sac/Ransac.hpp>
#include <opengv/sac_problems/relative_pose/TranslationOnlySacProblem.hpp>
#include <opengv/sac_problems/relative_pose/CentralRelativePoseSacProblem.hpp>
#include <opengv/sac_problems/point_cloud/PointCloudSacProblem.hpp>
#include <opengv/relative_pose/CentralRelativeAdapter.hpp>
#include <opengv/relative_pose/methods.hpp>
#include <opengv/point_cloud/PointCloudAdapter.hpp>
#include <opengv/point_cloud/methods.hpp>

#include "lab6_utils.h"
#include "pose_estimation.h"
#include "tracker_shim.h"

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  16.485 - Fall 2021  - Lab 6 coding assignment
// ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
//
//  In this code, we ask you to use the following methods for motion estimation:
//  - Nister's 5 point algorithm (2D-2D correspondences)
//  - Longuet-Higgins 8 point algorithm (2D-2D correspondences)
//  - OpenGV's 2 point algorithm (2D-2D correspondences, known rotation)
//  - Arun's 3 point algorithm (3D-3D correspondences)
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// These are Google Flags (also known as gflags).
// Have a look at the provided roslaunch to see how to modify them on the fly.
// Feel free to use ROS parameters, or command-line flags if you prefer.
DEFINE_bool(use_ransac, true, "Use Random Sample Consensus.");
DEFINE_bool(scale_translation, true, "Whether to scale estimated translation to match ground truth scale");
DEFINE_int32(pose_estimator, 0,
             "Pose estimation algorithm, valid values are:"
             "0 for OpengGV's 5-point algorithm."
             "1 for OpengGV's 8-point algorithm."
             "2 for OpengGV's 2-point algorithm."
             "3 for Arun's 3-point method.");
// Added flags (not in the stencil): RANSAC thresholds, logging and display.
DEFINE_double(ransac_px, 0.1,
              "2D-2D RANSAC inlier threshold, in pixels (converted to 1-cos(angle) with the focal length).");
DEFINE_double(ransac_3d_m, 0.01, "3D-3D RANSAC inlier threshold, in meters.");
DEFINE_int32(ransac_max_iter, 5000, "Maximum number of RANSAC iterations.");
DEFINE_bool(refine_inliers, true,
            "Re-estimate the RANSAC model on all its inliers (OpenGV's Ransac only "
            "returns the model of the best minimal sample).");
DEFINE_string(rpe_csv, "", "If non-empty, one row per frame pair with the RPE is written here.");
DEFINE_bool(show_matches, false, "Show lab5's inlier/outlier match window.");
DEFINE_bool(latest_only, false,
            "Live display: when processing falls behind the bag, skip stale frames and "
            "process the newest one (default: every frame pair is evaluated).");

using namespace std;
namespace enc = sensor_msgs::image_encodings;

// Global definitions.
// Mono OpenGV RANSAC problems and adapters.
// See OpenGV examples on how to use:
// https://laurentkneip.github.io/opengv/page_how_to_use.html
using RansacProblem = opengv::sac_problems::relative_pose::CentralRelativePoseSacProblem;
using Adapter = opengv::relative_pose::CentralRelativeAdapter;
using RansacProblemGivenRot = opengv::sac_problems::relative_pose::TranslationOnlySacProblem;
using AdapterGivenRot = opengv::relative_pose::CentralRelativeAdapter;
using Adapter3D = opengv::point_cloud::PointCloudAdapter;
using RansacProblem3D = opengv::sac_problems::point_cloud::PointCloudSacProblem;

// Global variables. As a general coding style, global variables are followed
// by a trailing underscore (Google coding style).
std::unique_ptr<TrackerWrapper> feature_tracker_;
ros::Publisher pub_pose_estimation_, pub_pose_gt_;
ros::Subscriber sub_cinfo_;
geometry_msgs::PoseStamped curr_pose_;
geometry_msgs::PoseStamped prev_pose_;

// Ground-truth camera poses received so far, used to look up the pose at the
// exact image timestamp (the latest odometry message can be several ms off,
// and later than the image if the callback is slower than the bag).
std::deque<geometry_msgs::PoseStamped> gt_buffer_;

// Per-frame information written next to the RPE (see evaluateRPE).
struct FrameLog {
  int frame = 0;
  double stamp = 0.0;
  int n_matches = 0;
  int n_inliers = 0;
  bool valid = false;
  double time_ms = 0.0;
};
FrameLog frame_log_;

// Synchronized RGB-D pairs waiting for ground truth newer than their stamp.
std::deque<std::pair<sensor_msgs::ImageConstPtr, sensor_msgs::ImageConstPtr>> pending_frames_;
std::unique_ptr<std::ofstream> rpe_csv_;

// See definition of CameraParams in lab6_utils.h
// We declare these global variables, and we assign values to them later in the main function
CameraParams camera_params_;
cv::Mat R_camera_body, t_camera_body;
cv::Mat T_camera_body;
geometry_msgs::Pose pose_camera_body;
tf::Transform transform_camera_body;


void poseCallbackTesse(const nav_msgs::Odometry::ConstPtr& msg){
  // This function takes a message from the simulator of type nav_msgs::Odometry,
  // and use it to update the ground-truth pose of the drone's camera frame.
  // 
  // Note that the simulator provides the pose of the drone's body frame,
  // Therefore, we need to use the fixed transformation from the drone's camera
  // to the drone's camera to obtain the pose of the drone's camera frame.
  // 
  // In math, we want to get T_{camera}^W, but the msg provides T_{body}^W,
  // so we should do T_{camera}^W = T_{body}^W * T_{camera}^{body} to get the 
  // drone's camera pose.

  // This is T_{body}^W
  curr_pose_.pose = msg->pose.pose;

  // Convert pose message to tf::Transform
  tf::Transform current_pose;
  tf::poseMsgToTF(curr_pose_.pose, current_pose);

  // Perform the coordinate transform T_{camera}^W = T_{body}^W * T_{camera}^{body}
  // and convert to pose message
  tf::poseTFToMsg(current_pose * transform_camera_body, curr_pose_.pose);

  // Buffer the camera pose; cameraCallback interpolates it at each image stamp and
  // publishes it on /gt_camera_pose together with the estimate, so the two RViz
  // arrows always refer to the same frame even when processing lags behind the bag.
  curr_pose_.header.frame_id = "world";
  curr_pose_.header.stamp = msg->header.stamp;

  gt_buffer_.push_back(curr_pose_);
  while (gt_buffer_.size() > 100000) gt_buffer_.pop_front();  // > 8 min at 200 Hz (~25 MB)
}

/**
 * @brief      Ground-truth camera pose at time `stamp`, interpolated between the two
 *             closest odometry messages (linear for the position, slerp for the rotation).
 * @return     false if `stamp` is not covered by the buffered odometry.
 */
bool lookupGtPose(const ros::Time& stamp, geometry_msgs::PoseStamped* out) {
  if (gt_buffer_.size() < 2) return false;
  for (size_t i = 1; i < gt_buffer_.size(); i++) {
    const auto& a = gt_buffer_[i - 1];
    const auto& b = gt_buffer_[i];
    if (b.header.stamp < stamp) continue;
    if (a.header.stamp > stamp) return false;  // older than the buffer
    const double dt = (b.header.stamp - a.header.stamp).toSec();
    const double alpha = dt > 0 ? (stamp - a.header.stamp).toSec() / dt : 0.0;
    tf::Transform ta, tb;
    tf::poseMsgToTF(a.pose, ta);
    tf::poseMsgToTF(b.pose, tb);
    tf::Transform t(ta.getRotation().slerp(tb.getRotation(), alpha),
                    ta.getOrigin().lerp(tb.getOrigin(), alpha));
    tf::poseTFToMsg(t, out->pose);
    out->header.stamp = stamp;
    out->header.frame_id = "world";
    return true;
  }
  return false;  // newer than the last odometry message
}

/**
 * @brief      Compute 3D bearing vectors from pixel points
 *
 * @param[in]  pts1              Feature correspondences from camera 1
 * @param[in]  pts2              Feature correspondences from camera 2
 * @param      bearing_vector_1  Bearing vector to pts1 in camera 1
 * @param      bearing_vector_2  Bearing vector to pts2 in camera 2
 */
void calibrateKeypoints(const std::vector<cv::Point2f>& pts1,
                        const std::vector<cv::Point2f>& pts2,
                        opengv::bearingVectors_t& bearing_vector_1,
                        opengv::bearingVectors_t& bearing_vector_2) {
    //
    // For this part, we perform:
    //   1. Use the function cv::undistortPoints to rectify the keypoints.
    //   2. Return the bearing vectors for each keypoint.
    //

    std::vector<cv::Point2f> points1_rect, points2_rect;
    cv::undistortPoints(pts1, points1_rect, camera_params_.K, camera_params_.D);
    cv::undistortPoints(pts2, points2_rect, camera_params_.K, camera_params_.D);

    for (auto const& pt: points1_rect){
      opengv::bearingVector_t bearing_vector(pt.x, pt.y, 1); // focal length is 1 after undistortion
      bearing_vector_1.push_back(bearing_vector.normalized());
    }

    for (auto const& pt: points2_rect){
      opengv::bearingVector_t bearing_vector(pt.x, pt.y, 1); // focal length is 1 after undistortion
      bearing_vector_2.push_back(bearing_vector.normalized());
    }
}

/**
 * @brief      Update pose estimate using previous absolue pose and estimated relative pose
 *
 * @param[in]  prev_pose         ground-truth absolute pose of previous frame
 * @param[in]  relative_pose     estimated relative pose between current frame and previous frame
 * @param      output            estimated absolute pose of current frame
 */
void updatePoseEstimate(geometry_msgs::Pose const& prev_pose, geometry_msgs::Pose const& relative_pose, geometry_msgs::Pose& output) {
  tf::Transform prev, relative;
  tf::poseMsgToTF(prev_pose, prev);
  tf::poseMsgToTF(relative_pose, relative);
  tf::poseTFToMsg(prev*relative, output);
}

/**
 * @brief      Given an estimated translation up to scale, return an absolute translation with correct scale using ground truth
 *
 * @param[in]  prev_pose         ground-truth absolute pose of previous frame
 * @param[in]  curr_pose         ground-truth absolute pose of current frame
 * @param      translation       estimated translation between current frame and previous frame
 */
void scaleTranslation(geometry_msgs::Point& translation, geometry_msgs::PoseStamped const& prev_pose, geometry_msgs::PoseStamped const& curr_pose) {
  if (!FLAGS_scale_translation) return;
  tf::Transform prev, curr;
  tf::poseMsgToTF(prev_pose.pose, prev);
  tf::poseMsgToTF(curr_pose.pose, curr);
  tf::Transform const relative_pose = prev.inverseTimes(curr);
  double const translation_scale = relative_pose.getOrigin().length();
  if (isnan(translation_scale) || isinf(translation_scale)) {
    ROS_WARN("Failed to scale translation");
    return;
  }
  double const old_scale = sqrt(pow(translation.x, 2) + pow(translation.y, 2) + pow(translation.z, 2));
  translation.x *= translation_scale / old_scale;
  translation.y *= translation_scale / old_scale;
  translation.z *= translation_scale / old_scale;
}


/**
 * @brief      Least-squares translation direction with known rotation (Deliverable 2):
 *             each correspondence gives a_i^T t = 0 with a_i = R f2_i x f1_i, so t is
 *             the right singular vector of [a_i^T] with the smallest singular value.
 *             The rotation is kept fixed (OpenGV's TranslationOnlySacProblem refit
 *             would re-optimize it too).
 * @param[in]  model    RANSAC model [R | t], used for R and for the sign of t
 */
opengv::transformation_t refineTranslationGivenRotation(const Adapter& adapter,
                                                        const std::vector<int>& inliers,
                                                        const opengv::transformation_t& model) {
  const Eigen::Matrix3d R = model.block<3, 3>(0, 0);
  Eigen::MatrixXd A(inliers.size(), 3);
  for (size_t k = 0; k < inliers.size(); k++) {
    const Eigen::Vector3d a = (R * adapter.getBearingVector2(inliers[k])).cross(
        adapter.getBearingVector1(inliers[k]));
    A.row(k) = a.normalized().transpose();  // residual = sine of the angle to the epipolar plane
  }
  Eigen::JacobiSVD<Eigen::MatrixXd> svd(A, Eigen::ComputeFullV);
  Eigen::Vector3d t = svd.matrixV().col(2);
  if (t.dot(model.col(3)) < 0) t = -t;  // same cheirality as the RANSAC model
  opengv::transformation_t refined = model;
  refined.col(3) = t;
  return refined;
}

/** @brief     (TODO) Compute Relative Pose Error (RPE) in translation and rotation.
    @param[in] gt_t_prev_frame ground-truth transform for previous frame.
    @param[in] gt_t_curr_frame ground-truth transform for current frame.
    @param[in] est_t_prev_frame estimated transform for previous frame.
    @param[in] est_t_curr_frame estimated transform for current frame.
*/
void evaluateRPE(const tf::Transform& gt_t_prev_frame,
                 const tf::Transform& gt_t_curr_frame,
                 const tf::Transform& est_t_prev_frame,
                 const tf::Transform& est_t_curr_frame) {

  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  //  DELIVERABLE 4 (Part 2) | Evaluate Relative Pose Error (RPE)
  // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
  //
  // For this part, you will need to:
  //   1. Follow the equations given in the README to compute the relative pose
  //     error at each time frame
  //   2. Print the error in translation and rotation.
  //   3. For plotting the statics, you might want to log the errors in a .txt or .csv file
  //
  // Hint: You might find tf::vectorTFToEigen and tf::matrixTFToEigen helpful

  tf::Transform const est_relative_pose = est_t_prev_frame.inverseTimes(est_t_curr_frame);
  tf::Transform const gt_relative_pose = gt_t_prev_frame.inverseTimes(gt_t_curr_frame);

  // ***************************** begin solution *****************************
  Eigen::Vector3d t_gt, t_est;
  Eigen::Matrix3d R_gt, R_est;
  tf::vectorTFToEigen(gt_relative_pose.getOrigin(), t_gt);
  tf::vectorTFToEigen(est_relative_pose.getOrigin(), t_est);
  tf::matrixTFToEigen(gt_relative_pose.getBasis(), R_gt);
  tf::matrixTFToEigen(est_relative_pose.getBasis(), R_est);

  // Rotation: chordal distance ||R_gt - R_est||_F, and the equivalent angle
  // (||R1 - R2||_F = 2 sqrt(2) sin(theta / 2)).
  const double rot_chordal = (R_gt - R_est).norm();
  const double rot_deg = 2.0 * std::asin(std::min(1.0, rot_chordal / (2.0 * std::sqrt(2.0)))) * 180.0 / M_PI;

  // Translation: 2D-2D methods only give the direction, so both translations are
  // scaled to unit norm (error in [0, 2]). The metric error is kept as well; it is
  // the meaningful one for Arun's method.
  const double gt_norm = t_gt.norm();
  const double est_norm = t_est.norm();
  const double tran_unit = (gt_norm > 1e-9 && est_norm > 1e-9)
      ? (t_gt / gt_norm - t_est / est_norm).norm()
      : std::numeric_limits<double>::quiet_NaN();
  const double tran_metric = (t_gt - t_est).norm();

  ROS_INFO("RPE frame %d: rot %.4f (%.3f deg), tran(unit) %.4f, tran %.5f m, inliers %d/%d",
           frame_log_.frame, rot_chordal, rot_deg, tran_unit, tran_metric,
           frame_log_.n_inliers, frame_log_.n_matches);

  if (rpe_csv_) {
    *rpe_csv_ << frame_log_.frame << "," << std::fixed << std::setprecision(6) << frame_log_.stamp << ","
              << std::defaultfloat << std::setprecision(9)
              << frame_log_.n_matches << "," << frame_log_.n_inliers << ","
              << frame_log_.valid << "," << frame_log_.time_ms << ","
              << gt_norm << "," << est_norm << ","
              << rot_chordal << "," << rot_deg << ","
              << tran_unit << "," << tran_metric << ","
              << t_gt.x() << "," << t_gt.y() << "," << t_gt.z() << ","
              << t_est.x() << "," << t_est.y() << "," << t_est.z() << std::endl;
  }
  // ***************************** end solution *****************************

}

/** @brief (TODO) This function is called when a new image is published. This is
 *   where all the magic happens for this lab
 *  @param[in]  rgb_msg    RGB Camera message
 *  @param[in]  depth_msg  Depth Camera message
 */
void cameraCallback(const sensor_msgs::ImageConstPtr &rgb_msg, const sensor_msgs::ImageConstPtr &depth_msg) {
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  //  DELIVERABLE 4-5 | A Suite of Methods for Motion Estimation
  // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
  //
  // For this part, you will need to:
  //   1. (Deliverable 4) 2D-2D Correspondences
  //     - 5 point Nister (with RANSAC)
  //     - 8 point Longuet-Higgins (with RANSAC)
  //     - 2 point OpenGV (with RANSAC)
  //   2. (Deliverable 5) 3D-3D Correspondences
  //     - 3 point Arun (with and without RANSAC)
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  cv::Mat bgr, depth;

  try {
    // Convert ROS msg type to OpenCV image type.
    bgr = cv_bridge::toCvShare(rgb_msg, "bgr8")->image;
    depth = cv_bridge::toCvShare(depth_msg, depth_msg->encoding)->image;
  } catch (cv_bridge::Exception &e) {
    ROS_ERROR("Could not convert rgb or depth images.");
  }

  // Depth in meters as float (16UC1 depth images are in millimeters).
  if (depth.type() == CV_16UC1) {
    cv::Mat depth_m;
    depth.convertTo(depth_m, CV_32F, 1e-3);
    depth = depth_m;
  }

  // Ground-truth camera pose at the image timestamp.
  geometry_msgs::PoseStamped gt_curr;
  if (!lookupGtPose(rgb_msg->header.stamp, &gt_curr)) {
    ROS_WARN_THROTTLE(1.0, "No ground-truth pose around the image stamp, skipping frame.");
    return;
  }
  curr_pose_ = gt_curr;

  // for drawing
  cv::Mat view = bgr.clone();

  // cv::imshow("view", view);

  // The static keyword makes this variable to be created only once.
  // Therefore, this line of code will only be evaluated the first time
  // cameraCallback is called, but never again.
  // Nevertheless, the variable `prev_image` will continue to be available.
  // store images from previous time step
  static cv::Mat prev_bgr = bgr.clone();
  static cv::Mat prev_depth = depth.clone();

  // The first frame has no previous frame: matching it with itself would give a
  // perfect (and meaningless) estimate, so only store it.
  static bool first_frame = true;
  if (first_frame) {
    first_frame = false;
    prev_pose_ = curr_pose_;
    return;
  }
  static int frame_idx = 0;
  frame_log_ = FrameLog();
  frame_log_.frame = ++frame_idx;
  frame_log_.stamp = rgb_msg->header.stamp.toSec();

  // Track features returns the 2D-2D matches between images
  // in pixels (pixel coords in image 1 -> pixel coords in image 2).
  std::pair<std::vector<cv::KeyPoint>, std::vector<cv::KeyPoint>> matched_kp_1_kp_2;
  feature_tracker_->track(prev_bgr, bgr, &matched_kp_1_kp_2);

  int N = matched_kp_1_kp_2.first.size();
  std::cout << "Matched " << N << " keypoints" << std::endl;
  std::vector<cv::Point2f> pts1, pts2;
  
  cv::KeyPoint::convert(matched_kp_1_kp_2.first, pts1);
  cv::KeyPoint::convert(matched_kp_1_kp_2.second, pts2);

  // (TODO) undistort the image keypoints and convert them to bearing vectors 
  // using camera intrinsics
  // Use the calibrateKeypoints function defined
  // Store the results in bearing_vector_1 and bearing_vector_2 defined here.
  opengv::bearingVectors_t bearing_vector_1, bearing_vector_2;
  // ***************************** begin solution *****************************
  if (N > 0) {
    calibrateKeypoints(pts1, pts2, bearing_vector_1, bearing_vector_2);
  }
  frame_log_.n_matches = N;
  // ***************************** end solution *****************************

  // We create the central relative adapter, have a look at OpenGV's
  // documentation to understand how this class works.
  Adapter adapter_mono (bearing_vector_1, bearing_vector_2);

  // (TODO) Compute the pose estimate using the different techniques
  // here. You should fill the variable `pose_estimate` with your pose
  // estimation.
  geometry_msgs::PoseStamped pose_estimation;
  tf::poseTFToMsg(tf::Pose::getIdentity(), pose_estimation.pose);

  // initialize a relative pose estimate, you will update relative_pose_estimate using the following algorithms
  geometry_msgs::Pose relative_pose_estimate = pose_estimation.pose;

  // RANSAC threshold for bearing vectors: 1 - cos(angle subtended by ransac_px pixels).
  const double focal = camera_params_.K.at<double>(0, 0);
  const double threshold_2d = 1.0 - std::cos(std::atan(FLAGS_ransac_px / focal));
  const auto t_start = std::chrono::steady_clock::now();

  switch(FLAGS_pose_estimator) {
  case 0: {
    // *********************************************************************************
    // ******************************** 5-point Method *********************************
    // *********************************************************************************

    // First, ensure we have the minimal number of correspondences to compute the relative pose.
    static constexpr size_t min_nr_of_correspondences = 5;
    if (adapter_mono.getNumberCorrespondences() >= min_nr_of_correspondences) {
      if (!FLAGS_use_ransac) {
        // Without RANSAC [OPTIONAL]
        // Consider using the "extractPose" function provided to obtain inliers, rotation, and translation

        // ***************************** begin solution *****************************
        // Nister on all correspondences at once (least-squares null space of the
        // N x 9 epipolar system), up to 10 candidate essential matrices.
        const opengv::essentials_t essentials = opengv::relative_pose::fivept_nister(adapter_mono);
        // OpenGV: f1^T E f2 = 0 with E = [t12]x R12. OpenCV's recoverPose expects
        // x2^T E x1 = 0, so pass (pts2, pts1): it then returns R12 and t12, i.e. the
        // pose of the current frame in the previous one.
        cv::Mat R, t;
        const int inliers = extractPose(essentials, pts2, pts1, camera_params_, R, t);
        if (!R.empty()) {
          relative_pose_estimate = cv2Pose(R, t);
          frame_log_.valid = true;
        }
        frame_log_.n_inliers = inliers;
        // ***************************** end solution *****************************
      } else {
        // (TODO) With RANSAC
        // Consider using ``eigen2Pose`` to convert the solution of ransac to ``relative_pose_estimate``

        // ***************************** begin solution *****************************
        opengv::sac::Ransac<RansacProblem> ransac;
        std::shared_ptr<RansacProblem> problem(
            new RansacProblem(adapter_mono, RansacProblem::NISTER));
        ransac.sac_model_ = problem;
        ransac.threshold_ = threshold_2d;
        ransac.max_iterations_ = FLAGS_ransac_max_iter;
        if (ransac.computeModel()) {
          // model_coefficients_ = [R12 | t12]: current frame w.r.t. previous frame.
          opengv::transformation_t model = ransac.model_coefficients_;
          // Nonlinear refinement of [R | t] on all inliers.
          if (FLAGS_refine_inliers) problem->optimizeModelCoefficients(ransac.inliers_, ransac.model_coefficients_, model);
          relative_pose_estimate = eigen2Pose(model);
          frame_log_.valid = true;
        }
        frame_log_.n_inliers = ransac.inliers_.size();
        // ***************************** end solution *****************************
      }
    } else {
      ROS_WARN("Not enough correspondences to compute pose estimation using"
               " Nister's algorithm.");
    }
    break;
  }
  case 1: {
    // *********************************************************************************
    // ******************************** 8-point Method *********************************
    // *********************************************************************************

    static constexpr size_t min_nr_of_correspondences = 8;

    if (adapter_mono.getNumberCorrespondences() >= min_nr_of_correspondences) {
      if (!FLAGS_use_ransac) {
        // Without RANSAC [OPTIONAL]
        // Consider using the "extractPose" function provided to obtain inliers, rotation, and translation
        // Consider using "cv2Pose(Rmat, tmat)" to recover the rotation Rmat and translation tmat

        // ***************************** begin solution *****************************
        // Longuet-Higgins on all correspondences (same E convention as above).
        const opengv::essentials_t essentials{opengv::relative_pose::eightpt(adapter_mono)};
        cv::Mat R, t;
        const int inliers = extractPose(essentials, pts2, pts1, camera_params_, R, t);
        if (!R.empty()) {
          relative_pose_estimate = cv2Pose(R, t);
          frame_log_.valid = true;
        }
        frame_log_.n_inliers = inliers;
       // ***************************** end solution *****************************
      } else {
        // (TODO) With RANSAC
        // Consider using ``eigen2Pose`` to convert the solution of ransac to ``relative_pose_estimate``


        // ***************************** begin solution *****************************
        opengv::sac::Ransac<RansacProblem> ransac;
        std::shared_ptr<RansacProblem> problem(
            new RansacProblem(adapter_mono, RansacProblem::EIGHTPT));
        ransac.sac_model_ = problem;
        ransac.threshold_ = threshold_2d;
        ransac.max_iterations_ = FLAGS_ransac_max_iter;
        if (ransac.computeModel()) {
          opengv::transformation_t model = ransac.model_coefficients_;
          if (FLAGS_refine_inliers) problem->optimizeModelCoefficients(ransac.inliers_, ransac.model_coefficients_, model);
          relative_pose_estimate = eigen2Pose(model);
          frame_log_.valid = true;
        }
        frame_log_.n_inliers = ransac.inliers_.size();
        // ***************************** end solution *****************************
      }
    } else {
      ROS_WARN("Not enough correspondences to compute pose estimation using"
               " Longuet-Higgins' algorithm.");
    }
    break;
  }
  case 2: {
    // *********************************************************************************
    // ******************************** 2-point Method *********************************
    // *********************************************************************************

    static constexpr size_t min_nr_of_correspondences = 2;
    if (adapter_mono.getNumberCorrespondences() >= min_nr_of_correspondences) {
      
      // Obtain the rotation part from ground-truth
      tf::Transform curr_frame, prev_frame;
      tf::poseMsgToTF(curr_pose_.pose, curr_frame);
      tf::poseMsgToTF(prev_pose_.pose, prev_frame);
      Eigen::Matrix3d rotation;
      tf::matrixTFToEigen(prev_frame.inverseTimes(curr_frame).getBasis(), rotation);
      adapter_mono.setR12(rotation);

      // We only estimate the translation part
      if (!FLAGS_use_ransac) {
        // Without RANSAC (OPTIONAL)
        // ***************************** begin solution *****************************
        ROS_WARN_ONCE("2-point method without RANSAC is not implemented (optional part).");
        // ***************************** end solution *****************************
      } else {
        // (TODO) With RANSAC
        // ***************************** begin solution *****************************
        // The adapter already holds R12 from ground truth (setR12 above); the
        // minimal solver only estimates the translation direction.
        opengv::sac::Ransac<RansacProblemGivenRot> ransac;
        std::shared_ptr<RansacProblemGivenRot> problem(new RansacProblemGivenRot(adapter_mono));
        ransac.sac_model_ = problem;
        ransac.threshold_ = threshold_2d;
        ransac.max_iterations_ = FLAGS_ransac_max_iter;
        if (ransac.computeModel()) {
          opengv::transformation_t model = ransac.model_coefficients_;
          if (FLAGS_refine_inliers) model = refineTranslationGivenRotation(adapter_mono, ransac.inliers_, model);
          relative_pose_estimate = eigen2Pose(model);
          frame_log_.valid = true;
        }
        frame_log_.n_inliers = ransac.inliers_.size();
        // ***************************** end solution *****************************
      }
    } else {
      ROS_WARN("Not enough correspondences to estimate relative translation using 2pt algorithm.");
    }
    break;
  }
  case 3: {
    // *********************************************************************************
    // ******************************** 3-point Method *********************************
    // *********************************************************************************

    // Scale the bearing vectors to point clouds, by querying the depth values of each keypoint
    std::vector<bool> has_depth(N, false);
    for (int i=0; i<N; i++) {

      // Use the pixel locations of the keypoints to query depth in the depth image  
      double d1 = double( prev_depth.at<float>(std::floor(pts1[i].y), std::floor(pts1[i].x)) ) ;
      double d2 = double( depth.at<float>(std::floor(pts2[i].y), std::floor(pts2[i].x)) ) ;
      // No depth return (0, NaN or inf): keep the correspondence out of the cloud.
      has_depth[i] = std::isfinite(d1) && std::isfinite(d2) && d1 > 0.0 && d2 > 0.0;

      // Normalize the bearing vectors such that the last entry is 1
      bearing_vector_1[i] /= bearing_vector_1[i](2,0);
      bearing_vector_2[i] /= bearing_vector_2[i](2,0);

      // Scale the bearing vectors so that the last entry is equal to depth
      bearing_vector_1[i] *= d1;
      bearing_vector_2[i] *= d2;
    }

    // OpenGV PointCloud 3D-3D Adapter
    opengv::points_t cloud_1, cloud_2;
    for (auto i = 0ul; i < bearing_vector_1.size(); i++) {
        if (!has_depth[i]) continue;
        cloud_1.push_back(bearing_vector_1[i]);
        cloud_2.push_back(bearing_vector_2[i]);
    }

    Adapter3D adapter_3d(cloud_1, cloud_2);

    static constexpr int min_nr_of_correspondences = 3; 
    if (adapter_3d.getNumberCorrespondences() >= min_nr_of_correspondences) {
      if (!FLAGS_use_ransac){
        // Without RANSAC (Optional)
        // ***************************** begin solution *****************************
        // Arun's SVD alignment on all points: cloud_1 = R12 * cloud_2 + t12.
        relative_pose_estimate = eigen2Pose(opengv::point_cloud::threept_arun(adapter_3d));
        frame_log_.valid = true;
        frame_log_.n_inliers = adapter_3d.getNumberCorrespondences();
        // ***************************** end solution *****************************
      } else{
        // (TODO) With RANSAC
        // ***************************** begin solution *****************************
        opengv::sac::Ransac<RansacProblem3D> ransac;
        std::shared_ptr<RansacProblem3D> problem(new RansacProblem3D(adapter_3d));
        ransac.sac_model_ = problem;
        ransac.threshold_ = FLAGS_ransac_3d_m;  // ||p1 - (R p2 + t)|| in meters
        ransac.max_iterations_ = FLAGS_ransac_max_iter;
        if (ransac.computeModel()) {
          opengv::transformation_t model = ransac.model_coefficients_;
          // Arun's method on all inliers.
          if (FLAGS_refine_inliers) problem->optimizeModelCoefficients(ransac.inliers_, ransac.model_coefficients_, model);
          relative_pose_estimate = eigen2Pose(model);
          frame_log_.valid = true;
        }
        frame_log_.n_inliers = ransac.inliers_.size();
        // ***************************** end solution *****************************
      }
    } else {
      ROS_WARN("Not enough correspondences to estimate absolute transform using Arun's 3pt algorithm.");
    }
    break;
  }
  default: {
    ROS_ERROR("Wrong pose_estimator flag!");
  }
  }

  frame_log_.time_ms = std::chrono::duration<double, std::milli>(
      std::chrono::steady_clock::now() - t_start).count();

  // scale the relative pose estimate (for 5-pt, 2-pt and 8-pt, the translation is up to scale)
  // (a failed estimate is the identity, whose zero translation cannot be scaled)
  if (FLAGS_pose_estimator < 3 && frame_log_.valid) {
    scaleTranslation(relative_pose_estimate.position, prev_pose_, curr_pose_);
  }

  // pose estimate w.r.t. ground truth
  updatePoseEstimate(prev_pose_.pose, relative_pose_estimate, pose_estimation.pose);

  // Compute tf::Transform in order to do actual pose operations.
  tf::Transform gt_t_prev_frame, gt_t_curr_frame;
  tf::Transform est_t_prev_frame, est_t_curr_frame;
  tf::poseMsgToTF(pose_estimation.pose, est_t_curr_frame);
  tf::poseMsgToTF(curr_pose_.pose, gt_t_curr_frame);
  tf::poseMsgToTF(prev_pose_.pose, est_t_prev_frame);
  tf::poseMsgToTF(prev_pose_.pose, gt_t_prev_frame);

  // Evaluate pose errors
  evaluateRPE(gt_t_prev_frame, gt_t_curr_frame,est_t_prev_frame,est_t_curr_frame);

  // (TODO) Now, publish your estimated pose here. Since your pose estimate is
  // relative to the previous frame, use the ground-truth pose of the previous
  // frame to publish your pose_estimate in world frame. This will allow you to
  // see how far away is your estimate from the ground-truth one in Rviz.
  // Remember to subscirbe to the right topic in Rviz. Make this abosolute pose
  // ***************************** begin solution *****************************
  // pose_estimation.pose = (GT pose at t-1) * (estimated T^{t-1}_{t}), computed
  // above by updatePoseEstimate.
  pose_estimation.header.frame_id = "world";
  pose_estimation.header.stamp = rgb_msg->header.stamp;
  pub_pose_estimation_.publish(pose_estimation);
  // Ground-truth camera pose of the same frame (interpolated at the image stamp).
  curr_pose_.header.frame_id = "world";
  curr_pose_.header.stamp = rgb_msg->header.stamp;
  pub_pose_gt_.publish(curr_pose_);
  // ***************************** end solution *****************************

  // Save for next iteration
  prev_bgr = bgr.clone();
  prev_depth = depth.clone();
  prev_pose_ = curr_pose_;
}

/**
 * @brief Queue a synchronized RGB-D pair. It is processed by cameraCallback from
 *        the main loop once odometry newer than its stamp has arrived, so the
 *        ground-truth pose can be interpolated (instead of extrapolated).
 */
void syncCallback(const sensor_msgs::ImageConstPtr &rgb_msg, const sensor_msgs::ImageConstPtr &depth_msg) {
  pending_frames_.emplace_back(rgb_msg, depth_msg);
}

// Processes at most one frame, so the main loop goes back to ros::spinOnce() between
// frames and the subscriber queues never overflow while a backlog is worked off.
void processPendingFrame() {
  if (FLAGS_latest_only) {
    // Drop frames that already have a newer frame with ground truth behind them.
    while (pending_frames_.size() > 1 && !gt_buffer_.empty() &&
           gt_buffer_.back().header.stamp >= pending_frames_[1].first->header.stamp) {
      pending_frames_.pop_front();
    }
  }
  if (!pending_frames_.empty() && !gt_buffer_.empty() &&
      gt_buffer_.back().header.stamp >= pending_frames_.front().first->header.stamp) {
    const auto frame = pending_frames_.front();
    pending_frames_.pop_front();
    cameraCallback(frame.first, frame.second);
  }
}

/**
 * @function main
 * @brief Main function
 */
int main(int argc, char** argv) {
  google::InitGoogleLogging(argv[0]);
  google::ParseCommandLineFlags(&argc, &argv, true);
  google::InstallFailureSignalHandler();

  ros::init(argc, argv, "keypoint_trackers");
  ros::NodeHandle local_nh("~");

  // populate camera intrinsics and distortion
  camera_params_.K = cv::Mat::zeros(3, 3, CV_64F);
  camera_params_.K.at<double>(0,0) = 415.69219381653056;
  camera_params_.K.at<double>(1,1) = 415.69219381653056;
  camera_params_.K.at<double>(0,2) = 360.0;
  camera_params_.K.at<double>(1,2) = 240.0;
  camera_params_.D = cv::Mat::zeros(cv::Size(5,1),CV_64F);

  // Constant extrinsics of the camera wrt the body, T_{camera}^{body}
  T_camera_body = cv::Mat::zeros(cv::Size(4,4),CV_64F);
  T_camera_body.at<double>(0,2) = 1.0;
  T_camera_body.at<double>(1,0) = -1.0;
  T_camera_body.at<double>(1,3) = 0.05;
  T_camera_body.at<double>(2,1) = -1.0;
  T_camera_body.at<double>(3,3) = 1.0;
  // convert to geometry_msgs::Pose
  R_camera_body = T_camera_body(cv::Range(0,3),cv::Range(0,3));
  t_camera_body = T_camera_body(cv::Range(0,3),cv::Range(3,4));
  pose_camera_body = cv2Pose(R_camera_body,t_camera_body);
  // convert to tf transform
  tf::poseMsgToTF(pose_camera_body, transform_camera_body);

  feature_tracker_.reset(new TrackerWrapper(FLAGS_show_matches));

  if (!FLAGS_rpe_csv.empty()) {
    rpe_csv_.reset(new std::ofstream(FLAGS_rpe_csv));
    *rpe_csv_ << "frame,stamp,n_matches,n_inliers,valid,time_ms,gt_tran_norm,est_tran_norm,"
                 "rot_err_chordal,rot_err_deg,tran_err_unit,tran_err_m,"
                 "gt_tx,gt_ty,gt_tz,est_tx,est_ty,est_tz" << std::endl;
  }

  // Subscribe to drone pose estimation.
  auto pose_sub = local_nh.subscribe("/ground_truth_pose", 2000, poseCallbackTesse);

  // Subscribe to rgb and depth images.
  image_transport::ImageTransport it(local_nh);
  // Large queues: frames are buffered (pending_frames_) instead of dropped when
  // the SIFT matching is slower than the bag.
  image_transport::SubscriberFilter sf_rgb(it, "/rgb_images_topic", 100);
  image_transport::SubscriberFilter sf_depth(it, "/depth_images_topic", 100);

  typedef message_filters::sync_policies::ApproximateTime<sensor_msgs::Image, sensor_msgs::Image> MySyncPolicy;
  message_filters::Synchronizer<MySyncPolicy> sync(MySyncPolicy(100), sf_rgb, sf_depth);
  sync.registerCallback(syncCallback);

  // Advertise drone pose.
  pub_pose_gt_ = local_nh.advertise<geometry_msgs::PoseStamped>("/gt_camera_pose", 1);
  pub_pose_estimation_ = local_nh.advertise<geometry_msgs::PoseStamped>("/camera_pose", 1);

  while (ros::ok()) {
    ros::spinOnce();
    processPendingFrame();
    if (FLAGS_show_matches) cv::waitKey(1);
    else if (pending_frames_.empty()) ros::Duration(0.001).sleep();
  }
  cv::destroyAllWindows();

  return EXIT_SUCCESS;
}
