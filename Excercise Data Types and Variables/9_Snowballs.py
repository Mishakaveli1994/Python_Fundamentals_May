snowballs = int(input())
snowballSnow = 0
snowballTime = 0
snowballQuality = 0
snowballValue = 0

for i in range(snowballs):
    snowballSnow_temp = int(input())
    snowballTime_temp = int(input())
    snowballQuality_temp = int(input())
    snowballValue_temp = int(snowballSnow_temp / snowballTime_temp) ** snowballQuality_temp

    if snowballValue_temp > snowballValue:
        snowballSnow = snowballSnow_temp
        snowballTime = snowballTime_temp
        snowballQuality = snowballQuality_temp
        snowballValue = snowballValue_temp

print(f"{snowballSnow} : {snowballTime} = {snowballValue} ({snowballQuality})")
