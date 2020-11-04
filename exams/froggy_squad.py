frogs = input().split()

while True:
    line = input()
    tokens = line.split()

    command = tokens[0]
    if command == 'Join':
        name = tokens[1]
        frogs.append(name)

    elif command == 'Jump':
        name = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(frogs):
            frogs.insert(index, name)

    elif command == 'Dive':
        index = int(tokens[1])
        if 0 <= index < len(frogs):
            frogs.pop(index)

    elif command == 'First':
        count = int(tokens[1])
        frogs_to_print = frogs[:count]
        print(" ".join(frogs_to_print))

    elif command == 'Last':
        count = int(tokens[1])
        slice_count = len(frogs) - count
        frogs_to_print = frogs[slice_count:]
        print(" ".join(frogs_to_print))

    elif command == 'Print':
        if tokens[1] == 'Reversed':
            frogs = frogs[::-1]

        final_frogs = " ".join(frogs)
        print(f'Frogs: {final_frogs}')
        break
