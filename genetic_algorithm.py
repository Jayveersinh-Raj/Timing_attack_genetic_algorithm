from Password.crack_password import crack_password
from Match_password.check_password import check_password
from random import randint
import sys
import string
import numpy as np
from Match_password.check_password import check_password
import timeit

# class with methods of the entire genetic algorithm loop
class GeneticAlgorithm:

    def __init__(self) -> None:
        pass


    # function to populate the population
    @classmethod
    def populate(cls, target, target_len,n) -> list:

    # empty list to store our initial population
      population = []
       
      # Size of population is n with size equal to the target
      for _ in range(n):
        # each element in population is a parent for future generations
        parent =""
        potential_parent = []
        times = np.empty(target_len)
        # generating parents randomly using the ascii values of characters
        for i in range(97, 122):
           trials = 1000
           time_taken = timeit.repeat(stmt = 'check_password(user, str)',
                                 setup = f'user = {target!r}; input_str = {chr(i)!r}',
                                 globals = globals(),
                                 number = trials,
                                 repeat=10)
           times[i] = min(time_taken)
        parent = parent + str()
  
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
  
      # for each character if they are the same and in the correct position
     # for i in range(len(target)):
     #     if(target[i] == individual[i]):
     #         score+=1      
     #     else:
     #         pass
     #       


    # function to create a mating pool for cross over by populating parents according to their fitting
    @classmethod
    def select(cls, population, scores, max_score) -> list:
      parents_to_breed = []
      # scores in integer values
      p1 = cls.accept(population,scores, max_score)
      p2 = cls.accept(population, scores, max_score)
      parents_to_breed.append(p1)
      parents_to_breed.append(p2)
            
      return parents_to_breed


    # check the probabilities of generated parent meets the criteria with random number probability
    def accept(population, scores, max_score):
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
    def mutate(individual) -> string:
      
      # to store genes of an individual (characters)
      genes = []
      for i in individual:
          genes.append(i)

      rand_num = randint(0, len(genes)-1)

      # according to given mutation chance change characters/genes of an individual
      ran_value = randint(97, 122)
      genes[rand_num] = chr(ran_value)
      individual = ''.join(genes)

      return individual


  