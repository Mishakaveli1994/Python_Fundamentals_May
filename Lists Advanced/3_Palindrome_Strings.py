words = input().split(' ')
needed_word = input()
all_pal = []
searched_pal = 0
for i in words:
    if i[::-1] == needed_word:
        searched_pal += 1
    if i[::-1] == i:
        all_pal.append(i)
print(all_pal)
print(f"Found palindrome {searched_pal} times")