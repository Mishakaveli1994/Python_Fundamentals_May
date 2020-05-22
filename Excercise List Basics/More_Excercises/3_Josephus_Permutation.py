# Breaks in Judge for some reason
# totalPeople = input().split(' ')
# step = int(input()) - 1
# solution = []
# index = 0
# while len(totalPeople) > 0:
#     index += step
#     if len(totalPeople) < index:
#         index = index % len(totalPeople)
#         solution.append(totalPeople.pop(index))
#     else:
#         solution.append(totalPeople.pop(index))
#
# print(f"[{','.join(solution)}]")


numbers = input().split(' ')
step = int(input())
counted = []
idx = 0

while len(numbers) > 0:
    idx = (idx + step - 1) % len(numbers)
    counted.append(numbers.pop(idx))

print(f"[{','.join(counted)}]")
