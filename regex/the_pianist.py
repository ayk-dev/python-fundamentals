n = int(input())

pieces = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]

while True:
    line = input()
    if line == 'Stop':
        break

    args = line.split('|')
    command = args[0]
    piece = args[1]

    if command == 'Add':
        composer = args[2]
        key = args[3]
        if piece in pieces:
            print(f'{piece} is already in the collection!')
        else:
            pieces[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif command == 'Remove':
        if piece not in pieces:
            print(f'Invalid operation! {piece} does not exist in the collection.')
            continue
        pieces.pop(piece)
        print(f'Successfully removed {piece}!')

    elif command == 'ChangeKey':
        new_key = args[2]
        if piece not in pieces:
            print(f'Invalid operation! {piece} does not exist in the collection.')
            continue
        value = pieces.pop(piece)
        new_value = [value[0], new_key]
        pieces[piece] = new_value
        print(f'Changed the key of {piece} to {new_key}!')

sorted_pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1][0])))
for k, v in sorted_pieces.items():
    print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')


