def check_is_index_valid(s, e, length):
    return 0 <= s < length and 0 < e < length


string = input()

while True:
    line = input()
    if line == 'Finish':
        break

    args = line.split()
    command = args[0]
    if command == 'Replace':
        current_ch = args[1]
        new_ch = args[2]
        while current_ch in string:
            string = string.replace(current_ch, new_ch)
        print(string)

    elif command == 'Cut':
        start_index = int(args[1])
        end_index = int(args[2])
        if not check_is_index_valid(start_index, end_index, len(string)):
            print(f'Invalid indexes!')
            continue
        string = string.replace(string[start_index:end_index + 1], '')
        print(string)

    elif command == 'Make':
        new_str = ''
        if args[1] == 'Upper':
            for ch in string:
                if ch.isalpha():
                    ch = ch.upper()
                new_str += ch
        elif args[1] == 'Lower':
            for ch in string:
                if ch.isalpha():
                    ch = ch.lower()
                new_str += ch
        string = new_str
        print(string)

    elif command == 'Check':
        substring = args[1]
        if substring in string:
            print(f'Message contains {substring}')
        else:
            print(f"Message doesn't contain {substring}")

    elif command == 'Sum':
        start_index = int(args[1])
        end_index = int(args[2])
        if not check_is_index_valid(start_index, end_index, len(string)):
            print(f'Invalid indexes!')
            continue

        substring = string[start_index:end_index + 1]
        value = 0
        for ch in substring:
            value += ord(ch)
        print(value)


