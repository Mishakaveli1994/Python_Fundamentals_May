array = [int(i) for i in input().split(' ')]


def swap(array, ind1, ind2):
    array[ind1], array[ind2] = array[ind2], array[ind1]


def multiply(array, ind1, ind2):
    array[ind1] =  array[ind1] * array[ind2]

while True:
    command = input()
    if command == 'end':
        print(', '.join([str(i) for i in array]))
        break
    else:
        comSplit = command.split(' ')
        if comSplit[0] == 'swap':
            swap(array, int(comSplit[1]), int(comSplit[2]))
        elif comSplit[0] == 'multiply':
            multiply(array, int(comSplit[1]), int(comSplit[2]))
        elif comSplit[0] == 'decrease':
            array = [i - 1 for i in array]