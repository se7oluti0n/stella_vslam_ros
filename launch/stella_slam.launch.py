from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, SetRemap
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import Shutdown
import os

def generate_launch_description():
  use_sim_time = LaunchConfiguration('use_sim_time')
  use_sim_time_arg = DeclareLaunchArgument(
    'use_sim_time', default_value='False')



  stella_vslam_ros_dir = get_package_share_directory('stella_vslam_ros')
  param_file = os.path.join(stella_vslam_ros_dir, 'config', 'params.yaml')
  config_file = os.path.join(stella_vslam_ros_dir, 'config', 'd455.yaml')
  bow_file = os.path.join(stella_vslam_ros_dir, 'config', 'orb_vocab.fbow')

  run_vslam = Node(
    package='stella_vslam_ros',
    executable='run_slam',
    output='screen',
    parameters=[param_file, {'use_sim_time': use_sim_time}],
    arguments=["-v", bow_file, "-c", config_file]
  )


  return LaunchDescription([
    use_sim_time_arg,
    run_vslam,
  ])
