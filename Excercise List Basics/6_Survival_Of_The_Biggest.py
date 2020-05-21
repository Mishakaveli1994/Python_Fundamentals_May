numbers = [int(i) for i in input().split(' ')]
numsToRemove = int(input())
for i in range(numsToRemove):
    min_num = min(numbers)
    numbers.pop(numbers.index(min_num))
print(numbers)