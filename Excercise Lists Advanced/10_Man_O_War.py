pirateShip = [int(i) for i in input().split('>')]
battleShip = [int(i) for i in input().split('>')]
maxHP = int(input())
pirateShipStatus = 0
battleShipStatus = 0
while pirateShipStatus == battleShipStatus:
    command = input()
    if command == 'Retire':
        print(f"Pirate ship status: {sum(i for i in pirateShip)}")
        print(f"Warship status: {sum(i for i in battleShip)}")
        break
    else:
        commandSplit = command.split(' ')
        subcom = commandSplit[0]
        if subcom == 'Fire':
            fireIndex = int(commandSplit[1])
            fireDamage = int(commandSplit[2])
            if 0 <= fireIndex < len(battleShip):
                battleShip[fireIndex] -= fireDamage
                if battleShip[fireIndex] <= 0:
                    print(f"You won! The enemy ship has sunken.")
                    battleShipStatus = 1
        elif subcom == 'Defend':
            fireStartIndex = int(commandSplit[1])
            fireEndIndex = int(commandSplit[2])
            fireDamage = int(commandSplit[3])
            if 0 <= fireStartIndex < len(pirateShip) and 0 <= fireEndIndex < len(pirateShip):
                for i in range(fireStartIndex, fireEndIndex + 1):
                    pirateShip[i] -= fireDamage
                    if pirateShip[i] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        pirateShipStatus = 1
                        break
        elif subcom == 'Repair':
            repairIndex = int(commandSplit[1])
            repairDamage = int(commandSplit[2])
            if 0 <= repairIndex < len(pirateShip):
                if (pirateShip[repairIndex] + repairDamage) > maxHP:
                    pirateShip[repairIndex] = maxHP
                else:
                    pirateShip[repairIndex] += repairDamage
        elif subcom == 'Status':
            perc = maxHP * 0.2
            print(f"{sum(1 for i in pirateShip if i < perc)} sections need repair.")
