def get_reversed_string(word):
    return word[::-1]


while True:
    string = input()
    if string == 'end':
        break

    rev_str = get_reversed_string(string)
    print(f'{string} = {rev_str}')

