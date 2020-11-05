collecting_items = input().split(', ')

while True:
    line = input()
    if line == 'Craft!':
        break

    tokens = line.split(" - ")
    command = tokens[0]
    item = tokens[1]

    if command == 'Collect':
        if item not in collecting_items:
            collecting_items.append(item)

    elif command == 'Drop':
        if item in collecting_items:
            collecting_items.remove(item)

    elif command == 'Combine Items':
        item_tokens = item.split(':')
        old_item = item_tokens[0]
        new_item = item_tokens[1]
        if old_item in collecting_items:
            for i in range(len(collecting_items)):
                if collecting_items[i] == old_item:
                    collecting_items.insert(i+1, new_item)
                    break

    elif command == 'Renew':
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

print(', '.join(collecting_items))