text = [i for i in input()]
charDict = {}
for i in text:
    if i != ' ':
        if i not in charDict:
            charDict[i] = 0
        charDict[i] += 1
[print(f"{k} -> {v}") for k, v in charDict.items()]
