contests = {}
while True:
    line = input()
    if line == 'end of contests':
        break

    contest, password = line.split(':')
    contests[contest] = password

users_submissions = {}
total_points = {}
while True:
    input_data = input()
    if input_data == 'end of submissions':
        break

    contest, password, username, points = input_data.split('=>')
    if contest not in contests.keys() or contests[contest] != password:
        continue
    if username not in users_submissions:
        users_submissions[username] = {contest: int(points)}
        total_points[username] = int(points)
    else:
        if contest not in users_submissions[username]:
            users_submissions[username][contest] = int(points)
            total_points[username] += int(points)
        else:
            if int(points) > users_submissions[username][contest]:
                users_submissions[username][contest] = int(points)
                total_points[username] = int(points)

total_points_items = [(key, value) for key, value in total_points.items()]
most_points_user = max(total_points_items)[0]
print(f'Best candidate is {most_points_user} with total {total_points[most_points_user]} points.')
print('Ranking:')

sorted_users_submissions = dict(sorted(users_submissions.items(), key=lambda x: (x[0])))
for key, value in sorted_users_submissions.items():
    print(key)
    sorted_values = dict(sorted(value.items(), key=lambda x: -x[1]))
    for k, v in sorted_values.items():
        print(f'#  {k} -> {v}')