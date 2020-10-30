days_of_pirating = int(input())
daily_plunder = int(input())
target_plunder = float(input())

total_plunder = 0

for day in range(1, days_of_pirating + 1):
    if day % 3 == 0:
        additional_plunder = daily_plunder * 0.50
        total_plunder += additional_plunder
    total_plunder += daily_plunder
    if day % 5 == 0:
        total_plunder -= total_plunder * 0.30


if total_plunder >= target_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    percentage = total_plunder / target_plunder * 100
    print(f'Collected only {percentage:.2f}% of the plunder.')
