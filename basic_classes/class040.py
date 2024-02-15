"""
Uses of partial from functools and map
"""

from functools import partial

def print_iter(iterable):
    print(*iterable, sep='\n')

products = [
    {'name': 'product1', 'price': 10},
    {'name': 'product2', 'price': 50},
    {'name': 'product3', 'price': 100},
    {'name': 'product8', 'price': 80},
    {'name': 'product9', 'price': 120},
]

###########################################################
# Complex example
###########################################################

def discount(price, percentage_discount):
    return round((price * (1 - percentage_discount / 100)), 2)

discount_products_10 = [
    {**product, 'price': discount(product['price'], 10)} for product in products
]

print_iter(discount_products_10)

###########################################################
# Same as above, but using partial
###########################################################

discount_20 = partial(discount, percentage_discount=20)

discount_products_20 = [
    {**product, 'price': discount_20(product['price'])} for product in products
]

print('\n------------------------------\n')
print_iter(discount_products_20)

###########################################################
# Using map, on map we can change the values of the list
###########################################################

def discount_50(product):
    return {**product, 'price': product['price'] * 0.5}

discount_products_50 = map(
    discount_50,
    products
)

print('\n------------------------------\n')

print_iter(discount_products_50)

###########################################################
# Using lambda
###########################################################

simple_values = [10, 24, 44, 11, 61]

new_values = map(
    lambda x: x * 3,
    simple_values
)

print('\n------------------------------\n')
print_iter(new_values)
