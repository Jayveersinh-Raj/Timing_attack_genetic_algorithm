## This is the proof of concept for `Timing attack`, using `Genetic Algorithm`
 The search utilizes the idea of timing attack as computation time information may leak due to lookup in the dictionary for password matching, and comparing. The fitness function would be based on the timing. However, it is important to note that this is just a proof of concept, and is solely for educational purposes.


## To run type the following in the console within the directory
    python3 main.py

## Project structure
### Serverside
* *Database* &rarr; Represents a database that the server utilizes for verification. 
* *Match password* &rarr; Represents the server that relies on Database for verification.

### Utlization by the attacker
* *Length* &rarr; The program utilizes to approximate length for computation information leaked by verification from Database.
* *Password* &rarr; Represents the login attempt that is trying the genetically found passwords of the found length to get their timing information.

### Project Report
*Report.pdf* &rarr; IEEE format project report.

### The programs that executes and puts everything together
* *genetic_algorithm.py* &rarr; The class that contains all the functions of the genetic algorithms, that main_loop_ga.py, and main.py can utilize
* *main_loop_ga.py* &rarr; The function that repeatedly runs all the functions (except `populate` because `main.py` will do it, although it can do it too) from the genetic algorithm class until, either early stopping, generation limit, or login successfull is achivied
* *main.py* &rarr; The main driver code that only calls :
  1. Populate from GeneticAlgorithm class, and 
  2. Passes it to `main_loop_ga.py`

## hyperparameters.yaml
It is the yaml file that contains `hyper-parameters` that one can `tweek, experiment or play with` without changing anything in the code.

## Flow diagram
![loop](https://user-images.githubusercontent.com/69463767/206545322-5416ead9-a756-47da-a32c-5cd941e5cbb3.png)
### The above continues till either one of the following is met:
1. Login succes
2. End of generation loop limit
3. Early stop &rarr; Stop after user defined iterations if no better solution is being found till that given iteration limit, i.e. no convergence towards better results till last n iterations

## Sample output:
<img width="628" alt="image" src="https://user-images.githubusercontent.com/69463767/206548224-a5ba9df3-f0ae-41d6-96ed-2953c960e45c.png">

## An important note
1. Patience is required since one needs to repeat in between `100-1000` times for `timeit`, and initial population, length of password, and the `number of generations` do affect it
2. Cannot cover larger search space on single computer. The sample output covers only lower case alphabets. ASCII from `97-122`.
3. Dedicated machine is require otherwise the timing informations would not be correct, and good output might not be achieved.

## References
1. H. Ali and M. Al-Salami “Timing Attack Prospect for RSA Cryptanalysts Using Genetic Algorithm Technique”, The International Arab Journal of Information Technology, vol. 1, no. 1, Jan 2004
2. J. Dekeyser, "Timing attack by Genetic algorithm", medium.com. https://medium.com/javarevisited/timing-attack-by-genetic-algorithm-b93a4357cd43 (accessed Nov. 27, 2022)

