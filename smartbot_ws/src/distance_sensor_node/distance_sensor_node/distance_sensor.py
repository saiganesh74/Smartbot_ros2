import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32
import random
import time
class DistanceSensorNode(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        self.publisher = self.create_publisher(
            Float32 ,
            '/distance',
            10
        )
        self.timer = self.create_timer(1.0 , self.publish_distance)
    def publish_distance(self):
        distance = random.uniform(5.0 , 100.0)
        msg = Float32()
        msg.data = distance
        self.publisher.publish(msg)
        self.get_logger().warn(f'Distance :{distance:.2f} cm')
def main(args = None):
    rclpy.init(args=args)
    node = DistanceSensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()