"""
Making classes relation.

Create classes: Car, Engine and Manufacturer (just field name to be simple)

Consider the relations:
- One car has one engine;
- One engine can be in N cars;
- One car has one manufacturer;
- One manufacturer can be in N cars;

Show: car, maufacturer and engine names

car --- has --- engine
car --- has --- manufacturer
"""


class Car:
    def __init__(self, name) -> None:
        self.name = name
        self._engine = None
        self._manufacturer = None
    
    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def show_car(self) -> str:
        return f'{self.name}: {self.engine} - {self.manufacturer}'

class Engine:
    def __init__(self, name, model) -> None:
        self.name = name
        self.model = model
    
    def __str__(self) -> str:
        return f'({self.name}, {self.model})'

class Manufacturer:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f'{self.name}'

generic_nv1 = Engine('Generics', 'NV8')
sport_nv500 = Engine('Sports', 'NV500')

volkswagen = Manufacturer('Volkswagen')
voyage = Car('Voyage')
voyage.engine = generic_nv1
voyage.manufacturer = volkswagen

fiat = Manufacturer('Fiat')
palio = Car('Palio')
palio.engine = generic_nv1
palio.manufacturer = fiat

nissan = Manufacturer('Nissan')
evo = Car('Evolution')
evo.engine = sport_nv500
evo.manufacturer = nissan

print(voyage.show_car())
print(palio.show_car())
print(evo.show_car())
