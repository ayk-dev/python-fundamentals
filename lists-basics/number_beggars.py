numbers_str = input().split(', ')
beggars = int(input())

numbers = [int(num) for num in numbers_str]
list_of_sums = [0] * beggars

for i in range(len(numbers)):
    index = i % beggars
    # [beggar for beggar in range(len(list_of_sums))]
    list_of_sums[index] += numbers[i]

print(list_of_sums)





