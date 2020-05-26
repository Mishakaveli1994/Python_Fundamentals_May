numOfRooms = int(input())
freeChairsTotal = 0
neededChairsTotal = 0
for i in range(1,numOfRooms+1):
    chair_split = input().split(' ')
    freeChairs = len(chair_split[0])
    people = int(chair_split[1])
    if freeChairs >= people:
        freeChairsTotal += freeChairs - people
    else:
        neededChairs = people - freeChairs
        neededChairsTotal += neededChairs
        print(f"{neededChairs} more chairs needed in room {i}")

if freeChairsTotal - neededChairsTotal >= 0:
    print(f"Game On, {freeChairsTotal} free chairs left")