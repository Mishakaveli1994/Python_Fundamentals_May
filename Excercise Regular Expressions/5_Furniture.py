import re
regex = r'>>(\w+)<<(\d+(\.\d+)?)!(\d+)'
furnitureList = []
total_price = 0
while True:
    command = input()
    if command == 'Purchase':
        break
    else:
        result = re.findall(regex,command)
        if result:
            furnitureList.append(result[0][0])
            total_price += float(result[0][1]) * int(result[0][3])
print('Bought furniture:')
[print(i) for i in furnitureList]
print(f'Total money spend: {total_price:.2f}')