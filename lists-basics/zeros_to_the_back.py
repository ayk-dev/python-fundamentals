numbers = input().split(', ')

for i in range(len(numbers)):
    numbers.append(numbers.pop(numbers.index('0')))

integers = [int(num) for num in numbers]

print(integers)