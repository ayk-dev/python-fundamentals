n = int(input())

heroes_hp = {}
heroes_mp = {}
for _ in range(n):
    hero = input().split()
    heroes_hp[hero[0]] = int(hero[1])
    heroes_mp[hero[0]] = int(hero[2])

while True:
    line = input()
    if line == 'End':
        break

    args = line.split(' - ')
    command = args[0]
    name = args[1]
    if command == 'CastSpell':
        mp_needed = int(args[2])
        spell_name = args[3]
        if heroes_mp[name] >= mp_needed:
            heroes_mp[name] -= mp_needed
            print(f'{name} has successfully cast {spell_name} and now has {heroes_mp[name]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')

    elif command == 'TakeDamage':
        damage = int(args[2])
        attacker = args[3]
        heroes_hp[name] -= damage
        if heroes_hp[name] > 0:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes_hp[name]} HP left!')
        else:
            print(f'{name} has been killed by {attacker}!')
            heroes_hp.pop(name)
            heroes_mp.pop(name)

    elif command == 'Recharge':
        amount = int(args[2])
        if heroes_mp[name] + amount > 200:
            amount = 200 - heroes_mp[name]
        heroes_mp[name] += amount
        print(f'{name} recharged for {amount} MP!')

    elif command == 'Heal':
        amount = int(args[2])
        if heroes_hp[name] + amount > 100:
            amount = 100 - heroes_hp[name]
        heroes_hp[name] += amount
        print(f'{name} healed for {amount} HP!')

sorted_heroes = dict(sorted(heroes_hp.items(), key=lambda x: (-x[1], x[0])))
for hero, value in sorted_heroes.items():
    print(hero)
    print(f'HP: {value}')
    print(f'MP: {heroes_mp[hero]}')