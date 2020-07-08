array = [int(i) for i in input().split(' ')]
average = sum(array) / len(array)
sortedList = [i for v, i in enumerate(sorted(array,reverse=True)) if i > average and v < 5]
if len(sortedList) == 0:
    print('No')
else:
    print(' '.join([str(i) for i in sortedList]))
