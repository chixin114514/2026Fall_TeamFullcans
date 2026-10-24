#include "lk_feature_tracker.h"

#include <chrono>
#include <numeric>
#include <vector>

#include <glog/logging.h>

#include <opencv2/calib3d.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/video/tracking.hpp>
#include <opencv2/imgcodecs.hpp>

#include <ros/ros.h>

using namespace cv;
using namespace cv::xfeatures2d;

/**
   LK feature tracker Constructor.
*/
LKFeatureTracker::LKFeatureTracker() {}

LKFeatureTracker::~LKFeatureTracker() {
  if (show_) cv::destroyWindow(window_name_);
}

void LKFeatureTracker::setOutput(const std::string& output_dir,
                                 const std::string& stats_csv,
                                 const std::string& frames_dir,
                                 int save_frame, bool show) {
  output_dir_ = output_dir;
  frames_dir_ = frames_dir;
  save_frame_ = save_frame;
  show_ = show;
  if (show_) cv::namedWindow(window_name_, cv::WINDOW_NORMAL);
  if (!stats_csv.empty()) {
    stats_csv_.reset(new std::ofstream(stats_csv));
    *stats_csv_ << "frame,kp1,kp2,matches,good_matches,inliers,inlier_ratio,time_ms"
                << std::endl;
  }
}

void LKFeatureTracker::detectCorners(const cv::Mat& gray,
                                     const std::vector<cv::Point2f>& existing,
                                     int max_new,
                                     std::vector<cv::Point2f>* corners) const {
  CHECK_NOTNULL(corners);
  corners->clear();
  if (max_new <= 0) return;
  // Do not re-detect where a corner is already being tracked.
  cv::Mat mask(gray.size(), CV_8UC1, cv::Scalar(255));
  for (const auto& pt : existing) {
    cv::circle(mask, pt, static_cast<int>(min_distance_), cv::Scalar(0), -1);
  }
  static constexpr int kBlockSize = 3;
  static constexpr bool kUseHarris = true;
  static constexpr double kHarrisK = 0.04;
  cv::goodFeaturesToTrack(gray, *corners, max_new, quality_level_,
                          min_distance_, mask, kBlockSize, kUseHarris, kHarrisK);
}

void LKFeatureTracker::printStats() const {
  std::cout << "Avg. Keypoints 1 Size: " << avg_num_keypoints_img1_ << std::endl;
  std::cout << "Avg. Keypoints 2 Size: " << avg_num_keypoints_img2_ << std::endl;
  std::cout << "Avg. Number of matches: " << avg_num_matches_ << std::endl;
  std::cout << "Avg. Number of good matches: " << avg_num_good_matches_ << std::endl;
  std::cout << "Avg. Number of Inliers: " << avg_num_inliers_ << std::endl;
  std::cout << "Avg. Inliers ratio: " << avg_inlier_ratio_ << std::endl;
  std::cout << "Avg. detect+track time [ms]: " << avg_time_ms_ << std::endl;
  std::cout << "Num. of samples: " << num_samples_ << std::endl;
}

