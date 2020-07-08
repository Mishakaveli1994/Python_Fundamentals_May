text = input()
newText = ''
lastLetter = ''
for i in range(len(text)):
    if text[i] != lastLetter:
        newText += text[i]
        lastLetter = text[i]
print(newText)