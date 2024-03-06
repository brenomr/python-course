"""
Class - multiple inheritance
With more class inheritance, more
complex your program will be

Diamond problem:
    A
  /   \
  B   C
  \   /
    D

When D call a method from A,
how it will be resolved?
Answer: C3 Linearization
https://en.wikipedia.org/wiki/C3_linearization
"""

class A:
    ...

    def whoami(self):
        print('I\'m A...')

class B(A):
    ...

    def whoami(self):
        print('I\'m B...')

class C(A):
    ...

    def whoami(self):
        print('I\'m C...')

class D(B,C):
    ...

    def whoami(self):
        print('I\'m D...')


d = D()

# If whoiam is remove from D, from what
# class it will be called? B or C?
d.whoami()


# To know how methods (even att) will be
# resolved, we can use MRO class.mro()

# Tuple
print(D.__mro__)

# List
print(D.mro())
