from omnicar_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class Sum(Node):
    def __init__(self):
        super().__init__('sum')
        self.srv = self.create_service(AddTwoInts, 'omnicar_service', self.omnicar_service)

    def omnicar_service(self, request, response):
        response.sum = request.numbera + request.numberb
        self.get_logger().info(f'Incoming request: a={request.numbera}, b={request.numberb}')
        return response

def main():
    rclpy.init()
    sum_service = Sum()
    rclpy.spin(sum_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
