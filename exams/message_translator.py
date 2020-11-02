import re

pattern = r'(!([A-Z][a-z]{3,})!:\[([a-zA-Z]{8,})\])'

n = int(input())
for i in range(n):
    message = input()
    match = re.findall(pattern, message)
    if not match:
        print('The message is invalid')
        continue

    valid_message = match[0][0]
    command = match[0][1]
    text = match[0][2]

    encrypted = []
    for ch in text:
        encrypted.append(str(ord(ch)))
    print(f'{command}: {" ".join(encrypted)}')





