import math
party_size = int(input())
days_of_adventure = int(input())

coins_earned = 0
coins_spent = 0

for day in range(1, days_of_adventure + 1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins_earned += 50
    coins_spent += 2 * party_size
    if day % 3 == 0:
        coins_spent += 3 * party_size
    if day % 5 == 0:
        coins_earned += 20 * party_size
    if day % 3 == 0 and day % 5 == 0:
        coins_spent += 2 * party_size

all_profit = coins_earned - coins_spent
profit_per_person = math.floor(all_profit / party_size)

print(f'{party_size} companions received {profit_per_person} coins each.')