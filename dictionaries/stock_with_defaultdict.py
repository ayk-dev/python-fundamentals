from collections import defaultdict

data = input()
elements = data.split(' ')
products = defaultdict(int)
for index in range(0, len(elements), 2):
    item = elements[index]
    quantity = int(elements[index + 1])
    products[item] = quantity

searched_products = input().split(' ')
for product in searched_products:
    quantity = products[product]
    print(f'We have {quantity} of {product} left')