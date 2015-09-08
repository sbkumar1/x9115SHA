#!/usr/bin/python -b

import random
listOfNumbers=[]
for i in range(10):
	listOfNumbers.append(random.randint(1,30))
print listOfNumbers
d = dict.fromkeys(listOfNumbers, 0)
#print d
#print listOfNumbers

def has_duplicates(originalList):
	print "The List Generated was"
	for i in originalList:
		print i," ",
	print 
	uniqueList=set(originalList)
	if (len(originalList)==len(uniqueList)):
		print "Unique!!"
		return True
	else:
		print "Not Unique !!"
		return False
print has_duplicates(listOfNumbers)	
	

