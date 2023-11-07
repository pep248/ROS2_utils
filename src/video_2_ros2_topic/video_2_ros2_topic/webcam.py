#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import os

class ImagePublisher(Node):
    def __init__(self,video_device : int, topic : str):
        super().__init__("image_publisher")
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(int(video_device))
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.pub = self.create_publisher(Image, topic, 10)
        self.rgb8pub = self.create_publisher(Image, topic + "/rgb", 10)
        self.bgr8pub = self.create_publisher(Image, topic + "/bgr", 10)
        self.mono8pub = self.create_publisher(Image, topic + "/mono", 10)

    def run(self):
        while rclpy.ok():
            try:
                r, frame = self.cap.read()
                if not r:
                    return
                self.pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))

                # BGR8
                self.bgr8pub.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))

                # RGB8
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.rgb8pub.publish(self.bridge.cv2_to_imgmsg(frame_rgb, "rgb8"))

                # MONO8
                frame_mono = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                self.mono8pub.publish(self.bridge.cv2_to_imgmsg(frame_mono, "mono8"))

            except CvBridgeError as e:
                print(e)
       
        self.cap.release()

def main(args=None):
    rclpy.init(args=args)
        
    if(len(sys.argv) != 3):
        print("Incorrect number of arguments\nUsage:\n\tros2 run video_2_ros2_topic webcam -- <video_device_number> </topic> ")
        exit()
    else:
        ip = ImagePublisher(sys.argv[1], sys.argv[2])
    print("Publishing...")
    ip.run()

    ip.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()