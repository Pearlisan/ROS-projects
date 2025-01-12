pearlisan@DESKTOP-K4897N8:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy

pearlisan@DESKTOP-K4897N8:~$ source /opt/ros/humble/setup.bash
pearlisan@DESKTOP-K4897N8:~$ printenv ROS_DISTRO
humble

sudo apt upgrade
sudo apt-get install gedit
sudo apt install ros-humble-robot-state-publisher
sudo apt install ros-humble-joint-state-publisher
sudo apt install ros-humble-joint-state-publisher-gui
ros2 pkg prefix rviz2

<!-- colcon build wasn't working so I had to do this extra step -->
sudo sh -c 'echo "deb [arch=amd64,arm64] http://repo.ros2.org/ubuntu/main `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
<!-- Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).  -->Using sudo apt-key-add brings up this error use the next step instead

curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo tee /etc/apt/trusted.gpg.d/ros.asc
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQINBFzvJpYBEADY8l1YvO7iYW5gUESyzsTGnMvVUmlV3XarBaJz9bGRmgPXh7jc
VFrQhE0L/HV7LOfoLI9H2GWYyHBqN5ERBlcA8XxG3ZvX7t9nAZPQT2Xxe3GT3tro
u5oCR+SyHN9xPnUwDuqUSvJ2eqMYb9B/Hph3OmtjG30jSNq9kOF5bBTk1hOTGPH4
K/AY0jzT6OpHfXU6ytlFsI47ZKsnTUhipGsKucQ1CXlyirndZ3V3k70YaooZ55rG
aIoAWlx2H0J7sAHmqS29N9jV9mo135d+d+TdLBXI0PXtiHzE9IPaX+ctdSUrPnp+
TwR99lxglpIG6hLuvOMAaxiqFBB/Jf3XJ8OBakfS6nHrWH2WqQxRbiITl0irkQoz
pwNEF2Bv0+Jvs1UFEdVGz5a8xexQHst/RmKrtHLct3iOCvBNqoAQRbvWvBhPjO/p
V5cYeUljZ5wpHyFkaEViClaVWqa6PIsyLqmyjsruPCWlURLsQoQxABcL8bwxX7UT
hM6CtH6tGlYZ85RIzRifIm2oudzV5l+8oRgFr9yVcwyOFT6JCioqkwldW52P1pk/
/SnuexC6LYqqDuHUs5NnokzzpfS6QaWfTY5P5tz4KHJfsjDIktly3mKVfY0fSPVV
okdGpcUzvz2hq1fqjxB6MlB/1vtk0bImfcsoxBmF7H+4E9ZN1sX/tSb0KQARAQAB
tCZPcGVuIFJvYm90aWNzIDxpbmZvQG9zcmZvdW5kYXRpb24ub3JnPokCVAQTAQgA
PgIbAwULCQgHAgYVCgkICwIEFgIDAQIeAQIXgBYhBMHPbjHmut6IaLFytPQu1vur
F8ZUBQJgsdhRBQkLTMW7AAoJEPQu1vurF8ZUTMwP/3f7EkOPIFjUdRmpNJ2db4iB
RQu5b2SJRG+KIdbvQBzKUBMV6/RUhEDPjhXZI3zDevzBewvAMKkqs2Q1cWo9WV7Z
PyTkvSyey/Tjn+PozcdvzkvrEjDMftIk8E1WzLGq7vnPLZ1q/b6Vq4H373Z+EDWa
DaDwW72CbCBLWAVtqff80CwlI2x8fYHKr3VBUnwcXNHR4+nRABfAWnaU4k+oTshC
Qucsd8vitNfsSXrKuKyz91IRHRPnJjx8UvGU4tRGfrHkw1505EZvgP02vXeRyWBR
fKiL1vGy4tCSRDdZO3ms2J2m08VPv65HsHaWYMnO+rNJmMZj9d9JdL/9GRf5F6U0
quoIFL39BhUEvBynuqlrqistnyOhw8W/IQy/ymNzBMcMz6rcMjMwhkgm/LNXoSD1
1OrJu4ktQwRhwvGVarnB8ihwjsTxZFylaLmFSfaA+OAlOqCLS1OkIVMzjW+Ul6A6
qjiCEUOsnlf4CGlhzNMZOx3low6ixzEqKOcfECpeIj80a2fBDmWkcAAjlHu6VBhA
TUDG9e2xKLzV2Z/DLYsb3+n9QW7KO0yZKfiuUo6AYboAioQKn5jh3iRvjGh2Ujpo
22G+oae3PcCc7G+z12j6xIY709FQuA49dA2YpzMda0/OX4LP56STEveDRrO+CnV6
WE+F5FaIKwb72PL4rLi4
=i0tj
-----END PGP PUBLIC KEY BLOCK-----

