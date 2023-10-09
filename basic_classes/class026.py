# Expression generator, iterables and iterators

#######################
# Iterator and iterable
#######################

# Iterable is an object where we can find multiple values to iterate over them
iterable = ["I", "have", "__iter__"]

# An iterator is used to iterate over an iterable and return one value at a time, it always goes through the next value
# In this example iterable.__iter__() is the same as iter(iterable)
iterator = iterable.__iter__()

# It doesn't know the length len(iterator), it doesn't know the index of iterable iterator[2], it just know how to reach the next value

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

###########
# Generator
###########
# Generator are functions who knows how to pause
# Generator is an iterator, because you can navigate through an iterable, but the inverse isn't true

# In this example all values - even unnecessary ones - are in memory, to convert it to a generator, change [ ] to ( )
random_numbers_list = [ n for n in range(1000) ]
random_numbers_generator = ( n for n in range(1000) )

import sys

# The sizes on memory
print(sys.getsizeof(random_numbers_list))
print(sys.getsizeof(random_numbers_generator))

# The list has all values in memory, occupying unnecessary space
# print(next(iter(random_numbers_list)))

# The generator still paused on the first value, awaiting to be called
# print(next(random_numbers_generator))

# ATTENTION: With the list we can have access to the indexes and methods for a list, on a generator we can't


############################
# Creating our own generator
############################


def generator(n=0):
    # yield to pause the function, not to stop, like with return 1
    yield 1
    print('Continue...')
    yield 2
    print('Continue...')
    yield 3

    return "No more values, STOPING INTERATION!"

gen = generator(0)
# print(gen)
# print(next(gen))
# print(next(gen))

# for n in gen:
#     print(n)

def gen2(minimum=0, maximum=10):
    while True:
        yield minimum
        minimum += 1

        if minimum >= maximum:
            return

# Continuing a function from another
def gen3(minimum=0):
    yield from gen2(minimum)
    yield 'Now the...'
    yield 'code...'
    yield 'terminates.'

result = gen3(5)

for number in result:
    print(number)
