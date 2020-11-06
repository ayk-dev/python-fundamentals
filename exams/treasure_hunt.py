def is_index_valid(i, length):
    return 0 <= i < length


initial_loot = input().split('|')

while True:
    line = input()
    if line == 'Yohoho!':
        break

    command = line.split(' ', maxsplit=1)
    if command[0] == 'Loot':
        items = command[1].split()
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command[0] == 'Drop':
        index = int(command[1])
        if not is_index_valid(index, len(initial_loot)):
            continue
        dropped_item = initial_loot.pop(index)
        initial_loot.append(dropped_item)

    elif command[0] == 'Steal':
        count = int(command[1])
        stolen_items = []
        if count <= len(initial_loot):
            for _ in range(count):
                stolen = initial_loot.pop()
                stolen_items.insert(0, stolen)
        else:
            for _ in range(len(initial_loot)):
                stolen = initial_loot.pop()
                stolen_items.insert(0, stolen)
        print(', '.join(stolen_items))

items_count = len(initial_loot)
if len(initial_loot) > 0:
    total_length = 0
    for item in initial_loot:
        item_length = len(item)
        total_length += item_length
    average_gain = total_length / items_count
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
else:
    print(f'Failed treasure hunt.')