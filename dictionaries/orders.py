orders_quantities = {}
products_price = {}

while True:
    command = input()
    if command == 'buy':
        break

    name, price, quantity = command.split()

    if name not in orders_quantities:
        orders_quantities[name] = float(quantity)
    else:
        orders_quantities[name] += float(quantity)
        final_price = float(price)
    products_price[name] = float(price)


for key, value in orders_quantities.items():
    final_price = value * products_price[key]
    print(f'{key} -> {final_price:.2f}')