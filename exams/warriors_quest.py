string = input()

while True:
    line = input()
    if line == 'For Azeroth':
        break

    args = line.split()
    command = args[0]
    if command == 'GladiatorStance':
        new_string = ''
        for ch in string:
            if ch.isalpha():
                ch = ch.upper()
            new_string += ch
        string = new_string
        print(string)

    elif command == 'DefensiveStance':
        new_string = ''
        for ch in string:
            if ch.isalpha():
                ch = ch.lower()
            new_string += ch
        string = new_string
        print(string)

    elif command == 'Dispel':
        index = int(args[1])
        letter = args[2]
        if index < 0 or index >= len(string):
            print('Dispel too weak.')
            continue
        string = string.replace(string[index], letter, 1)
        print('Success!')

    elif command == 'Target':

        if args[1] == 'Change':
            substring = args[2]
            second_substr = args[3]
            string = string.replace(substring, second_substr)
            print(string)

        elif args[1] == 'Remove':
            substring = args[2]
            string = string.replace(substring, '')
            print(string)
        else:
            print("Command doesn't exist!")

    else:
        print(f"Command doesn't exist!")