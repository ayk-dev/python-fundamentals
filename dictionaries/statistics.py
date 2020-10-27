from collections import defaultdict

products = defaultdict(int)

while True:
    command = input()
    if command == 'statistics':
        break

    item, quantity = command.split(': ')

    if item in products:
        products[item] += int(quantity)
    else:
        products[item] = int(quantity)

print('Products in stock:')

for key, value in products.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')