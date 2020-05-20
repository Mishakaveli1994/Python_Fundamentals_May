partySize = int(input())
days = int(input())
coins = 0
for i in range(1,days+1):
    if i % 15 == 0:
        partySize += 5
    if i % 10 == 0:
        partySize -= 2
    coins += 50 - 2 * partySize
    if i % 3 == 0:
        coins -= 3 * partySize
    if i % 5 == 0:
        coins += 20 * partySize
        if i % 3 == 0:
            coins -= 2 * partySize

print(f"{partySize} companions received {int(coins / partySize)} coins each.")
