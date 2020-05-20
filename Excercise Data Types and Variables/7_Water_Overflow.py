tankCapacity = 255
tankFill = 0
numberOfLines = int(input())
for i in range(numberOfLines):
    volume = int(input())
    if tankCapacity < volume:
        print("Insufficient capacity!")
    else:
        tankCapacity -= volume
        tankFill += volume
print(tankFill)