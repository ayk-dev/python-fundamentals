def check_is_ticket_winning(ticket, valid):
    right_half = ticket[:10]
    left_half = ticket[10:]
    result = 'no match'
    for symbol in valid:
        repeat = 9
        for i in range(4):
            if (symbol in right_half and right_half.count(symbol) == 10) \
                    and (symbol in left_half and left_half.count(symbol) == 10):
                result = f'10{symbol} Jackpot!'
            elif (symbol * repeat) in right_half and (symbol * repeat) in left_half:
                count = min(right_half.count(symbol), left_half.count(symbol))
                result = f'{count}{symbol}'
            repeat -= 1
    return result


winning = '@', '#', '$', '^'
tickets = input().split(', ')
for ticket in tickets:
    ticket = ticket.strip(' ')
    if len(ticket) != 20:
        print('invalid ticket')
    else:
        check_ticket = check_is_ticket_winning(ticket, winning)
        print(f'ticket "{ticket}" - {check_ticket}')