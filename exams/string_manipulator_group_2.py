string = input()

while True:
    line = input()
    if line == 'Done':
        break

    args = line.split()
    command = args[0]
    if command == 'Change':
        char = args[1]
        replacement = args[2]
        while char in string:
            string = string.replace(char, replacement)
        print(string)

    elif command == 'Includes':
        includes_str = args[1]
        print(includes_str in string)

    elif command == 'End':
        end_str = args[1]
        print(end_str in string)

    elif command == 'Uppercase':
        new_str = ''
        for ch in string:
            ch = ch.upper()
            new_str += ch
        string = new_str
        print(string)

    elif command == 'FindIndex':
        char = args[1]
        for i in range(len(string)):
            if string[i] == char:
                print(i)
                break

    elif command == 'Cut':
        start_index = int(args[1])
        length = int(args[2])
        string = string[start_index:start_index + length]
        print(string)

