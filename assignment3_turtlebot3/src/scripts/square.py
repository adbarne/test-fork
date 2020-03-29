#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def square():
	# Starts a new node
	rospy.init_node('squarebot_OL', anonymous=True)
	position_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	#Receiving the user's input
	print("Moving robot in 2x2 square")
	print(rospy.get_param_names())
	speed = rospy.get_param('speed')							# units/sec
	angleRate = rospy.get_param('angleRate')						# rad/sec
	side_length = rospy.get_param('side_length')						# define side length for square
	#Since we are moving just in x-axis

	#Converting from angles to radians
	# relative_angle = angleRate*
	angle = 0.5*PI

	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0

	#Loop to move the turtle in an specified distance
	for sides in range(4):
		# #Setting the current time for distance calculus
		t0 = float(rospy.Time.now().to_sec())
		# while loop which moves the turtlebot
		current_distance = 0
		while (current_distance < side_length):
			vel_msg.linear.x = speed
			vel_msg.angular.z = 0
			position_publisher.publish(vel_msg)
			t1 = float(rospy.Time.now().to_sec())
			current_distance = speed*(t1-t0)
			# print(current_distance)

		t0 = float(rospy.Time.now().to_sec())
		# while loop which turns the turtlebot
		current_angle = 0
		while (current_angle < angle):
			vel_msg.linear.x = 0
			vel_msg.angular.z = angleRate
			position_publisher.publish(vel_msg)
			t2 = float(rospy.Time.now().to_sec())
			current_angle = angleRate*(t2-t0)
			# print(current_angle)
			

	#After the loop, stops the robot
	vel_msg.linear.x = 0
	vel_msg.angular.z = 0
	#Force the robot to stop
	position_publisher.publish(vel_msg)
		


if __name__ == '__main__':
    try:
        #Testing our function
        square()
    except rospy.ROSInterruptException: pass
