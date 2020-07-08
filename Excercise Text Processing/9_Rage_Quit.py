string = input().lower()
finalString = ''
symbols = ''
numbers = ''
for i in range(len(string)):
    if not string[i].isdigit():
        symbols += string[i]
    else:
        numbers += string[i]
        if len(string)-1 == i or not string[i + 1].isdigit():
            finalString += symbols.upper() * int(numbers)
            symbols = ''
            numbers = ''
print(f'Unique symbols used: {len(set(finalString))}')
print(finalString)