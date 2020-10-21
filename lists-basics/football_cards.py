team_a = [1] * 11
team_b = [1] * 11

is_terminated = False

cards = input(). split()

for card in cards:
    card_letter = card[0]
    if len(card) == 4:
        card_num = card[2] + card[3]
    else:
        card_num = card[2]
    if card_letter == 'A':
        team_a[int(card_num)-1] = 0
    else:
        team_b[int(card_num)-1] = 0

team_a_sent_off_players = team_a.count(0)
team_b_sent_off_players = team_b.count(0)

team_a_remaining_players = len(team_a) - team_a_sent_off_players
team_b_remaining_players = len(team_b) - team_b_sent_off_players

message = f'Team A - {team_a_remaining_players}; Team B - {team_b_remaining_players} \n'

if team_a_remaining_players < 7 or team_b_remaining_players < 7:
    is_terminated = True
    message += 'Game was terminated'

print(message)