first_string = input()
second_string = input()

length = len(first_string)

for current_index in range(length):
    if first_string[current_index] != second_string[current_index]:
        for i in range(0, current_index+1):
            print(second_string[i], end='')

        for j in range(current_index+1, length):
            print(first_string[j], end='')

        print()
