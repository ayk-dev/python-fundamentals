def sort_fn(element):
    return element[0]


tasks_with_priority = []

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split('-', maxsplit=1)
    priority = int(tokens[0])
    task = tokens[1]
    tasks_with_priority.append((priority, task))

sorted_tasks = sorted(tasks_with_priority, key=sort_fn)
tasks = [task[1] for task in sorted_tasks]
print(tasks)