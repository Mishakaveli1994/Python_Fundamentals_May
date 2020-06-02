userDict = {}
examDict = {}

while True:
    command = input()
    if command == 'exam finished':
        break
    else:
        comSplit = command.split('-')
        if comSplit[1] == 'banned':
            eUser = comSplit[0]
            del userDict[eUser]
        else:
            eUser, exam, points = comSplit[0], comSplit[1], int(comSplit[2])
            if eUser not in userDict:
                userDict[eUser] = points
            else:
                if userDict[eUser] < points:
                    userDict[eUser] = points
            if exam not in examDict:
                examDict[exam] = 0
            examDict[exam] += 1
print('Results:')
[print(f"{k} | {v}") for k,v in sorted(userDict.items(), key=lambda x: (-x[1],x[0]))]
print("Submissions:")
[print(f"{k} - {v}") for k,v in sorted(examDict.items(), key=lambda x: (-x[1],x[0]))]

