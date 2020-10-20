num = int(input())
is_prime = True

if num > 1:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
else:
    is_prime = False

print(is_prime)
