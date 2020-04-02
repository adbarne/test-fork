#################################### OVERVIEW OF CONTENT ####################################

The contents of this package include the solutions to the following 2 tasks:

1. Line following in gazebo with launch file and python script
2. Apriltag following on the turtlebot with launch file and python script

#################################### HOW TO RUN EACH PART ###################################

1. Line following (Gazebo): 

	(In Gazebo): Open terminal, run "roslaunch assignment5_trackingandfollowing gazebo_follow_line.launch"  

2. Line following (turtlebot): 
	
	(On remote PC): Open a terminal, run "roscore"
	(On remote PC): Open a new terminal for turtlebot commands, run "ssh pi@<raspberry_pi_ipv4>"

	(On turtlebot): Bringup the turtlebot, "roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch"
	(On turtlebot): Open new terminal, "roslaunch turtlebot3_bringup turtlebot3_robot.launch"
	
	(On remote PC): Open terminal, run "roslaunch assignment5_trackingandfollowing turtlebot3_follow_line.launch"

3. Apriltag following:

	(On remote PC): Open a terminal, run "roscore"
	(On remote PC): Open a new terminal for turtlebot commands, run "ssh pi@<raspberry_pi_ipv4>"

	(On turtlebot): Bringup the turtlebot, "roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch"
	(On turtlebot): Open new terminal, "roslaunch turtlebot3_bringup turtlebot3_robot.launch"

	(On remote PC): run, "roslaunch apriltag_ros apriltag.launch"

#################################### DESCRIPTION OF EACH PART ###############################

1. Line following:

This code focuses on handout7, which aims to implement line following code for the turtlebot both in Gazebo and in the real world. To do this, changes had to be made in follow_line_step_hsv.py. First, a twist object was created so that commands for the turtlebot movement could be published to /cmd_vel. Then, a proportional steering controller was implemented fed by the error produced between the calculated centroid of the yellow line in the image frame to the center of the image frame in the x direction. Arguments in the launch files include the proportional gain for the steering controller, kp.  

2. Apriltag following:

This code utilized a prebuilt apriltag ROS repository, which provides code that enables april tag detection. Before carrying out apriltag detection, however, the camera on the turtlebot was calibrated and saved onto the device firmware. Once the camera was calibrated, the following steps specified in part 2 above were carried out for each new session with the turtebot.

#################################### MEMBER CONTRIBUTIONS ###################################

Bhooshan - Implementation of problem 2 code to robot, controller for april tag following, controller for line following.
Abhishek - Implementation of followtag.py to turtlebot, controller for problem 1 line following, followtag.py.
Rahul - Implementation of followtag.py to turtlebot, launch file for problem 1 (turtlebot implementation), followtag.py.
Drew - README, launch file for problem 1 (gazebo), controller for april tag following, gazebo videos.