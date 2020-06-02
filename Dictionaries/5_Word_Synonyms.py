numberOfLines = int(input())
synDict = {}
for i in range(numberOfLines):
    key = input()
    synonym = input()
    if key not in synDict:
        synDict[key] = []
    synDict[key].append(synonym)
for i in synDict.keys():
    print(f"{i} - {', '.join(synDict[i])}")
