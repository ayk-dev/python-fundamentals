lost_fights_count = int(input())  # in the range [0, 1000]
helmet_price = float(input())  # in range [0, 1000]
sword_price = float(input())  # in range [0, 1000]
shield_price = float(input())  # in range [0, 1000]
armor_price = float(input())  # in range [0, 1000]

expenses = 0
broken_shield_counter = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        expenses += shield_price
        broken_shield_counter += 1
        if broken_shield_counter % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")