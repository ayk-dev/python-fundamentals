employee_one_capacity = int(input())
employee_two_capacity = int(input())
employee_three_capacity = int(input())
total_people_count = int(input())

total_people_per_hour = employee_one_capacity + employee_two_capacity + employee_three_capacity
BREAK = 1
total_time = 0

while total_people_count > 0:
    total_people_count -= total_people_per_hour
    total_time += 1
    if total_time % 4 == 0:
        total_time += BREAK


print(f'Time needed: {total_time}h.')