string = input()

i = 0
total_strength = 0

while i < len(string):
    ch = string[i]

    if ch == '>':
        strength = int(string[i + 1])
        total_strength += strength
    else:
        if total_strength > 0:
            string = string[:i] + string[i + 1:]
            i -= 1
            total_strength -= 1
    i += 1

print(string)
