import Models
import math
import random
import copy
import numpy
import sk

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
                        best=copy.deepcopy(new1)
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

def gt(x,y): 
	return x > y
def lt(x,y): 
	return x < y

def type1(model1, model2):
	bettered = False
    	for i,(xi,yi) in enumerate(zip(model1.objectiveScore(),model2.objectiveScore())):
        	if lt(xi,yi):
            		bettered = True
        	elif (xi != yi):
            		return False
    	return bettered

def type2(list1, list2):
	if (sk.a12(list1, list2) <= 0.56):
        	return -1
    	else:
        	return 5

def DE(de1):
	maxtries=10
	Candidates=100
	best=de1()
	candidates=[best]
	printList=[]
	lives = 5
	Past,Current,Future=[],[],[]
	era=100
    
	for i in range(len(best.objectiveScore())):
		Past.append([])
        	Current.append([])
        	Future.append([])

    
    	for i in range(1,Candidates):
        	candidate=de1()
        	candidates.append(candidate)
        	if type1(candidate, best):
            		best=copy.deepcopy(candidate)
        	newcandidates = []
        
	for tries in range(maxtries):
                newcandidates = []
		for new,best in candidate_gen(de1,candidates,best,F=0.1,CR=0.75):
            		newcandidates.append(new)
        	candidates = newcandidates
        	if (len(Current[0]) < era):
            		for i in candidates:
                		x = i.objectiveScore()
                		for j in range(len(x)):
                    			Current[j].append(x[j])
        	else:
            		if (Past[0] != []):
                		for i in range(len(Past)):
                    			lives += type2(Past[i],Current[i])
                		if (lives <= 0):
                    			break
            	for i in range(len(Current)):
               		Past[i] = list(Current[i])
           	Current=[]
		
            	for i in range(len(Past)):
                	Current.append([]) 

	return best.decisionList,best.eval()


def candidate_gen(de1,candidates,best,F=0.1,CR=0.75):
	for i in range(len(candidates)):
                tmp=range(len(candidates))
                tmp.remove(i)
                while True:
                	choice=numpy.random.choice(tmp,3)
                        X = candidates[choice[0]]
                        Y = candidates[choice[1]]
                        Z = candidates[choice[2]]
                        old=candidates[i]
                        r=random.randint(0,old.noOfDecisions-1)
                        new=de1()
                        for j in range(old.noOfDecisions):
                        	if random.random()<CR or j==r:
                                        new.decisionList[j]=X.decisionList[j] + F*(Y.decisionList[j] - Z.decisionList[j])  #Mutate: X + F*(Y - Z)
                                else:
                                        new.decisionList[j]=old.decisionList[j]
                        if new.ok():
                                break
		if type1(new, best):
                        best=copy.deepcopy(new)
                elif (not type1(new, old)):
                        new=old
                yield new,best
