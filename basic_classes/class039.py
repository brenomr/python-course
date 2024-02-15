"""
USES of groupby from itertools

Groupby returns an iterator that returns
consecutive key sand groups from the iterable
"""
from itertools import groupby
from data.students_module import students

# Simple example, the elements will be grouped by the
# same value. To more accurate results, the iterable
# must be sorted, to avoid cases like the one below with 'a'

simple_test = ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'a']
group = groupby(simple_test)

for key, item in group:
    # print(f'{key} :: {list(item)}')
    pass

# More robust example, using the students iterable

def order_by_grade(student):
    return student['grade']

# Sorting the students by grade
sorted_students = sorted(students, key=order_by_grade)

# Grouping the students by grade
students_group = groupby(sorted_students, key=order_by_grade)

for key, student in students_group:
    print()
    print(f'Grade: {key}')
    print(*list(student), sep='\n')
    print()
