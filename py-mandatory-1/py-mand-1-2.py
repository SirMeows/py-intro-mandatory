# Using a list comprehension create a list of tuples from the folowing datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}

dict = {'a':'Alpha','b' :'Beta','g':'Gamma'}

list = [(k, v) for k, v in dict.items()]

print(list)

