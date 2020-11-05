paintings = list(map(int, input().split()))

while True:
    line = input()
    if line == 'END':
        break

    tokens = line.split()
    command = tokens[0]
    if command == 'Change':
        painting_number = int(tokens[1])
        changed_number = int(tokens[2])

        if painting_number in paintings:
            for i in range(len(paintings)):
                if paintings[i] == painting_number:
                    paintings[i] = changed_number
                    break

    elif command == 'Hide':
        painting_number = int(tokens[1])
        if painting_number in paintings:
            paintings.remove(painting_number)

    elif command == 'Switch':
        painting_number = int(tokens[1])
        second_painting = int(tokens[2])

        if painting_number in paintings and second_painting in paintings:
            i_one = None
            i_two = None

            for i in range(len(paintings)):
                if paintings[i] == painting_number:
                    i_one = i
                if paintings[i] == second_painting:
                    i_two = i
                if i_one and i_two:
                    break

            paintings[i_one], paintings[i_two] = paintings[i_two], paintings[i_one]

    elif command == 'Insert':
        place = int(tokens[1]) + 1
        painting_number = int(tokens[2])
        if 0 <= place < len(paintings):
            paintings.insert(place, painting_number)

    elif command == 'Reverse':
        paintings = paintings[::-1]

paintings = [str(p) for p in paintings]
print(' '.join(paintings))
