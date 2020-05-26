numbers = [int(i) for i in input().split(', ')]
groups = 0
while len(numbers) > 0:
    groups += 10
    tempList = []
    for index, value in enumerate(numbers):
        if groups - 10 < value <= groups:
            tempList.append(index)
    print(f"Group of {groups}'s: {[numbers[i] for i in tempList]}")
    for i in sorted(tempList, reverse=True):
        numbers.pop(i)
