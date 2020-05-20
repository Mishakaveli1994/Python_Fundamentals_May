triples = int(input())

for a in range(97,97+triples):
    for b in range(97,97+triples):
        for c in range(97, 97 + triples):
            print(f"{chr(a)}{chr(b)}{chr(c)}")