sudo apt update
sudo apt upgrade
sudo apt install python3-colcon-common-extensions 



<!-- TO START A NEW WORKSPACE -->
<!-- Source the environment -->
source /opt/ros/humble/setup.bash
mkdir -p ~/scara_robot_assg_ws/src
cd ~/scara_robot_assg_ws/src
colcon build

<!-- To see if the directory was made ise ls -l -->
ls -l 

cd ~/scara_robot_assg_ws/src
ros2 pkg create --build-type ament cmake my_scara_robot

cd ~/scara_robot_assg_ws/src/my_scara_robot
ls -l

pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot$ mkdir launch urdf config
ls -l

pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws$ colcon build

cd ~/scara_robot_assg_ws/src/my_scara_robot/urdf
gedit robot.urdf <!--if command gedit was not found: sudo apt-get install gedit -->

pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot/urdf$ gedit robot.urdf

pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src$ cd ~/scara_robot_assg_ws/src/my_scara_robot
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot$ ls -l
total 28
  -rw-r--r-- 1 pearlisan pearlisan  909 Dec 22 13:56 CMakeLists.txt
  drwxr-xr-x 2 pearlisan pearlisan 4096 Dec 22 14:04 config
  drwxr-xr-x 3 pearlisan pearlisan 4096 Dec 22 13:56 include
  drwxr-xr-x 2 pearlisan pearlisan 4096 Dec 22 14:04 launch
  -rw-r--r-- 1 pearlisan pearlisan  797 Dec 22 19:10 package.xml
  drwxr-xr-x 2 pearlisan pearlisan 4096 Dec 22 13:56 src
  drwxr-xr-x 2 pearlisan pearlisan 4096 Dec 22 19:04 urdf
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot$ gedit package.xml

<!-- Add this line to window that popped up -->
<exec_depend>joint_state_publisher</exec_depend>
<exec_depend>joint_state_publisher_gui</exec_depend>
<exec_depend>robot_state_publisher</exec_depend>
<exec_depend>rviz</exec_depend>
<!-- Between test_depend and export -->

<!-- Next line -->
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot$ cd ~/scara_robot_assg_ws/src/my_scara_robot/launch

pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot/launch$ gedit display.launch.py
<!-- Paste code in display.py in the window that popped up -->

pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot$ gedit CMakeLists.txt
<!-- Add this to the pop up menu before if(BUILD_TESTING) - Colcon build will now know where the source files, urdf launch % config, are located -->
install(
	DIRECTORY launch urdf config
	DESTINATION share/${PROJECT_NAME}
)

<!-- go back to root directory -->
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws/src/my_scara_robot$ cd ~
/scara_robot_assg_ws/
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws$ colcon build

<!-- *You may run into this error -->
[0.782s] WARNING:colcon.colcon_ros.prefix_path.ament:The path '/home/pearlisan/lesson2_6dof/install/lesson2_6dof' in the environment variable AMENT_PREFIX_PATH doesn't exist
[0.782s] WARNING:colcon.colcon_ros.prefix_path.catkin:The path '/home/pearlisan/lesson2_6dof/install/lesson2_6dof' in the environment variable CMAKE_PREFIX_PATH doesn't exist
<!-- *try this  -->
export AMENT_PREFIX_PATH=/home/pearlisan/lesson2_6dof/install/robot_6dof:$AMENT_PREFIX_PATH
export CMAKE_PREFIX_PATH=/home/pearlisan/lesson2_6dof/install/robot_6dof:$CMAKE_PREFIX_PATH
<!-- *then if error persist -->
export AMENT_PREFIX_PATH=/home/pearlisan/lesson2_6dof/install/robot_6dof:/opt/ros/humble
export CMAKE_PREFIX_PATH=/home/pearlisan/lesson2_6dof/install/robot_6dof
<!-- *end of special error -->

<!-- then source the set-up file -->
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws$ source ~/scara_robot_assg_ws/install/setup.bash
<!-- Launch rviz -->
pearlisan@DESKTOP-K4897N8:~/scara_robot_assg_ws$ ros2 launch my_scara_ro
bot display.launch.py





<!-- CONFIGURING RVIZ -->
Add (bottom left) ->robot model->ok
Robotmodel -> Description topic -> /robot description
fixed frame -> base link
To see coordinate system: Add-> TF
Robot model -> visual enabled (untick box)

<!-- To save this configuration for all rviz files -->
file -> save config as
or file -> home -> ~/scara_robot_assg_ws -> src -> my_scara_robot -> config
<!-- this file name is gotten from the display.py file under the rvizConfigPath -->
filename = config.rviz