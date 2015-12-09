#!/usr/bin/python -b

import time
import timeit
from Models import dtlz7
from simulated_anneal import sim_annealer as sa
from MWS_corrected import MaxWalkSat as mws
from DifferentialEvolution import DE as de
from sk import rdivDemo 

for model in [dtlz7]:
	start=timeit.default_timer()
       	rdivInput = [[],[],[]]
       	rdivInput[0].append("sa ")
       	rdivInput[1].append("mws")
       	rdivInput[2].append("de ")
	for j in xrange(1,21):
		print "Iteration ",j," Start Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
       		for algorithm in [sa,mws,de]:
                	if algorithm.__name__ == 'sim_annealer':
       	            		i = 0
               		if algorithm.__name__ == 'MaxWalkSat':
               			i = 1
      		 	if algorithm.__name__ == 'DE':
              			i = 2
               		list1,solution = algorithm(model)
           
     	    		print "***********************************************************************"
       			print "Model     : ",model.__name__
              		print "Algorithm : ",algorithm.__name__
		#	print "Iteration ",j," Start Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
              		print "***********************************************************************" 
			print "Best Solution:"
			print (" ".join( repr(e) for e in list1))
              		print "**************************"
              		print "Energy",solution
               		print "*************************"
			print
               		rdivInput[i].append(solution)
	print "Iteration ",j," End Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
	print "*********************************************************************"
	print 
       	rdivDemo(rdivInput)
	end=timeit.default_timer()
	print "Program Execution Time",end-start

