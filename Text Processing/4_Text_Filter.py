bannedWords = input().split(', ')
text = input()

for i in bannedWords:
    text = text.replace(i, len(i) * '*')
print(text)

