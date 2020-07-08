text = input()
cypheredText = ''
for i in range(len(text)):
    cypheredText += chr(ord(text[i])+3)
print(cypheredText)