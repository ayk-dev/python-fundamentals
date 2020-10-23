wagons = int(input())

train = [0] * wagons

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split()
    if tokens[0] == 'add':
        people = int(tokens[1])
        train[-1] += people
    elif tokens[0] == 'insert':
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] += people
    elif tokens[0] == 'leave':
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] -= people

print(train)
