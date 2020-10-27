words = [w.lower() for w in input().split(' ')]

words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

odd_occurences = [key for key, value in words_count.items() if words_count[key] % 2 != 0]

print(' '.join(odd_occurences))

