def calculate_diagonal_diff(arr, n):
    first_diagonal = [arr[i][i] for i in range(n)]
    second_diagonal = [arr[i][n - 1 - i] for i in range(n)]
    result = int(abs(sum(first_diagonal) - sum(second_diagonal)))
    return result


n = int(input()) # the number of rows and columns in the square matrix

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

get_result = calculate_diagonal_diff(arr, n)
print(get_result)


