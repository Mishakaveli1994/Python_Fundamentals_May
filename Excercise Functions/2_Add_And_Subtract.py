def sum_numbers(int1, int2):
    sumOfNum = int1 + int2
    return sumOfNum


def subtract(sum1, int4):
    return sum1 - int4


def add_and_subtract(int1, int2, int3):
    sum1 = sum_numbers(int1, int2)
    sub = subtract(sum1, int3)
    return sub

integer1 = int(input())
integer2 = int(input())
integer3 = int(input())

print(add_and_subtract(integer1,integer2,integer3))