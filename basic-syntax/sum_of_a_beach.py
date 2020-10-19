beach_str = input()

beach_str = beach_str.lower()
counter = 0

counter += beach_str.count('water')
counter += beach_str.count('sand')
counter += beach_str.count('fish')
counter += beach_str.count('sun')

print(counter)
