#Evaluation of Models DTLZ1,DTLZ3,DTLZ5 and DTLZ7 using Genetic Algorithm

###Submitted By - Shashank Bipin Kumar (sbkumar) for ASE Fall 2015 Code 9

##I. Overview
This project would be about evaluating models DTLZ1,DTLZ3,DTLZ5 and DTLZ7 using Genetic Algorithms. The models chosen in this project are multi-objective which means that optimal solutions has to be taken using trade-off between conflicting objectives. The selection decision is taken using binary domination technique.

##II. Background
####Genetic Algorithm
Genetic Algorithms(GA) are adaptive heuristic search algorithms based on the evolutionary ideas of natural selection and genetics. GA works better than other AI techniques like linear programming, dfs, etc even in presence of reasonable noise. The major steps of GA are :-  
1. Initially a random population is selected.  
2. Good individuals are selected based on a fitness function.  
3. Genes from the good individuals propagate throughout the population so that two good parents produce better offspring.  
4. With iterations, the population becomes fitter than previous generation as off-springs are from fittest individuals of previous generation. 

The Models used are DTL1, DTLZ3, DTLZ5 and DTLZ7 which are multi-objective functions.    

##III. Introduction
Genetic Algorithm(GA) is used for solving optimization problems. This project studies working of GA on multi-objective functions DTLZ1,DTLZ3,DTLZ5 and DTLZ7 for combination of 10,20,40 objectives and 2,4,6,8 decisions. For a particular population, fittest candidates is found through binary domination and moved to a particular generation. Offspring from those parents are found through mutation and added to the next generation. Hypervolume of the Pareto Frontier is used to score the effectiveness of the algorithm for a model.   

##IV. Implementation
1. The value of parameters like mutation, crossover is used as given in project specification.  
2. 100 candidates are generated randomly at start and using binary domination the fittest population is selected to be moved to next generation.
3. The children are produced using the one point crossover randomly choosing the fittest parents found in step 2.  
4. At end of each iteration, the new population is compared with the old one using the type 2 comparator. If there is no improvement in five successive iteration, then the algorithm is terminated early.  

##V. Results
###For DTLZ1
![root directory] (./images/Result1.PNG)
###For DTLZ3  
![root directory] (./images/Result2.PNG)
###For DTLZ5
![root directory] (./images/Result3.PNG)
###For DTLZ7
![root directory] (./images/Result4.PNG)


##VI. Threats to Validity
1. The number of candidates is only 100 per generation. With multi-objective models under use, it would be better to have more number of candidates and choose fitter parents.
2. The experiment has been tried for 0.8 value for crossover and 0.05 value for mutation. It is not known how changing these values will effect the results.
3. The validity for this experiment is good since it has been tried for 1000 generations.


##VII. Future Work
1. Comparison techniques like continuous dominance can be used instead of binary domination.  
2. Different values of mutation and crossover can be tried to see if the result of an algorithm improves.  
3. The initial population can be tuned using another algorithm like Differential Evolution.  
4. Runtime and Optimality are two important criterion when selecting an algorithm in real world for a particular model. We can try to find out runtime  for each of these algorithms.  
5. Try these models on different algorithms and validate performance of Genetic Algorithm.

##VIII. Running Instructions
1. On a ubuntu 14.04 machine please copy all the code in home directory.
2. Please give executable permission to "run.py".
3. Run the file using command "python run.py". 

## IX References
1. http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf
2. https://en.wikipedia.org/wiki/Genetic_algorithm
3. http://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol1/hmw/article1.html






