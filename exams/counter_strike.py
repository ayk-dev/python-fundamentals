initial_energy = int(input())

energy_left = initial_energy
is_out_of_energy = False
won_battles_counter = 0

command = input()

while command != 'End of battle':
    distance = int(command)
    if energy_left < distance:
        print(f'Not enough energy! Game ends with {won_battles_counter} won battles and {energy_left} energy')
        is_out_of_energy = True
        break
    else:
        energy_left -= distance
        won_battles_counter += 1
    if won_battles_counter % 3 == 0:
        energy_left += won_battles_counter
    command = input()

if not is_out_of_energy:
    print(f'Won battles: {won_battles_counter}. Energy left: {energy_left}')

