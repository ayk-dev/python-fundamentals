days_of_adventure = int(input())
players_count = int(input())
group_energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water = water_per_day_per_person * days_of_adventure * players_count
total_food = food_per_day_per_person * days_of_adventure * players_count
is_out_of_energy = False

for day in range(1, days_of_adventure + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        is_out_of_energy = True
        break
    else:
        if day % 2 == 0:
            group_energy += 0.05 * group_energy
            total_water -= 0.3 * total_water
        if day % 3 == 0:
            total_food -= (total_food / players_count)
            group_energy += 0.1 * group_energy

if is_out_of_energy:
    message = f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.'
else:
    message = f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!'

print(message)