cards = input().split()
shuffles = int(input())

cards_range = int(len(cards) / 2)
shuffled_cards = []

for j in range(shuffles):
    for i in range(cards_range):
        shuffled_cards.append(cards[i])
        shuffled_cards.append(cards[cards_range + i])
    cards = shuffled_cards
    shuffled_cards = []

print(cards)
