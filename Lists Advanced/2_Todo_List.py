todo_list = []

while True:
    command = input()
    if command == 'End':
        break
    else:
        com_sp = command.split('-')
        todo_list += [[int(com_sp[0]), com_sp[1]]]

todo_list = sorted((i for i in todo_list), key=lambda x: x[0])
todo_list = [i[1] for i in todo_list]
print(todo_list)
# todo_list.sort(key=lambda x: x[0])
# print(todo_list)
