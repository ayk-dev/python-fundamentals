users = {}

while True:
    line = input()
    if line == 'Statistics':
        break

    args = line.split("->")
    command = args[0]
    username = args[1]
    if command == 'Add':
        if username in users:
            print(f"{username} is already registered")
        else:
            users[username] = []

    elif command == 'Send':
        email = args[2]
        if username not in users:
            users[username] = []
        users[username].append(email)

    elif command == 'Delete':
        if username in users:
            users.pop(username)
        else:
            print(f'{username} not found!')

count = len(users.keys())
print(f'Users count: {count}')

sorted_users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in sorted_users.items():
    print(f'{k}')
    for i in range(len(v)):
        print(f'- {v[i]}')