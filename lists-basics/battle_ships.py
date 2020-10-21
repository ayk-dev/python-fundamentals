n = int(input()) # number of rows in the field

ships_field = []
for i in range(n):
    row = list(map(int, input().split()))
    ships_field += [row]

count = 0

squares_attacked = input().split()
number_of_attacks = len(squares_attacked)
for i in range(number_of_attacks):
    attack = list(map(int, squares_attacked[i].split('-')))
    row = attack[0]
    column = attack[1]
    if ships_field[row][column] == 0:
        continue
    ships_field[row][column] -= 1
    if ships_field[row][column] == 0:
        count += 1

print(count)
