def is_index_valid(i, length):
    return 0 <= i < length


gifts = input().split()

while True:
    line = input()
    if line == 'No Money':
        break

    tokens = line.split()
    command = tokens[0]
    gift = tokens[1]

    if command == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'

    elif command == 'Required':
        index = int(tokens[2])
        if not is_index_valid(index, len(gifts)):
            continue

        gifts[index] = gift

    elif command == 'JustInCase':
        gifts[-1] = gift

final_gifts = [g for g in gifts if g != 'None']
print(' '.join(final_gifts))

