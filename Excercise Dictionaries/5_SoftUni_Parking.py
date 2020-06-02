def registerCar(command, dictionary):
    user = command[1]
    carNumber = comSplit[2]
    if user not in dictionary:
        dictionary[user] = carNumber
        print(f"{user} registered {carNumber} successfully")
    else:
        print(f"ERROR: already registered with plate number {dictionary[user]}")


def unregisterCar(command, dictionary):
    user = command[1]
    if user in dictionary:
        del dictionary[user]
        print(f"{user} unregistered successfully")
    else:
        print(f"ERROR: user {user} not found")


parkingDict = {}
numberOfUsers = int(input())

for i in range(numberOfUsers):
    comSplit = input().split(' ')
    if comSplit[0] == 'register':
        registerCar(comSplit, parkingDict)
    elif comSplit[0] == 'unregister':
        unregisterCar(comSplit, parkingDict)

[print(f"{k} => {v}") for k,v in parkingDict.items()]