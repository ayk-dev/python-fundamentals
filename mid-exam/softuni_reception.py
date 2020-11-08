first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

total_students_per_hour = first_employee + second_employee + third_employee

BREAK = 1
time_needed = 0

while students_count > 0:
    students_count -= total_students_per_hour
    time_needed += 1

    if time_needed % 4 == 0:
        time_needed += BREAK

print(f'Time needed: {time_needed}h.')
