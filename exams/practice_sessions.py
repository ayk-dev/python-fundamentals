roads = {}

while True:
    input_cmd = input()
    if input_cmd == 'END':
        break

    args = input_cmd.split('->')
    command = args[0]
    road = args[1]

    if command == 'Add':
        racer = args[2]
        if road not in roads.keys():
            roads[road] = []
        roads[road].append(racer)

    elif command == 'Move':
        racer = args[2]
        next_road = args[3]
        if racer in roads[road]:
            roads[road].remove(racer)
            roads[next_road].append(racer)

    elif command == 'Close':
        if road in roads.keys():
            roads.pop(road)

sorted_roads = dict(sorted(roads.items(), key=lambda x: (-len(x[1]), x[0])))
print('Practice sessions:')
for k, v in sorted_roads.items():
    print(k)
    for racer in v:
        print(f'++{racer}')

