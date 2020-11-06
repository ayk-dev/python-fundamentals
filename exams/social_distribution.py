population = list(sorted(map(int, input().split(', '))))

min_wealth = int(input())

if len(population) * min_wealth > sum(population):
    print('No equal distribution possible')

else:
    poorest_i = 0
    richest_i = len(population) - 1
    for i in range(len(population)):
        if population[i] < min_wealth:
            diff = min_wealth - population[i]
            population[i] += diff
            population[richest_i] -= diff
    print(population)


