targets = list(map(int, input().split()))

while True:
    line = input()
    if line == 'End':
        break

    tokens = line.split()
    command = tokens[0]
    index = int(tokens[1])

    if command == 'Shoot':
        power = int(tokens[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif command == 'Add':
        value = int(tokens[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    elif command == 'Strike':
        radius = int(tokens[2])
        start_i = index - radius
        end_i = index + radius
        if (0 <= start_i < len(targets)) and (0 <= end_i < len(targets)):
            for i in range(start_i, end_i + 1):
                targets[i] = -1
            targets = [t for t in targets if t != -1]
        else:
            print('Strike missed!')

targets = [str(t) for t in targets]
print('|'.join(targets))



