import sys
from omnicar_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class Number(Node):
    def __init__(self):
        super().__init__('number')
        self.cli = self.create_client(AddTwoInts, 'omnicar_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, num1, num2):
        self.req.numbera = num1
        self.req.numberb= num2
        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    number_client = Number()

    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        number_client.get_logger().error('Usage: number.py <num1> <num2>')
        return

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        number_client.get_logger().error('Invalid input: both arguments must be integers.')
        return

    future = number_client.send_request(num1, num2)
    rclpy.spin_until_future_complete(number_client, future)

    if future.result() is not None:
        response = future.result()
        number_client.get_logger().info(
            f'Result of add_two_ints: for {num1} + {num2} = {response.sum}')
    else:
        number_client.get_logger().error('Service call failed.')

    number_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
