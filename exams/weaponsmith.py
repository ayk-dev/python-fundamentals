def is_index_valid(i, length):
    return 0 <= i < length


name_parts = input().split('|')

while True:
    line = input()
    if line == 'Done':
        break

    command = line.split()
    if command[0] == 'Move':
        index = int(command[2])
        if not is_index_valid(index, len(name_parts)):
            continue
        direction = command[1]
        if direction == 'Left' and index-1 >= 0:
            name_parts[index], name_parts[index-1] = name_parts[index-1], name_parts[index]
        elif direction == 'Right' and index+1 < len(name_parts):
            name_parts[index], name_parts[index + 1] = name_parts[index + 1], name_parts[index]

    elif command[0] == 'Check':
        if command[1] == 'Even':
            to_print = ''
            for i in range(len(name_parts)):
                if i % 2 == 0:
                    to_print += name_parts[i] + ' '
            print(to_print)
        else:
            to_print = ''
            for i in range(len(name_parts)):
                if i % 2 != 0:
                    to_print += name_parts[i] + ' '
            print(to_print)

weapon_name = ''.join(name_parts)
print(f'You crafted {weapon_name}!')