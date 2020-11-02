import re

pattern = r'(\*|@)([A-Z][a-z]{2,})\1: (\[([a-zA-Z])]\|)(\[([a-zA-Z])]\|)(\[([a-zA-Z])]\|)$'

n = int(input())
for _ in range(n):
    string = input()
    matches = re.search(pattern, string)
    if not matches:
        print('Valid message not found!')
    else:
        tag = matches[2]
        first_ch = matches[4]
        second = matches[6]
        third_ch = matches[8]
        encrypted_message = f'{ord(first_ch)} {ord(second)} {ord(third_ch)}'
        print(f'{tag}: {encrypted_message}')




