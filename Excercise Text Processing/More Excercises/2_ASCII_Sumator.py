char1 = ord(input()) + 1
char2 = ord(input()) - 1
string = input()
asciiSum = 0
for i in string:
    if min(char1,char2) <= ord(i) <= max(char1,char2):
        asciiSum += ord(i)
print(asciiSum)