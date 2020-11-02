import re

pattern = r'#([a-zA-Z]{3,})##([a-zA-Z]{3,})#|@([a-zA-Z]{3,})@@([a-zA-Z]{3,})@'

string = input()
matches = re.finditer(pattern, string)
count_pairs = 0
mirror_words = []

for match in matches:
    count_pairs += 1
    if '#' in match[0]:
        first_word = match[1]
        second_word = match[2]

    else:
        first_word = match[3]
        second_word = match[4]
    if first_word == second_word[::-1]:
        mirror_pair = f'{first_word} <=> {second_word}'
        mirror_words.append(mirror_pair)

if count_pairs == 0:
    print('No word pairs found!')
else:
    print(f'{count_pairs} word pairs found!')
if len(mirror_words) == 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirror_words))