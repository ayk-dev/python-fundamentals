stores = {}

while True:
    cmd_input = input()
    if cmd_input == 'END':
        break

    args = cmd_input.split('->')
    command = args[0]
    store = args[1]

    if command == 'Add':
        items = args[2].split(',')
        if store not in stores:
            stores[store] = []
        stores[store] += items

    elif command == 'Remove':
        if store in stores.keys():
            stores.pop(store)

sorted_stores = dict(sorted(stores.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))
print('Stores list:')
for k, v in sorted_stores.items():
    print(k)
    for item in v:
        print(f'<<{item}>>')