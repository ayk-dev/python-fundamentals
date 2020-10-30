targets = list(map(int, input().split('|')))
shoot = 5
points = 0

while True:
    line = input()
    if line == 'Game over':
        break

    commands = line.split('@')
    if commands[0] == 'Shoot Left':
        start_index = int(commands[1])
        length = int(commands[2])
        if start_index >= len(targets) or start_index < 0:
            continue
        position = start_index - length
        if abs(position) > len(targets):
            position = position % len(targets)
        if targets[position] >= shoot:
            targets[position] -= shoot
            points += shoot
        else:
            points += targets[position]
            targets[position] = 0

    elif commands[0] == 'Shoot Right':
        start_index = int(commands[1])
        length = int(commands[2])
        if start_index >= len(targets) or start_index < 0:
            continue
        position = length + start_index
        if position > len(targets):
            position = position % len(targets)
        if targets[position] >= shoot:
            targets[position] -= shoot
            points += shoot
        else:
            points += targets[position]
            targets[position] = 0

    elif commands[0] == 'Reverse':
        targets = targets[::-1]

targets = list(map(str, targets))
final_targets = ' - '.join(targets)
print(final_targets)
print(f'Iskren finished the archery tournament with {points} points!')

