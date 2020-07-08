import re
regex = r'(\+359([ |-])2\2[0-9]{3}\2[0-9]{4}\b)'
numbers = input()
results = re.findall(regex,numbers,)
resultList = []
for i in results:
    resultList.append(i[0])
print(', '.join(resultList))