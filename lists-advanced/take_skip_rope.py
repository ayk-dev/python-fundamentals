encrypted = list(input())

numbers = []
non_numbers = []
for symbol in encrypted:
    if symbol.isdigit():
        numbers.append(int(symbol))
    else:
        non_numbers.append(symbol)

take_numbers = []
skip_numbers = []
for i, num in enumerate(numbers):
    if i % 2 == 0:
        take_numbers.append(num)
    else:
        skip_numbers.append(num)

decrypted = []
count = len(take_numbers)
for i in range(count):
    decrypted += non_numbers[0:take_numbers[i]]

    non_numbers = non_numbers[take_numbers[i]:]
    for j in range(skip_numbers[i]):
        non_numbers.pop(0)

print("".join(decrypted))