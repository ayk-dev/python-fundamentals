guest_meals = {}

unliked_meals = 0

while True:
    line = input()
    if line == 'Stop':
        break

    command, guest, meal = line.split('-')

    if command == 'Like':
        if guest not in guest_meals:
            guest_meals[guest] = [meal]
        else:
            if meal not in guest_meals[guest]:
                guest_meals[guest].append(meal)

    else:
        if guest not in guest_meals:
            print(f'{guest} is not at the party.')
        else:
            if meal not in guest_meals[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                unliked_meals += 1
                print(f"{guest} doesn't like the {meal}.")
                guest_meals[guest].remove(meal)

sorted_guests = dict(sorted(guest_meals.items(), key=lambda x: (-len(x[1]), x[0])))
for guest, meal in sorted_guests.items():
    print(f'{guest}: {", ".join(meal)}')

print(f'Unliked meals: {unliked_meals}')


