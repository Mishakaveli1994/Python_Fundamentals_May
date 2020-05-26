employeeHappiness = [int(i) for i in input().split(' ')]
improvementFactor = int(input())
employeeHappiness = [(i * improvementFactor) for i in employeeHappiness]
average = sum(employeeHappiness) / len(employeeHappiness)
happyEmployees = [i for i in employeeHappiness if i >= average]

if len(happyEmployees) >= len(employeeHappiness) / 2:
    print(f"Score: {len(happyEmployees)}/{len(employeeHappiness)}. Employees are happy!")
else:
    print(f"Score: {len(happyEmployees)}/{len(employeeHappiness)}. Employees are not happy!")
