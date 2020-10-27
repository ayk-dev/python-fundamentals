def get_position_skill(line):
    pl, pos, sk = line.split(' -> ')
    return pl, pos, sk


def player_vs_player(line):
    first, second = line.split(' vs ')
    return first, second


players_pool = {}
player_skill = {}

while True:
    line = input()
    if line == 'Season end':
        break

    if '->' in line:
        player, position, skill = get_position_skill(line)
        if player not in players_pool:
            players_pool[player] = {}
            players_pool[player][position] = int(skill)
            player_skill[player] = int(skill)
        else:
            if position not in players_pool[player]:
                players_pool[player][position] = int(skill)
                player_skill[player] += int(skill)
            else:
                if players_pool[player][position] < int(skill):
                    players_pool[player][position] = int(skill)
                    player_skill[player] += (int(skill) - players_pool[player][position])

    elif 'vs' in line:
        player_one, player_two = player_vs_player(line)
        if player_one in players_pool and player_two in players_pool:
            positions_in_common = False
            for position in players_pool[player_one]:
                if position in players_pool[player_two]:
                    positions_in_common = True
                    break
            if positions_in_common:
                if player_skill[player_one] > player_skill[player_two]:
                    loser = player_two
                elif player_skill[player_one] < player_skill[player_two]:
                    loser = player_one
                else:
                    loser = None
                if loser:
                    players_pool.pop(loser)
                    player_skill.pop(loser)

sorted_player_skill = dict(sorted(player_skill.items(), key=lambda x: -x[1]))
for k, v in sorted_player_skill.items():
    print(f'{k}: {v} skill')
    sorted_player_positions = dict(sorted(players_pool[k].items(), key=lambda x: -x[1]))
    for position, skill in sorted_player_positions.items():
        print(f'- {position} <::> {skill}')