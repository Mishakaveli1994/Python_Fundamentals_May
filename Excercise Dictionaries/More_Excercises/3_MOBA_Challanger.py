playersDict = {}
totalSkillDict = {}

while True:
    command = input()
    if command == 'Season end':
        break
    else:
        if '->' in command:
            comSplit = command.split(' -> ')
            player, position, skill = comSplit[0], comSplit[1], int(comSplit[2])
            if player not in playersDict:
                playersDict[player] = {position: skill}
                totalSkillDict[player] = skill
            else:
                if position not in playersDict[player]:
                    playersDict[player][position] = skill
                    totalSkillDict[player] += skill
                else:
                    if playersDict[player][position] < skill:
                        playersDict[player][position] = skill
                        totalSkillDict[player] += skill - playersDict[player][position]
        elif ' vs ' in command:
            comSplit = command.split(' vs ')
            player1, player2 = comSplit[0], comSplit[1]
            if player1 in totalSkillDict and player2 in totalSkillDict:
                commonPosition = False
                for i in playersDict[player1].keys():
                    if i in playersDict[player2]:
                        commonPosition = True
                        break
                if commonPosition is True:
                    if totalSkillDict[player1] > totalSkillDict[player2]:
                        del playersDict[player2]
                        del totalSkillDict[player2]
                    elif totalSkillDict[player1] < totalSkillDict[player2]:
                        del playersDict[player1]
                        del totalSkillDict[player1]
sortedSkillDict = dict(sorted(totalSkillDict.items(), key=lambda x: (-x[1], x[0])))
sortedPlayerDict = {}
for k, v in sortedSkillDict.items():
    print(f"{k}: {v} skill")
    for c, b in sorted(playersDict[k].items(), key=lambda x: (-x[1],x[0])):
        print(f"- {c} <::> {b}")
