import re

pattern = r'([d-z{}|#]+)'

encrypted_string = input()
first_substr, second_substr = input().split()

match = re.match(pattern, encrypted_string)
if match:
    decoded_str = ''
    for ch in encrypted_string:
        new_ch = chr(ord(ch) - 3)
        decoded_str += new_ch

    while first_substr in decoded_str:
        decoded_str = decoded_str.replace(first_substr, second_substr)

    print(decoded_str)
else:
    print('This is not the book you are looking for.')


