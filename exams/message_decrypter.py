import re

pattern = r'(\$|%)([A-Z][a-z]{2,})(\1): (\[(\d+)\]\|)(\[(\d+)\]\|)(\[(\d+)\]\|)'

n = int(input())
for _ in range(n):
    message = input()
    matches = re.fullmatch(pattern, message)
    if not matches:
        print('Valid message not found!')
    else:
        tag = matches.group(2)
        first_num = int(matches.group(5))
        second_num = int(matches.group(7))
        third_num = int(matches.group(9))
        decrypted_message = chr(first_num) + chr(second_num) + chr(third_num)
        print(f'{tag}: {decrypted_message}')
