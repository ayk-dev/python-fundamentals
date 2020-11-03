string = input()

while True:
    line = input()
    if line == 'End':
        break

    args = line.split()
    command = args[0]
    if command == 'Translate':
        char = args[1]
        replacement = args[2]
        while char in string:
            string = string.replace(char, replacement)
        print(string)

    elif command == 'Includes':
        includes_str = args[1]
        print(includes_str in string)

    elif command == 'Start':
        start_str = args[1]
        print(string.startswith(start_str, 0, len(start_str)))

    elif command == 'Lowercase':
        new_str = ''
        for ch in string:
            ch = ch.lower()
            new_str += ch
        string = new_str
        print(string)

    elif command == 'FindIndex':
        char = args[1]
        indexes = []
        for i in range(len(string)):
            if string[i] == char:
                indexes.append(i)
        print(indexes[-1])

    elif command == 'Remove':
        start_index = int(args[1])
        count = int(args[2])
        to_remove = string[start_index:start_index + count]
        string = string.replace(to_remove, '')
        print(string)
