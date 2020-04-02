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
	z_ang_tag = data.detections[0].pose.pose.pose.orientation.z
	# print(x_tag,y_tag,z_ang_tag)

	# Enter Controller
	move = Twist()
	# lateral error
	y_error = y_tag
	x_error = 0.5 - x_tag
	kp = 1
	# kd = 
	if abs(y_error) >= 0.1:
		move.angular.z = kp*y_error
	else:	
		move.angular.z = 0

	if abs(x_error) >= 0.1:
		move.linear.x = kp*x_error
	else:
		move.linear.x = 0
	# print(move.linear.x, move.angular.z)

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