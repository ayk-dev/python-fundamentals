words = input().split()

while True:
    line = input()
    if line == 'Stop':
        break

    tokens = line.split()
    command = tokens[0]
    if command == 'Delete':
        index = int(tokens[1]) + 1
        if 0 <= index < len(words):
            words.pop(index)

    elif command == 'Swap':
        word_one = tokens[1]
        word_two = tokens[2]
        if word_one in words and word_two in words:
            i_one = None
            i_two = None

            for i in range(len(words)):
                if words[i] == word_one:
                    i_one = i
                if words[i] == word_two:
                    i_two = i
                if i_one and i_two:
                    break

            words[i_one], words[i_two] = words[i_two], words[i_one]

    elif command == 'Put':
        w = tokens[1]
        index = int(tokens[2]) - 1
        if index == len(words):
            words.append(w)
        elif 0 <= index < len(words):
            words.insert(index, w)

    elif command == 'Sort':
        words.sort(reverse=True)

    elif command == 'Replace':
        word_one = tokens[1]
        word_two = tokens[2]

        if word_two in words:
            index_two = None
            for i in range(len(words)):
                if words[i] == word_two:
                    index_two = i
                if index_two:
                    break

            words[index_two] = word_one

print(" ".join(words))