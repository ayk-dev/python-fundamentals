my_list = []
N = int(input())
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

for i in range(N):
    line = input().split()
    command = line[0]
    if command == 'insert':
        index = int(line[1])
        element = int(line[2])
        my_list.insert(index, element)

    elif command == 'print':
        print(my_list)

    elif command == 'remove':
        element = int(line[1])
        my_list.remove(element)

    elif command == 'append':
        element = int(line[1])
        my_list.append(element)

    elif command == 'sort':
        my_list = sorted(my_list)

    elif command == 'pop':
        my_list.pop(-1)

    elif command == 'reverse':
        my_list = my_list[::-1]



