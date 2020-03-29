Command for launching the turtlebot codes
1. roslaunch assignment3_turtlebot3 move.launch code:=circle
2. roslaunch assignment3_turtlebot3 move.launch code:=square
3. roslaunch assignment3_turtlebot3 turtlebot_collide.launch

Part 1:

1. Moving the turtlebot3 in a circle in Gazebo

The circle.py code has been modified from last assignment to make it work in gazebo. The change made was that the velocity publishing command is now changed to cmd_vel to publish velocity to the turtlebot in gazebo instead of previous turtle1/cmd_vel that would publish velocity to the turtle in turtlesim
To carry out this task, entire the following command in terminal
roslaunch assignment3_turtlebot3 circle.launch

Launch file
circle.launch:
Launches the gazebo environment and spawns the turtlebot. Once this environment is initialized, the turtlebot will move in a circle based on the parameters specified in circle.py. The launch file itself is built upon "turtlebot3_empty_world.launch", where it is modified to run the python script "circle.py". 

2. Moving the turtlebot3 in a square in Gazebo

Just as above, this file has also been modified the same way as above by changing the publisher command.

To carry out this task, entire the following command in terminal
roslaunch assignment3_turtlebot3 square_openloop.launch


Launch file
square_openloop.launch:
Launches the gazebo environment and spawns the turtlebot. Once this environment is initialized, the turtlebot will move in a square with constant linear velocity 0.2 and constant angular velocity 0.2. The launch file itself is built upon "turtlebot3_empty_world.launch", where it is modified to run the python script "square.py". 


3. move.launch

move.launch:
Launches the gazebo environment and spawns the turtlebot. Once this environment is initialized, the turtlebot will move in a square with constant linear velocity 0.2 and constant angular velocity 0.2, or it will move in a circle depending on the arguments passed in the terminal. The launch file itself is built upon "turtlebot3_empty_world.launch", where it is modified to run the python script "square.py" or "circle.py". 

-------------------------------------------------------------------------------------------------

Part 2: Emergency braking on turtlebot3 in gazebo

To find out the distance of the wall from our turtlebot, we need to subscribe to the LIDAR's data. This can be done by using the subscription command 'scan'

The turtlebot is given a linear velocity of 1 in X-direction and its moving straight towards the wall. We store a part of the LIDAR's data i.e. the readings that are in the front 90 deg field of view in an array. This helps the turtlebot continue its travel and not be affected by obstacles in its vicinity that it would not crash into.

The turtlebot stops when the minimum value of our stored array is less than 1.8m.

The launch file for this part was created as follows

launch file - turtlecollide.launch 

launch file arguments :
	1.arg name = "model" 
	values : burger,waffle,waffle_pi
	"changes the robot model in the launch file as per the argument value" 

	2.arg name = "x_pos" "y_pos" "z_pos"  
	values = type <float>, type <float>, type <float>
	"changes initial spawn location of the robot" 

Included files : 
1. empty_world.launch 
	1. File arguments:
		a. arg name = "world_name" 
		value = "custom world.world" (default=turtlebot3_wall.world)
		"turtlebot3_wall.world or turtlebot_house.world located in /worlds folder" 

		b. arg name="paused"
		value = type<boolean> (default false)
		"Start Gazebo in a paused state"
		
		c. arg name="use_sim_time"
		value = type<boolean> (default true)
		Tells ROS nodes asking for time to get the Gazebo-published simulation time, published over the ROS topic /clock
 
		d. arg name="gui"
		value = type<boolean> (default true)
		"Launch the user interface window of Gazebo"

		e. arg name="headless"
		value = type<boolean>
		"Enable gazebo state log recording"

		f. arg name="debug"
		value = type<boolean> (default false)
		"Start gzserver (Gazebo Server) in debug mode using gdb"

Included Nodes: 
1.wall_scan.py 
A node publishing /cmd_vel based on /scan subscription. The bot will perform emergency brakes if there is an obstacle immediately in front of it. 


Member contributions - 

Andrew Barnett - Created the circle and square launch files for part 1
Bhooshan Deshpande - Worked on part 2 code and created its launch file.
Abhishek Bhagwat - Worked on part 2 code and created the world.
Narhari Rahul - Created the move.launch file for part 1

