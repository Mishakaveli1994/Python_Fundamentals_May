resource_dict = {}
while True:
    command = input()
    if command == 'stop':
        break
    else:
        quantity = int(input())
        if command not in resource_dict:
            resource_dict[command] = 0
        resource_dict[command] += quantity
[print(f"{k} -> {v}") for k, v in resource_dict.items()]