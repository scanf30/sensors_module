#!/usr/bin/env python
import time
import serial
import string #
import os
from lib.GpsLibrary import GpsLibrary
#Import ros"
import rospy
from geometry_msgs.msg import Twist
from gps_common.msg import GPSFix
import roslib
#from gps_ros_test.msg import GpsMyMsg
"""
#import gpio revisar
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
data='hi'
gpsdata = GpsLibrary()
"""
#FILE = open("GPSErroData.txt", "w")

#pGps = Twist()
pGps = GPSFix()

def gps():
    global pGps
    os.system("sudo chmod 777 /dev/ttyAMA0")
    port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
    ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
    gpsdata= GpsLibrary()
    pub = rospy.Publisher('GPS',GPSFix, queue_size=10)
    rospy.init_node('gps',anonymous=True)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        try:
	        data = ser.readline() 
        except:
            print("loading")
        
        Gprmc_fl = 0
		#Check if the data is read from serial and is save in 'data' is the type GPRMC
        if data[0:6]=='$GPRMC':
		#If is the case call the method parse GPRMC which request the data that is read from serial,in order to split it
            gpsdata.parseGPRMC(data)
            Gprmc_fl = 1
		#Check if the data is read from serial and is save in 'data' is the type GPGGA
        if data [0:6] == '$GPGGA':
		#If is the case call the method parse GPGGA which request the data that is read from serial,in order to split it
            gpsdata.parseGPGGA(data)
        try:
            #rospy.loginfo(data)
            pGps.latitude  = float(gpsdata.lat)
            pGps.longitude = float(gpsdata.lon)
            pGps.track     = float(gpsdata.angle)
            #pGps.linear.x =  float(gpsdata.lat)
            #pGps.linear.y =  float(gpsdata.lon)
            #pGps.linear.z =  float(gpsdata.angle)
            #pGps.angular.x = float(gpsdata.speed)
            #pGps.angular.y = int(gpsdata.quality)
            #pGps.angular.z = int(gpsdata.satellites)
            
            if gpsdata.errorGprmc == 0 and gpsdata.errorGgpga == 0 and Gprmc_fl == 1:
                rospy.loginfo(pGps)
                pub.publish(pGps)
            else:
                gpsdata.errorGprmc = 0
                gpsdata.errorGgpga = 0
        except:
            #Gps = Twist()
            print "dato del gps corrupto"

        now = rospy.get_rostime()
        secs = now.to_sec()
        
        '''
        if ((gpsdata.errorGgpga == 1) or (gpsdata.errorGprmc == 1)):
            FILE.write("\nGPS...............[ %.4f ]\n" % (secs))
            FILE.write("Data: %s\n" % (data))
            FILE.write("Ggpga: %i\n" % (gpsdata.errorGgpga))
            FILE.write("GgpRMC: %i\n" % (gpsdata.errorGprmc))
            gpsdata.errorGprmc = 0
            gpsdata.errorGgpga = 0
        '''

        time.sleep(.1)



"""        
        try:
            if data[0:6]=='$GPRMC':
		#If is the case call the method parse GPRMC which request the data that is read from serial,in order to split it
                gpsdata.parseGPRMC(data)
		#Check if the data is read from serial and is save in 'data' is the type GPGGA
            if data [0:6] == '$GPGGA':
		#If is the case call the method parse GPGGA which request the data that is read from serial,in order to split it
                gpsdata.parseGPGGA(data)
            rospy.loginfo(data)
            pGps.linear.x = float(gpsdata.lat)
            pGps.linear.y = float(gpsdata.lon)
            pGps.linear.z = float(gpsdata.angle)
            pGps.angular.x = float(gpsdata.speed)
            pGps.angular.y = int(gpsdata.quality)
            pGps.angular.z = int(gpsdata.satellites)
            rospy.loginfo(pGps)
            pub.publish(pGps)


        #except:
            #pGps = Twist()
           # print "dato del gps corrupto"


        #rospy.loginfo(pGps)
        #pub.publish(pGps)
        time.sleep(.5)
"""

#wait for the serial port to churn out data
if __name__=='__main__':
    try:
        gps()
    except rospy.ROSInterruptException:
        pass
       

