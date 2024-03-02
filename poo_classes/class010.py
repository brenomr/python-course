"""
Agregation - Relation between two classes where one class is part of another.
Can be a relation of (1 to 1), (1 to N) or  (N to N).

E.g.: A car can have 1 or more wheels, but a wheel can only be part of 1 car.

Weak relation: One object can exists without the other.

In association: One writer can uses a pen, just simple
In agregation: A shopping cart (SC) have products, some methods of SC don't work
without product.
"""

class ShoppingCar:
    def __init__(self) -> None:
        self._products = list()
        self._total_price = 0
    
    @property
    def product(self):
        return self._products
    
    @product.setter
    def product(self, product):
        self._products.append(product)

    # This method can't work without a product
    def total_price(self):
        self._total_price = sum([product.price for product in self._products])
        return self._total_price

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


cart1 = ShoppingCar();

candy = Product('Candy', 10)
chocolate = Product('Chocolate', 15)
juicebox = Product('Juice Box', 18)

cart1.product = candy
cart1.product = chocolate
cart1.product = juicebox

print(cart1.total_price())
