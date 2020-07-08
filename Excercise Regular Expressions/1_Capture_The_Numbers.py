import re

regex = r'(\d+)'
result = []
numbers = input()
while numbers:
    for i in re.findall(regex, numbers):
        print(i, end=' ')
    numbers = input()
