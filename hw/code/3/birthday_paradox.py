#!/usr/bin/python -b

import random

def birthdayGenerator():
	month=random.randint(01,12)
	if (month==2):
		date=random.randint(1,28)
	elif (month in (4,6,9,11)):
		date=random.randint(1,30)
	else: 
		date=random.randint(1,31)
	#print month,date
	if (len(str(month))!=2):
		month=str(0)+str(month)
	if (len(str(date))!=2):
		date=str(0)+str(date)
	birthday=str(month)+str(date)		
        return birthday 

def has_duplicates(originalList):
	#print "The List Generated was"
	#for i in originalList:
	#	print i," ",
	#print 
	uniqueList=set(originalList)
	if (len(originalList)==len(uniqueList)):
		#print "Unique!!"
		return True
	else:
		"""print "Duplicate Birthdays"
		findUnique=[]
		for i in originalList:
			if i not in findUnique:
				findUnique.append(i)
			else:
				print i
		"""			
		return False
unique=0
not_unique=0
print "evaluating..."
for i in range(10000):
	listOfBirthdays=[]
	for i in range(23):
		listOfBirthdays.append(int(birthdayGenerator()))	
	if (has_duplicates(listOfBirthdays)==True):
		#print listOfBirthdays
		#print "unique"
		unique=unique+1
		#print "True"
	else:
		#print listOfBirthdays
		#print "not unique"
		not_unique=not_unique+1
		#print "False"
print "*************RESULTS OF Birthday Paradox Tests*******************************************" 
print "No of iterations Performed = 10000"
print "In a class of 23 out of 10000 times, no of times two students have same birthday",not_unique
print "In a class of 23 out of 1000 times, no of times two student do not have same birthday",unique
print "****************************************************************************************"
print "In a class of 23, probability of having birthdays on same day",not_unique/10000.0
print "In a class of 23, probability of not having birthdays on same day",unique/10000.0
print "********************************************************"
