budget = float(input())
price_flour_klg = float(input())

price_eggs_pack = 0.75 * price_flour_klg
price_milk_litre = 1.25 * price_flour_klg
price_milk_per_cozonac = price_milk_litre * 0.25

price_cozonac = price_flour_klg + price_eggs_pack + price_milk_per_cozonac

cozonacs_count = 0
colored_eggs = 0

while budget > price_cozonac:
    budget -= price_cozonac
    cozonacs_count += 1
    colored_eggs += 3
    if cozonacs_count % 3 == 0:
        colored_eggs -= (cozonacs_count - 2)

print(f'You made {cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

