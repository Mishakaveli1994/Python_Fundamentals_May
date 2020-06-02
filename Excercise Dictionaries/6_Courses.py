courseDict = {}
while True:
    command = input()
    if command == 'end':
        break
    else:
        comSplit = command.split(' : ')
        course = comSplit[0]
        student = comSplit[1]
        if course not in courseDict:
            courseDict[course] = []
        courseDict[course].append(student)

for k, v in courseDict.items():
    courseDict[k] = sorted(courseDict[k])
sortedCourses = {k: v for k, v in sorted(courseDict.items(), key=lambda x: -len(x[1]))}

for i in sortedCourses:
    print(f"{i}: {len(sortedCourses[i])}")
    for b in sortedCourses[i]:
        print(f"-- {b}")