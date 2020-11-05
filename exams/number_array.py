def is_index_valid(i, length):
    return 0 <= i < length


numbers = list(map(int, input().split()))

while True:
    line = input()
    if line == 'End':
        break

    commands = line.split()
    if commands[0] == 'Switch':
        index = int(commands[1])
        if not is_index_valid(index, len(numbers)):
            continue

        numbers[index] = -numbers[index]

    elif commands[0] == 'Change':
        index = int(commands[1])
        if not is_index_valid(index, len(numbers)):
            continue

        value = int(commands[2])
        numbers[index] = value

    elif commands[0] == 'Sum':
        if commands[1] == 'Negative':
            negatives = [num for num in numbers if num < 0]
            print(sum(negatives))

        elif commands[1] == 'Positive':
            positives = [num for num in numbers if num >= 0]
            print(sum(positives))

        else:
            print(sum(numbers))

positive_numbers = [str(num) for num in numbers if num >= 0]
print(' '.join(positive_numbers))


