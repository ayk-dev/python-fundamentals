import math

biscuits = int(input()) # produced per day per worker
workers_count = int(input())
competition_biscuits = int(input()) # for 30 days
month = 30
total_production = 0

for day in range(1, month + 1):
    daily_production = biscuits * workers_count
    if day % 3 == 0:
        daily_production = math.floor(0.75 * daily_production)
    total_production += daily_production

print(f'You have produced {total_production} biscuits for the past month.')

diff = abs(competition_biscuits - total_production)
percent_diff = diff / competition_biscuits * 100

if total_production > competition_biscuits:
    print(f'You produce {percent_diff:.2f} percent more biscuits.')
else:
    print(f'You produce {percent_diff:.2f} percent less biscuits.')