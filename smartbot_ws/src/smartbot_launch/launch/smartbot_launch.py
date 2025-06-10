from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='teleop_node',
            executable='teleop',
            name='teleop_node',
            output='screen'
        ),
        Node(
            package='distance_sensor_node',
            executable='distance_sensor',
            name='distance_sensor_node',
            output='screen'
        ),
        Node(
            package='safety_controller_node',
            executable='safety_controller',
            name='safety_controller_node',
            output='screen'
        ),
        Node(
            package='motor_driver_node',
            executable='motor_driver',
            name='motor_driver_node',
            output='screen'
        ),
    ])
