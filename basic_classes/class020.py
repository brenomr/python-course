# CLOSURE
# Classes 074, 075
# A function who creates another function (return another function)

def welcome(message):
    def welcome_run(name):
        return f'{message} {name}!'
    return welcome_run

good_afternoon = welcome('Good afternoon')
good_night = welcome('Good night')

# print(good_afternoon("Loise"))
# print(good_night("Raul"))


# Exercise
# Create a function that creates other functions to duplicate, triplicate and quadruplicate a given number

def calc(number):
    def multiplicate(multiplier):
        return number * multiplier
    return multiplicate

duplicate = calc(5)
triplicate = calc(10)
quadruplicate = calc(4)

print(duplicate(2))
print(triplicate(3))
print(quadruplicate(4))