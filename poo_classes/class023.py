"""
Using __call__
The special method __call__ is used to
make an object (instance) callable.
"""

class CallMe:
    def __init__(self, phone: str) -> None:
        self._phone = phone

    def __call__(self, name: str) -> None:
        print(f'{name} is calling to {self._phone}')

call = CallMe('(55) 11 2232-3233')
call('John')
