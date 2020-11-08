integers = list(map(int, input().split()))

while True:
    line = input()
    if line == 'end':
        break

    tokens = line.split()
    command = tokens[0]

    if command == 'swap':
        i_one = int(tokens[1])
        i_two = int(tokens[2])

        integers[i_one], integers[i_two] = integers[i_two], integers[i_one]

    elif command == 'multiply':
        i_one = int(tokens[1])
        i_two = int(tokens[2])

        integers[i_one] *= integers[i_two]

    elif command == 'decrease':
        DECREASE = 1

        integers = [num-1 for num in integers]

integers = [str(num) for num in integers]
print(', '.join(integers))