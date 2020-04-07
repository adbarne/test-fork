#!/usr/bin/env python
import rospy
import time 
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from apriltag_ros.msg import AprilTagDetection
from apriltag_ros.msg import AprilTagDetectionArray
from geometry_msgs.msg import Point

def callback(data):
	if data.detections: 
		x = data.detections[0].pose.pose.pose.position.x
		y = data.detections[0].pose.pose.pose.position.y
		z = data.detections[0].pose.pose.pose.orientation.z
		
		move = Twist()

		kpx = 5	
		kpz = 10
		if abs(x) >= 0.1:
			move.angular.z = -kpz*(x)
		else: 
			move.angular.z = 0

		if abs(y) >= 0.1:
			move.linear.x = -kpx*(y-0.1)
		else:
			move.linear.x = 0

		
	else:
		x = 0;y = 0;z = 0
		move = Twist()
		move.linear.x = 0
		move.angular.z = 0
	
	print(y,move.linear.x,'---',x,move.angular.z)
	pub.publish(move)		
if __name__=='__main__':
	try:
		rospy.init_node('turtle_motion', anonymous=True)
		pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		rospy.Subscriber('/tag_detections',AprilTagDetectionArray,callback)
		rate = rospy.Rate(10)
		time.sleep(100000)
		
	except rospy.ROSInterruptException:
		pass	