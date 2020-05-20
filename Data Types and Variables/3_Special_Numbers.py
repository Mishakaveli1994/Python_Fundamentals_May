number = int(input())
for i in range(1, number + 1):
    special = sum([int(b) for b in str(i)])
    if special == 5 or special == 7 or special == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")