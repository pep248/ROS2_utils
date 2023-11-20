# Video to ROS2 topic
Package to publish the frames of a video into a ROS2 topic or to publish the frames of a video into a ROS2 topic

## Video file to ROS2 topic

'''
ros2 run video_2_ros2_topic video -- <path_to_video_file> </topic>
# example
# ros2 run video_2_ros2_topic video -- /home/user/sqarerootoftwo.mp4 /video
'''

## Webcam to ROS2 topic
Video device, makes reference to the specific device "/dev/video*".
'''
ros2 run video_2_ros2_topic webcam -- <video_device> </topic>
# example
# ros2 run video_2_ros2_topic webcam -- 0 /video
'''


