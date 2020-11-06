def is_index_valid(i, length):
    return 0 <= i < length


tasks = input().split()

COMPLETED = "0"
DROPPED = "-1"


while True:
    line = input()
    if line == 'End':
        break

    command = line.split()
    if command[0] == 'Complete':
        index = int(command[1])
        if not is_index_valid(index, len(tasks)):
            continue
        tasks[index] = COMPLETED

    elif command[0] == 'Change':
        index = int(command[1])
        if not is_index_valid(index, len(tasks)):
            continue

        time = command[2]
        tasks[index] = time

    elif command[0] == 'Drop':
        index = int(command[1])
        if not is_index_valid(index, len(tasks)):
            continue
        tasks[index] = DROPPED

    elif command[0] == 'Count':
        count_completed = tasks.count(COMPLETED)
        count_dropped = sum(x.startswith("-") for x in tasks)
        if command[1] == 'Completed':
            print(count_completed)

        elif command[1] == 'Dropped':
            print(count_dropped)

        else:
            count_incomplete = len(tasks) - (count_completed + count_dropped)
            print(count_incomplete)

incomplete_tasks = [task for task in tasks if not task.startswith('-') and task != COMPLETED]
print(' '.join(incomplete_tasks))

