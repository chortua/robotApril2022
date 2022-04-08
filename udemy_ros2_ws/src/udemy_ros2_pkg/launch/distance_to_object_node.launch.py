from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="udemy_ros2_pkg",
            executable = "hc_sensor_publisher.py",
            name="ultrasonic_sensor"
        ),
        ExecuteProcess(
            cmd =['ros2', 'topic', 'list'],
            output='screen'
        )
    ])