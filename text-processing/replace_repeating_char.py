string = input()

new_string = string[0]

for i in range(len(string)):
    if i == len(string) - 1:
        break
    if string[i + 1] != string[i]:
        new_string += string[i + 1]

print(new_string)