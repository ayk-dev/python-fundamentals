def ascii_to_letter(word):
    temp = list(word)
    digits = []
    others = []
    for ch in temp:
        if ch.isdigit():
            digits.append(ch)
        else:
            others.append(ch)

    letter = list(chr(int(''.join(digits))))
    final_word = ''.join(letter + others)
    return final_word


def switch_letters(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    result = ''.join(temp)
    return result


def decipher_word(word):
    temp = ascii_to_letter(word)
    result = switch_letters(temp)
    return result


message = [decipher_word(string) for string in input().split()]
new_message = ' '.join(message)
print(new_message)