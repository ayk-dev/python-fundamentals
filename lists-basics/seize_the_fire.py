def cell_fire_value_range(type_fire):
    if type_fire == 'Low':
        min_fire_value = 1
        max_fire_value = 50
    elif type_fire == 'Medium':
        min_fire_value = 51
        max_fire_value = 80
    elif type_fire == 'High':
        min_fire_value = 81
        max_fire_value = 125
    return min_fire_value, max_fire_value


fire_cells = input().split('#')
water = int(input())

effort = 0
fire_put_out = 0

print('Cells:')
for i in range(len(fire_cells)):
    cell = fire_cells[i].split(' = ')
    cell_fire_type = cell[0]
    cell_fire_value = int(cell[1])

    min_fire, max_fire = cell_fire_value_range(cell_fire_type)
    if min_fire <= cell_fire_value <= max_fire:
        if water >= cell_fire_value:
            effort += 0.25 * cell_fire_value
            fire_put_out += cell_fire_value
            print(' -', cell_fire_value)
        else:
            continue
    else:
        continue
    water -= cell_fire_value
    if water < 0:
        break

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire_put_out}')






