#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from apriltag_ros.msg import AprilTagDetection
from apriltag_ros.msg import AprilTagDetectionArray
from geometry_msgs.msg import Point
	

def callback(data):
	
	x_tag = data.detections[0].pose.pose.pose.position.x
	y_tag  = data.detections[0].pose.pose.pose.position.y
	z_tag = data.detections[0].pose.pose.pose.position.z
	# print(x_tag,y_tag,z_tag)

	# Enter Controller
	move = Twist()
	# lateral error
	publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=20)
	z_error = 0.5 - z_tag
	x_error = -x_tag
	kp_steer = 0.5
	kp_throttle = 0.2
	# kd = 
	# move.linear.x = 1
	if abs(x_error) >= 0.025:
		move.angular.z = kp_steer*x_error
	else:	
		move.angular.z = 0

	if 0.2 <= z_error:
		move.linear.x = kp_throttle*z_error
	# if 0.1 < z_error < 0.2:
	# 	move.linear.x = -kp*z_error
	else:
		move.linear.x = 0 

	# print(move.linear.x, move.angular.z)
	publisher.publish(move)

def follow_tag(): 
	'''Initialize ROS node'''
	rospy.init_node('tag_detector', anonymous=True)
	subscriber = rospy.Subscriber('/tag_detections',AprilTagDetectionArray,callback)
	try: 
		rospy.spin()
	except KeyboardInterrupt:
		print "shutting down the controller"

if __name__ == '__main__':
	follow_tag()