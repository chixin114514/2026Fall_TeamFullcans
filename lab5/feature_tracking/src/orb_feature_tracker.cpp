// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  16.485 - Fall 2019  - Lab 5 coding assignment
// ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
//
//  In this code, we ask you to implement an ORB feature tracker derived class
//  that inherits from your FeatureTracker base class.
//
// NOTE: Deliverables for the TEAM portion of this assignment start at number 3
// and end at number 7. If you have completed the parts labeled Deliverable 3-7,
// you are done with the TEAM portion of the lab. Deliverables 1-2 are
// individual.
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  DELIVERABLE 6 (continued) | Comparing Feature Matching on Real Data
// ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
//
// For this part, you will need to implement the same functions you've just
// implemented in the case of SIFT and SURF, but now for ORB features. You'll
// also implement these functions for the case of FAST+BRIEF.
// For that case, see fast_feature_tracker.cpp (and its respective header)
//
// NOTE: We do not provide template code for this section or the corresponding
// header file (orb_feature_tracker.h), but you should define and implement
// the same set of functions as for SIFT and SURF (see the template code for
// those cases for reference as needed)
//
// NOTE: Don't forget to modify the CMakeLists.txt to add these files!
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "orb_feature_tracker.h"
#include <glog/logging.h>
#include <opencv2/features2d.hpp>

using namespace cv;
using namespace cv::xfeatures2d;

OrbFeatureTracker::OrbFeatureTracker(int nfeatures, int nlevels)
    : detector(ORB::create(nfeatures, 1.2f, nlevels)) {}

void OrbFeatureTracker::detectKeypoints(const cv::Mat &img,
                                         std::vector<cv::KeyPoint> *keypoints) const {
  CHECK_NOTNULL(keypoints);
  detector->detect(img, *keypoints);
}

void OrbFeatureTracker::describeKeypoints(const cv::Mat &img,
                                           std::vector<cv::KeyPoint> *keypoints,
                                           cv::Mat *descriptors) const {
  CHECK_NOTNULL(keypoints);
  CHECK_NOTNULL(descriptors);
  detector->compute(img, *keypoints, *descriptors);
}

void OrbFeatureTracker::matchDescriptors(const cv::Mat &descriptors_1,
                                          const cv::Mat &descriptors_2,
                                          std::vector<std::vector<cv::DMatch>> *matches,
                                          std::vector<cv::DMatch> *good_matches) const {
  matchBinaryDescriptors(descriptors_1, descriptors_2, matches, good_matches);
}
