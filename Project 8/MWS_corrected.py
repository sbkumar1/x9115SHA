#!/usr/bin/python -b
from __future__ import division
import sys
import random,math
import copy
import sk
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
def newPerson(object1,model,i):
    newList=model()
    newList=copy.deepcopy(object1)
    while True:
        newList.decisionList[i]=random.uniform(newList.minRange[i],newList.maxRange[i])
        if newList.ok():
                return newList
                break

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

def gt(model1,modet2):
        if (model1>model2):
                return True
        else:
                return False

def lt(model1,model2):
        if model1<model2:
                return True
        else:
                return False

def type1(model1,model2):
        k=1
        for i,(j,k) in enumerate(zip(model1.objectiveScore(),model2.objectiveScore())):
                if lt(j,k):
                        k=0
                else:
                        return False
        return True

def type2(model1,model2):
    if (sk.a12(model1,model2) <= 0.6):
        return -1
    else:
        return 5

def MaxWalkSat(mws1):
	trials=1000
	changes=10
	p=0.5
	threshold=-10000
	step=10
	lives=5
	lp=1
	era=25
	eval1=0
	evalx=0
	best=mws1()
	MWS_MIN,MWS_MAX=baseline()
	bestEnergy=normalized(best.eval(),MWS_MIN,MWS_MAX)
	Past,Current,Future=[],[],[]
	for i in range(trials):
		new_list=mws1()
		if (i==0):
			sBest=mws1()
			sBest=copy.deepcopy(new_list)
			for i in range(len(new_list.objectiveScore())):
				Current.append([])
				Past.append([])
		for j in range(changes):
			lp=1			
			if ((normalized(new_list.eval(),MWS_MIN,MWS_MAX))>threshold and len(Past)==era):
				return sBest.decisionList,sBest.eval()
			
			#if (normalized(new_list.eval()MWS_MIN<MWS_MAX)>normalized(best.eval()MWS_MIN<MWS_MAX)):
			#	#print "if2"
			#	best=list(new_list)
			#	formatList.append('!')
			
			if (p<random.uniform(0,1)):
				#print "if3"
				#formatList.append('?')
				new_list=newPerson(new_list,mws1,random.randint(0,len(new_list.decisionList)-1))
				#print "random"
			else:
				new_list=newPerson(new_list,mws1,random.randint(0,len(new_list.decisionList)-1))
				#print "else"
				if (type1(new_list,sBest)):
					sBest=copy.deepcopy(new_list)
					evalx=eval1
					
			if (len(Current[0])<era):
                        	x=list(new_list.objectiveScore())
                        	for i in range(len(x)):
                                	Current[i].append(x[i])
                	else:
                        	if (Past[0]!=[]):
                                	for j in range(len(Past)):
                                        	lives=lives+type2(Past[j],Current[j])
                                if (lives<=0):
                                        break
                        	for i in range(len(Current)):
                                	Past[i]=list(Current[i])
                        	Current=[]
                        	for i in range(len(Past)):
                                	Current.append([])
        return sBest.decisionList,sBest.eval()
			

	
