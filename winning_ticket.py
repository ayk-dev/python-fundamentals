def check_symbols_repetition(ticket):
    symbols = {'winning_symbols': ['@', '#', '$', '^']}
    right_half = ticket[:10]
    left_half = ticket[10:]
    right_counter = 0
    left_counter = 0
    for s in right_half:
        if s in symbols['winning_symbols']:
            right_counter += 1
            winning_right = s
    for s in left_half:
        if s in symbols['winning_symbols']:
            left_counter += 1
            wining_left = s

    if right_counter < 6 or left_counter < 6:
        result = 'no match'

    elif right_counter == left_counter and winning_right == wining_left:
        winning_symbol = winning_right
        count = right_counter
        min_winning_combo = 6 * winning_symbol
        if min_winning_combo in right_half and min_winning_combo in left_half:
            if 6 <= count <= 9:
                result = f'{count}{winning_symbol}'
            elif count == 10:
                result = f'{count}{winning_symbol} Jackpot!'
        else:
            result = 'no match'

    return result


tickets = input().split(', ')
for ticket in tickets:
    ticket = ticket.strip(' ')
    if len(ticket) != 20:
        print('invalid ticket')
    else:
        check_ticket = check_symbols_repetition(ticket)
        print(f'ticket "{ticket}" - {check_ticket}')