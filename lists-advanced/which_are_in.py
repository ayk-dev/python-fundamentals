strings_one = input().split(', ')
text = input()

new_strings = [word for word in strings_one if word in text]

print(new_strings)