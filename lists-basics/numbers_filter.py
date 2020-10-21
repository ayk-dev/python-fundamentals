n = int(input())

numbers_list = [int(input()) for _ in range(n)]
filtered_list = []

command = input()

for i in range(n):
    if command == 'even':
        filtered_list = list(filter(lambda num: num % 2 == 0, numbers_list))
    elif command == 'odd':
        filtered_list = list(filter(lambda num: num % 2 != 0, numbers_list))
    elif command == 'negative':
        filtered_list = list(filter(lambda num: num < 0, numbers_list))
    else:
        filtered_list = list(filter(lambda num: num >= 0, numbers_list))

print(filtered_list)