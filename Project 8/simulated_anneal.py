#!/usr/bin/python
from __future__ import division
import sys
import math
import random
#from __future__ import division
import copy
import sk
#print "Simulted Annealing"
SIM_MAX=10**5
SIM_MIN=-(10**5)
MINIMUM=-10000
MAXIMUM=10000
lives=0

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
	
def normalized(y):
	global MINIMUM
	global MAXIMUM
	base_rand=y
	normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
	return normalized_rand

def baseline1():
	global MINIMUM
	global MAXIMUM
        #MAXIMUM = MINIMUM = schaffer(random.uniform(-10**5, 10**5))
	for i in range(100):
		schaffer1=random.uniform(-10**5,10**5)
		energy=schaffer(schaffer1)
		#print energy
		if (energy<MINIMUM):
			MINIMUM=energy
		if (energy>MAXIMUM):
			MAXIMUM=energy
	return(MINIMUM,MAXIMUM)

def newPerson(object1,model,i):
    newList=model()
    newList=copy.deepcopy(object1)
    while True:
        newList.decisionList[i]=random.uniform(newList.minRange[i],newList.maxRange[i])
	if newList.ok():
		return newList
		break

def sim_annealer(sim1):	
	s=sim1()
	sBest=sim1()
	eMin,eMax=s.baseline()
	eBest = normalized(sBest.eval())
    	sEnergy = normalized(s.eval())
	kMax=1000
	k=1
	era=25
	Past,Current,Future=[],[],[]
	#print s.objectiveScore()
	lives=5
	for i in range(len(s.objectiveScore())):
		Past.append([])
		Current.append([])
		Future.append([])
	
	while ((k<kMax)):
		sNeighbor=newPerson(s,sim1,random.randint(0,len(s.decisionList)-1))
		if (type1(sNeighbor,sBest)):
			sBest=copy.deepcopy(sNeighbor)
			s=copy.deepcopy(sNeighbor)
		if (type1(sNeighbor,s)):
			s=copy.deepcopy(sNeighbor)
			#sEnergy=neighborEnergy
			#formatList.append('+')
		#elif (math.exp((s.eval()-sNeighbor.eval())/(k/kMax))<random.uniform(0,1)):
		#	s=copy.deepcopy(sNeighbor)
                        #sEnergy=neighborEnergy
                        #formatList.append('?')
		#formatList.append('.')
		#print formatList
		k+=1
                #print k
		#print Current
		if (len(Current[0])<era):
			x=list(s.objectiveScore())
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

		
"""if (k%25==0):
			print k,"    ",	
			print "".join(formatList)
			formatList=[]
	string1="Solution is "+str(sBest.decisionList)
print string1"""



