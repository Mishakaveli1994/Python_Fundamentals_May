numberOfTrains = int(input())
trainList = [0] * numberOfTrains

while True:
    command = input()
    if command == 'End':
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'add':
            trainList[len(trainList) - 1] += int(command_split[1])
        elif command_split[0] == 'insert':
            trainList[int(command_split[1])] += int(command_split[2])
        elif command_split[0] == 'leave':
            trainList[int(command_split[1])]-= int(command_split[2])
print(trainList)