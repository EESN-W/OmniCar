import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'omnicar_topic',
            self.listener_callback,
            10
        )
        self.subscription
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    hello_listener = Listener()
    rclpy.spin(hello_listener)
    hello_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
