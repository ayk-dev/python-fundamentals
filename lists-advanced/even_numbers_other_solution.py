is_even = lambda n: n % 2 != 0

numbers = [i for i, n in enumerate(map(int, input().split(', ')))]

even_indices = list(filter(is_even, numbers))

print(even_indices)

