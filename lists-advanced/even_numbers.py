numbers = list(map(lambda num: int(num), input().split(', ')))

even_indices = [index for index, num in enumerate(numbers) if num % 2 == 0]
print(even_indices)