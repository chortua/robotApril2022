#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyCustomeNode(Node): #MODIFY NAME
    def __init__(self):
        super().__init__("node_name")

def main(args=None):
    rclpy.init(args=args)
    node = MyCustomeNode() # MODIFI NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ = "__main__":
    main()