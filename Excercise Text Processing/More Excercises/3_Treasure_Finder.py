key = [int(i) for i in input().split(' ')]
while True:
    command = input()
    if command == 'find':
        break
    else:
        decryptedText = ''
        counter = 0
        for i in command:
            if counter == len(key):
                counter = 0
            decryptedText += chr(ord(i) - key[counter])
            counter += 1
        resourceStart = decryptedText.index('&') + 1
        resourceEnd = decryptedText.index('&', resourceStart)
        resource = decryptedText[resourceStart:resourceEnd]
        locationStart = decryptedText.index('<') + 1
        locationEnd = decryptedText.index('>', resourceStart)
        location = decryptedText[locationStart:locationEnd]
        print(f'Found {resource} at {location}')