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

class dtlz1(model):
	def __init__(self,m,n):
                self.noOfDecisions=m
                self.noOfObjectives=n
                self.nameDecision="DTLZ1"
                #self.nameObjective="DTLZ1"
                self.decisionList=[0]*m
                self.minRange=[0]*m
                self.maxRange=[1]*m
		self.m=m
		self.n=n
		self.any()
	
	def objectiveScore(self):
		list1=list(self.decisionList)
		sum1=self.m-self.n+1
		return1=[]
		for t in self.decisionList[self.n-1:]:
			sum1+=(((t-0.5)**2)-math.cos(20*math.pi*(t-0.5)))
		gx=100*sum1
		for i in xrange(self.n):
			f1=float(0.5*(1+gx))
			for x in self.decisionList[:self.n-1-i]:
				f1=f1*x
			if i!=0:
				f1*=(1-self.decisionList[self.n-1])
			return1.append(f1)
			#self.objectiveScore=return1			
		return return1

class dtlz3(model):
	def __init__(self,m,n):
                self.noOfDecisions=m
                self.noOfObjectives=n
                self.nameDecision="DTLZ3"
                self.decisionList=[0]*m
                self.minRange=[0]*m
                self.maxRange=[1]*m
                self.any()
		self.m=m
		self.n=n

        def objectiveScore(self):
                list1=list(self.decisionList)
                x1=self.decisionList[0]
               	return1=[]
        	sum1=self.m-self.n+1
        	for x in self.decisionList[self.n-1:]:
            		sum1+=((x-0.5)**2)-math.cos((x-0.5)*20*math.pi)
        	g=sum1*100
        	for i in xrange(self.n):
            		f1=1+g
            		for x in self.decisionList[:self.n-1-i]:
                		f1*=math.cos(x*math.pi/2)
            		if not i==0:
                		f1*=math.sin(self.decisionList[self.n-i]*math.pi/2)
            		return1.append(f1)
        		#self.objectiveScore=return1
        	return return1

class dtlz7(model):
	def __init__(self,m,n):
                self.noOfDecisions=m
                self.noOfObjectives=n
                self.nameDecision="DTLZ7"
                self.nameObjective="DTLZ7"
                self.decisionList=[0]*m
                self.minRange=[0]*m
                self.maxRange=[1]*m
                self.any()
		self.m=m
		self.n=n

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
                for i in range(self.noOfObjectives -1):
                        f.append(self.decisionList[i])
                f.append( (1+self.g()) * self.h() )
                return f
	
		
class dtlz5(model):
        def __init__(self,m,n):
                self.noOfDecisions=m
                self.noOfObjectives=n
                self.nameDecision="DTLZ1"
                #self.nameObjective="DTLZ1"
                self.decisionList=[0]*m
                self.minRange=[0]*m
                self.maxRange=[1]*m
                self.m=m
                self.n=n
                self.any()

        def objectiveScore(self):
		return1=[]
		g=0
        	for x in self.decisionList[self.n-1:]:
            		g=g+(x-0.5)**2
        	theta=[math.pi*self.decisionList[0]/2]
        	for x in self.decisionList[1:self.n-1]:
            		theta.append((1+2*g*x)*math.pi/(4*(1+g)))
       		for i in xrange(self.n):
            		tmp=1+g
            		for x in theta[:self.n-1-i]:
                		tmp=tmp*math.cos(x*math.pi/2)
            		if not i==0:
                		tmp=tmp*math.sin(theta[self.n-i-1]*math.pi/2)
            		return1.append(tmp)
        	return return1	
