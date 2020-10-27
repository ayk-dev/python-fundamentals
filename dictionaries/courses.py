courses = {}

while True:
    command = input()
    if command == 'end':
        break

    tokens = command.split(" : ")
    course_name = tokens[0]
    student = tokens[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student)

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for key, value in sorted_courses.items():
    print(f'{key}: {len(value)}')
    sorted_names = sorted(value)
    for i in range(len(sorted_names)):
        print(f'-- {sorted_names[i]}')


