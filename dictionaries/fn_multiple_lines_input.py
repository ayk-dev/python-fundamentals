def get_multiline_input(prompt):
    print(prompt)
    multiline_input = ''
    while True:
        s = input()
        if s != '':
            multiline_input += s + '\n'
        else:
            break
    return multiline_input


text = get_multiline_input('Please enter multiple lines input:')
print(text)
