#pragma once

#include <fstream>
#include <memory>
#include <string>
#include <vector>
#include "feature_tracker.h"

#include <opencv2/core.hpp>
#include <opencv2/features2d.hpp>
#include <opencv2/xfeatures2d.hpp>

class LKFeatureTracker {
 public:
  LKFeatureTracker();

  ~LKFeatureTracker();

  /** TODO: this function tracks features for a given frame
   * @param[in] the current image frame
   * Should update prev_frame_ and prev_corners_ as needed
   */
  void trackFeatures(const cv::Mat& frame);

  void printStats() const;

  /// Same meaning as FeatureTracker::setOutput.
  void setOutput(const std::string& output_dir, const std::string& stats_csv,
                 const std::string& frames_dir, int save_frame = -1,
                 bool show = true);

  /// Harris corner parameters for cv::goodFeaturesToTrack.
  void setCornerParams(int max_corners, double quality_level,
                       double min_distance) {
    max_corners_ = max_corners;
    quality_level_ = quality_level;
    min_distance_ = min_distance;
  }

  /** Compute Inlier Mask out of the given matched keypoints.
   @param[in] pts1 List of keypoints detected on the first image.
   @param[in] pts2 List of keypoints detected on the second image.
   @param[out] inlier_mask Mask indicating inliers (1) from outliers (0).
  */
  void inlierMaskComputation(const std::vector<cv::Point2f>& pts1,
                             const std::vector<cv::Point2f>& pts2,
                             std::vector<uchar>* inlier_mask) const;

 private:

  /** TODO Display image with tracked features from prev to curr on the image
   * corresponding to 'frame'
   * @param[in] frame The current image frame, to draw the feature track on
   * @param[in] prev The previous set of keypoints
   * @param[in] curr The set of keypoints for the current frame
   */
  void show(const cv::Mat& frame, std::vector<cv::Point2f>& prev,
                 std::vector<cv::Point2f>& curr);

  /// Harris corners in `gray`, away from the points in `existing`.
  void detectCorners(const cv::Mat& gray,
                     const std::vector<cv::Point2f>& existing,
                     int max_new, std::vector<cv::Point2f>* corners) const;

  static constexpr const char* window_name_ = "LK";
  cv::Mat prev_frame_;
  std::vector<cv::Point2f> prev_corners_;
  // Pixel history of every tracked corner (parallel to prev_corners_), only
  // used for drawing; capped at kMaxTrackLength points.
  std::vector<std::vector<cv::Point2f>> tracks_;
  static constexpr size_t kMaxTrackLength = 20;

  int max_corners_ = 500;
  double quality_level_ = 0.01;
  double min_distance_ = 10.0;

  bool show_ = true;
  std::string output_dir_;
  std::string frames_dir_;
  int save_frame_ = -1;
  std::unique_ptr<std::ofstream> stats_csv_;

  // Statistics
  float avg_num_keypoints_img1_ = 0;
  float avg_num_keypoints_img2_ = 0;
  float avg_num_matches_ = 0;
  float avg_num_good_matches_ = 0;
  float avg_num_inliers_ = 0;
  float avg_inlier_ratio_ = 0;
  float avg_time_ms_ = 0;
  unsigned int num_samples_ = 0;
};
