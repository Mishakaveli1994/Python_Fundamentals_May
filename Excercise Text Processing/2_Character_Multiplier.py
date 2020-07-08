from itertools import zip_longest
strings = input().split(' ')
characterCodeSum = 0
for i, b in zip_longest(strings[0], strings[1], fillvalue=' '):
    if i == ' ':
        characterCodeSum += ord(b)
    elif b == ' ':
        characterCodeSum += ord(i)
    else:
        characterCodeSum += ord(i) * ord(b)
print(characterCodeSum)
