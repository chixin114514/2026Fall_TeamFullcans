#include "tracker_shim.h"

#include <cstring>

#include "feature_tracker.h"
#include "sift_feature_tracker.h"

/// Lab 5's SIFT tracker, reorganised for video: each frame is detected and described
/// once, and its keypoints/descriptors are reused as the "previous" frame of the next
/// call. trackFeatures() instead re-detects both images every time, and also runs a
/// fundamental-matrix RANSAC and draws a match image that lab 6 never uses. Detection,
/// description, FLANN matching and Lowe's ratio test are lab 5's own functions.
class CachedSiftTracker : public SiftFeatureTracker {
 public:
  void track(const cv::Mat& prev, const cv::Mat& curr, FeatureResult* result) {
    std::vector<cv::KeyPoint> kp_1, kp_2;
    cv::Mat desc_1, desc_2;
    if (sameImage(prev, cache_img_)) {
      kp_1 = cache_kp_;
      desc_1 = cache_desc_;
    } else {
      detectKeypoints(prev, &kp_1);
      describeKeypoints(prev, &kp_1, &desc_1);
    }
    detectKeypoints(curr, &kp_2);
    describeKeypoints(curr, &kp_2, &desc_2);

    std::vector<std::vector<cv::DMatch>> matches;
    std::vector<cv::DMatch> good_matches;
    if (!desc_1.empty() && !desc_2.empty()) {
      matchDescriptors(desc_1, desc_2, &matches, &good_matches);
    }
    result->first.clear();
    result->second.clear();
    for (const auto& m : good_matches) {
      result->first.push_back(kp_1[m.queryIdx]);
      result->second.push_back(kp_2[m.trainIdx]);
    }
    cache_img_ = curr.clone();
    cache_kp_ = std::move(kp_2);
    cache_desc_ = desc_2;
  }

 private:
  static bool sameImage(const cv::Mat& a, const cv::Mat& b) {
    if (a.empty() || b.empty() || a.size() != b.size() || a.type() != b.type()) return false;
    if (!a.isContinuous() || !b.isContinuous()) return false;
    return std::memcmp(a.data, b.data, a.total() * a.elemSize()) == 0;
  }

  cv::Mat cache_img_, cache_desc_;
  std::vector<cv::KeyPoint> cache_kp_;
};

TrackerWrapper::TrackerWrapper(bool show) {
  if (show) {
    impl_.reset(new SiftFeatureTracker());
    // lab5's tracker starts in pair-of-images mode (blocks on every imshow);
    // switch it to video mode, no files written.
    impl_->setOutput(/*pause_on_display=*/false, "", "", "", -1, show);
  } else {
    cached_.reset(new CachedSiftTracker());
  }
}

TrackerWrapper::~TrackerWrapper() {}

void TrackerWrapper::track(const cv::Mat& prev, const cv::Mat& curr, FeatureResult* ret) {
  if (cached_) {
    cached_->track(prev, curr, ret);
  } else {
    impl_->trackFeatures(prev, curr, ret);
  }
}
