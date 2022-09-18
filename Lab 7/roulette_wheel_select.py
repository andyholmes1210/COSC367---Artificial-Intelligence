def roulette_wheel_select(population, fitness, r):
    sum_fitness = sum(fitness(i) for i in population)
    percent_fitness = [(i, fitness(i)/sum_fitness) for i in population]
    total = 0
    for individual, fit in percent_fitness:
        total += fit
        if total > r:
            return individual



population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))



population = ['cosc']

def fitness(x):
    return 50

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))