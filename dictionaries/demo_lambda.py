items = [
    (2, 1),
    (4, 2),
    (1, 5),
    (3, 4),
    (5, 3),
]

print(sorted(items, key=lambda item: item[1], reverse=True))

