cmake_minimum_required(VERSION 3.8)
project(simple_cpp_python_publish_subscribe)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# DEPENDENCIES
find_package(ament_cmake_python REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()


# CPP
# Add the action client executable
ament_auto_add_executable(publisher_cpp src/publisher.cpp)
# Install the executable
install(TARGETS publisher_cpp
  DESTINATION lib/${PROJECT_NAME}
)
# Add the action client executable
ament_auto_add_executable(subscriber_cpp src/subscriber.cpp)
# Install the executable
install(TARGETS subscriber_cpp
  DESTINATION lib/${PROJECT_NAME}
)


# PYTHON
# Install Python modules
ament_python_install_package(${PROJECT_NAME})
# Install Python executables
install(PROGRAMS
  scripts/publisher.py
  scripts/subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()