highest_number_of_stars = int(input())

for star in range(1, highest_number_of_stars + 1):
    print('*' * star)

for star in range(highest_number_of_stars - 1, 0, -1):
    print('*' * star)