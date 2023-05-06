import numpy as np
import random
# Define the target solution
target_solution = "Hellow World!"
#Define the number of the generations and population size
population_size = 100
number_gen = 50
# Define the mutation rate
mutation_rate = 0.01

def generate_random_solution():
    
    solution = ""
    for _ in range(len(target_solution)):
        
        #Generate random character
        char = chr(random.randint(32,126))
        solution +=char
    return solution

def cal_fitness(solution):
    
    # generate random solution
    # Fitness is the number of character that matches the target solution
    fitness = 0
    for i in range(len(target_solution)):
        if solution[i] == target_solution[i]:
            fitness +=1
    return fitness 

def crossover(parent1, parent2):
    
    #Perform crossover between two parents to produce a new child
    child = ""
    for i in range(len(target_solution)):
        if random.random() < 0.5:
            child += parent1[i]
        else:
            child += parent2[i]
    return child

def mutation(solution):
    
    # perform mutation
    # randomly change the character of the string
    
    mutated_solution = ""
    for i in range(len(target_solution)):
        if random.random()<mutation_rate:
            
            # Generate random character
            char = chr(np.random.randint(32,126))
            mutated_solution += char
        else:
            mutated_solution += solution[i]
    return mutated_solution


# Generate the initial population
population = []
for _ in range(population_size):
    solution = generate_random_solution()
    population.append(solution)
    
for generation in range(number_gen):
    
    print('Generation :- ', generation)
    
    # Calculate the fitness of each solution
    fitness_score = []
    for solution in population:
        fitness = cal_fitness(solution)
        fitness_score.append(fitness)
        
    # Find the best solution
    best_fitness = max(fitness_score)
    best_solution = population[fitness_score.index(best_fitness)]
    
    print("Best Solution", best_solution)
    print("Fitness", best_fitness)
    
    #Create the next generation
    next_generation = []
    for _ in range(population_size):
        
        # Select the two parents based on their fitness
        parent1 = random.choices(population, weights = fitness_score)[0]
        parent2 = random.choices(population, weights = fitness_score)[0]
        
        #perform crossover and mutation to create new child
        child = crossover(parent1, parent2)
        child = mutation(child)
        
        # Add the child to the next generation
        next_generation.append(child)
        
    #Replace the current population with the next generation
    population = next_generation
    
        
        
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    