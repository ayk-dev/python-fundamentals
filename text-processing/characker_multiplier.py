first_str, second_str = input().split(' ')

multiplied = 0
if len(first_str) == len(second_str):
    for i in range(len(first_str)):
        multiplied += ord(first_str[i]) * ord(second_str[i])
else:
    min_length = min(len(first_str), len(second_str))
    for i in range(min_length):
        multiplied += ord(first_str[i]) * ord(second_str[i])

    bigger_word = first_str
    if len(first_str) < len(second_str):
        bigger_word = second_str
    for i in range(min_length, len(bigger_word)):
        multiplied += ord(bigger_word[i])

print(multiplied)