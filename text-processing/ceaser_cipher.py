text = input()

encrypted = ''
for ch in text:
    encrypted += chr(ord(ch) + 3)

print(encrypted)