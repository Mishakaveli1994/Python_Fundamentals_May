bakery_dict = {}
bakery_items = input().split(' ')
for i in range(0, len(bakery_items) - 1, 2):
    bakery_dict[bakery_items[i]] = int(bakery_items[i + 1])

print(bakery_dict)