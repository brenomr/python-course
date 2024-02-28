"""
Staticmethod

Not too useful but it can define a simple method
(function) without access to the class (cls) or self
"""

class Something:

    @staticmethod
    def say_something():
        print('Something...')


# works
Something.say_something()

# works
s1 = Something()
s1.say_something()
