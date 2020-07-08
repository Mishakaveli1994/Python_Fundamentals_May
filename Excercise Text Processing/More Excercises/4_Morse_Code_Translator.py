morseCodeDict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                 '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                 '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z'}
decryptedText = ''
morseText = [i for i in input().split() if i != ' ' or i != '']
for i in morseText:
    if i == '|':
        decryptedText += ' '
    else:
        decryptedText += morseCodeDict[i]
print(decryptedText)
