<!-- PLEASE TAKE NOTE OF PATH CHANGES -->

sudo apt-get update
sudo apt-get upgrade
<!-- Then restart pc is anything upgraded -->

source /opt/ros/humble/setup.bash
pearlisan@Pearlisan:~$ sudo apt-get install gedit
pearlisan@Pearlisan:~$ sudo apt install ros-humble-joint-state-publisher
pearlisan@Pearlisan:~$ sudo apt install ros-humble-joint-state-publisher-gui
pearlisan@Pearlisan:~$ sudo apt install ros-humble-xacro
pearlisan@Pearlisan:~$ sudo apt install ros-humble-ros-gz
pearlisan@Pearlisan:~$ sudo apt install ros-humble-gazebo-ros-pkgs
pearlisan@Pearlisan:~$ sudo apt install ros-humble-ros-core

pearlisan@Pearlisan:~$ sudo apt install ros-humble-geometry2
pearlisan@Pearlisan:~$ sudo apt-get install ros-humble-gazebo-msgs
pearlisan@Pearlisan:~$ sudo apt-get install ros-humble-gazebo-plugins

pearlisan@Pearlisan:~$ sudo apt-get install ros-humble-ros-ign-bridge
pearlisan@Pearlisan:~$ sudo apt-get install ros-humble-teleop-twist-keyboard

pearlisan@Pearlisan:~$ gazebo   <!-- to check if gazebo was installed-->
pearlisan@Pearlisan:~$ gazebo --version
<!-- Gazebo multi-robot simulator, version 11.10.2 -->


pearlisan@Pearlisan:~$ source /opt/ros/humble/setup.bash
pearlisan@Pearlisan:~$ mkdir -p ~/lesson_differential_drive_robot/src
pearlisan@Pearlisan:~$ cd lesson_differential_drive_robot/
<!-- Show directory path using pwd -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ pwd
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ colcon build
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ ls -la 
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src$ ros2 pkg create --build-type ament_cmake mobile_dd_robot

pearlisan@Pearlisan:~/lesson_differential_drive_robot/src$ cd mobile_dd_robot
<!-- Model file contains urdf and xacro file, launch has python file -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src/mobile_dd_robot$ mkdir launch model
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ colcon build

pearlisan@Pearlisan:~/lesson_differential_drive_robot$ cd ~/lesson_differential_drive_robot/src/mobile_dd_robot/model

<!-- see files in the folder for the following below, copy and paste in gedit. PLEASE NOTE THE PATH CHANGES -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src/mobile_dd_robot/model$ gedit robot.xacro
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src/mobile_dd_robot/model$ gedit robot.gazebo
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src/mobile_dd_robot/launch$ gedit gazebo_model.launch.py
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src/mobile_dd_robot$ g
edit package.xml
        <!--Paste this Between test_depend and export --> 
        <exec_depend>joint_state_publisher</exec_depend>
        <exec_depend>robot_state_publisher</exec_depend>
        <exec_depend>gazebo_ros</exec_depend>
        <exec_depend>xacro</exec_depend>
        <exec_depend>ros_gz_bridge</exec_depend>

<!-- Adjust the CMakeLists so that it knows that there are two important files are in the folders launch and model -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot/src/mobile_dd_robot$ g
edit CMakeLists.txt
      <!-- Append this before if (BUILD_TESTING) -->
      install(
        DIRECTORY launch model
        DESTINATION share/${PROJECT_NAME}
      )

<!-- go back to home folder -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ colcon build
<!-- Source the package -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ source ~/lesson_differential_drive_robot/install/setup.bash

<!-- Launch the model in gazebo -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ ros2 launch mobile_dd_robot gazebo_model.launch.py

<!-- To see topic list while gazebo os running -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ ros2 topic list

<!-- TO see what is communicated to odometry -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ ros2 topic echo /odom

<!-- what is being communicated through command velocity -->
pearlisan@Pearlisan:~/lesson_differential_drive_robot$ ros2 topic info /cmd_vel