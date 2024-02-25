"""
CLASSES with Python

Classes generate objetcs (instances)
By convention we use PascalCase to name classes, e.g: MyCustomClass
We can do many actions throuth class methods
param 'self' always refers to the own class instance
Methods are functions inside a class
More detail of 'self' after line 66
"""

####################
# Classes definition
####################

class Person:
    
    # 'constructor'
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
    
    # main reference of class
    def __str__(self) -> str:
        return f'Person: {self.name} {self.surname}'

class Car:

    def __init__(self, name, color, model) -> None:
        self.name = name
        self.color = color
        self.model = model
    
    def __str__(self) -> str:
        return self.name
    
    def show_color(self, new_color=None):
        print(f'{self.name} is {new_color if new_color else self.color}!')
    
    def speed_up(self, speed):
        print(f'The {self.name} is speeding up at {speed}km')
    
    def what_the_color(self, *args, **kwargs):
        return self.show_color(*args, **kwargs)

fusca = Car('Fusca', 'Amarelo', 'Antigo')
uno = Car(name='Uno', color='Grey', model='Fire')


###########
# Instances
###########

person1 = Person('Bob', 'Marley')


##############
# Show results
##############

print(person1)
print(person1.name, person1.surname)
print(fusca)
print(uno)

##################
# Calling a method
##################
fusca.show_color()

##################
# Behavior of self
##################

etios = Car('Etios', 'Silver', 'Flex')

etios.speed_up(50)
etios.what_the_color('Blue')

# By calling etios.show_color is the same as invoking
# the class and send to it the instance of etios
Car.show_color(etios)
