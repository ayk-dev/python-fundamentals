the_dwarfs = {}

while True:
    line = input()
    if line == 'Once upon a time':
        break

    name, hat_color, physics = line.split(' <:> ')
    if hat_color not in the_dwarfs:
        the_dwarfs[hat_color] = {}
        the_dwarfs[hat_color][name] = int(physics)
    else:
        if name not in the_dwarfs[hat_color]:
            the_dwarfs[hat_color][name] = int(physics)
        else:
            if int(physics) > the_dwarfs[hat_color][name]:
                the_dwarfs[hat_color][name] = int(physics)

print(the_dwarfs)
sorted_dwarfs = dict(sorted(the_dwarfs.items(), key=lambda x: -x[2]))
print(sorted_dwarfs)
