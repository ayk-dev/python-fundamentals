input_str = input()

length = len(input_str)
indexes_of_capitals = []

for i in range(length):
    if 65 <= ord(input_str[i]) <= 90:
        indexes_of_capitals.append(i)

print(indexes_of_capitals)