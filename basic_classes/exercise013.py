"""
Catch the values (int or float) from two lists and
return the sum of each element on a third list.
Consider the elements of the shortest list.

e.g:
list_a = [ 2, 4, 10, 15, 3, 5, 7 ]
list_b = [ 20, 25, 33, 19, 12 ]

list_c = [ 22, 29, 43, 34, 15 ]
"""

from itertools import zip_longest

list_a = [ 2, 4, 10, 15, 3.2, 5, 7 ]
list_b = [ 20.5, 25, 33.3, 19, 12 ]

def list_sum(l1: list, l2: list):
    """Sum two lists."""

    shortest_list = l1 if len(l1) < len(l2) else l2
    return [ (l1[i] + l2[i]) for i, item in enumerate(shortest_list) ]

print(list_sum(list_a, list_b))

# course's proposal short list
sum_list = [ x + y for x, y in zip(list_a, list_b)]
print(sum_list)

# course's proposal large list (fill missing values from short list with zero)
sum_list2 = [ x + y for x, y in zip_longest(list_a, list_b, fillvalue=0) ]
print(sum_list2)
