from Password.crack_password import crack_password
from Match_password.check_password import check_password
from random import randint
import string
import numpy as np
from Match_password.check_password import check_password
import timeit
import yaml

# read the hyper-parameters from yaml file using with context manager
with open('hyperparameters.yaml') as parameters:
       hyper_parameter = yaml.load(parameters, Loader=yaml.FullLoader)

# A class with methods of the entire genetic algorithm loop
class GeneticAlgorithm:

    def __init__(self) -> None:
        pass


    # function to populate the population
    @classmethod
    def populate(cls, target, target_len, n) -> list:

      # empty list to store our initial population
      population = []
      for _ in range(n):
      # each element in population is a parent for future generations
        parent =""
        char_found = []
        # generating parents randomly using the ascii values of characters
        for i in range(target_len):
         cf = ""
         times = []
         for j in range(hyper_parameter['lower_limit'], hyper_parameter['upper_limit']):
           trials = 100
           time_taken = timeit.repeat(stmt = 'check_password(user, str)',
                                 setup = f'user = {target!r}; input_str = {cf + chr(j)!r}',
                                 globals = globals(),
                                 number = trials,
                                 repeat=10)
           times.append(min(time_taken))
         cf+= chr(97 + times.index(max(times)))
         char_found.append(chr(97 + times.index(max(times))))
        parent = ''.join(char_found)
  
        # once the loop ends we have a parent  
        population.append(parent)

      return population


    # function to calculate fitness
    def fitness(user, individual) -> float:

      score = 0
      
      if(check_password(user, individual) == True):
        score = -1
        return score

      # fitness score of individual
      for i in range(len(individual)):
       score += crack_password(user, individual[i])
      return score
  

    # function to create a mating pool for cross over by populating parents according to their fitting
    @classmethod
    def select(cls, population, scores) -> list:
      parents_to_breed = []
      # scores in integer values
      p1 = cls.accept(population,scores)
      p2 = cls.accept(population, scores)
      parents_to_breed.append(p1)
      parents_to_breed.append(p2)
            
      return parents_to_breed


    # check the probabilities of generated parent meets the criteria with random number probability
    def accept(population, scores) -> list:
      while True:
        parent_index = randint(0, len(population)-1)
        rand_num = np.random.randn()
        if(rand_num < scores[parent_index]):
          return population[parent_index]
        else:
          pass 
  

    # function for crossover
    def crossover(parent1, parent2, split_point) -> string:
      p1 = parent1
      p2 = parent2
  
      child = p1[:split_point] + p2[split_point:]
  
      return child

    
     # function for mutation
    def mutate(individual, chance) -> string:
     
      # if chance is not provided as percentage, multiply by 100
      if(chance<=1):
         chance = chance * 100
         random_char = randint(hyper_parameter['lower_limit'], hyper_parameter['upper_limit'])
      else:
          pass

      # to store genes of an individual (characters)
      genes = []
      for i in individual:
          genes.append(i)
      
      # according to given mutation chance change characters/genes of an individual
      for i in range(len(genes)):
           mutation_genes = randint(0, 100)
           gene_to_modify = randint(0, len(genes)-1)
           if (mutation_genes <= chance):
              genes[gene_to_modify] = chr(random_char)
   
      individual = ''.join(genes)
      
      return individual


  