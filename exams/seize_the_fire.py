def is_cell_valid(type, value):
    if type == 'High':
        return 81 <= value <= 125
    elif type == 'Medium':
        return 51 <= value <= 80
    else:
        return 1 <= value <= 50


fire_cells = input().split('#')
water = int(input())
total_effort = 0
total_fire = 0

print('Cells:')
for i in range(len(fire_cells)):
    tokens = fire_cells[i].split(' = ')
    type_fire = tokens[0]
    fire_value = int(tokens[1])

    if not is_cell_valid(type_fire, fire_value):
        continue

    if water >= fire_value:
        water -= fire_value
        effort = 0.25 * fire_value
        total_effort += effort
        put_out_cell = fire_value
        total_fire += fire_value
        print(f' - {fire_value}', end='\n')

print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')



