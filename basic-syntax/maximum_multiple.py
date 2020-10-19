divisor = int(input())
bound = int(input())

max_n = 0

for n in range(divisor, bound + 1):
    if n % divisor == 0 and 0 < n <= bound:
        if max_n < n:
            max_n = n

print(max_n)