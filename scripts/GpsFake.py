#!/usr/bin/env python
import time
import serial
import string #
import os
from lib.GpsLibrary import GpsLibrary
#Import ros"
import rospy
from geometry_msgs.msg import Twist
import roslib
#FILE = open("GPSErroData.txt", "w")

pGps = Twist()
directory = os.path.expanduser("~/catkin_ws/src/gps_ros_test/scripts/GpsLog/")
filename = "GPSLog_CHIDO.txt"

def gps():
    global pGps
    global directory
    global filename
    '''
    os.system("sudo chmod 777 /dev/ttyAMA0")
    port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
    ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
    '''
    gpsdata = GpsLibrary()
    pub = rospy.Publisher('gpsfake',Twist, queue_size=10)
    rospy.init_node('gps_fake',anonymous=True)
    rate = rospy.Rate(5)

    #OPEN FILE
    FILE = open(directory+filename,"r") 
    first_data = 1    
    
    #timing for each pub
    prev_time = 0
    curr_time = 0

    while not rospy.is_shutdown():

        #data = ser.readline()
        data = FILE.readline()
        if data is None or len(data) == 0:
            FILE.close()
            time.sleep(1.0) 
            FILE = open(directory+filename,"r")
            first_data = 1    
        else:
            #print("esto es data: %s %d\n" % (data,len(data)))
            datagps = data.split(',')
            curr_time           = float(datagps[0])
            gpsdata.lat         = datagps[1]
            gpsdata.lon         = datagps[2]
            gpsdata.angle       = datagps[3]
            gpsdata.speed       = datagps[4]
            gpsdata.quality     = datagps[5]
            gpsdata.satellites  = datagps[6]
            
            #try:
            #rospy.loginfo(data)
            pGps.linear.x =  float(gpsdata.lat)
            pGps.linear.y =  float(gpsdata.lon)
            pGps.linear.z =  float(gpsdata.angle)
            pGps.angular.x = float(gpsdata.speed)
            pGps.angular.y = float(gpsdata.quality)
            pGps.angular.z = float(gpsdata.satellites)

            if first_data:
                first_data = 0
                time.sleep(.1)
                rospy.loginfo(pGps)
                pub.publish(pGps)
            else:
                diff = curr_time - prev_time
                time.sleep(diff)
                rospy.loginfo(pGps)
                pub.publish(pGps)

            prev_time = curr_time

            #except:
            #    print "dato del gps corrupto"

        
        '''
        if ((gpsdata.errorGgpga == 1) or (gpsdata.errorGprmc == 1)):
            FILE.write("\nGPS...............[ %.4f ]\n" % (secs))
            FILE.write("Data: %s\n" % (data))
            FILE.write("Ggpga: %i\n" % (gpsdata.errorGgpga))
            FILE.write("GgpRMC: %i\n" % (gpsdata.errorGprmc))
            gpsdata.errorGprmc = 0
            gpsdata.errorGgpga = 0
        '''

#wait for the serial port to churn out data
if __name__=='__main__':
    try:
        gps()
    except rospy.ROSInterruptException:
        pass
       

