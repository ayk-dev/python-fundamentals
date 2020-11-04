experience_required = float(input())
count_of_battles = int(input())

is_enough = False
total_experience = 0

for battle in range(1, count_of_battles + 1):
    experience = float(input())
    if battle % 3 == 0:
        experience += experience * 0.15
    if battle % 5 == 0:
        experience -= experience * 0.10
    total_experience += experience
    if total_experience >= experience_required:
        battles_done = battle
        is_enough = True
        break

if is_enough:
    print(f'Player successfully collected his needed experience for {battles_done} battles.')
else:
    experience_short = experience_required - total_experience
    print(f'Player was not able to collect the needed experience, {experience_short:.2f} more needed.')
