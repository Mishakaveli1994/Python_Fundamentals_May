numberOfPeople = int(input())
elevatorCapacity = int(input())

if numberOfPeople % elevatorCapacity == 0:
    print(f"{int(numberOfPeople/elevatorCapacity)}")
else:
    print(f"{int(numberOfPeople / elevatorCapacity)+1}")