def char_list(char1,char2):
    for i in range(char1 +1,char2):
        print(chr(i), end=' ')

char1 = ord(input())
char2 = ord(input())

char_list(char1,char2)