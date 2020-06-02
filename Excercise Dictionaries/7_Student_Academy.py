studentDict = {}
numberOfPairs = int(input())
for i in range(numberOfPairs):
    name = input()
    grade = float(input())
    if name not in studentDict:
        studentDict[name] = []
    studentDict[name].append(grade)

sortedDict = {k: sum(v)/len(v) for k, v in studentDict.items() if sum(v)/len(v) >= 4.5}
sortedDict = dict(sorted(sortedDict.items(),key=lambda x: -x[1]))

for k,v in sortedDict.items():
    print(f"{k} -> {v:.2f}")