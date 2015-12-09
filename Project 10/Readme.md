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
Differential Evolution is used to tune the population for Genetic Algorithm(GA). This is run against the tuned crossover factors of [0.1,0.8 and 0.9] and mutation numbers [0.05, 0.1, 0.2] on DTLZ1 and DTLZ5 model  with 10 decisions and 2 objectives to find the optimum solutions. The DE would choose optimal solutions by removing the bad decisions using binary dominations.

##IV. Implementation
Below are the steps for implementation:-  
1. The setting for DE Algorithm was as below :-  
	epsilon amount=0.1  
    extrapolate =0.75  
	crossover probability = 0.3  
	no of trials = 10  
2. Initially the DE algorithm is used to find the candidates for GA which in turn is worked upon by the GA algorithm.  
3  The algorithm is run for 50,100,500 generations on DTLZ5 and DTLZ7 models with 10 decisions and 2 objectives.
4. The mutation rate and crossover rate are chosen as (0.2,0.8), (0.01,0.3) and (0.1,0.5)

The running time of the algorithm was extremely slow. I have used a technique where I have generated the population in steps of 10 and then finally reached the total population count. This helped me reduce the time of running the algorithm.

##V. Results
###The Results have been shown below. It is found that tuning the GA parameters using DE does improve the outcome of both DTLZ5 and DTLZ7 with less number of candidates, however as the number of candidates begin to increase, the improvement is not significant.
![root directory] (./images/Results.PNG)
###For DTLZ5 50 candidates 0.8 crossover 0.2 mutation  
![root directory] (./images/DTLZ5_50_0.2_0.8.PNG)
###For DTLZ5 50 candidates 0.3 crossover 0.1 mutation
![root directory] (./images/DTLZ5_50_0.3_0.1.PNG)
###For DTLZ7 50 candidates 0.3 crossover 0.1 mutation
![root directory] (./images/DTLZ7_50_0.3_0.1.PNG)
###For DTLZ7 500 candidates 0.8 crossover 0.2 mutation
![root directory] (./images/DTLZ7_500_0.8_0.2.PNG)
###For DTLZ5 and DTLZ7 50 candidates 0.8 crossover 0.2 mutation
![root directory] (./images/dtlz5_7_10_2_tuned_50_2.png)
###For DTLZ5 500 candidates 0.8 crossover 0.2 mutation
![root directory] (./images/dtlz7_10_2_tuned_500.png)

##VI. Threats to Validity
1. The tuned algorithm has been run on DTLZ5 and DTLZ7 with only 10 decisions and 2 objectives. It remains to be seen how the algorithm behaves with DTLZ1 and DTLZ3 models and with higher number of decisions.  
2. To make the algorithm run faster, I have used energy as a tuning parameter in DE, I would have to see how does the algorithm behaves with binary domination.  
3. Hypervolume is not a very credible parameter in multi-objective functions. I might need to look at other parameters like co-variance etc.  

##VII. Future Work
1. The run time of the algorithm is really slow, Future work would include using better techniques to improve the runtime.  
2. Using DE, the number of candidates generated is very slow after 10 or so candidates, so I have used technique to generate population in step. I would need to see if this effects results.  
3. The work would be much more credible if I have results for all the models used in code 9.
4. I would like to check if any other algorithm can tune GA better than GE.
5. I would like to check if using continuous dominance will help the runtime.

##VIII. Running Instructions
On a ubuntu 14.04 machine please copy all the code in home directory.  
Please give executable permission to "run.py".  
Run the file using command "python run.py".  

##IX References
1. https://www.easycalculation.com/statistics/inter-quartile-range.php  
2. http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf  
3. https://www.onepetro.org/conference-paper/SPE-64765-MS  
4. https://www.researchgate.net/post/How_to_tune_parameters_for_genetic_algorithm_approach_for_a_problem  













