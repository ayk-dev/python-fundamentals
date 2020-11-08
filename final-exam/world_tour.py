destinations = input()

while True:
    line = input()
    if line == 'Travel':
        break

    args = line.split(':')
    command = args[0]

    if command == 'Add Stop':
        index = int(args[1])
        string = args[2]
        if 0 <= index < len(destinations) + 1:
            destinations = destinations[:index] + string + destinations[index:]

    elif command == 'Remove Stop':
        start_index = int(args[1])
        end_index = int(args[2])
        if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
            replace = destinations[start_index:end_index + 1]
            destinations = destinations.replace(replace, '')

    elif command == 'Switch':
        old_string = args[1]
        new_string = args[2]
        while old_string in destinations:
            destinations = destinations.replace(old_string, new_string)

    print(destinations)

print(f'Ready for world tour! Planned stops: {destinations}')