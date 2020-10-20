tank_capacity = 255 # liters
n = int(input())

water_in_tank = 0
available_capacity = tank_capacity


for _ in range(n):
    liters = int(input())
    if available_capacity < liters:
        print('Insufficient capacity!')
        continue
    available_capacity -= liters
    water_in_tank += liters

print(water_in_tank)

