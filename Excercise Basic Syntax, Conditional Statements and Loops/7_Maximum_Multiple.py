divisor = int(input())
bound = int(input())
n = bound

while True:
    if n % divisor == 0 and bound >= n > 0:
        print(n)
        break
    else:
        n -= 1
