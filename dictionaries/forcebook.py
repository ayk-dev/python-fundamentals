def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


force_side = {}

while True:
    data = input()
    if data == 'Lumpawaroo':
        break

    if ' | ' in data:
        args = data.split(' | ')
        side = args[0]
        user = args[1]

        all_users = [item for current_list in force_side.values() for item in current_list]
        if user in all_users:
            continue

        validate_key_existing(force_side, side, [])
        force_side[side].append(user)

    else:
        args = data.split(' -> ')
        user = args[0]
        side = args[1]
        validate_key_existing(force_side, side, [])
        for k in force_side:
            if user in force_side[k]:
                force_side[k].remove(user)
        force_side[side].append(user)
        print(f'{user} joins the {side} side!')

force_side = dict(sorted(force_side.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in force_side.items():
    if len(v) == 0:
        continue
    print(f'Side: {k}, Members: {len(v)}')
    v = list(sorted(v))
    for member in v:
        print(f'! {member}')