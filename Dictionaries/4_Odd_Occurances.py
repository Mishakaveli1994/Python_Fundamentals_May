wordsList = [i.lower() for i in input().split(' ')]
wordsDict = {}
for i in wordsList:
    if i not in wordsDict:
        wordsDict[i] = 0
    wordsDict[i] += 1
wordsDict = {k: v for k, v in wordsDict.items() if v % 2 != 0}
print(*wordsDict.keys())
