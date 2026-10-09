cmake_minimum_required(VERSION 3.0.2)
project(two_drones_pkg)

add_compile_options(-Wall -Wextra -Wpedantic)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  tf2
  tf2_ros
  visualization_msgs
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs roscpp rospy tf2 tf2_ros visualization_msgs
)

include_directories(${catkin_INCLUDE_DIRS})

add_executable(frames_publisher_node src/frames_publisher_node.cpp)
target_link_libraries(frames_publisher_node ${catkin_LIBRARIES})

add_executable(plots_publisher_node src/plots_publisher_node.cpp)
target_link_libraries(plots_publisher_node ${catkin_LIBRARIES})

install(TARGETS frames_publisher_node plots_publisher_node
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch config mesh
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
