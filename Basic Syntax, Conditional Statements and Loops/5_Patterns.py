number = int(input())
stars = 0
for i in range(1, number * 2 + 1):
    print('*' * stars)
    if i <= number:
        stars += 1
    else:
        stars -= 1
