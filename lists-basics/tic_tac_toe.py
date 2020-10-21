first_line = input().split()
second_line = input().split()
third_line = input().split()

player_one = '1'
player_two = '2'

player_one_moves = []
player_two_moves = []


if player_one in first_line:
    player_one_moves.append(first_line.index(player_one))
if player_one in second_line:
    player_one_moves.append(second_line.index(player_one))
if player_one in third_line:
    player_one_moves.append(third_line.index(player_one))

if player_two in first_line:
    player_two_moves.append(first_line.index(player_two))
if player_two in second_line:
    player_two_moves.append(second_line.index(player_two))
if player_two in third_line:
    player_two_moves.append(third_line.index(player_two))

if player_one_moves == [2, 1, 0] or player_one_moves == [0, 1, 2]:
    print('First player won')
elif player_two_moves == [2, 1, 0] or player_two_moves == [0, 1, 2]:
    print('Second player won')
else:
    print('Draw!')