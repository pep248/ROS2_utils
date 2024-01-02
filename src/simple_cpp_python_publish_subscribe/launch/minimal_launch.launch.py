#!/usr/bin/env python3

import sys
from launch import LaunchService

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

        return LaunchDescription([
                # publisher_node
                Node(
                        package='simple_cpp_python_publish_subscribe',
                        executable='publisher_cpp',
                        output='screen',
                        name='publisher_cpp_node',
                ),
                # subscriber_node
                Node(
                        package='simple_cpp_python_publish_subscribe',
                        executable='subscriber_cpp',
                        output='screen',
                        name='subscriber_cpp_node',
                ),
        ])
        

if __name__ == '__main__':
    desc = generate_launch_description()
    service = LaunchService(argv=sys.argv[1:])
    service.include_launch_description(desc)
    service.run()        