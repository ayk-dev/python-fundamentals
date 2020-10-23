employees_happiness = list(map(int, input().split()))
factor = int(input())

factored_happiness = list(map(lambda n: n * factor, employees_happiness))
average_happiness = sum(factored_happiness) / len(factored_happiness)


filtered_employees = list(filter(lambda n: n >= average_happiness, factored_happiness))
happy_employees = len(filtered_employees)
total_employees = len(factored_happiness)

if happy_employees >= total_employees / 2:
    print(f'Score: {happy_employees}/{total_employees}. Employees are happy!')
else:
    print(f'Score: {happy_employees}/{total_employees}. Employees are not happy!')