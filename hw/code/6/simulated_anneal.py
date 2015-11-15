#!/usr/bin/python
from __future__ import division
import math
import random
#from __future__ import division
import copy
print "Simulted Annealing"
SIM_MAX=10**5
SIM_MIN=-(10**5)
MINIMUM=0
MAXIMUM=0
def schaffer(x):
	f1=x**2
	f2=(x-2)**2
	return (f1+f2)
	
def normalized(y,MINIMUM,MAXIMUM):
	base_rand=y
	normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
	return normalized_rand

def baseline1():
	global MINIMUM, MAXIMUM
        MAXIMUM = MINIMUM = schaffer(random.uniform(-10**5, 10**5))
	for i in range(100):
		schaffer1=random.uniform(-10**5,10**5)
		energy=schaffer(schaffer1)
		#print energy
		if (energy<MINIMUM):
			MINIMUM=energy
		if (energy>MAXIMUM):
			MAXIMUM=energy
	return(MINIMUM,MAXIMUM)
	

def sim_annealer(sim1):	
	s=sim1()
	sBest=sim1()
	#sBest=copy.deepcopy(s)
	eMin,eMax=s.baseline()
        print "MIN "+ str(eMin), str(eMax)
	eBest = normalized(sBest.eval(),eMin,eMax)
    	sEnergy = normalized(s.eval(),eMin,eMax)
	print eMin,eMax
	print eBest,sEnergy
	kMax=500
	k=1
	formatList=[]
        #print k, "Begin"
	while ((k<kMax)):
		sNeighbor=sim1()
		neighborEnergy=normalized(sNeighbor.eval(),eMin,eMax)
		if (neighborEnergy<eBest):
			sBest=sNeighbor
			eBest=neighborEnergy
			formatList.append('!')
		if (neighborEnergy<sEnergy):
			s=sNeighbor
			sEnergy=neighborEnergy
			formatList.append('+')
		elif (math.exp((sEnergy-neighborEnergy)/(k/kMax))<random.uniform(0,1)):
			s=sNeighbor
                        sEnergy=neighborEnergy
                        formatList.append('?')
		formatList.append('.')
		#print formatList
		k=k+1
                #print k
		if (k%25==0):
			print k,"    ",	
			print "".join(formatList)
			formatList=[]
	string1="Solution is "+str(sBest.decisionList)
	print string1



