import re

pattern = r'((@#+)([A-Z][a-zA-Z0-9]{4,})[A-Z](@#+))'
default_group = '00'

n = int(input())
for i in range(n):
    string = input()
    matches = re.fullmatch(pattern, string)
    if not matches:
        print('Invalid barcode')
        continue
    product_group = ''
    barcode = matches[0]
    for s in barcode:
        if s.isdigit():
            product_group += s
    if not product_group:
        product_group = default_group
    print(f'Product group: {product_group}')





