"""
Abstract Properties
-------------------

If we define a property as abstract, the referring
setter will need to be implemented too otherwise it
won't work
"""

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name) -> None:
        self._name = None
        self.name = name
    
    @property
    @abstractmethod
    def name(self):
        ...
    
    # we can avoid define setter here, once it won't
    # work because of the abstractmethod on property
    @name.setter
    def name(self, name):
        self._name = name

class Foo(AbstractFoo):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

bar = Foo('Bar')
print(bar.name)
