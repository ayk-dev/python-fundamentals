company_users = {}

while True:
    data = input()
    if data == 'End':
        break

    company, employee_id = data.split(' -> ')
    if company not in company_users:
        company_users[company] = []
    if employee_id not in company_users[company]:
        company_users[company].append(employee_id)

sorted_companies = dict(sorted(company_users.items(), key=lambda x: x[0]))
for key, value in sorted_companies.items():
    print(key)
    for v in value:
        print(f'-- {v}')
