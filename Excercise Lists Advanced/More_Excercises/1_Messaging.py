numbers = [i for i in input().split(' ')]
text = [i for i in input()]
for i in numbers:
    numSum = sum(int(b) for b in i)
    if numSum < len(text):
        print(text[numSum],end='')
        text.pop(numSum)
    else:
        print(text[numSum % len(text)],end='')
        text.pop(numSum % len(text))
