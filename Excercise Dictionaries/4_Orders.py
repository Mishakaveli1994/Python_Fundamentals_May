productDict = {}

while True:
    command = input()
    if command == 'buy':
        [print(f"{k} -> {productDict[k][0]*productDict[k][1]:.2f}") for k in productDict.keys()]
        break
    else:
        commandSplit = command.split(' ')
        item = commandSplit[0]
        price = float(commandSplit[1])
        quantity = int(commandSplit[2])
        if item not in productDict:
            productDict[item] = [price,quantity]
        else:
            productDict[item][0] = price
            productDict[item][1] += quantity