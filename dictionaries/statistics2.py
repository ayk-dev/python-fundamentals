products = {}

while True:
    command = input()
    if command == 'statistics':
        break

    item, quantity = command.split(': ')

    if item not in products:
        products[item] = 0

    products[item] += int(quantity)


print('Products in stock:')

for key, value in products.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')