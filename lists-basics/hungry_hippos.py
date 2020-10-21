n = int(input())

board = []

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)

print(board)