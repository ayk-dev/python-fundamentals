events = input().split('|')

energy = 100
coins = 100

is_bankrupt = False

ENERGY_DECREASE_FROM_ORDER = 30
REST_ENERGY_POINTS = 50

for i in range(len(events)):
    single_event = events[i].split('-')
    event_or_ingredient = single_event[0]
    number = int(single_event[1])

    if event_or_ingredient == 'rest':
        gained_energy = number
        energy += gained_energy
        if energy > 100:
            energy = 100
            gained_energy = 0
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event_or_ingredient == 'order':
        if energy >= ENERGY_DECREASE_FROM_ORDER:
            earned_coins = number
            energy -= ENERGY_DECREASE_FROM_ORDER
            print(f'You earned {earned_coins} coins.')
            coins += earned_coins
        else:
            energy += REST_ENERGY_POINTS
            print('You had to rest!')
    else:
        coins_to_spend = number
        if coins > coins_to_spend:
            coins -= coins_to_spend
            print(f'You bought {event_or_ingredient}.')
        else:
            print(f'Closed! Cannot afford {event_or_ingredient}.')
            is_bankrupt = True
            break

if not is_bankrupt:
    print(f'Day completed!')
    print(f"Coins: {coins}")
    print(f'Energy: {energy}')