/** TODO This is the main tracking function, given two images, it detects,
 * describes and matches features.
 * We will be modifying this function incrementally to plot different figures
 * and compute different statistics.
 @param[in] frame Current image frame
*/
void LKFeatureTracker::trackFeatures(const cv::Mat& frame) {

  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  //  DELIVERABLE 7 | Feature Tracking: Lucas-Kanade Tracker
  // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
  //
  // For this part, you will need to:
  //
  //   1. Using OpenCV’s documentation and the C++ API for the LK tracker, track
  //   features for the video sequences we provided you by using the Harris
  //   corner detector (like here). Show the feature tracks at a given frame
  //   extracted when using the Harris corners (consider using the 'show'
  //   function below)
  //
  //   Hint 1: take a look at cv::goodFeaturesToTrack and cv::calcOpticalFlowPyrLK
  //
  //   2. Add an extra entry in the table you made previously for the Harris +
  //   LK tracker
  //
  //   Note: LKFeatureTracker does not inherit from the base tracker like other
  //   feature trackers, so you need to also implement the statistics gathering
  //   code right here.
  //
  // ~~~~ begin solution
  cv::Mat gray;
  if (frame.channels() == 3) {
    cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
  } else {
    gray = frame.clone();
  }

  // First frame: nothing to track yet, only detect.
  if (prev_frame_.empty()) {
    detectCorners(gray, {}, max_corners_, &prev_corners_);
    tracks_.clear();
    for (const auto& pt : prev_corners_) tracks_.push_back({pt});
    prev_frame_ = gray;
    return;
  }

  const auto t_start = std::chrono::steady_clock::now();
  std::vector<cv::Point2f> curr_corners;
  std::vector<uchar> status;
  std::vector<float> err;
  if (!prev_corners_.empty()) {
    cv::calcOpticalFlowPyrLK(prev_frame_, gray, prev_corners_, curr_corners,
                             status, err, cv::Size(21, 21), 3,
                             cv::TermCriteria(cv::TermCriteria::COUNT |
                                              cv::TermCriteria::EPS, 30, 0.01));
  }

  // status[i] == 1 <=> corner i was found in the current frame: these are
  // the LK "matches".
  std::vector<cv::Point2f> prev_tracked, curr_tracked;
  std::vector<std::vector<cv::Point2f>> tracked_history;
  for (size_t i = 0; i < status.size(); ++i) {
    if (!status[i]) continue;
    prev_tracked.push_back(prev_corners_[i]);
    curr_tracked.push_back(curr_corners[i]);
    tracked_history.push_back(tracks_[i]);
  }

  std::vector<uchar> inlier_mask;
  if (prev_tracked.size() >= 8) {
    inlierMaskComputation(prev_tracked, curr_tracked, &inlier_mask);
  }
  if (inlier_mask.size() != prev_tracked.size()) {
    inlier_mask.assign(prev_tracked.size(), 0);
  }
  const unsigned int num_inliers =
      std::accumulate(inlier_mask.begin(), inlier_mask.end(), 0u);

  // Keep tracking only the inliers, and top the set up with new Harris
  // corners so that there are always ~max_corners_ points.
  std::vector<cv::Point2f> next_corners;
  std::vector<std::vector<cv::Point2f>> next_tracks;
  for (size_t i = 0; i < curr_tracked.size(); ++i) {
    if (!inlier_mask[i]) continue;
    next_corners.push_back(curr_tracked[i]);
    next_tracks.push_back(tracked_history[i]);
    next_tracks.back().push_back(curr_tracked[i]);
    if (next_tracks.back().size() > kMaxTrackLength) {
      next_tracks.back().erase(next_tracks.back().begin());
    }
  }
  std::vector<cv::Point2f> new_corners;
  detectCorners(gray, next_corners,
                max_corners_ - static_cast<int>(next_corners.size()),
                &new_corners);
  const double time_ms = std::chrono::duration<double, std::milli>(
      std::chrono::steady_clock::now() - t_start).count();

  // Draw before adding the fresh corners (they have no track yet).
  tracks_ = next_tracks;
  show(frame, prev_tracked, curr_tracked);

  for (const auto& pt : new_corners) {
    next_corners.push_back(pt);
    tracks_.push_back({pt});
  }

  // Statistics, with the same meaning as for the descriptor-based trackers:
  //   kp1 = corners in the previous frame that LK tries to track (one query
  //   per corner, so #matches = kp1), kp2 = corners available in the current
  //   frame (tracked inliers + newly detected), good matches = status == 1.
  const size_t num_kp_1 = prev_corners_.size();
  const size_t num_kp_2 = next_corners.size();
  const size_t num_matches = prev_corners_.size();
  const size_t num_good_matches = prev_tracked.size();
  const float inlier_ratio = num_good_matches == 0 ? 0.0f :
      static_cast<float>(num_inliers) / static_cast<float>(num_good_matches);

  float const new_num_samples = static_cast<float>(num_samples_) + 1.0f;
  float const old_num_samples = static_cast<float>(num_samples_);
  auto update = [&](float* avg, float value) {
    *avg = (*avg * old_num_samples + value) / new_num_samples;
  };
  update(&avg_num_keypoints_img1_, num_kp_1);
  update(&avg_num_keypoints_img2_, num_kp_2);
  update(&avg_num_matches_, num_matches);
  update(&avg_num_good_matches_, num_good_matches);
  update(&avg_num_inliers_, num_inliers);
  update(&avg_inlier_ratio_, inlier_ratio);
  update(&avg_time_ms_, time_ms);
  if (stats_csv_) {
    *stats_csv_ << num_samples_ << "," << num_kp_1 << "," << num_kp_2 << ","
                << num_matches << "," << num_good_matches << "," << num_inliers
                << "," << inlier_ratio << "," << time_ms << std::endl;
  }
  ++num_samples_;

  prev_frame_ = gray;
  prev_corners_ = next_corners;
  // ~~~~ end solution
  // ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
  //                             end deliverable 7
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

}

