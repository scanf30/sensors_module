#!/usr/bin/env python
import rospy
#from gps_ros_test.msg import GpsMyMsg
from geometry_msgs.msg import Twist

pGPS = Twist()
FILE = None

def callback(data):
    global FILE
    global pGPS
    #rospy.loginfo("lat: %d" % (data.linear.x))
    #print data.linear.x
    pGPS = data
    now = rospy.get_rostime()
    secs = now.to_sec()
    FILE.write("%.4f,%.4f,%.4f,%.2f,%.2f,%.1f,%.1f\n" % (secs,data.linear.x,data.linear.y,data.linear.z,data.angular.x,data.angular.y,data.angular.z))

    '''
    FILE.write("\nGPS...............[ %.4f ]\n" % (secs))
    FILE.write("lat: %.6f\n" % (data.linear.x))
    FILE.write("lon: %.6f\n" % (data.linear.y))
    FILE.write("angle: %.6f\n" % (data.linear.z))
    FILE.write("speed: %.6f\n" % (data.angular.x))
    FILE.write("qty: %.1f\n" % (data.angular.y))
    FILE.write("sat: %.1f\n" % (	data.angular.z)) 
    '''
	
    
def listener():
    global FILE
    rospy.init_node('gpstopic_listener',anonymous=True)
    rospy.Subscriber('gpstopic',Twist, callback)
    start = rospy.get_rostime()
    start_secs = start.to_sec()
    filename = "/home/sensors/catkin_ws/src/gps_ros_test/scripts/GpsLog/"+str(int(start_secs))+".txt"
    FILE = open(filename,"w")
    while not rospy.is_shutdown():
        now = rospy.get_rostime()
        secs = now.to_sec()
        if secs-start_secs >= 10.0:
            print("Time: %.4f secs\n" % (secs-start_secs))
            break
    #rospy.spin()
    
if __name__=='__main__':
    listener()
    FILE.close()
     
