MIN_VALUE = 1
MAX_VALUE = 100

while True:
    num = int(input())
    if MIN_VALUE <= num <= MAX_VALUE:
        print(f'The number {num} is between {MIN_VALUE} and {MAX_VALUE}')
        break
    else:
        num = int(input())