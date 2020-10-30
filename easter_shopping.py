shops_to_visit = input().split()
n = int(input()) # count of commands

for i in range(n):
    commands = input().split()
    if commands[0] == 'Include':
        shop = commands[1]
        shops_to_visit.append(shop)

    elif commands[0] == 'Visit':
        place = commands[1]
        number = int(commands[2])
        if len(shops_to_visit) < number:
            continue
        if number > len(shops_to_visit):
            continue
        if place == 'first':
            for _ in range(0, number):
                shops_to_visit.pop(0)
        elif place == 'last':
            for _ in range(0, number):
                shops_to_visit.pop(-1)

    elif commands[0] == 'Prefer':
        index_one = int(commands[1])
        index_two = int(commands[2])
        if 0 <= index_one < len(shops_to_visit) and 0 <= index_two < len(shops_to_visit):
            shops_to_visit[index_one], shops_to_visit[index_two] = shops_to_visit[index_two], shops_to_visit[index_one]

    elif commands[0] == 'Place':
        shop = commands[1]
        index = int(commands[2])
        insert_index = index + 1
        if 0 <= insert_index < len(shops_to_visit):
            shops_to_visit.insert(insert_index, shop)

print('Shops left:')
print(' '.join(shops_to_visit))