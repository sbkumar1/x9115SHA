#!/usr/bin/python -b

from __future__ import division
import random
import math


#Defining model class


class model(object):
	def __init__(self):
		self.noOfDecisions=0
		self.noOfObjectives=0
		self.nameDecision=None
		self.nameObjective=None
		self.decisionList=[]
		self.minRange=[]
		self.maxRange=[]
	
	def ok(self):
		for i in xrange(self.noOfDecisions):
			if (self.decisionList[i]<self.minRange[i] or self.decisionList[i]>self.maxRange[i]):
				return False
		return True
	
	def any(self):
		while True:
			self.decisionList = []
			for i in xrange(self.noOfDecisions):
				self.decisionList.append(random.uniform(self.minRange[i],self.maxRange[i]))
			if (self.ok()==True):
				break

	def objectiveScore(self):
		return []
	
	def eval(self):	
		x=sum(self.objectiveScore())
		return x
	
	def baseline(self):
		min1,max1=self.eval(),self.eval()
		for i in range(1000):
			self.any()
			now1=self.eval()
			if now1<min1:
				min1=now1
			if now1>max1:
				max1=now1
			#print self.decisionList, min1,max1
		return (min1,max1)

class schaffer(model):
	def __init__(self):
		self.noOfDecisions=1
                self.noOfObjectives=2
                self.nameDecision="Schaffer"
                self.nameObjective="SChaffer"
                self.decisionList=[0]
                self.minRange=[-100]
                self.maxRange=[100]
		self.any()
	
	def objectiveScore(self):
		dec1=self.decisionList[0]
		f1=dec1**2
		f2=(dec1-2)**2
		return [f1,f2]

class osyczka2(model):
	def __init__(self):
		self.noOfDecisions=6
                self.noOfObjectives=2
                self.nameDecision="Osyczka2"
                self.nameObjective="Osyczka2"
                self.decisionList=[0,0,0,0,0,0]
                self.minRange=[0,0,1,0,1,0]
                self.maxRange=[10,10,5,6,5,10]
                self.any()
	
	def ok(self):
		randList=list(self.decisionList)
		if (((randList[0]+randList[1]-2)>=0) and ((6-randList[0]-randList[1])>=0) and ((2-randList[1]+randList[0])>=0) and ((2-randList[0]+(3*randList[1]))>=0) and ((4-((randList[2]-3)**2)-randList[3])>=0) and (((randList[4]-3)**3)+randList[5]-4)>=0):
			return True
		else:
			return False
	
	def objectiveScore(self):
		list2=list(self.decisionList)
		f1=(((-1)*(25*((list2[0]-2)**2)))+((list2[1]-2)**2)+(((list2[2]-1)**2)*((list2[3]-4)**2))+((list2[4]-1)**2))
		f2=((list2[0]**2)+(list2[1]**2)+(list2[2]**2)+(list2[3]**2)+(list2[4]**2)+(list2[5]**2))
		#print "obj"
		return (f1,f2)

class kursawe(model):
        def __init__(self):
                self.noOfDecisions=3
                self.noOfObjectives=2
                self.nameDecision="Kursawe"
                self.nameObjective="Kursave"
                self.decisionList=[0,0,0]
                self.minRange=[-5,-5,-5]
                self.maxRange=[5,5,5]
                self.any()
	
	def objectiveScore(self):
		list2=list(self.decisionList)
		f1,f2=0,0
		for i in list2:
			f1+=(-10)*math.exp((-0.2)*math.sqrt((i**2)+((i+1)**2)))
		for i in list2:
			f2+=(math.pow(math.fabs(i),0.8)+5*math.sin(i))
		return (f1,f2)




			
				
	
	
		

