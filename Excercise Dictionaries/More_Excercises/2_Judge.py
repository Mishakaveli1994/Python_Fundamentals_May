contestDict = {}
usersDict = {}

while True:
    command = input()
    if command == 'no more time':
        break
    else:
        comSplit = command.split(' -> ')
        user, contest, points = comSplit[0], comSplit[1], int(comSplit[2])
        if contest not in contestDict:
            contestDict[contest] = {user: points}
            if user not in usersDict:
                usersDict[user] = points
            else:
                usersDict[user] += points
        else:
            if user not in contestDict[contest]:
                contestDict[contest][user] = points
                if user not in usersDict:
                    usersDict[user] = points
                else:
                    usersDict[user] += points
            else:
                if contestDict[contest][user] < points:
                    usersDict[user] += points - contestDict[contest][user]
                    contestDict[contest][user] = points


for k, v in contestDict.items():
    print(f"{k}: {len(v)} participants")
    for b, c in enumerate(sorted(v.items(), key=lambda x: (-x[1], x[0])),1):
        print(f"{b}. {c[0]} <::> {c[1]}")
print(f"Individual standings:")
for k, v in enumerate(sorted(usersDict.items(), key=lambda x: (-x[1], x[0])),1):
    print(f"{k}. {v[0]} -> {v[1]}")