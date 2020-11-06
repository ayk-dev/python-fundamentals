groceries = input().split('!')

while True:
    is_in_list = False
    command = input()
    if command == 'Go Shopping!':
        break

    tokens = command.split()
    if tokens[0] == 'Urgent':
        item = tokens[1]
        for grocery in groceries:
            if item == grocery:
                is_in_list = True
        if not is_in_list:
            groceries.insert(0, item)

    elif tokens[0] == 'Unnecessary':
        item = tokens[1]
        for grocery in groceries:
            if item == grocery:
                groceries.remove(grocery)

    elif tokens[0] == 'Correct':
        old_item = tokens[1]
        new_item = tokens[2]
        for i in range(len(groceries)):
            if groceries[i] == old_item:
                groceries[i] = new_item
                break

    elif tokens[0] == 'Rearrange':
        item = tokens[1]
        for i in range(len(groceries)):
            if groceries[i] == item:
                groceries.remove(groceries[i])
                index = len(groceries)
                groceries.insert(index, item)

final_groceries = ', '.join(groceries)
print(final_groceries)
