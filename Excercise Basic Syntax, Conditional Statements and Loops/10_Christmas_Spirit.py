allowed_quality = int(input())
days_left = int(input())
christmas_spirit = 0
total_cost = 0
for i in range(1, days_left + 1):
    if i % 11 == 0:
        allowed_quality += 2
    if i % 2 == 0:
        christmas_spirit += 5
        total_cost += 2 * allowed_quality
    if i % 3 == 0:
        christmas_spirit += 13
        total_cost += 8 * allowed_quality
    if i % 5 == 0:
        christmas_spirit += 17
        total_cost += 15 * allowed_quality
        if i % 3 == 0:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        total_cost += 23
    if i == days_left and i % 10 == 0:
        christmas_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
