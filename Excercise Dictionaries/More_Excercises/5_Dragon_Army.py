dragonDict = {}
numberOfDragons = int(input())
for i in range(numberOfDragons):
    dragonSplit = input().split(' ')
    dType, name, damage, health, armor = dragonSplit[0], dragonSplit[1], dragonSplit[2], dragonSplit[3], dragonSplit[4]
    if dType[0].isupper() and name[0].isupper():
        if damage == 'null':
            damage = 45
        else:
            damage = int(damage)
        if health == 'null':
            health = 250
        else:
            health = int(health)
        if armor == 'null':
            armor = 10
        else:
            armor = int(armor)
        if dType not in dragonDict:
            dragonDict[dType] = {}
            dragonDict[dType][name] = {'damage': damage, 'health': health, 'armor': armor}
        else:
            if name not in dragonDict[dType]:
                dragonDict[dType][name] = {'damage': damage, 'health': health, 'armor': armor}
            else:
                dragonDict[dType][name] = {'damage': damage, 'health': health, 'armor': armor}
for k, v in dragonDict.items():
    dragonDict[k] = dict(sorted(v.items(), key=lambda x: x[0]))
    avgDamage = sum([dragonDict[k][b]['damage'] for b, c in dragonDict[k].items()]) / len(v)
    avgHealth = sum([dragonDict[k][b]['health'] for b, c in dragonDict[k].items()]) / len(v)
    avgArmor = sum([dragonDict[k][b]['armor'] for b, c in dragonDict[k].items()]) / len(v)
    print(f"{k}::({avgDamage:.2f}/{avgHealth:.2f}/{avgArmor:.2f})")
    for b, c in dragonDict[k].items():
        print(
            f'-{b} -> damage: {dragonDict[k][b]["damage"]}, health: {dragonDict[k][b]["health"]}, armor: {dragonDict[k][b]["armor"]}')
