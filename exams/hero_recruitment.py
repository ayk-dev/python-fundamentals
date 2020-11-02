spell_book = {}

while True:
    line = input()
    if line == 'End':
        break

    args = line.split()
    command = args[0]
    hero_name = args[1]

    if command == 'Enroll':
        if hero_name in spell_book:
            print(f'{hero_name} is already enrolled.')
        else:
            spell_book[hero_name] = []

    elif command == 'Learn':
        spell = args[2]
        if hero_name not in spell_book:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell in spell_book[hero_name]:
                print(f'{hero_name} has already learnt {spell}.')
            else:
                spell_book[hero_name].append(spell)

    elif command == 'Unlearn':
        spell = args[2]
        if hero_name not in spell_book:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell not in spell_book[hero_name]:
                print(f"{hero_name} doesn't know {spell}.")
            else:
                spell_book[hero_name].remove(spell)

print('Heroes:')
sorted_heroes = dict(sorted(spell_book.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in sorted_heroes.items():
    print(f'== {k}: {", ".join(v)}')
