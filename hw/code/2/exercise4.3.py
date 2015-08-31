################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###CODE 2 Exercise 4.2##########################################

#!/usr/bin/python -b
import math
from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
#print bob
rt(bob,45)
def polygon(t,sides):
	angle = 360.0/sides	
	top_angle=180-angle
	base_angle=(180-(top_angle/2))
	base_side=100
	cos_angle=(180-angle)/2
	side=50/math.cos(math.radians(cos_angle))
	for i in range(sides):
		rt(t,top_angle)
		fd(t,side)
		rt(t,base_angle)
		fd(t,base_side)
		rt(t,base_angle)
		fd(t,side)
		rt(t,top_angle)
		lt(t,180)


polygon(bob,5)

wait_for_user()







