cmake_minimum_required(VERSION 2.8.3)
project(lab_6)

add_compile_options(-std=c++14)

find_package(lab_5 REQUIRED)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  opencv3_catkin
  image_transport
  cv_bridge
  opengv
  eigen_catkin
  tf_conversions
)

catkin_package(
 INCLUDE_DIRS include
 LIBRARIES
 CATKIN_DEPENDS roscpp rospy image_transport cv_bridge lab_5 opengv eigen_catkin opencv3_catkin
)

# glog/gflags come from the system (libgoogle-glog-dev, libgflags-dev) instead of glog_catkin,
# same as lab_5.
find_library(GLOG_LIBRARY glog REQUIRED)
find_library(GFLAGS_LIBRARY gflags REQUIRED)

# cv_bridge exports the system OpenCV 4.2 libraries; keep only opencv3_catkin's 3.4
# (see lab5/feature_tracking/CMakeLists.txt for the GTK2/GTK3 imshow abort this avoids).
list(FILTER catkin_LIBRARIES EXCLUDE REGEX "libopencv_[a-z0-9_]+\\.so\\.4")
list(FILTER lab_5_LIBRARIES EXCLUDE REGEX "libopencv_[a-z0-9_]+\\.so\\.4")

include_directories(
  include
  ${EIGEN3_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
)

add_library(tracker_shim src/tracker_shim.cpp)
target_include_directories(tracker_shim PRIVATE ${lab_5_INCLUDE_DIRS})
target_link_libraries(tracker_shim PRIVATE ${lab_5_LIBRARIES})

add_executable(pose_estimation src/pose_estimation.cpp)
target_link_libraries(pose_estimation tracker_shim ${catkin_LIBRARIES} ${GLOG_LIBRARY} ${GFLAGS_LIBRARY})
