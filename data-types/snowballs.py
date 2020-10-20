n = int(input()) # number of snowballs being made by Tony and Andi

highest_value = 0
for ball in range(n):

    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > highest_value:
        highest_value = value
        high_snow = snow
        high_time = time
        high_quality = quality

print(f'{high_snow} : {high_time} = {int(highest_value)} ({high_quality})')

