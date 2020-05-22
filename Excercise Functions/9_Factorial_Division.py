def factorial_division(num1, num2):
    fac1 = 1
    fac2 = 1
    for i in range(1, num1 + 1):
        fac1 *= i
    for i in range(1, num2 + 1):
        fac2 *= i
    return f"{fac1 / fac2:.2f}"


number1, number2 = int(input()), int(input())
print(factorial_division(number1,number2))
