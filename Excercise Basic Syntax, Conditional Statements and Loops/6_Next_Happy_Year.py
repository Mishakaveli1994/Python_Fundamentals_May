year = int(input()) + 1
while True:
    unique = len(set(str(year)))
    if unique == len(str(year)):
        print(year)
        break
    else:
        year += 1

# No set used
year = int(input()) + 1
while True:
    unique = str(year)
    temp_str = ''
    for i in unique:
        if i not in temp_str:
            temp_str += i
        else:
            break
    if len(temp_str) == len(unique):
        print(temp_str)
        break
    else:
        year += 1
