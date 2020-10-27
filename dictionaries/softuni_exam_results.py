def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


results = {}
submissions = {}

while True:
    data = input()
    if data == 'exam finished':
        break

    args = data.split('-')
    username = args[0]
    language = args[1]

    if language == 'banned':
        results.pop(username)
        continue

    validate_key_existing(submissions, language, 0)
    submissions[language] += 1
    points = int(args[2])
    validate_key_existing(results, username, 0)
    if results[username] < points:
        results[username] = points

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
print('Results:')
print_dict(results, '{} | {}')

submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))
print('Submissions:')
print_dict(submissions, '{} - {}')