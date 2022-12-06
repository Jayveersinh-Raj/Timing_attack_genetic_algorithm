from Length.find_length import find_length
from Database.database import database
import time
from genetic_algorithm import GeneticAlgorithm
import main_loop_ga as main_loop



if __name__ == "__main__":

    target_length = find_length('jayveersinh_raj', 32)
    print(target_length)

    t = time.time()
    # size of population
    population_size = 1000

    # Populate
    population = GeneticAlgorithm.populate(target_length, population_size)

    # main ga(genetic algorithm) loop to find the result
    
    ''' Important to consider that the password from database is used as a stopping condition,
        however in real life scenario this can be considered if reponse is recieved as logged in'''

    result = main_loop.ga_loop(int(target_length), 'jayveersinh_raj', population, n_generations=100)
    print(result)
    print(f"\nTime taken: {time.time()-t:.2f} seconds")