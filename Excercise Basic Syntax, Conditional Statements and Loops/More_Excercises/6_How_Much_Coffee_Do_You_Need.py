coffee_count = 0
events = ['cat', 'dog', 'coding', 'movie']
while True:
    command = input()
    if command == 'END':
        break
    else:
        if command.lower() in events:
            if command.isupper():
                coffee_count += 2
            elif command.islower():
                coffee_count += 1
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)