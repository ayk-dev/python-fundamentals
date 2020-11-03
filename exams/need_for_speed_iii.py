n = int(input())

cars_mileage = {}
cars_fuels = {}
for _ in range(n):
    car = input().split('|')
    cars_mileage[car[0]] = int(car[1])
    cars_fuels[car[0]] = int(car[2])

while True:
    line = input()
    if line == 'Stop':
        break

    args = line.split(' : ')
    command = args[0]
    car = args[1]

    if command == 'Drive':
        distance = int(args[2])
        fuel = int(args[3])
        if cars_fuels[car] < fuel:
            print('Not enough fuel to make that ride')
            continue
        cars_mileage[car] += distance
        cars_fuels[car] -= fuel
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars_mileage[car] >= 100000:
            print(f'Time to sell the {car}!')
            cars_mileage.pop(car)
            cars_fuels.pop(car)

    elif command == 'Refuel':
        fuel = int(args[2])
        if cars_fuels[car] + fuel > 75:
            fueled_liters = 75 - cars_fuels[car]
            cars_fuels[car] = 75
            message = f'{car} refueled with {fueled_liters} liters'
        else:
            cars_fuels[car] += fuel
            message = f'{car} refueled with {fuel} liters'
        print(message)

    elif command == 'Revert':
        kilometers = int(args[2])
        cars_mileage[car] -= kilometers
        if cars_mileage[car] < 10000:
            cars_mileage[car] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')

sorted_cars = dict(sorted(cars_mileage.items(), key=lambda x: (-x[1], x[0])))
for car, value in sorted_cars.items():
    print(f'{car} -> Mileage: {value} kms, Fuel in the tank: {cars_fuels[car]} lt.')






