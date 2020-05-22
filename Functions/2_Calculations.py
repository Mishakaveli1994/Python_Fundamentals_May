def Operations(com, num1, num2):
    if com == 'multiply':
        return num1 * num2
    elif com == 'divide':
        return int(num1 / num2)
    elif com == 'add':
        return int(num1 + num2)
    elif com == 'subtract':
        return int(num1 - num2)


command = input()
integer1 = int(input())
integer2 = int(input())
print(Operations(command, integer1, integer2))
