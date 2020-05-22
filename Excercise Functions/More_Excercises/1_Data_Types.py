def inspect_type(datatype, string):
    if datatype == 'int':
        print(int(string) * 2)
    elif datatype == 'real':
        print(f"{float(string) * 1.5:.2f}")
    elif datatype == 'string':
        print(f"${string}$")


datatype = input()
initial_text = input()
inspect_type(datatype, initial_text)
