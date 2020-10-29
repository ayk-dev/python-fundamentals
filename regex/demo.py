import re

text = 'The rain in Spain'
search_pattern = r'^The.*Spain$'
x = re.search(search_pattern, text)
next_pattern = r'ai'
y = re.findall(next_pattern, text)
print(x)
print(y)
