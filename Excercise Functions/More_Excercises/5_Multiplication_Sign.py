num1 = int(input())
num2 = int(input())
num3 = int(input())


def multiplication(number1, number2, number3):
    if number1 == 0 or number2 == 0 or number3 == 0:
        print('zero')
    elif len([i for i in [number1, number2, number3] if i < 0]) % 2 != 0:
        print('negative')
    else:
        print('positive')


multiplication(num1, num2, num3)
