factor = int(input())
count = int(input())

my_list = [num for num in range(factor, count * factor + 1, factor)]

print(my_list)
