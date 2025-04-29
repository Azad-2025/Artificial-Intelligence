import random

def fitness(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def create_board(n):
    return random.sample(range(n), n)

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

def mutate(board):
    n = len(board)
    i, j = random.sample(range(n), 2)
    board[i], board[j] = board[j], board[i]

def select(population, fitnesses):
    tournament = random.sample(list(zip(population, fitnesses)), 5)
    tournament.sort(key=lambda x: x[1])
    return tournament[0][0]

def genetic_algorithm(n, population_size=100, generations=1000, mutation_rate=0.05):
    population = [create_board(n) for _ in range(population_size)]
    for generation in range(generations):
        fitnesses = [fitness(board) for board in population]
        min_fitness = min(fitnesses)
        if min_fitness == 0:
            return population[fitnesses.index(min_fitness)]
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            if random.random() < mutation_rate:
                mutate(child1)
            if random.random() < mutation_rate:
                mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
        print(f"Generation {generation + 1}: Best Fitness = {min_fitness}")
    return None

if __name__ == "__main__":
    n = int(input("Enter size of chessboard (N): "))
    population_size = int(input("Enter population : "))
    generations = int(input("Enter  number of generations: "))
    mutation_rate = float(input("Enter the mutation rate (e.g., 0.05): "))
    solution = genetic_algorithm(n, population_size, generations, mutation_rate)
    print(f"Solution: {solution}")
    print(f"Fitness: {fitness(solution)}")
