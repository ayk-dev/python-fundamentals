strings = input().split(' ')

repeated_string = ''

for s in strings:
    repeated_string += s * len(s)

print(repeated_string)