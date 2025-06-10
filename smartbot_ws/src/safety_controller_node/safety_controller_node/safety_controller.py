import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
class SafetyControllerNode(Node):
    def __init__(self):
        super().__init__('safety_controller')
        self.distance = 100 
        self.sub_distance = self.create_subscription(
            Float32 , 
            '/distance',
            self.distance_callback,
            10
        )
        self.sub_cmd = self.create_subscription(
            Twist ,
             '/cmd_vel',
             self.cmd_callback , 
             10
        ) 
        self.pub_safe_cmd = self.create_publisher(
            Twist ,
            '/safe_cmd_vel',
            10
        )
    def distance_callback(self,msg):
        self.distance = msg.data
    def cmd_callback(self,msg):
        if self.distance < 20.0 :
            self.get_logger().error('Obstacle too close !!! Stopping the robot')
            msg.linear.x =0.0 
            msg.angular.z = 0.0
        self.pub_safe_cmd.publish(msg)
def main(args = None):
    rclpy.init(args=args)
    node = SafetyControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()