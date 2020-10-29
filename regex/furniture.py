import re

pattern = r'>>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)'
total_money = 0
print('Bought furniture:')
while True:
    line = input()
    if line == 'Purchase':
        break

    match = re.fullmatch(pattern, line)
    if match is None:
        continue

    print(match.group(1))
    price = float(match.group(2))
    quantity = int(match.group(4))
    total_money += price * quantity

print(f'Total money spend: {total_money:.2f}')

