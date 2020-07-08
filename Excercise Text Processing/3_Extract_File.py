directory = input()
file = directory[(directory.rindex('\\'))+1:]
filename = file[:(file.index('.'))]
extension = file[(file.index('.'))+1:]
print(f'File name: {filename}')
print(f'File extension: {extension}')