key = int(input())
n = int(input())

message = ''

for _ in range(n):
    character = input()
    decrypted_chr = chr(ord(character) + key)
    message += decrypted_chr

print(message)

