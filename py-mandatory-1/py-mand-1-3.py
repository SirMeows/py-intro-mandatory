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