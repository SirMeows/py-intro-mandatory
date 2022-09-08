def print_title(exercise_nr):
    print('**********\nEXERCISE ' + str(exercise_nr) + '\n**********')

# **********
# EXERCISE 1
# **********
print_title(1)


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



# **********
# EXERCISE 2
# **********
print_title(2)


# Using a list comprehension create a list of tuples from the folowing datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

dict = {'a':'Alpha','b' :'Beta','g':'Gamma'}

list = [(k, v) for k, v in dict.items()]

print(list)



# **********
# EXERCISE 3
# **********
print_title(3)


# From these 2 sets:
# {'a', 'e', 'i', 'o', 'u', 'y'}
# {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
# Of the 2 sets create a:


# Union

first_set = {'a', 'e', 'i', 'o', 'u', 'y'}
second_set = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

print(first_set.union(second_set))


# Symmetric difference

print(first_set.symmetric_difference(second_set))


# Difference

diff_set = first_set.difference(second_set)
if(len(diff_set) == 0):
    print('first set has no unique items')
else:
    print(diff_set)


# Disjoint

print(first_set.isdisjoint(second_set))



# **********
# EXERCISE 4
# **********
print_title(4)


# Date Decoder.
# A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.
# Create a dict suitable for decoding month names to numbers.
# Create a function which uses string operations to split the date into 3 items using the "-" character.
# Translate the month, correct the year to include all of the digits.
# The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).

date = '8-MAR-85'

months = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

def month_decoder(date):

    splitted = date.split('-')


    # handle day

    day_str = splitted[0]

    splitted[0] = int(day_str)


    # handle month

    month_input = splitted[1]

    if (len(month_input)) == 3:
        splitted[1] = months.get(month_input)


    # handle year

    year_input = splitted[2]

    divider_year = 70

    if len(year_input) == 2:

        two_digit_year = int(year_input)
        
        if divider_year < two_digit_year:
            splitted[2] = 1900 + two_digit_year

        else:
            splitted[2] = '20' + str(two_digit_year)
            

    return splitted

print(month_decoder(date))