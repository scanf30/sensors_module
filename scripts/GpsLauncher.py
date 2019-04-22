#!/usr/bin/env python

import roslaunch
import rospy
from os.path import expanduser

# File to launch
filepath = expanduser("~/catkin_ws/src/gps_ros_test/launch/gps.launch")

#Initialize launcher
rospy.init_node('gps_launcher', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

launch = roslaunch.parent.ROSLaunchParent(uuid, [filepath])
launch.start()
rospy.loginfo("started")

while not rospy.is_shutdown():
    rospy.sleep(1)

launch.shutdown()
