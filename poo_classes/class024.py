"""
Class decorators
"""

###### Decorator class without parameters ######
class Multiply:
    def __init__(self, func) -> None:
        self.func = func
        self._multiplier = 10

    def __call__(self, *args, **kwargs):
        sum_result = self.func(*args, **kwargs)
        return sum_result * self._multiplier

@Multiply
def my_sum(a: int, b: int) -> int:
    return a + b

###### Tesintg ######
RESULT = my_sum(2, 3)
print(RESULT)

###### Decorator class with parameters ######
class NewMultiply:
    def __init__(self, multiplier) -> None:
        self._multiplier = multiplier

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            sum_result = func(*args, **kwargs)
            return sum_result * self._multiplier
        return wrapper

@NewMultiply(4)
def my_sum_(a: int, b: int) -> int:
    return a + b

###### Tesintg ######
RESULT = my_sum_(2, 3)
print(RESULT)
