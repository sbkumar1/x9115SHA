#!/usr/bin/python -b
from __future__ import division
import sys
import random,math,copy
random.seed(10)
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

def mutate(s1,index,model):
	s2=model()
	s2=copy.deepcopy(s1)
	
	while (1):
		s2.decisionList[index]=random.uniform(s2.minRange[index],s2.maxRange[index])
		if (s2.ok()==True):
			#print "~~~",s2.decisionList
			return s2

def max_score(s1,index,model,step):
	s2=model()
	s2=copy.deepcopy(s1)
    	sbest=model()
    	sbest=copy.deepcopy(s2)
    	step2=(s2.maxRange[index]-s2.minRange[index])/step
	if step2 != 0:
        	for i in range(-int((s2.decisionList[index]-s2.minRange[index])/step2),int((s2.maxRange[index]-s2.decisionList[index])/step2)+1):
            		s2.decisionList[index]=s2.decisionList[index]+i*step2
            		if s2.ok(): 
            			if s2.eval()<sbest.eval():
                			sbest=copy.deepcopy(s2)
    	return sbest

def normalized(y,MINIMUM,MAXIMUM):
        base_rand=y
        normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
        return normalized_rand

def MaxWalkSat(mws1):
	trials=500
	changes=10
	p=0.5
	threshold=1
	best=mws1()
	MWS_MIN,MWS_MAX=best.baseline()
	bestEnergy=normalized(best.eval(),MWS_MIN,MWS_MAX)
	formatList=[]
	for i in range(trials):
		new_list=mws1()
		#print new_list
		for j in range(changes):
			#print j	
			if (normalized(new_list.eval(),MWS_MIN,MWS_MAX)>threshold):
				#print "if1"
				string1=" Best Solution "+str(new_list.decisionList)
				print string1
				sys.exit()
			
			if (normalized(new_list.eval(),MWS_MIN,MWS_MAX)<normalized(best.eval(),MWS_MIN,MWS_MAX)):
				#print "if2"
				best=mws1()
				best=copy.deepcopy(new_list)
				formatList.append('!')
			
			intr_list=copy.deepcopy(new_list)
			if (p<random.uniform(0,1)):
				#print "if3"
				formatList.append('?')
				new_list=mutate(new_list,random.randint(0,new_list.noOfDecisions-1),mws1)
				#print "random"
			else:
				new_list=max_score(new_list,random.randint(0,new_list.noOfDecisions-1),mws1,10)
				#print "else"
				if (intr_list.eval()==new_list.eval()):
					formatList.append('.')
				else:
					formatList.append('+')
			
			if (len(formatList)>=50):
				print i,"   ",	
				print "".join(formatList)
				formatList=[]
	string1="Best Solution "+str(best.decisionList)
	print string1
	

	
