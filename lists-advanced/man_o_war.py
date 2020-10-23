def is_index_valid(i, length):
    return 0 <= i < length


pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health_capacity = int(input())
is_sunken = False

while True:
    command = input()
    if command == 'Retire':
        break
    tokens = command.split()
    if tokens[0] == 'Fire':
        index = int(tokens[1])
        damage = int(tokens[2])
        if is_index_valid(index, len(warship)):
            warship[index] -= damage
        else:
            continue

        if warship[index] <= 0:
            is_sunken = True
            print('You won! The enemy ship has sunken.')
            break

    elif tokens[0] == 'Defend':
        start_i = int(tokens[1])
        end_i = int(tokens[2])
        damage = int(tokens[3])
        if is_index_valid(start_i, len(pirate_ship)) and is_index_valid(end_i, len(pirate_ship)):
            for i in range(start_i, end_i+1):
                pirate_ship[i] -= damage

                if pirate_ship[i] < 0:
                    is_sunken = True
                    print('You lost! The pirate ship has sunken.')
                    break
            if is_sunken:
                break
        else:
            continue

    elif tokens[0] == 'Repair':
        index = int(tokens[1])
        health = int(tokens[2])
        if is_index_valid(index, len(pirate_ship)):
            pirate_ship[index] += health
        else:
            continue

        if pirate_ship[index] > max_health_capacity:
            pirate_ship[index] = max_health_capacity

    elif tokens[0] == 'Status':
        count = 0
        for i in range(len(pirate_ship)):
            section = pirate_ship[i]
            if section < 0.20 * max_health_capacity:
                count += 1
        print(f'{count} sections need repair.')

if not is_sunken:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')