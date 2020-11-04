journey_cost = float(input())
months = int(input())

money_saved = 0

for month in range(1, months + 1):
    if month > 1 and month % 2 != 0:
        money_saved -= 0.16 * money_saved
    if month % 4 == 0:
        bonus = 0.25 * money_saved
        money_saved += bonus
    money_saved += 0.25 * journey_cost

if money_saved >= journey_cost:
    money_over = money_saved - journey_cost
    print(f'Bravo! You can go to Disneyland and you will have {money_over:.2f}lv. for souvenirs.')
else:
    money_short = journey_cost - money_saved
    print(f'Sorry. You need {money_short:.2f}lv. more.')
