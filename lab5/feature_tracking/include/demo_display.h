#pragma once

#include <algorithm>
#include <set>
#include <string>

#include <poll.h>
#include <unistd.h>
#include <opencv2/highgui.hpp>
#include <ros/ros.h>

// Shared presentation options; saved figures retain their original resolution.
class DemoDisplay {
 public:
  void configure(const ros::NodeHandle& nh) {
    width_ = std::max(1, nh.param<int>("window_width", 1600));
    height_ = std::max(1, nh.param<int>("window_height", 900));
    enter_only_ = nh.param<bool>("enter_only", false);
    terminal_enter_ = nh.param<bool>("terminal_enter", false);
  }

  void open(const std::string& name) {
    if (windows_.insert(name).second) {
      cv::namedWindow(name, cv::WINDOW_NORMAL);
      cv::resizeWindow(name, width_, height_);
    }
  }

  void close(const std::string& name) {
    cv::destroyWindow(name);
    windows_.erase(name);
  }

  bool enterOnly() const { return enter_only_; }

  bool advanceRequested(int key) const {
    if (key >= 0 && (!enter_only_ || (key & 0xff) == 13 || (key & 0xff) == 10)) {
      return true;
    }
    // Pair-mode roslaunch inherits stdin. Nonblocking polling keeps the
    // OpenCV window responsive while waiting for a terminal newline.
    if (terminal_enter_) {
      pollfd input{STDIN_FILENO, POLLIN, 0};
      if (poll(&input, 1, 0) > 0 && (input.revents & POLLIN)) {
        char buffer[256];
        const ssize_t size = read(STDIN_FILENO, buffer, sizeof(buffer));
        for (ssize_t i = 0; i < size; ++i) {
          if (buffer[i] == '\n' || buffer[i] == '\r') return true;
        }
      }
    }
    return false;
  }

 private:
  int width_ = 1600;
  int height_ = 900;
  bool enter_only_ = false;
  bool terminal_enter_ = false;
  std::set<std::string> windows_;
};
