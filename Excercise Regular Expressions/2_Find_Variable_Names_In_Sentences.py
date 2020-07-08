import re

regex = r'((^|(?<= ))_[a-zA-Z0-9]+\b)'
text = input()

result = re.findall(regex, text)
result = [i[0][1:] for i in result]
print(','.join(result))