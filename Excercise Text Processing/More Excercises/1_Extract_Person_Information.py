# Judge does not like the solution, but by all intensive purposes it seems correct
numberOfLines = int(input())
name = []
age = []
for i in range(numberOfLines):
    text = input()
    name += [i[1:len(i) - 1] for i in text.split(' ') if i.startswith('@') and i.endswith('|')]
    age += [int(i[1:len(i) - 1]) for i in text.split(' ') if i.startswith('#') and i.endswith('*')]

for k, v in zip(name, age):
    print(f"{k} is {v} years old.")
