first_line = input().split()
second_line = input().split()
third_line = input().split()

board_list = [
    first_line,
    second_line,
    third_line
]

first = '1'
second = '2'
empty = '0'
first_win = [first] * 3
second_win = [second] * 3

is_first_player = False
is_second_player = False

diagonals = [
    board_list[0][0], board_list[1][1], board_list[2][2],
    board_list[0][2], board_list[1][1], board_list[2][0]
]

columns = [
    board_list[0][0], board_list[1][0], board_list[2][0],
    board_list[0][1], board_list[1][1], board_list[2][1],
    board_list[0][2], board_list[1][2], board_list[2][2],
]

for i in range(8):
    if first_line == first_win or second_line == first_win or third_line == first_win:
        is_first_player = True
        break

    if diagonals[:3] == first_win or diagonals[3:] == first_win:
        is_first_player = True
        break

    if columns[:3] == first_win or columns[3:6] == first_win or columns[6:] == first_win:
        is_first_player = True
        break

    if first_line == second_win or second_line == second_win or third_line == second_win:
        is_second_player = True
        break

    if diagonals[:3] == second_win or diagonals[3:] == second_win:
        is_second_player = True
        break

    if columns[:3] == second_win or columns[3:6] == second_win or columns[6:] == second_win:
        is_second_player = True
        break

if is_first_player:
    message = 'First player won'
elif is_second_player:
    message = 'Second player won'
else:
    message = 'Draw!'

print(message)




