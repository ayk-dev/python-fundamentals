cities_gold = {}
cities_population = {}
while True:
    line = input()
    if line == 'Sail':
        break

    city, population, gold  = line.split('||')
    if city in cities_gold:
        cities_gold[city] += int(gold)
        cities_population[city] += int(population)
    else:
        cities_gold[city] = int(gold)
        cities_population[city] = int(population)

while True:
    input_line = input()
    if input_line == 'End':
        break

    args = input_line.split('=>')
    command = args[0]
    town = args[1]

    if command == 'Plunder':
        people = int(args[2])
        gold = int(args[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        cities_gold[town] -= gold
        cities_population[town] -= people
        if cities_gold[town] == 0 or cities_population[town] == 0:
            print(f'{town} has been wiped off the map!')
            cities_gold.pop(town)
            cities_population.pop(town)

    elif command == 'Prosper':
        gold = int(args[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number!')
            continue
        cities_gold[town] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities_gold[town]} gold.')

if cities_gold and cities_population:
    print(f'Ahoy, Captain! There are {len(cities_gold.keys())} wealthy settlements to go to:')
    sorted_cities = dict(sorted(cities_gold.items(), key=lambda x: (-x[1], x[0])))
    for key, value in sorted_cities.items():
        print(f'{key} -> Population: {cities_population[key]} citizens, Gold: {value} kg')