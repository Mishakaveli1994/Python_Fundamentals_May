import re
text = input()
word = f'\\b{input()}\\b'
result = re.findall(word,text,re.IGNORECASE)
print(len(result))