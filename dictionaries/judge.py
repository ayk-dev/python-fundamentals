user_contests = {}
user_points = {}
contest_participants = {}

while True:
    line = input()
    if line == 'no more time':
        break

    username, contest, points = line.split(' -> ')

    if contest not in contest_participants:
        contest_participants[contest] = [username]
    else:
        if username not in contest_participants[contest]:
            contest_participants[contest].append(username)

    if contest not in user_contests.keys():
        user_contests[contest] = {}
        user_contests[contest][username] = int(points)
    else:
        if username not in user_contests[contest]:
            user_contests[contest][username] = int(points)
        else:
            if int(points) > user_contests[contest][username]:
                user_contests[contest][username] = int(points)

    if username not in user_points:
        user_points[username] = int(points)
    else:
        if int(points) >= user_points[username]:
            user_points[username] = int(points)

for key, value in user_contests.items():
    participants_count = len(contest_participants[key])
    print(f'{key}: {participants_count} participants')
    sorted_value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    number = 1
    for k, v in sorted_value.items():
        print(f'{number}. {k} <::> {v}')
        number += 1

sorted_individual_rankings = dict(sorted(user_points.items(), key=lambda x: (-x[1], x[0])))
print('Individual standings:')
num = 1
for k, v in sorted_individual_rankings.items():
    print(f'{num}. {k} -> {v}')
    num += 1
