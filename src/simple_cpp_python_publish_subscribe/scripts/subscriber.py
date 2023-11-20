#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from simple_cpp_python_publish_subscribe.src.subscriber_class import MySubscriber
from rclpy.executors import MultiThreadedExecutor

def main(args=None):
    rclpy.init(args=args)

    # Create nodes
    subscriber_node = MySubscriber()

    # Create executor and add nodes
    executor = MultiThreadedExecutor()
    executor.add_node(subscriber_node)

    try:
        # Run the nodes within the executor
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup
        executor.shutdown()
        subscriber_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()