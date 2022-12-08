from random import randint
from genetic_algorithm import GeneticAlgorithm as ga
import string

# storing good individuals, and good times
best_so_far = ""
best_max_time = 0

# to store number of generation, early stopping (drop out)
generation = 1
dropout_counter = 0

def ga_loop(target_len, target, population, mutation_rate, dropout, n_generations) -> string:

    global generation, best_so_far, best_max_time, dropout_counter
    generation += 1

    # if not getting better solution for a particular number of epochs, early stop, and return the best so far
    if(dropout[0] == True and dropout_counter == dropout[1]):
        print("\n dropped out")
        return (sum, best_so_far)

     # to stop on a particular epoch/generation
    if(generation == n_generations):
        return f"best achieved: {best_so_far}"


    # scores from fitting function
    scores = []
    for p in population:
        individual_score = (ga.fitness(target, p))

        # stop if login success
        if(individual_score == -1):
               return f"\n\nTarget achieved: '{p}' on {generation} generation \n"

        # if a good individual is found 
        if(1/(1+individual_score) < 1/(1+best_max_time)):
            print(f"Best found so far : {p}, goodness percentage: {1 - 1/(1+individual_score)}")
            best_so_far = p
            dropout_counter = 0
         
         # increment early stopping if no better solution found
        dropout_counter += 1
        scores.append(individual_score)

    # min and max scores
    min_score = sorted(scores)[0]
    max_score = sorted(scores, reverse=True)[0]
       
    # normalizing the scores
    norm_scores = [((score-min_score)/(max_score-min_score)) for score in scores]

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
        # finding parents for mating 
        mating_parents = ga.select(candidates, candidate_scores)

        # split from random points
        split_point = randint(0, target_len-1)

        # crossover of those parents to yield a breed
        breed = ga.crossover(mating_parents[0], mating_parents[1], split_point)

        # mutating the produced breed and adding it to the population
        new_population.append(ga.mutate(breed, mutation_rate))

    # increment generation
    generation += 1

    # Repeat by calculating the fitness
    return ga_loop(target_len, target, new_population, mutation_rate, dropout, n_generations)