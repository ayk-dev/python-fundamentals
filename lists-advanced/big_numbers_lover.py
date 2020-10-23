numbers = input().split()

sorted_strings = sorted(numbers, reverse=True)

big_number_str = ''.join(sorted_strings)
print(big_number_str)