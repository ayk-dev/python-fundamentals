def blacklist_friend(value, friends_list):
    for i in range(len(friends_list)):
        if friends_list[i] == value:
            friends_list[i] = 'Blacklisted'
    return friends_list


friends = input().split(', ')

while True:
    line = input()
    if line == 'Report':
        break

    command = line.split()
    if command[0] == 'Blacklist':
        name = command[1]
        if name not in friends:
            print(f'{name} was not found.')
        else:
            friends = blacklist_friend(name, friends)
            print(f'{name} was blacklisted.')

    elif command[0] == 'Error':
        index = int(command[1])
        name = friends[index]
        if friends[index] != 'Blacklisted' and friends[index] != 'Lost':
            friends[index] = 'Lost'
            print(f'{name} was lost due to an error.')

    elif command[0] == 'Change':
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(friends):
            current_name = friends[index]
            friends[index] = new_name
            print(f'{current_name} changed his username to {new_name}.')

blacklist_count = friends.count('Blacklisted')
lost_count = friends.count('Lost')
print(f'Blacklisted names: {blacklist_count}')
print(f'Lost names: {lost_count}')
print(' '.join(friends))