n = int(input())

phonebook = {}
for _ in range(n):
    name, number = input().split()
    phonebook[name] = number

while True:
    try:
        query_name = input()
        if query_name in phonebook:
            print(f'{query_name}={phonebook[query_name]}')
        else:
            print('Not found')
    except:
        break
