academy = {}

n = int(input())

for i in range(n):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name].append(grade)

top_average_grades = {}
for key, value in academy.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        top_average_grades[key] = average_grade

sorted_top_average_grades = dict(sorted(top_average_grades.items(), key=lambda x: -x[1]))
for key, value in sorted_top_average_grades.items():
    print(f'{key} -> {value:.2f}')