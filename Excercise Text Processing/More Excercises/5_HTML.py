counter = 0
while True:
    command = input()
    if command == 'end of comments':
        break
    else:
        if counter == 0:
            print(f'<h1>\n    {command}\n</h1>')
            counter += 1
        elif counter == 1:
            print(f'<article>\n    {command}\n</article>')
            counter += 1
        else:
            print(f'<div>\n    {command}\n</div>')
