giftsToBuy = input().split(' ')

while True:
    command = input()
    if command == 'No Money':
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'OutOfStock':
            for i in giftsToBuy:
                if i == command_split[1]:
                    giftsToBuy[giftsToBuy.index(command_split[1])] = 'None'
        elif command_split[0] == 'Required':
            if 0 <= int(command_split[2]) <= len(giftsToBuy) - 1:
                giftsToBuy[int(command_split[2])] = command_split[1]
        elif command_split[0] == 'JustInCase':
            giftsToBuy[len(giftsToBuy) - 1] = command_split[1]

print(' '.join([i for i in giftsToBuy if i != 'None']))
