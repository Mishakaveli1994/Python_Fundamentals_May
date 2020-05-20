numberOfLines = int(input())
bracket_status = ''
status = 0
for i in range(numberOfLines):
    line = input()
    if line == '(':
        if '(' in bracket_status:
            status = 1
        else:
            bracket_status = line
    elif line == ')':
        if '(' not in bracket_status:
            status = 1
        elif ')' in bracket_status:
            status = 1
        elif '(' in bracket_status:
            bracket_status = ''

if status == 0:
    print("BALANCED")
else:
    print("UNBALANCED")