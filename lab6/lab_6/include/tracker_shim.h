#pragma once
#include <vector>
#include <utility>
#include <memory>

namespace cv {
    class Mat;
    class KeyPoint;
}

class FeatureTracker;
class CachedSiftTracker;
using FeatureResult = std::pair<std::vector<cv::KeyPoint>, std::vector<cv::KeyPoint>>;

struct TrackerWrapper {
  /// show: display lab5's inlier/outlier match window (waitKey(10), never blocks).
  explicit TrackerWrapper(bool show = false);
  ~TrackerWrapper();
  void track(const cv::Mat& prev, const cv::Mat& curr, FeatureResult* result);

 private:
  std::unique_ptr<FeatureTracker> impl_;       // lab5 tracker, used when show == true
  std::unique_ptr<CachedSiftTracker> cached_;  // same SIFT + ratio test, one detection per frame
};
