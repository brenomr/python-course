"""
Abstract Classes - Abstract Base Class (ABC)
--------------------------------------------
It's like contracts, it's a way to force the
child class to implement some methods.

To be an abstract class, need to extends from
ABC and have at least one abstract method.
"""

from abc import ABC, abstractmethod

class Log(ABC):

    @abstractmethod
    def _log(self, msg):
        ...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}.')
    
    def log_success(self, msg):
        return self._log(f'Succes: {msg}.')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} - from {self.__class__.__name__}.')

# This will fail: TypeError: Can't instantiate abstract class...
# testing = Log()

l = LogPrintMixin()
l.log_success('It works')
