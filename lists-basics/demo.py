gifts = input().split(' ')

while True:
    commands = input().split()
    command_string = ''.join(commands)
    if command_string == 'No Money':
        break
    elif commands[0] == 'Required':
        value_to_replace_with = commands[1]
        index_to_be_replaced = int(commands[2])
        if index_to_be_replaced + 1 <= len(gifts):
            gifts[index_to_be_replaced] = value_to_replace_with
    elif commands[0] == 'JustInCase':
        value_to_replace_with = commands[1]
        gifts[-1] = value_to_replace_with

for _ in range(gifts.count('None')):
    gifts.remove('None')
print(' '.join(gifts), end='')