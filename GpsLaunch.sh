#!/bin/bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash

#Ros Config
export ROS_MASTER_URI=http://192.168.0.100:11311
export ROS_HOSTNAME=192.168.0.220
export ROS_IP=192.168.0.220

echo 'q verga'
~/catkin_ws/src/gps_ros_test/scripts/GpsLauncher.py &
echo 'pero q verga'
exit
