steps_made = int(input())
step_length = float(input())  # in cm
target_distance = int(input())  # in meters

shorter_step = 0.70 * step_length
shorter_step_count = steps_made // 5

normal_steps = steps_made - shorter_step_count
shorter_step_distance = shorter_step * shorter_step_count
normal_step_distance = normal_steps * step_length
distance_traveled_in_meters = (shorter_step_distance + normal_step_distance) / 100

percent = distance_traveled_in_meters / target_distance * 100

print(f'You travelled {percent:.2f}% of the distance!')



