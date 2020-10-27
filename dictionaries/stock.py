data = input()
elements = data.split(' ')

products = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    quantity = int(elements[index + 1])
    products[key] = quantity

searched_products = input().split(' ')

for item in searched_products:
    if item in products.keys():
        quantity = products[item]
        print(f'We have {quantity} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")

