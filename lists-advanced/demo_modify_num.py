def modify_number(x):
    result = x
    if x % 2 ==0:
        result = 2 * x
    return result


numbers = input().split()
numbers = list(map(int, numbers))

modified_numbers = [modify_number(num) for num in numbers]

print(numbers)
print(modified_numbers)