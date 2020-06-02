initialStock = input().split(' ')
stockDict = {initialStock[i]: int(initialStock[i + 1]) for i in range(0, len(initialStock) - 1, 2)}
searchItems = input().split(' ')
for i in searchItems:
    if i in stockDict:
        print(f"We have {stockDict[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")