def calculate_sum_of_number(string):
    result = 0
    position = 0
    first_letter = string[0]
    second_letter = string[-1]
    number = int(string[1:-1])

    if first_letter.isupper():
        position = ord(first_letter) - 64
        result = number / position
    else:
        position = ord(first_letter) - 96
        result = number * position

    if second_letter.isupper():
        position = ord(second_letter) - 64
        result -= position
    else:
        position = ord(second_letter) - 96
        result += position

    return result


strings = input().split()
total_sum = 0
for string in strings:
    total_sum += calculate_sum_of_number(string)

print(f"{total_sum:.2f}")


