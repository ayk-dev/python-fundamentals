string = input()

while True:
    line = input()
    if line == 'Done':
        break

    args = line.split()
    command = args[0]
    if command == 'TakeOdd':
        raw_password = ''
        for i in range(len(string)):
            if i % 2 != 0:
                raw_password += string[i]
        print(raw_password)
        string = raw_password

    elif command == 'Cut':
        index = int(args[1])
        length = int(args[2])
        to_cut = string[index:index + length]
        string = string.replace(to_cut, '', 1)
        print(string)

    elif command == 'Substitute':
        substring = args[1]
        substitute = args[2]
        if substring in string:
            while substring in string:
                string = string.replace(substring, substitute)
            print(string)
        else:
            print('Nothing to replace!')

print(f'Your password is: {string}')
