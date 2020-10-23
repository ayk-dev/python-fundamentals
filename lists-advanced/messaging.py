numbers = list(map(int, input().split()))
string = list(input())

message = []
sum_of_digits = []
for num in numbers:
    digits_of_num = list(map(int, list(str(num))))
    sum_of_digits.append(sum(digits_of_num))

for n in sum_of_digits:
    index = n
    if 0 <= index < len(string):
        letter = string.pop(index)
        message.append(letter)

    else:
        index = n % len(string)
        letter = string.pop(index)
        message.append(letter)

print(''.join(message))

