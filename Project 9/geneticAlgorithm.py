#!/usr/bin/python -b

from __future__ import division
import timeit
import time
import math
import random
import sys
import numpy as np
GE_MAX=sys.maxint
GE_MIN=-(sys.maxint-1)

def normalized(y,MINIMUM,MAXIMUM):
        base_rand=y
        normalized_rand=(base_rand-MINIMUM)/(MAXIMUM-MINIMUM)
        return normalized_rand

def baseline():
	global GE_MAX
    	global GE_MIN
    	for index in xrange(1000):
		list1=corrected_list()
		x=objective_function(list1)
        	#x =energy(list1)
        	if (x < GE_MIN):
          	  	GE_MIN = x
        	if ( x> GE_MAX):
            		MWS_MAX = x
	return (GE_MIN,GE_MAX)

def gt(ga1,ga2): return ga1>ga2
def lt(ga1,ga2): return ga1<ga2

def binaryDomination(ga1,ga2):
	#print ga1,ga2
	a=ga1.objectiveScore()
	#print a
	b=ga2.objectiveScore()
 	if a==b:
        	return False
    	for i in xrange(len(ga1.objectiveScore())):
        	if (a[i]<b[i]):
            		return False
    	return True

def dominate(population):
	counter=0
	for i in population:
		for j in population:
			if binaryDomination(i,j):
				counter+=1
	print counter
		

def select(population):
	new_population=[]	
	flag=True
	#while (len(new_population)<=20):
	#print len(new_population)
	population1=list(population)
	for a in population:
            flag=True
            for b in population:
                if binaryDomination(b,a):
                    flag=False
                    break
            if flag:
                new_population.append(a)
	return new_population	
	
def mutate(ge1):
	r=random.uniform(0,1)
	mutationRate=0.05
	if r>mutationRate:
		return ge1
	else:
		integ1=random.randint(0,len(ge1.decisionList))
		r=random.uniform(0,1)
		ge1.decisionList[integ1-1]=r
		return ge1

def crossover(dad,mom,ge1):
	crossOverRate=0.8
	r=random.uniform(0,1)
	if r>=crossOverRate:
		return ge1
	else:
		r=random.randint(0,len(mom.decisionList))
		ge1.decisionList=dad.decisionList[0:r]
		ge1.decisionList.extend(mom.decisionList[r:])
	return ge1

def GA(ga1,o,d):
	counter=0
	generations=100
	candidates=100
	iterations=20
	currentPopulation=[]
	tempList=[]
	grandDad=[]
	solutionList=[]
	lives=5
	#initial population creation
	for index1 in range(candidates):
		n1=ga1(o,d)
		currentPopulation.append(n1)
	reference=[ga1(o,d) for _ in xrange(10000)]
        max1=[np.max([i.objectiveScore()[x] for i in reference]) for x in range(d)]
        min1=[np.min([j.objectiveScore()[y] for j in reference]) for y in range(d)]
	#bestCandidate=currentPopulation[random.randint(0,99)]
	#bestEnergy=bestCandidate.eval()
	grandDad=currentPopulation
	for index2 in range(generations):
		#print index2
		grandDad=currentPopulation
		tempList=list(currentPopulation)
		newGeneration=select(currentPopulation)
		if (len(newGeneration)<20):
			while (len(newGeneration)<20):
				x1=random.randint(0,len(tempList)-1)
				newGeneration.append(tempList[x1])
		noOfParentsLeft=len(newGeneration)
		noOfChildrenToAdd=100-noOfParentsLeft
		currentPopulation=list(newGeneration)
		#print len(currentPopulation),len(newGeneration)
		for index3 in xrange(noOfChildrenToAdd):
			x=random.randint(0,len(newGeneration)-1)
			y=random.randint(0,len(newGeneration)-1)
			dad,mom=newGeneration[x],newGeneration[y]
			new1=ga1(o,d)
			new1=crossover(dad,mom,new1)
			new1=mutate(new1)
			currentPopulation.append(new1)
			#print "End",len(currentPopulation)
		#if (len(currentPopulation)==100):
		#	break
		for p in grandDad:
			flag=0
			for k in currentPopulation:
				if (binaryDomination(k,p)):
					flag=1
					lives=5
					break
		if (flag==0):
			lives-=1				
		solutionList=list(currentPopulation)
		if (lives==0):
			return solutionList,max1,min1
			break
	return solutionList,max1,min1					

"""			for index1 in newGeneration:
                		tempDict[index1]=index1.eval()
        			currentPopulation=sorted(tempDict,key=tempDict.get,reverse=True)
        			currentEnergy=currentPopulation[0].eval()
				grandDad=currentPopulation
	
			



		if (currentEnergy>bestEnergy):
			bestEnergy=currentEnergy
			bestCandidate=currentPopulation[0]
			printList.append('!')
			
		elif (currentEnergy<bestEnergy):
			printList.append('+')
		
		else:
			printList.append('.')
		
		counter=counter+1
		if (counter%50==0):
			print counter," ",time.strftime('%l:%M%p %Z on %b %d, %Y'),"   ","".join(printList)
			printList=[] 	
		"""
	
		
				
			
		
		
		

