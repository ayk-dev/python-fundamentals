n = int(input())

parking = {}

for i in range(n):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        license_plate = command[2]
        if username in parking:
            print(f'ERROR: already registered with plate number {parking[username]}')
        else:
            parking[username] = license_plate
            print(f'{username} registered {license_plate} successfully')

    elif command[0] == "unregister":
        if username not in parking:
            print(f'ERROR: user {username} not found')
        else:
            parking.pop(username)
            print(f'{username} unregistered successfully')

for key, value in parking.items():
    print(f'{key} => {value}')



