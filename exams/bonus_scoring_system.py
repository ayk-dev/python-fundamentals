
import math
students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
max_bonus = 0
total_bonus = 0

for student in range(students_count):
    attendances = int(input())
    total_bonus = attendances / lectures_count * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_bonus_attendances = attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_bonus_attendances} lectures.')