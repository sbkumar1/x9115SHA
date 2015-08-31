################################################################
###Author:- Shashank Bipin Kumar(sbkumar@ncsu.edu)##############
###CODE 2 Exercise 4.2##########################################
################################################################
#!/usr/bin/python -b

import math
from swampy.TurtleWorld import *
import math

turtle_world = TurtleWorld()
turtle = Turtle()
#print bob
def leaves1(t, n, length, angle):
		for i in range(n/4):
			fd(t, length)
			lt(t, angle)
		rt(t,180)
		for i in range(n/4):
			rt(t,angle)
			pu(t)
			fd(t,length)
			pd(t)
		for i in range(n/4):
			fd(t, length)
			rt(t, angle)
		rt(t,180)
		for i in range(n/4):
			lt(t,angle)
			pu(t)
			fd(t,length)
			pd(t)
		lt(t,360/7)
#Below Function is taken from the book "Think Python" Page 36
def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)
#Below Function is taken from the book "Think Python" Page 36
def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)
	
def overlap_leaves(t, n, r):
	angle1=360.0/n
	angle=angle1*2
	for i in range(n):
	        for i in range(2):
			arc(t, r, angle)
			lt(t, 180-angle)
	        lt(t, 360.0/n)
def leaves(t, n, r):
	angle=360/n
	for i in range(n):
	        for i in range(2):
			arc(t, r, angle)
			lt(t, 180-angle)
	        lt(t, 360.0/n)
leaves(turtle, 20, 200)
#leaves(turtle, 7, 200)
#overlap_leaves(turtle,10,150)
wait_for_user()


