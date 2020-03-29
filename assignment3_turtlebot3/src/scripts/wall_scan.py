#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rospy import Time

def callback(data): 
    # print len(data.ranges)
    left_sweep = data.ranges[0:45]
    right_sweep = data.ranges[314:359]      
    total_sweep = left_sweep + right_sweep
    middle_reading = total_sweep[0:10]+total_sweep[349:359]
    # print(middle_reading)
    if min(middle_reading)< 0.3:
        print('Stopping!!!')
        velocity_msg.linear.x = 0
    else: 
        print('Going Straight.....')
        velocity_msg.linear.x = 1
    return velocity_msg

rospy.init_node('turtle_control', anonymous=True)
velocity_msg=Twist()
pub = rospy.Publisher('cmd_vel', Twist, queue_size= 10) 
sub = rospy.Subscriber('scan', LaserScan,callback)
# rate = rospy.Rate(3)

while not rospy.is_shutdown():
    pub.publish(velocity_msg)
    # rate.sleep()