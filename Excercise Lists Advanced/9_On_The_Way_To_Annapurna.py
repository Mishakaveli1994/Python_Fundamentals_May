storeList = []
storeInfo = []

while True:
    command = input()
    if command == 'END':
        break
    else:
        commandSplit = command.split('->')
        subcom = commandSplit[0]
        if subcom == 'Add':
            store = commandSplit[1]
            items = commandSplit[2].split(',')
            if store not in storeList:
                storeList.append(store)
                storeInfo.append(items)
            else:
                storeIndex = storeList.index(store)
                storeInfo[storeIndex] += items
        elif subcom == 'Remove':
            store = commandSplit[1]
            if store in storeList:
                storeIndex = storeList.index(store)
                storeList.pop(storeIndex)
                storeInfo.pop(storeIndex)

sortingList = [[i, len(storeInfo[storeList.index(i)])] for i in storeList]
sortingList = sorted(sortingList, key=lambda x: (x[1], x[0]), reverse=True)
print('Stores list:')
for i in sortingList:
    print(i[0])
    storeIndex = storeList.index(i[0])
    for b in storeInfo[storeIndex]:
        print(f"<<{b}>>")

