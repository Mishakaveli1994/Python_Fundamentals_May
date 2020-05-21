listOfOffers = input().split(', ')
numberOfBeggars = int(input())
cash_taken = [0]*numberOfBeggars

while len(listOfOffers) > 0:
    for i in range(numberOfBeggars):
        if len(listOfOffers) > 0:
            cash_taken[i] += int(listOfOffers[0])
            listOfOffers.pop(0)
print(cash_taken)