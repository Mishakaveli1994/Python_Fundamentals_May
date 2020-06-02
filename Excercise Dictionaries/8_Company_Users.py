companyDict = {}

while True:
    command = input()
    if command == 'End':
        break
    else:
        comSplit = command.split(' -> ')
        company = comSplit[0]
        id = comSplit[1]
        if company not in companyDict:
            companyDict[company] = []
        if id not in companyDict[company]:
            companyDict[company].append(id)
sortedComDict = dict(sorted(companyDict.items(), key=lambda x: x[0]))

for k, v in sortedComDict.items():
    print(k)
    for i in v:
        print(f"-- {i}")
