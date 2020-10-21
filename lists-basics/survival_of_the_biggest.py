numbers_str = input().split()
n = int(input())

numbers = [int(numbers_str[i]) for i in range(len(numbers_str))]

biggest_numbers = []
biggest_numbers_range = len(numbers) - n

for _ in range(biggest_numbers_range):
    biggest_numbers.append(max(numbers))
    numbers.remove(max(numbers))

print(biggest_numbers)


