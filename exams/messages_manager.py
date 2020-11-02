messages_sent = {}
messages_received = {}

capacity = int(input())

while True:
    line = input()
    if line == 'Statistics':
        break

    args = line.split('=')
    command = args[0]
    if command == 'Add':
        username = args[1]
        sent = int(args[2])
        received = int(args[3])
        if username not in messages_sent and username not in messages_received:
            messages_sent[username] = sent
            messages_received[username] = received

    elif command == 'Message':
        sender = args[1]
        receiver = args[2]
        if sender in messages_sent and receiver in messages_received:
            messages_sent[sender] += 1
            messages_received[receiver] += 1
            if messages_sent[sender] + messages_received[sender] == capacity:
                print(f'{sender} reached the capacity!')
                messages_sent.pop(sender)
                messages_received.pop(sender)
            if messages_received[receiver] + messages_sent[receiver] == capacity:
                print(f'{receiver} reached the capacity!')
                messages_sent.pop(receiver)
                messages_received.pop(receiver)

    elif command == 'Empty':
        username = args[1]
        if username == 'All':
            messages_received.clear()
            messages_sent.clear()
        else:
            messages_sent.pop(username)
            messages_received.pop(username)

total_messages = {}
for k, v in messages_sent.items():
    total_messages[k] = v + messages_received[k]

users_count = len(total_messages.keys())
print(f'Users count: {users_count}')

sorted_messages = dict(sorted(messages_received.items(), key=lambda x: (-x[1], x[0])))
for k, v in sorted_messages.items():
    print(f'{k} - {total_messages[k]}')
