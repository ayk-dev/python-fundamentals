def convert_to_binary(num):
    result = ''
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result


def get_max_count_of_1(binary):
    counter = 0
    max_count = counter
    for digit in binary:
        if digit == '1':
            counter += 1
            if counter > max_count:
                max_count = counter

        else:
            counter = 0
    return max_count


n = int(input())
binary_n = convert_to_binary(n)
max_count_of_ones = get_max_count_of_1(binary_n)
print(max_count_of_ones)