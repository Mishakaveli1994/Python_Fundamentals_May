numbers = [int(i) for i in input().split(', ')]
indexed = [index for index,value in enumerate(numbers) if value % 2 == 0]
print(indexed)