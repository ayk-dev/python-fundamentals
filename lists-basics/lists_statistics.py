n = int(input())

positives = []
negatives = []

for _ in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

count_of_positives = len(positives)
sum_of_negatives = sum(negatives)

print(positives)
print(negatives)
print(f'Count of positives: {count_of_positives}. Sum of negatives: {sum_of_negatives}')