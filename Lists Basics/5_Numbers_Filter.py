number = int(input())
all_list = []

for i in range(number):
    num = int(input())
    all_list.append(num)
command = input()

if command == 'even':
    filtered_list = [i for i in all_list if i % 2 == 0]
elif command == 'odd':
    filtered_list = [i for i in all_list if i % 2 != 0]
elif command == 'negative':
    filtered_list = [i for i in all_list if i < 0]
elif command == 'positive':
    filtered_list = [i for i in all_list if i >= 0]
print(filtered_list)