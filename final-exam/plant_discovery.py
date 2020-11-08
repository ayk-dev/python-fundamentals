plants = {}

n = int(input())
for _ in range(n):
    plant, rarity = input().split('<->')
    if plant not in plants:
        plants[plant] = [[], []]  # rarity[0], ratings[1]
    plants[plant][0] = int(rarity)

while True:
    line = input()
    if line == 'Exhibition':
        break

    args = line.split(': ')
    command = args[0]
    if command == 'Rate':
        plant, rating = args[1].split(' - ')
        if plant in plants:
            plants[plant][1].append(float(rating))
        else:
            print('error')

    elif command == 'Update':
        plant, new_rarity = args[1].split(' - ')
        if plant in plants:
            plants[plant][0] = int(new_rarity)
        else:
            print('error')

    elif command == 'Reset':
        plant = args[1]
        if plant in plants:
            plants[plant][1] = []
        else:
            print('error')

    else:
        print('error')

average_ratings = {}
for key, value in plants.items():
    if len(value[1]) == 0:
        average = 0
    else:
        average = sum(value[1]) / len(value[1])
    average_ratings[key] = [value[0], average]

print('Plants for the exhibition:')
sorted_plants = dict(sorted(average_ratings.items(), key=lambda x: (-x[1][0], -x[1][1])))
for key, value in sorted_plants.items():
    print(f'- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}')

