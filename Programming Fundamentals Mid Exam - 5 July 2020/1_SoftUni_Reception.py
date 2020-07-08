pph = int(input()) + int(input()) + int(input())
people = int(input())
hours = 0
while people > 0:
    hours += 1
    if hours >= 4 and hours % 4 == 0:
        continue
    else:
        if people <= pph:
            pph = 0
            break
        else:
            people -= pph
print(f'Time needed: {hours}h.')