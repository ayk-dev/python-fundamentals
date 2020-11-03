username = input()

while True:
    line = input()
    if line == 'Sign up':
        break

    args = line.split()
    command = args[0]
    if command == 'Case':
        new_str = ''
        if args[1] == 'lower':
            for ch in username:
                if ch.isalpha():
                    ch = ch.lower()
                new_str += ch
        else:
            for ch in username:
                if ch.isalpha():
                    ch = ch.upper()
                new_str += ch
        username = new_str
        print(username)

    elif command == 'Reverse':
        start_index = int(args[1])
        end_index = int(args[2]) + 1
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            rev_str = ''.join(list(reversed(username[start_index:end_index])))
            print(rev_str)

    elif command == 'Cut':
        substring = args[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif command == 'Replace':
        char = args[1]
        while char in username:
            username = username.replace(char, '*')
        print(username)

    elif command == 'Check':
        char = args[1]
        if char in username:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')