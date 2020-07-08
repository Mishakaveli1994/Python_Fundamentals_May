usernames = input().split(', ')
allowedSymobs = ('-', '_')
for i in usernames:
    if 3 <= len(i) <= 16 and ' ' not in i:
        validSymbolsCheck = ''.join([b for b in i if not b.isalnum() and b not in allowedSymobs])
        if len(validSymbolsCheck) == 0:
            print(i)
