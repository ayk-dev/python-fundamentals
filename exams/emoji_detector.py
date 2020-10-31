import re
from functools import reduce

string = input()

pattern = r'((::|\*\*)([A-Z][a-z]{2,})\2)'
pattern_digits = r'(\d)'

matches = re.findall(pattern, string)
emojis = [t[0] for t in matches]
emojis_only_letters = [t[2] for t in matches]

match_digits = re.findall(pattern_digits, string)
coolness_digits = [int(d) for d in match_digits]
cool_threshold = reduce((lambda x, y: x * y), coolness_digits)

emojis_coolness = []
for emoji in emojis_only_letters:
    coolness = 0
    for ch in emoji:
        coolness += ord(ch)
    emojis_coolness.append(coolness)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis_only_letters)} emojis found in the text. The cool ones are:')
for i in range(len(emojis_only_letters)):
    if emojis_coolness[i] > cool_threshold:
        print(f'{emojis[i]}')



