string = input()

for i in range(len(string)):
    emoticon = ''
    if string[i] == ':':
        emoticon += string[i] + string[i + 1]
        print(emoticon)
