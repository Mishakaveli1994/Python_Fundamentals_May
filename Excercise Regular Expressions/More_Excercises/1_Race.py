import re

contenstants = {i: 0 for i in input().split(', ')}
nameRegex = r'[a-zA-Z]'
distanceRegex = r'[\d]'
while True:
    command = input()
    if command == 'end of race':
        break
    else:
        name = ''.join(re.findall(nameRegex, command))
        distance = sum(int(i) for i in re.findall(distanceRegex, command))
        if name in contenstants:
            contenstants[name] += distance
ordContest = sorted(contenstants.items(), key=lambda x: -x[1])
for i in range(3):
    if i == 0:
        print(f'1st place: {ordContest[i][0]}')
    elif i == 1:
        print(f'2nd place: {ordContest[i][0]}')
    elif i == 2:
        print(f'3rd place: {ordContest[i][0]}')
