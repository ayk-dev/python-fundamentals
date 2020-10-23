electrons = int(input())

shell = []
shield_index = 1
electrons_left = electrons

while electrons_left > 0:
    electrons_in_shield = 2 * shield_index ** 2
    if electrons_in_shield <= electrons_left:
        shield_index += 1
        shell.append(electrons_in_shield)
    else:
        shell.append(electrons_left)
    electrons_left -= electrons_in_shield

print(shell)