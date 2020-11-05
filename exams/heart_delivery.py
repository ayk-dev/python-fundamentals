neighborhood = list(map(int, input().split('@')))
hearts = 2
i = 0

while True:
    line = input()
    if line == 'Love!':
        last_position = i
        break

    tokens = line.split()
    length = int(tokens[1])
    if length < len(neighborhood) and (i + length) < len(neighborhood):
        i += length

    else:
        i = 0
    if neighborhood[i] == 0:
        print(f"Place {i} already had Valentine's day.")
    elif neighborhood[i] == hearts:
        neighborhood[i] -= hearts
        print(f"Place {i} has Valentine's day.")
    else:
        neighborhood[i] -= hearts

print(f"Cupid's last position was {last_position}.")
successful_delivery = neighborhood.count(0)
if successful_delivery == len(neighborhood):
    print(f'Mission was successful.')
else:
    unsuccessful = len(neighborhood) - successful_delivery
    print(f"Cupid has failed {unsuccessful} places.")

