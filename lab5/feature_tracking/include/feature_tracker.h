#pragma once

#include "feature_tracker.h"
#include <chrono>
#include <fstream>
#include <memory>
#include <string>
#include <vector>

#include <opencv2/core.hpp>
#include <opencv2/xfeatures2d.hpp>

class FeatureTracker {
public:
  FeatureTracker() = default;

  virtual ~FeatureTracker() = default;

  /** Main function (TODO)
   * This function receives a pair of images and tracks features from one image
   * to the other.
    @param[in] img_1, img_2 Images where to track features.
    @param[out] matched_kp_1_kp_2 pair of vectors of keypoints with the same size
    so that matched_kp_1_kp_2.first[i] matches with matched_kp_1_kp_2.second[i].
  */
  void trackFeatures(const cv::Mat& img_1, const cv::Mat& img_2,
                     std::pair<std::vector<cv::KeyPoint>,
                               std::vector<cv::KeyPoint>>* matched_kp_1_kp_2 = nullptr);

  void printStats() const;

  /// Lowe's ratio test threshold used by matchDescriptors (default 0.8).
  void setRatioThreshold(float ratio) { ratio_thresh_ = ratio; }

  /// Binary descriptors only: brute-force Hamming (true) or FLANN-LSH (false).
  void setUseBruteForceMatcher(bool use_bf) { use_bf_matcher_ = use_bf; }

  /** Visualization / logging options (not part of the original stencil).
    @param[in] pause_on_display Block on every imshow until a key is pressed
    (pair-of-images mode) instead of waitKey(10) (video mode).
    @param[in] output_dir If non-empty, figures are written here (pair mode:
    every figure; video mode: only frame number `save_frame`).
    @param[in] stats_csv If non-empty, per-frame statistics are appended here.
    @param[in] frames_dir If non-empty, every inlier/outlier frame is saved here
    (used to make the tracking video).
  */
  void setOutput(bool pause_on_display, const std::string& output_dir,
                 const std::string& stats_csv, const std::string& frames_dir,
                 int save_frame = -1, bool show = true);

protected:
  /// Keep match[0] if match[0].distance < ratio_thresh_ * match[1].distance.
  void ratioTest(const std::vector<std::vector<cv::DMatch>>& matches,
                 std::vector<cv::DMatch>* good_matches) const;

  /// knnMatch (k=2) + ratio test for binary descriptors (ORB, BRIEF):
  /// brute-force Hamming if use_bf_matcher_, else FLANN with an LSH index.
  void matchBinaryDescriptors(const cv::Mat& descriptors_1,
                              const cv::Mat& descriptors_2,
                              std::vector<std::vector<cv::DMatch>>* matches,
                              std::vector<cv::DMatch>* good_matches) const;

  float ratio_thresh_ = 0.8f;
  bool use_bf_matcher_ = true;

  /**
    @param[in] img Image input where to detect keypoints.
    @param[out] keypoints List of keypoints detected on the given image.
  */
  virtual void detectKeypoints(const cv::Mat& img,
                               std::vector<cv::KeyPoint>* keypoints) const = 0;

  /**
    @param[in] img Image used to detect the keypoints.
    @param[in, out] keypoints List of keypoints detected on the image. Depending
    on the detector used some keypoints might be added or removed.
    @param[out] descriptors List of descriptors for the given keypoints.
  */
  virtual void describeKeypoints(const cv::Mat& img,
                                 std::vector<cv::KeyPoint>* keypoints,
                                 cv::Mat* descriptors) const = 0;

  /** This function matches descriptors.
      @param[in] descriptors_1 First list of descriptors.
      @param[in] descriptors_2 Second list of descriptors.
      @param[out] matches List of k best matches between descriptors.
      @param[out] good_matches List of descriptors classified as "good"
  */
  virtual void matchDescriptors(
      const cv::Mat& descriptors_1,
      const cv::Mat& descriptors_2,
      std::vector<std::vector<cv::DMatch>>* matches,
      std::vector<cv::DMatch>* good_matches) const = 0;

  /** Compute Inlier Mask out of the given matched keypoints.
   *  Both keypoints_1 and keypoints_2 input parameters must be ordered by match
   * i.e. keypoints_1[0] has been matched to keypoints_2[0].
   * Therefore, both keypoints vectors must have the same length.
    @param[in] keypoints_1 List of keypoints detected on the first image.
    @param[in] keypoints_2 List of keypoints detected on the second image.
    @param[out] inlier_mask Mask indicating inliers (1) from outliers (0).
  */
  void inlierMaskComputation(const std::vector<cv::KeyPoint>& keypoints_1,
                             const std::vector<cv::KeyPoint>& keypoints_2,
                             std::vector<uchar>* inlier_mask) const;

  void drawMatches(const cv::Mat& img_1, const cv::Mat& img_2,
                   const std::vector<cv::KeyPoint>& keypoints_1,
                   const std::vector<cv::KeyPoint>& keypoints_2,
                   const std::vector<std::vector<cv::DMatch>>& matches);

private:
  void showAndSave(const std::string& name, const cv::Mat& img, bool save);

  bool pause_on_display_ = true;
  bool show_ = true;
  std::string output_dir_;
  std::string frames_dir_;
  int save_frame_ = -1;
  std::unique_ptr<std::ofstream> stats_csv_;

  //Statistics
  float avg_num_keypoints_img1_ = 0;
  float avg_num_keypoints_img2_ = 0;
  float avg_num_matches_ = 0;
  float avg_num_good_matches_ = 0;
  float avg_num_inliers_ = 0;
  float avg_inlier_ratio_ = 0;
  float avg_time_ms_ = 0;
  unsigned int num_samples_ = 0;
};
