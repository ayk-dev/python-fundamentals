def is_price_valid(product, price):
    is_valid = (product == 'Clothes' and price <= 50.00) or (product == 'Shoes' and price <= 35.00) or\
    (product == 'Accessories' and price <= 20.50)
    return is_valid


TICKETS_TO_FRANCE = 150
items_with_prices_list = input().split('|')
budget = float(input())
budget_left = budget
items_bought = 0
PRICE_INCREASE = 40 / 100
sum_new_prices = 0

for i in range(len(items_with_prices_list)):
    single_item_with_price = items_with_prices_list[i].split('->')
    item = single_item_with_price[0]
    price_of_item = float(single_item_with_price[1])

    check_is_price_valid = is_price_valid(item, price_of_item)
    if check_is_price_valid:
        if budget_left >= price_of_item:
            budget_left -= price_of_item
            items_bought += price_of_item
            item_new_price = price_of_item +  price_of_item * PRICE_INCREASE
            sum_new_prices += item_new_price
            print(f'{item_new_price:.2f}', end=' ')
        else:
            continue

print()

profit = sum_new_prices - items_bought
print(f'Profit: {profit:.2f}')

is_enough = (sum_new_prices + budget_left) >= TICKETS_TO_FRANCE

if is_enough:
    print(f'Hello, France!')
else:
    print(f'Time to go.')










