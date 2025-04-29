import random


def create_pop(pop_size, list_len):
    population = []
    for _ in range(pop_size):
        individual = [random.randint(0, 9) for _ in range(list_len)]
        population.append(individual)
    return population

def fitness(individual, T):
    return abs(T - (individual[0] + individual[1]))  

def select_best_two(population, T):
    sort_pop = sorted(population, key=lambda x: fitness(x, T))
    return sort_pop[0], sort_pop[1]



def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]



def mutate(individual, rate=0.3):
    if random.random() < rate:
        index = random.randint(0, 1) 
        
        individual[index] = random.randint(0, 9)
    return individual

def genetic_algorithm(T, k, pop_size=100, generations=1000):
    population = create_pop(pop_size, k)

    for _ in range(generations):
        parent1, parent2 = select_best_two(population, T)

        cl1, cl2 = crossover(parent1, parent2)
        cl1 = mutate(cl1)
        cl2 = mutate(cl2)

        population.append(cl1)
        population.append(cl2)

        population = sorted(population, key=lambda x: fitness(x, T))[:pop_size]

        for individual in population:
            if individual[0] + individual[1] == T:
                individual[2:] = [0] * (len(individual) - 2)
                return individual

    return population[0]

T = int(input("Enter target T: ")) 
k = int(input("Enter length k: ")) 

solution = genetic_algorithm(T, k)

print("Output:", ' '.join(str(num) for num in solution))
