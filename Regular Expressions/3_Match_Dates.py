import re

numbers = input()
regex = r"((\d{2})([/|.|-])([A-Z]{1}[a-z]{2})\3(\d{4}))"
matches = re.findall(regex, numbers)

for i in matches:
    print(f"Day: {i[1]}, Month: {i[3]}, Year: {i[4]}")