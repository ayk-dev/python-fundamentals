import re


def get_encrypted_msg(string):
    artist, song = string[0].split(':')
    key = len(artist)
    new_str = ''
    for ch in string[0]:
        if ch == "'" or ch == " " or ch == ":":
            new_str += ch
            continue
        new_value = ord(ch) + key
        if new_value > 90 and 65 <= ord(ch) <= 90:
            new_value = 64 + (new_value - 90)
        if new_value > 122:
            new_value = 96 + (new_value - 122)
        ch = chr(new_value)
        new_str += ch

    new_str = new_str.replace(':', '@')
    return new_str


full_pattern = r"([A-Z][a-z' ]+):([A-Z ]+)"

while True:
    line = input()
    if line == 'end':
        break

    full_match = re.fullmatch(full_pattern, line)
    if not full_match:
        print(f'Invalid input!')
        continue

    encrypted = get_encrypted_msg(full_match)
    print(f'Successful encryption: {encrypted}')



