"""
Uses of COUNT
count is a endless iterator that will return a number from a start point to infinity,
different from range where you can set a stop point (limit).
"""

from itertools import count

r1 = range(6)
c1 = count(start=5, step=2)

print(hasattr(c1, '__iter__'))
print(hasattr(c1, '__next__'))
print(hasattr(r1, '__iter__'))
print(hasattr(r1, '__next__'))

print('--------------', end=2*'\n')
print(next(c1)) # 0
print(next(c1)) # 1
print('--------------', end=2*'\n')

for i in c1:
    if i > 20:
        break
    print(i)
