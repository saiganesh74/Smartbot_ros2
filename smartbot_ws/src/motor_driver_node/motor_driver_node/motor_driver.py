import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
class MotorDriverNode(Node):
    def __init__(self):
        super().__init__('motor_driver')
        self.subscription = self.create_subscription(
            Twist ,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )
    def cmd_vel_callback(self,msg):
        linear = msg.linear.x
        angular = msg.angular.z
        
        left_speed = linear-angular
        right_speed = linear+angular 
        self.get_logger().warn(f'Motor Speeds: Left -->{left_speed} and right ---> {right_speed}')
def main(args = None):
    rclpy.init(args=args)
    node = MotorDriverNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__== '__main__':
    main()