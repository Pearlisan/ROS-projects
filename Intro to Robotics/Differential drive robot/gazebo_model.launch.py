import os
from ament_index_python. packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
import xacro


def generate_launch_description():

  # this name has to match the robot name in the Xacro file
  # Must match name in xacro file, check first line
  robotXacroName='differential_drive_robot'

  # this is the name of our package, at the same time this is the name of the
  # folder that will be used to define the paths
  namePackage = 'mobile_dd_robot'

  # this is a relative path to the xacro file defining the model
  modelFileRelativePath = 'model/robot.xacro'
  # this is a relative path to the Gazebo world file
  worldFileRelativePath = 'model/empty_world.world'

  # this is the absolute path to the model
  # pathModelFile = mobile_dd_robot/model/robot.xacro
  pathModelFile = os.path.join(get_package_share_directory(namePackage),modelFileRelativePath)

  # this is the absolute path to the world model
  pathWorldFile = os.path.join(get_package_share_directory(namePackage),worldFileRelativePath)
  # get the robot description from the xacro model file
    # pathModelFile = mobile_dd_robot/model/robot.xacro then convert th efile to xml
  robotDescription = xacro.process_file(pathModelFile).toxml()

  # this is the launch file from the gazebo_ros package
  # gazebo_ros is inside the gazebo folder we installed
  gazebo_rosPackageLaunch=PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'),
                                                      'launch', 'gazebo.launch.py'))

  # This is the launch description
  # creates a dictionary with the entry 'world': pathWorldFile}
  gazeboLaunch=IncludeLaunchDescription(gazebo_rosPackageLaunch, launch_arguments={'world': pathWorldFile}.items())
   
  # here, we create a gazebo_ros Node
  # spawn entity is a  standard gazebo python file for creating nodes
  # robotXacroName defines the geometry of the robot
  spawnModelNode = Node(package='gazebo_ros', executable='spawn_entity.py', arguments = ['-topic', 'robot_description','-entity', robotXacroName],output='screen')

  # Robot State Publisher Node
  #  'use_sim_time': True- this creates the robot state publisher node
  nodeRobotStatePublisher = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    output='screen',
    parameters=[{'robot_description': robotDescription,
    'use_sim_time': True}]
  )

  # here we create an empty launch description object
  launchDescriptionObject = LaunchDescription()

  # add gazebo Launch
  launchDescriptionObject.add_action(gazeboLaunch)

  # Here we add 2 nodes
  launchDescriptionObject.add_action(spawnModelNode)
  launchDescriptionObject.add_action(nodeRobotStatePublisher)
  return launchDescriptionObject
