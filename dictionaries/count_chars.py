def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


string = input()

characters = {}

list_of_chars = [ch for ch in string if ch != ' ']

for ch in list_of_chars:
    validate_key_existing(characters, ch)
    characters[ch] += 1

print_dict(characters, '{} -> {}')
