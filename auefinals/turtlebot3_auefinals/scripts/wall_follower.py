#! /usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np
import math
from nav_msgs.msg import Odometry
# reference :
# distance between the walls -  #bot scan reading at one extreme 0.12
                                #bot scan reading at other exterme 1.2
# we might want to add a D controller in this code.


def callback(data):
    # Acquire LiDAR data
    sweep = list(data.ranges[0:360])
    # Filter LiDAR sweep values to a reasonable range   
    filtered_sweep = [v for v in sweep if not v > 50]
    # Define right and left sweep by slicing filtered_sweep 
    right_sweep = filtered_sweep[300:360]
    left_sweep = filtered_sweep[0:60]
    right_mean = sum(right_sweep)/len(right_sweep)
    left_mean = sum(left_sweep)/len(left_sweep)
    # Define error between left and right average distance
    diff = right_mean - left_mean
    threshold =  0
    error = diff - threshold
    # print(error)
    # Define controller gains
    kp = rospy.get_param('kp') #0.4
    kd = rospy.get_param('kd') #0.3
    speed = rospy.get_param('speed') #0.2

    if (error > 0.05 ):
        velocity_msg.angular.z = -kp * error #+ kd * (error - error_prev) / 0.34
        velocity_msg.linear.x = speed

    elif (error < -0.05 ):
        velocity_msg.angular.z = -kp * error
        velocity_msg.linear.x = speed
    else:
        velocity_msg.angular.z = 0
        velocity_msg.linear.x = speed
    error_prev = error

rospy.init_node('turtle_control', anonymous=True)
velocity_msg=Twist()
pub = rospy.Publisher('cmd_vel', Twist, queue_size= 10)
scan_sub = rospy.Subscriber('scan', LaserScan,callback)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(velocity_msg)
    rate.sleep()
    pass