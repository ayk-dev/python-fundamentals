coffee_counter = 0
events = ['coding', 'dog', 'cat', 'movie']
events_big = ['CODING', 'DOG', 'CAT', 'MOVIE']
command = input()

while command != 'END':
    if command in events:
        coffee_counter += 1
    elif command in events_big:
        coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)



