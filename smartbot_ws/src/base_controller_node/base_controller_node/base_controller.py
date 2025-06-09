import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
class BaseController(Node):
    def __init__(self):
        super().__init__('base_controller')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10
        ) 
        self.subscription
    def listener_callback(self,msg):
        linear = msg.linear.x 
        angular = msg.angular.z
        self.get_logger().warn(f"Recieved cmd_vel: linear{linear:.1f}, angular {angular:.1f}")
def main(args= None):
    rclpy.init(args=args)
    node = BaseController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()