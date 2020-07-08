import re
regex = r'((^|(?<= ))-?\d+(\.\d+)?($|(?=\s)))'
numbers = input()
result = [i[0] for i in re.findall(regex,numbers)]
print(' '.join(result))