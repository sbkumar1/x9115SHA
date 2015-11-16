#!/usr/bin/python

from Models import schaffer,osyczka2,kursawe,golinski
from simulated_anneal import sim_annealer
from MWS import MaxWalkSat
from DE import Differential_evolution
import time
import timeit
for model in [golinski]:
	for optimizer in [Differential_evolution,MaxWalkSat,sim_annealer]:
		print "******************************************************"
     		print "Start Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
     		print "Model", model.__name__
     		print "Optimizer", optimizer.__name__
     		optimizer(model)
		print "End Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
     		print "******************************************************"
