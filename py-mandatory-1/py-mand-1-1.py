directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
managers = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

# who in the board of directors is not an employee?

non_employees = []

for d in directors:
    if d not in employees:
        non_employees.append(d)

print(non_employees)

# who in the board of directors is also an employee?

director_emplyees = [d for d in directors if d in set(employees)]

print(director_emplyees)

# how many of the management is also member of the board?

manager_directors = [m for m in managers if m in set(directors)]

print(len(manager_directors))

# All members of the managent also an employee

manager_employees = [m for m in managers if m in set(employees)]

print(manager_employees)

# All members of the management also in the board?

print(manager_directors)

# Who is an employee, member of the management, and a member of the board?

director_manager_employees = set(manager_directors).intersection(set(manager_employees))

print(director_manager_employees)

# Who of the employee is neither a memeber or the board or management?

print((employees-managers)-directors)

