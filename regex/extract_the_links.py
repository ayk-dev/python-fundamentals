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


pattern = r'((www\.)([^_][a-zA-Z0-9\-]+)(\.[a-z]+)+)'

text = get_multiline_input()
links = re.finditer(pattern, text)

for link in links:
    print(link.group(0))