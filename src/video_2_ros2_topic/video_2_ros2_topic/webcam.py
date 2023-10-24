#!/usr/bin/python3
import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImagePublisher(Node):
    def __init__(self):
        super().__init__("image_publisher")
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)
        self.pub = self.create_publisher(Image, "/image", 10)
        self.rgb8pub = self.create_publisher(Image, "/image/rgb", 10)
        self.bgr8pub = self.create_publisher(Image, "/image/bgr", 10)
        self.mono8pub = self.create_publisher(Image, "/image/mono", 10)

    def run(self):
        while True:
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

    ip = ImagePublisher()
    print("Publishing...")
    ip.run()

    ip.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()