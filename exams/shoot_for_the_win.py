def change_value_of_target(integers, ind):
    for i in range(len(integers)):
        if i == ind:
            continue
        if integers[i] > value and integers[i] != SHOT_TARGET:
            integers[i] -= value
        elif integers[i] <= value and integers[i] != SHOT_TARGET:
            integers[i] += value
    return integers


def get_final_output(integers):
    final_targets_list = [str(integer) for integer in integers]
    return ' '.join(final_targets_list)


input_targets = input().split()
targets = [int(target) for target in input_targets]

SHOT_TARGET = -1
counter = 0
command = input()

while command != 'End':
    index = int(command)
    if index >= len(targets):
        command = input()
        continue
    value = targets[index]
    if value == SHOT_TARGET:
        continue
    else:
        targets[index] = SHOT_TARGET
        counter += 1
        targets = change_value_of_target(targets, index)
    command = input()


final_targets = get_final_output(targets)

print(f'Shot targets: {counter} -> {final_targets}')