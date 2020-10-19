herd = input().split(', ')

if herd[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
elif herd[0] == 'wolf':
    print(f'Oi! Sheep number {len(herd) - 1}! You are about to be eaten by a wolf!')
else:
    for i in range(len(herd)):
        if herd[i] == 'wolf':
            print(f'Oi! Sheep number {len(herd) - i - 1}! You are about to be eaten by a wolf!')


