days_of_vacation = int(input())
budget = float(input())
people_count = int(input())
fuel_price_per_km = float(input())
food_per_person_day = float(input())
room_per_person_night = float(input())

is_budget_enough = True

hotel_expenses = room_per_person_night * people_count * days_of_vacation
if people_count > 10:
    hotel_expenses -= 0.25 * hotel_expenses

food_expenses = food_per_person_day * days_of_vacation * people_count
current_expenses = food_expenses + hotel_expenses

for day in range(1, days_of_vacation + 1):
    traveled_distance = float(input())
    fuel_expenses = fuel_price_per_km * traveled_distance
    current_expenses += fuel_expenses
    if day % 3 == 0 or day % 5 == 0:
        additional_expenses = 0.40 * current_expenses
        current_expenses += additional_expenses
    if day % 7 == 0:
        money_received = current_expenses / people_count
        current_expenses -= money_received
    if current_expenses > budget:
        is_budget_enough = False
        break

if is_budget_enough:
    money_over = budget - current_expenses
    message = f'You have reached the destination. You have {money_over:.2f}$ budget left.'
else:
    money_short = current_expenses - budget
    message = f'Not enough money to continue the trip. You need {money_short:.2f}$ more. '

print(message)