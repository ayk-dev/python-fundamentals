quantity = int(input())
days_until_xmas = int(input())

ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLAND = 3
TREE_LIGHTS = 15

xmas_spirit = 0
total_cost = 0

for day in range(1, days_until_xmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ORNAMENT_SET * quantity
        xmas_spirit += 5
    if day % 3 == 0:
        total_cost += (TREE_SKIRT + TREE_GARLAND) * quantity
        xmas_spirit += 13
    if day % 5 == 0:
        total_cost += TREE_LIGHTS * quantity
        xmas_spirit += 17
    if day % 5 == 0 and day % 3 == 0:
        xmas_spirit += 30
    if day % 10 == 0:
        xmas_spirit -= 20
        total_cost += TREE_SKIRT + TREE_GARLAND + TREE_LIGHTS
    if day % 10 == 0 and day == days_until_xmas:
        xmas_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {xmas_spirit}')


