import re

string = input()

pattern = r'(#|\|)([A-Z][a-z]+(\s?[A-Z][a-z]+)*)(#|\|)(\d{2}\/\d{2}\/\d{2})\1([0-9]{1,4}|10000)(#|\|)'

dci = 2000 # daily calorie intake

matches = re.findall(pattern, string)

foods_expiration = {}
foods_calories = {}
for match in matches:
    foods_expiration[match[2]] = match[4]
    foods_calories[match[2]] = int(match[5])

total_food_calories = 0
for v in foods_calories.values():
    total_food_calories += v

days = total_food_calories / dci
print(f'You have food to last you for: {int(days)} days!')

for k in foods_expiration.keys():
    print(f'Item: {k}, Best before: {foods_expiration[k]}, Nutrition: {foods_calories[k]}')
