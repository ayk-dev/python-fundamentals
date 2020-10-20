n = int(input())

is_special = False

for i in range(1, n + 1):
    sum_of_digits = 0
    num = i
    while num > 0:
        last_digit = num % 10
        sum_of_digits += last_digit
        num //= 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
    else:
        is_special = False
    print(f'{i} -> {is_special}')
