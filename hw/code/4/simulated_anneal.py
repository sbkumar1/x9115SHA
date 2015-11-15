#!/usr/bin/python
from __future__ import division
import math
import random
import time
import timeit
random.seed(100)
#from __future__ import division
#print "Simulted Annealing"
SIM_MAX=10**5
SIM_MIN=-(10**5)
MINIMUM=0
MAXIMUM=0
def schaffer(x):
	f1=x**2
	f2=(x-2)**2
	return (f1+f2)
	
def normalized(y):
	base_rand=y
	normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
	return normalized_rand

def baseline():
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
	

def sim_annealer():	
	MAX,MIN= baseline()
	#print MAX,MIN	
	s=random.uniform(0,1)
	energy=schaffer(s)
	sEnergy=normalized(energy)
	sBest=s
	eBest=sEnergy
	eMax=-0.1
	kMax=1000
	k=1
	formatList=[]
	while ((k<kMax) and (sEnergy>eMax)):
		sNeighbor=random.uniform(-10000,10000)+s
		nEnergy=schaffer(sNeighbor)
		neighborEnergy=normalized(nEnergy)
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
		if (k%25==0):
			print k,"    ",time.strftime('%l:%M%p %Z on %b %d, %Y'),"     ",
			print "".join(formatList)
			formatList=[]
	string1="\t Solution Found "+str(sBest)
	string2="\t Best Energy "+str(math.fabs(eBest))
	print string1
	print string2
print "#################################Simulated annealer started#################################################################"
start=timeit.default_timer()
print "Start Time->",time.strftime('%l:%M%p %Z on %b %d, %Y')
sim_annealer()
end=timeit.default_timer()
print "\t Algorithm Runtime",end-start
print "\t End Time->",time.strftime('%l:%M%p %Z on %b %d, %Y')
print "###################################Simulated Anneling ends#################################################################"




