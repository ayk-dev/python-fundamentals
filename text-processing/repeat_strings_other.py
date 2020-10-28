def repeat_by_length(word):
    return word * len(word)


words = input().split(' ')
repeated_words = ''.join(list(map(repeat_by_length, words)))
print(repeated_words)


words = input().split(' ')
repeated_words = ''.join(list(map(lambda word: word * len(word), words)))
print(repeated_words)
