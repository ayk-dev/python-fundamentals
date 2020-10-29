import re

sentence = input().lower()
word = input().lower()

pattern = f'{word}\\b'
matches = re.findall(pattern, sentence)
count = len(matches)
print(count)
