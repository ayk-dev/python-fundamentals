import re

pattern = r'(([^>]+)>([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<]{3})<\2)'

n = int(input())
for _ in range(n):
    string = input()
    matches = re.findall(pattern, string)
    if not matches:
        print('Try another password!')
        continue

    password = matches[0][2] + matches[0][3] + matches[0][4] + matches[0][5]
    print(f'Password: {password}')


