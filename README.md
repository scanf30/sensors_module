# sensors_module

- GPS ready

# robot startup (node launches automatically at startup)

For robot_upstart to load node at startup, it is needed the following code at /etc/ros/setup.bash

```
#Ros Config
export ROBOT_SETUP=/etc/ros/setup.bash
export ROS_MASTER_URI=http://192.168.0.100:11311
export ROS_HOSTNAME=192.168.0.220
export ROS_IP=192.168.0.220
export HOME=/home/sensors

source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash

```

If you want to debug the startup service use the command

```
sudo gps-start
```

To ckeck the service file check the path /usr/sbin/gps-start
