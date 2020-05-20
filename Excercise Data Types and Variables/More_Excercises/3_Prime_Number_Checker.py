number = int(input())
isPrime = 0
if number <= 1:
    print('False')
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = 1

if isPrime == 0:
    print("True")
else:
    print("False")
