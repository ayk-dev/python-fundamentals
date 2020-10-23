def get_time_of_car(car):
    if 0 in car:
        zero = car.index(0)
        sum_car = sum(car[:zero]) * 0.8 + sum(car[zero:])
    else:
        sum_car = sum(car)
    return sum_car


time_needed = list(map(int, input().split()))
finish_line = len(time_needed) // 2 + 1 # middle index

left_car = [time for i, time in enumerate(time_needed) if 0 <= i < finish_line-1]
right_car = [time for i, time in enumerate(time_needed) if finish_line <= i < len(time_needed)]

sum_left = get_time_of_car(left_car)
sum_right = get_time_of_car(right_car[::-1])

if sum_left < sum_right:
    print(f'The winner is left with total time: {sum_left:.1f}')
else:
    print(f'The winner is right with total time: {sum_right:.1f}')