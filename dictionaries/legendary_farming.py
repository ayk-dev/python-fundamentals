def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


legendary_items = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'
}

key_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

junk = {}

winner = None
goal = 250

while not winner:
    data = input().lower().split(' ')
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1]

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= goal:
                winner = material
                key_materials[material] -= goal
                break
        else:
            validate_key_existing(junk, material)
            junk[material] += quantity

item_won = legendary_items[winner]
print(f'{item_won} obtained!')

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
print_dict(key_materials, '{}: {}')

junk = dict(sorted(junk.items(), key=lambda x: x[0]))
print_dict(junk, '{}: {}')