/** TODO Display image with tracked features from prev to curr on the image
 * corresponding to 'frame'
 * @param[in] frame The current image frame, to draw the feature track on
 * @param[in] prev The previous set of keypoints
 * @param[in] curr The set of keypoints for the current frame
 */
void LKFeatureTracker::show(const cv::Mat& frame, std::vector<cv::Point2f>& prev,
                            std::vector<cv::Point2f>& curr) {
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // ~~~~ begin solution
  // Green: track history of the corners kept (RANSAC inliers) ending at a
  // dot in the current frame. Red: tracked by LK but rejected by RANSAC.
  cv::Mat img = frame.clone();
  if (img.channels() == 1) cv::cvtColor(img, img, cv::COLOR_GRAY2BGR);
  for (const auto& track : tracks_) {
    for (size_t j = 1; j < track.size(); ++j) {
      cv::line(img, track[j - 1], track[j], cv::Scalar(0, 255, 0), 1, cv::LINE_AA);
    }
    cv::circle(img, track.back(), 2, cv::Scalar(0, 255, 0), -1, cv::LINE_AA);
  }
  // Outliers: whatever LK tracked that is not the end point of a kept track.
  for (size_t i = 0; i < curr.size(); ++i) {
    bool is_kept = false;
    for (const auto& track : tracks_) {
      if (track.back() == curr[i]) { is_kept = true; break; }
    }
    if (is_kept) continue;
    cv::line(img, prev[i], curr[i], cv::Scalar(0, 0, 255), 1, cv::LINE_AA);
    cv::circle(img, curr[i], 2, cv::Scalar(0, 0, 255), -1, cv::LINE_AA);
  }

  if (static_cast<int>(num_samples_) == save_frame_ && !output_dir_.empty()) {
    cv::imwrite(output_dir_ + "/lk_tracks.png", img);
  }
  if (!frames_dir_.empty()) {
    char name[64];
    std::snprintf(name, sizeof(name), "/frame_%06u.png", num_samples_);
    cv::imwrite(frames_dir_ + name, img);
  }
  if (show_) {
    cv::imshow(window_name_, img);
    cv::waitKey(10);
  }
  // ~~~~ end solution
  // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
}

/** Compute Inlier Mask out of the given matched keypoints.
 @param[in] pts1 List of keypoints detected on the first image.
 @param[in] pts2 List of keypoints detected on the second image.
 @param[out] inlier_mask Mask indicating inliers (1) from outliers (0).
*/
void LKFeatureTracker::inlierMaskComputation(const std::vector<cv::Point2f>& pts1,
                                             const std::vector<cv::Point2f>& pts2,
                                             std::vector<uchar>* inlier_mask) const {
  CHECK_NOTNULL(inlier_mask);

  static constexpr double max_dist_from_epi_line_in_px = 3.0;
  static constexpr double confidence_prob = 0.99;
  try {
    findFundamentalMat(pts1, pts2, CV_FM_RANSAC,
                       max_dist_from_epi_line_in_px, confidence_prob,
                       *inlier_mask);
  } catch(...) {
    ROS_WARN("Inlier Mask could not be computed, this can happen if there"
             "are not enough features tracked.");
  }
}
