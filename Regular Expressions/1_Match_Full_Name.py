import re
regex = r'(\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b)'
names = input()
matches = re.findall(regex, names)
print(' '.join(matches))
