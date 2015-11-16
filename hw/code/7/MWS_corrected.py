#!/usr/bin/python -b
from __future__ import division
import sys
import random,math
random.seed(100)
MWS_MIN=MWS_MAX=0
def randomlist():
	randList=[]
	randList.append(random.uniform(0,10))
	randList.append(random.uniform(0,10))
	randList.append(random.uniform(1,5))
	randList.append(random.uniform(0,6))
	randList.append(random.uniform(1,5))		
	randList.append(random.uniform(0,10))
	return randList

def check_constraint(randList):
	if (((randList[0]+randList[1]-2)>=0) and ((6-randList[0]-randList[1])>=0) and ((2-randList[1]+randList[0])>=0) and ((2-randList[0]+(3*randList[1]))>=0) and ((4-((randList[2]-3)**2)-randList[3])>=0) and (((randList[4]-3)**3)+randList[5]-4)>=0):
		return True
	else:
		return False
"""
def normalized(y):
        base_rand=y
        normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
        return normalized_rand  
"""
def corrected_list():
	correct_list=randomlist()	
	while (check_constraint(correct_list)!=True):
		#print correct_list
		correct_list=randomlist()
	#print "correct"
	return correct_list

def objective_function(list2):	
	f1=(((-1)*(25*((list2[0]-2)**2)))+((list2[1]-2)**2)+(((list2[2]-1)**2)*((list2[3]-4)**2))+((list2[4]-1)**2))
	f2=((list2[0]**2)+(list2[1]**2)+(list2[2]**2)+(list2[3]**2)+(list2[4]**2)+(list2[5]**2))
	#print "obj"
	return (f1+f2)

def energy(list2):
	global MWS_MIN
	global MWS_MAX
	list2=corrected_list()
	energy1=objective_function(list2)
	#energy1= a+b
	return ((energy1-MWS_MIN)/(MWS_MAX-MWS_MIN))

def baseline():
	global MWS_MAX
    	global MWS_MIN
	#MWS_MAX=objective_function(list1)
	#MWS_MIN=objective_function(list1)
	#print MWS_MAX,MWS_MIN
    	for index in xrange(1000):
		list1=corrected_list()
		x=objective_function(list1)
        	#x =energy(list1)
        	if (x < MWS_MIN):
          	  	MWS_MIN = x
        	if ( x> MWS_MAX):
            		MWS_MAX = x
	return (MWS_MIN,MWS_MAX)

def mutate(mutation_list,index):
	top=[0,0,1,0,1,0]
	bottom=[10,10,5,6,5,10]
	while (1):
		mutation_list[index]=random.uniform(top[index],bottom[index])
		if (check_constraint(mutation_list)==True):
			return mutation_list

def max_score(mutation_list,index):
	top=[0,0,1,0,1,0]
        bottom=[10,10,5,6,5,10]
	max_solution=list(mutation_list)
	min1=top[index]
	max1=bottom[index]
	steps=(max1-min1)/10.0
	start=min1/10.0
	end=max1/10.0
	while min1<=end:
		treat=list(mutation_list)
		#print "treat"	
		treat[index]=min1
		if check_constraint(treat):
			if (objective_function(max_solution)<objective_function(treat)):
				best=list(treat)
		min1=min1+steps
	return max_solution

def normalized(y,MINIMUM,MAXIMUM):
        base_rand=y
        normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
        return normalized_rand

def MaxWalkSat(mws1):
	trials=1000
	changes=10
	p=0.5
	threshold=1
	best=mws1()
	MWS_MIN,MWS_MAX=x.baseline()
	bestEnergy=normalized(best.eval(),MWS_MIN,MWS_MAX)
	formatList=[]
	for i in range(trials):
		new_list=mws1()
		#print new_list
		for j in range(changes):
			#print j	
			if (normalized(new_list.eval()MWS_MIN<MWS_MAX),>threshold):
				#print "if1"
				string1="With energy "+str(normalized(new_list.eval()MWS_MIN<MWS_MAX))+" Best Solution now is "+str(new_list)
				print string1
				sys.exit()
			
			if (normalized(new_list.eval()MWS_MIN<MWS_MAX)>normalized(best.eval()MWS_MIN<MWS_MAX)):
				#print "if2"
				best=list(new_list)
				formatList.append('!')
			
			intr_list=list(new_list)
			if (p<random.uniform(0,1)):
				#print "if3"
				formatList.append('?')
				list_new=mutate(intr_list,random.randint(0,5))
				#print "random"
			else:
				list_new=max_score(intr_list,random.randint(0,5))
				#print "else"
				if (intr_list==list_new):
					formatList.append('.')
				else:
					formatList.append('+')
			
			if (len(formatList)>=50):
				print i,"   ",	
				print "".join(formatList)
				formatList=[]

MaxWalkSat()
			

	
