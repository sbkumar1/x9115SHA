#!/usr/bin/python

from Models import schaffer,osyczka2,kursawe
from simulated_anneal import sim_annealer
from MWS import MaxWalkSat
import time
import timeit
for model in [schaffer,osyczka2,kursawe]:
	for optimizer in [sim_annealer, MaxWalkSat]:
		print "******************************************************"
     		print "Start Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
     		print "Model", model.__name__
     		print "Optimizer", optimizer.__name__
     		optimizer(model)
		print "End Time ->",time.strftime('%l:%M%p %Z on %b %d, %Y')
     		print "******************************************************"
