import re

string = input()
pattern = r'(=|\/)\b([A-Z][a-zA-Z]{2,})\1'

destinations = []
travel_points = 0

matches = re.findall(pattern, string)
for match in matches:
    valid_destination = match[1]
    destinations.append(valid_destination)
    travel_points += len(valid_destination)

print(f'Destinations: {", ".join(destinations)}')
print(f"Travel Points: {travel_points}")
