#Hyper Parameter Optimization - Models DTLZ1 and DTLZ5 using Differential Evolution tuned Genetic Algorithm

###Submitted By - Shashank Bipin Kumar (sbkumar) for ASE Fall 2015 Code 10

##I. Overview
This project is an extension of project 9. This project would use Differential Evolution(DE) algorithm to tune the parameters for Genetic Algorithm(GA) and test them on DTLZ1 and DTLZ5 models. It would compare the metrics number of iterations to reach the optimal solution and optimal solution found.

##II. Background
####Genetic Algorithm
Genetic Algorithms(GA) are adaptive heuristic search algorithms based on the evolutionary ideas of natural selection and genetics. GA works better than other AI techniques like linear programming, dfs, etc even in presence of reasonable noise. The major steps of GA are :-  
1. Initially a random population is selected.  
2. Good individuals are selected based on a fitness function.  
3. Genes from the good individuals propagate throughout the population so that two good parents produce better offspring.  
4. With iterations, the population becomes fitter than previous generation as off-springs are from fittest individuals of previous generation. 

####Differential Evolution
Differential Evolution (DE) optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. DE is suited for multidimensional real-valued functions but does not use the gradient of the problem being optimized. DE does not require the optimization problem to be differentiable as required by classic optimization methods. DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones saving candidate solution that has the best score.

##III. Introduction
Differential Evolution is used to create the base population for Genetic Algorithm(GA). This is run against the tuned crossover factors of [0.1,0.8 and 0.9] and mutation numbers [0.05, 0.1, 0.2] on DTLZ1 and DTLZ5 model  with 10 decisions and 2 objectives to find the optimum solutions. The DE would choose optimal solutions by removing the bad decisions using binary dominations.

##IV. Implementation
Below are the steps for implementation:-  
1. 











