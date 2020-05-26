text = input().split(' ')
deciphered = []
for i in range(len(text)):
    firstLetter = ''.join([b for b in text[i] if b.isdigit()])
    textList = [i for i in text[i] if i.isalpha()]
    textLen = len(textList)
    textList[0], textList[textLen - 1] = textList[textLen - 1], textList[0]
    deciphered.append(chr(int(firstLetter)) + ''.join(textList))
print(' '.join(deciphered))
