import re

regex = r'((^|(?<= ))[a-zA-Z]+[\.|_|-]?[a-zA-Z]+@([a-z]+[-|\.])+[a-z]+)'
text = input()
result = re.findall(regex,text)
for i in result:
    print(i[0])