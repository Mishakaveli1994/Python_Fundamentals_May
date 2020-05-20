numberOfLines = int(input())
sumOfChars = 0
for i in range(numberOfLines):
    character = input()
    sumOfChars += ord(character)

print(f"The sum equals: {sumOfChars}")