animalList = []
animalInfo = []
zoneName = []
zoneInfo = []

while True:
    command = input()
    if command == 'Last Info':
        break
    else:
        commandSplit = command.split(':')
        subCom = commandSplit[0]
        animalName = commandSplit[1]
        animalFood = int(commandSplit[2])
        animalArea = commandSplit[3]
        if subCom == 'Add':
            if animalName not in animalList:
                animalList.append(animalName)
                animalInfo.append([animalName, animalFood, animalArea])
                if animalArea not in zoneName:
                    zoneName.append(animalArea)
                    zoneInfo.append([1, animalArea])
                else:
                    zoneIndex = zoneName.index(animalArea)
                    zoneInfo[zoneIndex][0] += 1
            else:
                animalIndex = animalList.index(animalName)
                animalInfo[animalIndex][1] += animalFood
        elif subCom == 'Feed':
            if animalName in animalList:
                animalIndex = animalList.index(animalName)
                animalInfo[animalIndex][1] -= animalFood
                if animalInfo[animalIndex][1] <= 0:
                    print(f"{animalName} was successfully fed")
                    animalList.pop(animalIndex)
                    animalInfo.pop(animalIndex)
                    zoneIndex = zoneName.index(animalArea)
                    zoneInfo[zoneIndex][0] -= 1
                    if zoneInfo[zoneIndex][0] == 0:
                        zoneInfo.pop(zoneIndex)
                        zoneName.pop(zoneIndex)

print("Animals:")
sortedAnimalInfo = sorted(animalInfo, key=lambda x: (-x[1], x[0]))
for index, value in enumerate(sortedAnimalInfo):
    print(f"{value[0]} -> {value[1]}g")
sortedZoneList = sorted(zoneInfo, key=lambda x: -x[0])
print("Areas with hungry animals:")
for i in sortedZoneList:
    print(f"{i[1]} : {i[0]}")
