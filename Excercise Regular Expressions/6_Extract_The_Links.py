import re
regex = r'(www\.[a-zA-Z\d-]*\.[a-z\.]+)'

address = input()
while address:
    result = re.findall(regex,address)
    if result:
        print(result[0])
    address = input()