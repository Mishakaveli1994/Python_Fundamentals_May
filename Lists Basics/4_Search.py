number = int(input())
word = input()

all_list = []
filtered_list = []

for i in range(number):
    text = input()
    all_list.append(text)
    if word in text:
        filtered_list.append(text)

print(all_list)
print(filtered_list)
