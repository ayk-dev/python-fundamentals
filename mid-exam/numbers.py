numbers = list(map(int, input().split()))

average_value = sum(numbers) / len(numbers)

greater_than_average_value = [num for num in numbers if num > average_value]

greater_than_average_value = sorted(greater_than_average_value, reverse=True)

if len(greater_than_average_value) > 5:
    greater_than_average_value = greater_than_average_value[:5]
    greater_than_average_value = [str(num) for num in greater_than_average_value]
    print(' '.join(greater_than_average_value))

elif 0 < len(greater_than_average_value) <= 5:
    greater_than_average_value = [str(num) for num in greater_than_average_value]
    print(' '.join(greater_than_average_value))

else:
    print('No')