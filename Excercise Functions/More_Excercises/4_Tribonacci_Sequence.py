start = int(input())


def tribonacci(start):
    numbers = [1]
    for i in range(1, start):
        numbers.append(sum(numbers[-3:]))
    print(*numbers)


tribonacci(start)
