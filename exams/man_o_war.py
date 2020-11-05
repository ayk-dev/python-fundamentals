def is_index_valid(i, length):
    return 0 <= i < length


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
is_sunken = False

while True:
    line = input()
    if line == 'Retire':
        break

    tokens = line.split()
    command = tokens[0]

    if command == 'Fire':
        index = int(tokens[1])
        if not is_index_valid(index, len(warship)):
            continue
        damage = int(tokens[2])
        warship[index] -= damage
        if warship[index] <= 0:
            is_sunken = True
            print('You won! The enemy ship has sunken.')
            break

    elif command == 'Defend':
        start_i = int(tokens[1])
        end_i = int(tokens[2])
        if not (is_index_valid(start_i, len(pirate_ship)) and is_index_valid(end_i, len(pirate_ship))):
            continue
        damage = int(tokens[3])
        for i in range(start_i, end_i + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                is_sunken = True
        if is_sunken:
            print('You lost! The pirate ship has sunken.')
            break

    elif command == 'Repair':
        index = int(tokens[1])
        if not is_index_valid(index, len(pirate_ship)):
            continue
        health = int(tokens[2])
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health

    elif command == 'Status':
        count = 0
        for i in range(len(pirate_ship)):
            if pirate_ship[i] < 0.20 * max_health:
                count += 1
        print(f'{count} sections need repair.')

if not is_sunken:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')
