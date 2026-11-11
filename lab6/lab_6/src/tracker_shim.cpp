#include "tracker_shim.h"
#include "feature_tracker.h"
#include "sift_feature_tracker.h"


TrackerWrapper::TrackerWrapper(bool show) {
  impl_.reset(new SiftFeatureTracker());
  // lab5's tracker starts in pair-of-images mode (blocks on every imshow);
  // switch it to video mode, no files written.
  impl_->setOutput(/*pause_on_display=*/false, "", "", "", -1, show);
}

TrackerWrapper::~TrackerWrapper() {}

void TrackerWrapper::track(const cv::Mat& prev, const cv::Mat& curr, FeatureResult* ret) {
  impl_->trackFeatures(prev, curr, ret);
}
