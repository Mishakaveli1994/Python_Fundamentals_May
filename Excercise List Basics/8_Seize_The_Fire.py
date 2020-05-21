fireLevels = input().split('#')
waterLevel = int(input())
totalEffort = 0
totalFire = 0
putOutCells = []
for i in fireLevels:
    fireLevels_split = i.split(' = ')
    fireIntensity = fireLevels_split[0]
    waterNeeded = int(fireLevels_split[1])
    if fireIntensity == 'High' and 81 <= waterNeeded <= 125:
        if waterNeeded <= waterLevel:
            waterLevel -= waterNeeded
            totalEffort += waterNeeded * 0.25
            putOutCells.append(waterNeeded)
            totalFire += waterNeeded
    elif fireIntensity == 'Medium' and 51 <= waterNeeded <= 80:
        if waterNeeded <= waterLevel:
            waterLevel -= waterNeeded
            totalEffort += waterNeeded * 0.25
            putOutCells.append(waterNeeded)
            totalFire += waterNeeded
    if fireIntensity == 'Low' and 1 <= waterNeeded <= 50:
        if waterNeeded <= waterLevel:
            waterLevel -= waterNeeded
            totalEffort += waterNeeded * 0.25
            putOutCells.append(waterNeeded)
            totalFire += waterNeeded


print('Cells:')
for i in putOutCells:
    print(f" - {i}")
print(f"Effort: {totalEffort:.2f}")
print(f"Total Fire: {totalFire}")