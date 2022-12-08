from Length.find_length import find_length
import time
from genetic_algorithm import GeneticAlgorithm
import main_loop_ga as main_loop
import yaml

# The main driver code
if __name__ == "__main__":

    # read the hyper-parameters from yaml file using with context manager
    with open('hyperparameters.yaml') as parameters:
       hyper_parameter = yaml.load(parameters, Loader=yaml.FullLoader)

    # find the approximated length of the password
    target_length = find_length('jayveersinh_raj', 32)
    print(f"Found approximated password length: {target_length}")

    t = time.time()

    # size of population
    population_size = 100

    # Populate
    population = GeneticAlgorithm.populate('jayveersinh_raj', target_length, hyper_parameter['population_size'])

    # main ga(genetic algorithm) loop to find the result
    
    ''' Important to consider that the password from database is used as a stopping condition,
        however in real life scenario this can be considered if reponse is recieved as logged in'''

    result = main_loop.ga_loop(int(target_length), 'jayveersinh_raj', population, 
                               hyper_parameter['mutation_per'],
                               (hyper_parameter['dropout'], hyper_parameter['dropout_number']),
                               hyper_parameter['n_generations'])
    print(result)
    print(f"\nTime taken: {time.time()-t:.2f} seconds")