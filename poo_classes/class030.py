"""
Creating our own list class to comprehend
how the Python list protocol works.
"""
from collections.abc import Sequence
# We can use Iterable or Iterator to create our own list class


class MyList(Sequence):

    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        # to allow multiple appends
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self):
        return len(self._index)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


people_list = MyList()
people_list.append("John")
people_list.append("Mary")


# Without the __iter__ method, we can't iterate over the object,
# it will ends in error because the the interpreter don't know
# when to stop the iteration (John and Mary will be printed)

# with __iter__ we can iterate over the object
for person in people_list:
    print(person)

# with __setitem__ we can set a value to an index
people_list[0] = "Alice"

# with *args in append method we can append multiple values
people_list.append("Bob", "Eve")

for person in people_list:
    print(person)
