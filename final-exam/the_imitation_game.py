message = input()

while True:
    line = input()
    if line == 'Decode':
        break

    args = line.split('|')
    command = args[0]

    if command == 'Move':
        number_of_letters = int(args[1])
        if 0 <= number_of_letters < len(message):
            letters_to_move = message[:number_of_letters]
            message = message[number_of_letters:] + letters_to_move

    elif command == 'Insert':
        index = int(args[1])
        value = args[2]
        message = message[:index] + value + message[index:]

    elif command == 'ChangeAll':
        substring = args[1]
        replacement = args[2]
        while substring in message:
            message = message.replace(substring, replacement)

print(f'The decrypted message is: {message}')