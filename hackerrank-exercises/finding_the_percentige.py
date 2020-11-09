n = int(input())

students = {}
for _ in range(n):
    data = input().split(maxsplit=1)
    name = data[0]
    marks = list(map(float, data[1].split()))

    students[name] = marks

query_name = input()
average_score = 0
length_marks = 3

if query_name in students.keys():
    average_score = sum(students[query_name]) / length_marks
    print(f"{average_score:.2f}")