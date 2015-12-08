#!/usr/bin/python -b

from __future__ import division
import random
import math

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

class dtlz7(model):

	def __init__(self):
        	self.noOfDecisions=10
        	self.noOfObjectives=2
		self.nameDecision="DTLZ7"
		self.nameObjective="DTLZ7"
        	self.decisionList=[0]*10
        	self.minRange=[0]*10
        	self.maxRange=[1]*10
		self.m=10
		self.n=2
        	self.any()

	def g(self):
        	return (1 + (9/self.noOfDecisions*sum(self.decisionList)))

	def h(self):
        	sumtemp = 0
        	n = 0
        	for j in range(len(self.decisionList)):
            		if (self.m+self.n-1) == self.noOfObjectives-2:
               			break
            		sumtemp += (self.decisionList[j] / ( 1.0 + self.g() ) ) * ( 1 + math.sin( 3.0 * math.pi * self.decisionList[j] ) )
            		n += 1
        	return (self.noOfObjectives-sumtemp)# k = 0,...., M-2

	def objectiveScore(self):
        	f = []
        	for i in range(self.noOfObjectives-1):
            		f.append(self.decisionList[i])
        	f.append((1+self.g())*self.h())
		return f
