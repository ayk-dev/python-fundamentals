all_cards = input().split(':')
cards = []

while True:
    line = input()
    if line == 'Ready':
        break

    tokens = line.split()
    command = tokens[0]
    card_name = tokens[1]

    if command == 'Add':
        if card_name in all_cards:
            cards.append(card_name)
        else:
            print('Card not found.')

    elif command == 'Insert':
        index = int(tokens[2])
        if card_name not in all_cards or (index < 0 or index > len(cards)):
            print('Error!')
        else:
            cards.insert(index, card_name)

    elif command == 'Remove':
        if card_name in cards:
            cards.remove(card_name)
        else:
            print('Card not found.')

    elif command == 'Swap':
        second_card = tokens[2]
        first_index = None
        second_index = None
        for i in range(len(cards)):
            if cards[i] == card_name:
                first_index = i
            elif cards[i] == second_card:
                second_index = i
            if first_index and second_index:
                break
        cards[first_index], cards[second_index] = cards[second_index], cards[first_index]

    elif command == 'Shuffle':
        cards = cards[::-1]

print(' '.join(cards))

