#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np 
import math

from nav_msgs.msg import Odometry

def divide(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 1000


def callback(data):
    # Gather data from the LiDAR
    left = data.ranges[5:45]
    front = data.ranges[0:5] + data.ranges[355:360]
    right = data.ranges[320:355] 
    # Filters out unnecessary values detected by the LiDAR
    filtered_left = [num for num in left if num<1000]
    filtered_right = [num for num in right if num<1000]
    filtered_front = [num for num in front if num<1000]
    # Average readings of the LiDAR 
    avg_left =  divide(sum(filtered_left),len(filtered_left))
    avg_right= divide(sum(filtered_right),len(filtered_right))
    avg_front = divide(sum(filtered_front),len(filtered_front))
    # Calculate the minimum distance detected by the LiDAR
    closest_dist = min(avg_left,avg_right,avg_front)
    # Gain used as input to angular speed in z direction
    kz = 1.5
    # Define important parameters of turtlebot
    distance_target = rospy.get_param('distance_target')
    speed = rospy.get_param('speed')

    if closest_dist < distance_target: 
        print('obstacle ahead!')
        if closest_dist == avg_left:
            velocity_msg.angular.z = -kz/(closest_dist)
            velocity_msg.linear.x = 0.0
        elif closest_dist == avg_right:
            velocity_msg.angular.z = kz/(closest_dist)
            velocity_msg.linear.x = 0.0
        elif closest_dist == avg_front:
            velocity_msg.angular.z = kz/(closest_dist)
            velocity_msg.linear.x = 0.0
        else: 
            velocity_msg.angular.z = 0
            velocity_msg.linear.x = speed
    else:
        print('cruising..')
        velocity_msg.angular.z = 0
        velocity_msg.linear.x = speed
    pub.publish(velocity_msg)

rospy.init_node('turtle_control', anonymous=True)
velocity_msg=Twist()
pub = rospy.Publisher('cmd_vel', Twist, queue_size= 10)
scan = rospy.Subscriber('scan', LaserScan,callback)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(velocity_msg)
    rate.sleep()
    pass