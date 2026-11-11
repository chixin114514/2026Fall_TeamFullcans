cmake_minimum_required(VERSION 3.0.2)
project(eigen_catkin)
find_package(catkin REQUIRED)
# Downstream packages (opengv, lab_6) only need the Eigen include path;
# it is added by cmake/eigen_catkin-extras.cmake when they find_package(eigen_catkin).
catkin_package(CFG_EXTRAS eigen_catkin-extras.cmake)
