"""
USES of Combination, permutation and products fom itertools
"""

from itertools import combinations, permutations, product

people = ['Jones', 'Paulo', 'Amanda', 'Letícia']
tshirts = [
    ['black', 'white', 'red', 'blue'],
    ['small', 'medium', 'large'],
    ['adult', 'child']
]

def print_iter(iter):
    print()
    print(*iter, sep='\n')
    print()

# Combinations return all possible combinations of a given list (without repetition)
print_iter(combinations(people, 3))

# Permutations return all possible permutations of a given list (with repetition)
print_iter(permutations(people, 2))

# Product return all possible combinations of the given lists
print_iter(product(*tshirts))
