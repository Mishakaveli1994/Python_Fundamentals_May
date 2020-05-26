substrings = input().split(', ')
strings = input().split(', ')
result = []
for i in substrings:
    for b in strings:
        if i in b:
            if i not in result:
                result.append(i)
print(result)