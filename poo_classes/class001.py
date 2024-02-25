"""
CLASSES with Python

Classes generate objetcs (instances)
By convention we use PascalCase to name classes, e.g: MyCustomClass
We can do many actions throuth class methods
param 'self' always refers to the own class instance
Methods are functions inside a class
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
    
    def show_color(self):
        print(f'{self.name} are {self.color}!')

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
