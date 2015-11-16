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

class golinski(model):
	def __init__(self):
                self.noOfDecisions=7
                self.noOfObjectives=2
                self.nameDecision="Golinski"
                #self.nameObjective="Golinski"
                self.decisionList=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
                self.minRange=[2.6,0.7,17.0,7.3,7.3,2.9,5.0]
                self.maxRange=[3.6,0.8,28.0,8.3,8.3,3.9,5.5]
                self.any()

	def ok(self):
                randList=list(self.decisionList)
                if ((((1.0/(randList[0] * randList[1]**2 * randList[2])) - (1.0/27.0)) >0) or ((math.pow(randList[3],3)/((randList[1]*randList[2]**2)*(randList[5]**4)) - (1.0/1.93)) > 0) or ((math.pow(randList[4],3) / (randList[1] * randList[2] * randList[6]**4) - (1.0/1.93)) > 0) or (((randList[1]*randList[2]) - 40) > 0) or (((randList[0] / randList[1]) - 12) > 0) or ((5 - (randList[0] / randList[1]))>0) or ((1.9 - randList[3] + (1.5*randList[5]))>0) or ((1.9 - randList[4] + (1.1*randList[6]))>0)):
                        return False
		
                if  ((math.sqrt(math.pow((745.0*randList[3])/(randList[1]*randList[2]),2) + 1.69*(10**7)))/(0.1*math.pow(randList[5],3)))>1300:
			return False
		
		a = (745.0*randList[4]) / (randList[1]*randList[2])
        	b = 1.575 *(10**8)
		if (math.sqrt((a**2) + b) / (0.1 * math.pow(randList[6],3))) > 1100:
            		return False
                     
		return True 
			
	def objectiveScore(self):
		randList=list(self.decisionList)
		f1=((0.7854)*randList[0]*math.pow(randList[1],2)*(10/3*math.pow(randList[2],2)+(14.933)*randList[2]-43.0934)-(1.508)*randList[0]*(math.pow(randList[6],2)+math.pow(randList[5],2))+(7.477)*(math.pow(randList[6],3)+math.pow(randList[5],3))+(0.7854)*(randList[3]*math.pow(randList[5],2)+randList[4]*math.pow(randList[6],2)))
		f2=((math.sqrt(math.pow((745.0*randList[3])/(randList[1]*randList[2]),2) + 1.69*(10**7)))/(0.1*math.pow(randList[5],3)))
		return (f1,f2)
	
		

