import math

numbers = list(map(int, input().split(', ')))

groups_count = math.ceil(max(numbers) / 10)

start_value = 0
end_value = 10

for i in range(1, groups_count + 1):
    nums = []
    for num in numbers:
        if start_value < num <= end_value:
            nums.append(num)

    print(f"Group of {i}0's: {nums}")
    start_value += 10
    end_value += 10

