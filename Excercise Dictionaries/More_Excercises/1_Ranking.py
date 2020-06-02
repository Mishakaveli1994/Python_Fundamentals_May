contestsDict = {}
studentsDict = {}
studentRanking = {}
while True:
    command = input()
    if command == 'end of contests':
        break
    else:
        comSplit = command.split(':')
        contest, password = comSplit[0], comSplit[1]
        contestsDict[contest] = password

while True:
    command = input()
    if command == 'end of submissions':
        break
    else:
        comSplit = command.split('=>')
        contest, password, name, score = comSplit[0], comSplit[1], comSplit[2], int(comSplit[3])
        if contest in contestsDict and password == contestsDict[contest]:
            if name not in studentsDict:
                studentsDict[name] = {contest: score}
            else:
                if contest not in studentsDict[name]:
                    studentsDict[name][contest] = score
                else:
                    if studentsDict[name][contest] < score:
                        studentsDict[name][contest] = score

for k, v in studentsDict.items():
    studentRanking[k] = sum(v.values())
bestStudent = sorted(studentRanking.items(), key=lambda x: (-x[1], x[0]))[0]

print(f"Best candidate is {bestStudent[0]} with total {bestStudent[1]} points.")
print("Ranking:")
for k, v in sorted(studentsDict.items(), key=lambda x: x[0]):
    print(f"{k}")
    for i, k in sorted(v.items(), key=lambda x: -x[1]):
        print(f"#  {i} -> {k}")
