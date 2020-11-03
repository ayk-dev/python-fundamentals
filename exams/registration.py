import re

pattern = r'(U\$([A-Z][a-z]{2,})U\$P@\$([a-zA-Z]{5,}\d+)P@\$)'

count_successfull = 0
n = int(input())
for _ in range(n):
    registration = input()
    matches = re.findall(pattern, registration)
    if not matches:
        print('Invalid username or password')
        continue

    print('Registration was successful')
    count_successfull += 1
    username = matches[0][1]
    password = matches[0][2]
    print(f'Username: {username}, Password: {password}')

print(f'Successful registrations: {count_successfull}')

