numbers = [i for i in input().split(' ')]
numbers = sorted(numbers,reverse=True)
biggest_num = ''
for i in numbers:
    biggest_num += str(i)
print(biggest_num)