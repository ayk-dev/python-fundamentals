def is_index_valid(i, length):
    message = None
    if i < 0 or i >= length:
        message = 'Index out of range'
        return message


tanks_owned = input().split(', ')
n = int(input())

for i in range(n):
    line = input()
    tokens = line.split(', ')
    command = tokens[0]
    if command == 'Add':
        tank_name = tokens[1]
        if tank_name in tanks_owned:
            print('Tank is already bought')
        else:
            tanks_owned.append(tank_name)
            print('Tank successfully bought')

    elif command == 'Remove':
        tank_name = tokens[1]
        if tank_name in tanks_owned:
            tanks_owned.remove(tank_name)
            print('Tank successfully sold')
        else:
            print(f'Tank not found')

    elif command == 'Remove At':
        index = int(tokens[1])
        if is_index_valid(index, len(tanks_owned)):
            print(is_index_valid(index, len(tanks_owned)))
            continue
        tanks_owned.pop(index)
        print('Tank successfully sold')

    elif command == 'Insert':
        index = int(tokens[1])
        if is_index_valid(index, len(tanks_owned)):
            print(is_index_valid(index, len(tanks_owned)))
            continue
        else:
            tank_name = tokens[2]
            if tank_name not in tanks_owned:
                tanks_owned.insert(index, tank_name)
                print('Tank successfully bought')
            else:
                print('Tank is already bought')

print(', '.join(tanks_owned))

