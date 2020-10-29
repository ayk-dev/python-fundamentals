import re

text = input()

pattern = r'(( |^)[a-zA-Z0-9]+([\.\-_][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([\-][a-zA-Z0-9]+)*([\.][a-z]+)+)'
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(0))

