line = input().upper()

i = 0
rage_str = ''
final_rage = ''

while i < len(line):
    ch = line[i]

    if ch.isdigit():
        if i + 1 < len(line) and line[i + 1].isdigit():
            ch += line[i + 1]
            i += 1
        count = int(ch)
        current_rage = rage_str * count
        final_rage += current_rage
        rage_str = ''

    else:
        rage_str += ch

    i += 1

print(f'Unique symbols used: {len(set(final_rage))}')
print(final_rage)