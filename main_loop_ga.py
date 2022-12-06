from random import randint
from genetic_algorithm import GeneticAlgorithm as ga
import numpy as np

best_so_far = ""
best_max_time = 0

# to store number of generation
generation = 1

def ga_loop(target_len, target, population, n_generations):
    # calculate fitness for each
    # list to store fitness values
    global generation, best_so_far, best_max_time
    generation += 1
     # to stop on a particular epoch/generation
    if(generation == n_generations):
        return f"best achieved: {best_so_far}"
    # scores from fitting function
    scores = []
    for p in population:
        individual_score = (ga.fitness(target, p))

        if(individual_score > best_max_time):
            print(f"Best found so far : {p}")
            best_so_far = p

        if(individual_score == -1):
               return f"\n\nTarget achieved: '{p}' on {generation} generation \n"

        scores.append(individual_score)

    min_score = sorted(scores)[0]
    max_score = sorted(scores, reverse=True)[0]
       
    # normalizing the scores
    norm_scores = [((score-min_score)/(max_score-min_score)) for score in scores]
#
    max_score = max(norm_scores)
  ##
    # just a little fanciness for output
    bar = '█'*(int(generation/n_generations*100)) + '-' *(100 - int(generation/n_generations*100)-1)
    print(f"\r|{bar}| {int(generation/n_generations*100)+1}%", end = "\r")

     # list of candidates with score > 0
    candidates = []
    candidate_scores = []
    for i in range(len(norm_scores)):
        # all those with atleast 1 correct order of letter would be allowed to mate
        if(norm_scores[i]>0):
            good_candidate = population[i]
            candidate_scores.append(norm_scores[i])
            candidates.append(good_candidate)
   
    # new population from mating pool
    new_population = []
        
    for i in range(len(population)):
        # creating a mating pool of elements using their probabilities from fitting 
        mating_parents = ga.select(candidates, candidate_scores, max_score)

        # split from random points
        split_point = randint(0, target_len-1)

        # crossover of those parents to yield a breed
        breed = ga.crossover(mating_parents[0], mating_parents[1], split_point)
        if(ga.fitness(target, breed) == -1):
              return f"\n\nTarget achieved: '{breed}' on {generation} generation \n"

        # mutating the produced breed and adding it to the population
        new_population.append(ga.mutate(breed))

    generation += 1

    # Repeat by calculating the fitness
    return ga_loop(target_len, target, new_population, n_generations)