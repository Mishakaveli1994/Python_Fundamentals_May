electrons = int(input())
shell = 1
shellList = []
while electrons != 0:
    neededElectrons = 2 * shell ** 2
    if electrons >= neededElectrons:
        electrons -= neededElectrons
        shellList.append(neededElectrons)
    else:
        shellList.append(electrons)
        electrons = 0
    shell += 1
print(shellList)