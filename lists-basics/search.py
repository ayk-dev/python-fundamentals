n = int(input())
word = input()

list_of_strings = [input() for _ in range(n)]

filtered_list = []

for i in range(n):
    if word in list_of_strings[i]:
        filtered_list.append(list_of_strings[i])

print(list_of_strings)
print(filtered_list)

