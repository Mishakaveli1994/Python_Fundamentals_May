key = int(input())
letters = int(input())
message = ""
for i in range(letters):
    letter = input()
    message += chr(ord(letter)+key)

print(message)