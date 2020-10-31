dictionary = {}

first_str = input().split(' | ')
for string in first_str:
    word, definition = string.split(': ')
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)

sorted_def = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))
second_str = input().split(' | ')
for word in second_str:
    if word in sorted_def.keys():
        print(f'{word}')
        sorted_values = sorted(sorted_def[word], key=len)
        for value in sorted_def[word]:
            print(f' -{value}')

third_str = input()
if third_str == 'End':
    pass
elif third_str == 'List':
    sorted_words = dict(sorted(sorted_def.items(), key=lambda x: x[0]))
    for word in sorted_words.keys():
        print(word, end=' ')