def exists(dictionary, keyword):
    if keyword not in dictionary:
        dictionary[keyword] = 0

itemsDict = {}
while True:
    command = input()
    if command == 'statistics':
        print("Products in stock:")
        for k, v in itemsDict.items():
            print(f"- {k}: {v}")
        print(f"Total Products: {len(itemsDict)}")
        print(f"Total Quantity: {sum(itemsDict.values())}")
        break
    else:
        commandSplit = command.split(': ')
        item = commandSplit[0]
        quantity = int(commandSplit[1])
        exists(itemsDict, item)
        itemsDict[item] += quantity
