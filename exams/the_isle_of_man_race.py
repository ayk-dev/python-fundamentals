import re

pattern = r'(#|\$|%|\*|&)([a-zA-Z]+)\1=(\d+)!!(.+)'
is_found = False

while not is_found:
    message = input()
    matches = re.fullmatch(pattern, message)
    if not matches:
        print('Nothing found!')
        continue

    full_message = matches[0]
    name_racer = matches[2]
    length_of_geohashcode = int(matches[3])
    encrypted_geohashcode = matches[4]

    length = len(encrypted_geohashcode)

    if length_of_geohashcode != length:
        print('Nothing found!')
        continue

    geohashcode = ''
    for ch in encrypted_geohashcode:
        ch = chr(ord(ch) + length)
        geohashcode += ch
    is_found = True
    print(f"Coordinates found! {name_racer} -> {geohashcode}")

