n = int(input())

numbers_list = []
for _ in range(n):
    number = int(input())
    numbers_list.append(number)

command = input()
filtered_list = []
for number in numbers_list:
    filter_passes = (
        (command == 'even' and number % 2 == 0) or
        (command == 'odd' and number % 2 != 0) or
        (command == 'positive' and number >= 0) or
        (command == 'negative' and number < 0)
    )
    if filter_passes:
        filtered_list.append(number)

print(filtered_list)
