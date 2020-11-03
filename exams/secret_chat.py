message = input()

while True:
    line = input()
    if line == 'Reveal':
        break

    commands = line.split(':|:')
    if commands[0] == 'InsertSpace':
        index = int(commands[1])
        message = message[:index] + ' ' + message[index:]

    elif commands[0] == 'Reverse':
        substring = commands[1]
        if substring not in message:
            print('error')
            continue
        reversed_substr = substring[::-1]
        message = message.replace(substring, '', 1)
        message += reversed_substr

    elif commands[0] == 'ChangeAll':
        substring = commands[1]
        replacement = commands[2]
        while substring in message:
            message = message.replace(substring, replacement)
    print(message)

print(f'You have a new text message: {message}')


