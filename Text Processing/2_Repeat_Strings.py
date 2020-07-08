from io import StringIO
textList = input().split(' ')
text = StringIO()
for i in textList:
    text.write(i * len(i))
text.seek(0)
print(text.read())