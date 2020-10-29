import re


def get_multiline_input():
    multiline_input = ''
    while True:
        s = input()
        if s != '':
            multiline_input += s + '\n'
        else:
            break
    return multiline_input


pattern = r'(\d+)'
text = get_multiline_input()
matches = re.findall(pattern, text, re.MULTILINE)

print(' '.join(matches))
