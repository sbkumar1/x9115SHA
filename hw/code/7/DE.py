#!/usr/bin/python -b

from __future__ import division

import math,random
import time,timeit,sys
import copy
printList=[]
counter=0
def energy(de1,de_min,de_max):
	local1,local2=de1.objectiveScore()
	norm1=(local1-de_min)/(de_max-de_min)
	norm2=(local2-de_min)/(de_max-de_min)	
	bump1=(1-norm1)
	bump2=(1-norm2)
	energy1=1-(math.sqrt(bump1**2+bump2**2)/1.414)
	return energy1

def generateSolution(de1,de_min,de_max,best):
	solutionList=[]
	for i in range(100):
		new1=de1()
      		local1,local2 = new1.objectiveScore()
      		if local1 < de_min:
        		de_min=local1
      		if local1 > de_max:
        		de_max=local1
      		if local2<de_min:
			de_min=local2
        	if local2>de_max:
			de_max=local2
		solutionList.append(new1)
		if (energy(new1,de_min,de_max)>best.eval()):
			best=copy.deepcopy(new)
	return (solutionList,best,de_min,de_max)

def candidates1(solutionList,currentSolution):
	returnList=[]
	x=solutionList.index(currentSolution)
	newList1=list(solutionList)
	newList1.remove(currentSolution)
	while (len(returnList)<3):
		for i in newList1:
			returnList.append(i)
			if (len(returnList)>3):
				break
	return returnList

def Differential_evolution(de1):
	start=timeit.default_timer()
	candidates=100
	change=0.1
	epl=0.75
	crsovr = 0.3
	trials=10
	n=de1()
	best=de1()
	best=copy.deepcopy(n)
	de_min,de_max=best.baseline()
	deSol=de1()
	printList=[]
	counter=0	
	for i in range(trials):
		#print i
		newList=[]
		returnList=[]
		any1=de1()
		newList,best,de_min,de_max=generateSolution(de1,de_min,de_max,best)
		#print best
		#print newList
		for tr1 in newList:
			#print tr1
			while True:
				returnList=candidates1(newList,tr1)
				index=random.randint(0,len(tr1.decisionList)-1)
				#print len(returnList),"ReturnList"
				deSol=de1()
				#print deSol.decisionList			
				for l in range(len(deSol.decisionList)):
					flag=False
					x=random.random()
					if (x<crsovr or l==index):
						flag=True
						deSol.decisionList[index]=returnList[0].decisionList[l-1]+(0.75*(returnList[1].decisionList[l-1]-returnList[2].decisionList[l-1]))
					else:
						deSol.decisionList[index]=tr1.decisionList[l-1]
					#print deSol.decisionList
				if (deSol.ok()==True):
					break
				#print deSol.eval(), best.eval()	       
			if (deSol.eval()<best.eval()):
				best=copy.deepcopy(deSol)
				printList.append('!')
				#print "if"	
			elif (deSol.eval()<tr1.eval()):
				printList.append('+')
				#print "elif"
			else:
				printList.append('.')
				#print "else"
			counter=counter+1
			if (counter%50==0):
				print counter," ",time.strftime('%l:%M%p %Z on %b %d, %Y'),"   ","".join(printList)
				printList=[]
	score=energy(best,de_min,de_max)
	print "Best Solution",best.decisionList
	print "Aggregate Score",score  
	end=timeit.default_timer()
	print "Execution Time",end-start
