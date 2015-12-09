
from Models import dtlz1,dtlz3,dtlz7,dtlz5
from geneticAlgorithm import GA
import time
import timeit
#import matplotlib.pyplot as plt
import os

objs=[2]
decs=[10]
start=timeit.default_timer()
print "Start Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
#os.rmdir("Pareto_Fronts")
for model in [dtlz7,dtlz5]:
	for optimizer in [GA]:
		print "******************************************************"
     		print "Model", model.__name__
     		print "Optimizer", optimizer.__name__
		for d in decs:
			for o in objs: 
				for k in xrange(1,21):
					print "Iteration No: ",k
					x1,max1,min1=optimizer(model,d,o,0.3,0.05)
					string1=str(model.__name__)+"-PF-"+str(d)+"-"+str(o)+"-"+str(k)+".txt"
					string1="Pareto_Fronts/"+string1
					f=open(string1,'w')
					for j in x1:
						for l in j.objectiveScore():
							k=j.objectiveScore().index(l)
                                                        p=((l-min1[k])/(max1[k]-min1[k]))
							s=str(p)
							f.write(s)
							f.write(" ")
						f.write("\n")
					f.close()
		"""
			for i in xrange(len(x1[k])):
				x=len(x1[k][i].objectiveScore())
				for j in xrange(x):
					energy1.append(x1[k][i].eval())
		plt.plot(objectives,energy1, 'ro')
		plt.show()"""
end=timeit.default_timer()
print "Total Run Time",end-start
print "End Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
print "******************************************************"
