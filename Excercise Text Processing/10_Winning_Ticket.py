tickets = [i.strip() for i in input().split(', ')]
winningSymbols = ['@', '$', '#', '^']


def winning(p):
    winning_dict = {i: 0 for i in p if i in winningSymbols and p.count(i) > 5}
    if len(winning_dict) != 0:
        winning_key = [i for i in winning_dict.keys()][0]

        for i, v in enumerate(p):
            if v in winning_dict:
                winning_dict[winning_key] += 1
            else:
                if winning_dict[winning_key] < 6:
                    winning_dict[winning_key] = 0
        winSym = winning_dict[winning_key]
    else:
        winning_key = 0
        winSym = 0
    return winning_key, winSym


for i in tickets:
    i = i.strip()
    if len(i) != 20:
        print('invalid ticket')
    else:
        leftPart = i[0:10]
        rightPart = i[10:]
        lwk, lkc = winning(leftPart)
        rwk, rkc = winning(rightPart)
        # CHECK IF BOTH ABOVE 5 AND DIFFERENT
        if lwk == rwk and lkc > 5 and rkc > 5 and lwk != 0 and rwk != 0:
            if lkc + rkc == 20:
                print(f'ticket "{i}" - {lkc}{lwk} Jackpot!')
            else:
                print(f'ticket "{i}" - {min(lkc, rkc)}{lwk}')
        else:
            print(f'ticket "{i}" - no match')
