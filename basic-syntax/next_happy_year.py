year = int(input())

next_year = year + 1

is_found = False

while not is_found:
    next_year_str = str(next_year)
    unique_symbols = set(next_year_str)
    if len(unique_symbols) == len(next_year_str):
        next_happy_year = next_year
        is_found = True
        break
    next_year += 1

print(next_happy_year)




