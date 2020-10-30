contacts = input().split()

while True:
    line = input()
    tokens = line.split()
    command = tokens[0]

    if command == 'Add':
        name = tokens[1]
        index = int(tokens[2])
        if name not in contacts:
            contacts.append(name)
        else:
            if 0 <= index < len(contacts):
                contacts.insert(index, name)

    elif command == 'Remove':
        index = int(tokens[1])
        if 0 <= index < len(contacts):
            contacts.pop(index)

    elif command == 'Export':
        start_i = int(tokens[1])
        count = int(tokens[2])

        contacts_to_print = contacts[start_i:start_i + count]
        print(' '.join(contacts_to_print))

    elif command == 'Print':
        if tokens[1] == 'Reversed':
            contacts = contacts[::-1]

        final_contacts = " ".join(contacts)
        print(f'Contacts: {final_contacts}')
        break
