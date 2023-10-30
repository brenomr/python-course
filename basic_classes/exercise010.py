"""
Exercise 010
"""

import copy

# Base list
from data import products

######################################################
# In a new list raise the price of all products in 10%
######################################################
# Personal option, doing without deepcopy

# new_products = []

# for product in products:
#     new_products.append(product.copy())

# for product in new_products:
#     product['price'] = round((product['price'] * 1.1), 2)

# Short version from code on lines: 21, 23, 24, 26 and 27

new_products = [
    { **product, 'price': round(product['price'] * 1.1, 2) } for product in products
]

#################################################
# In a new list order the products by name (DESC)
#################################################

# order_by_name = copy.deepcopy(products)
# order_by_name.sort(key=lambda product: product['name'], reverse=True)

# Short version. Deepcopy isn't necessary, but exercise request it's use

order_by_name = sorted(
    copy.deepcopy(products), key=lambda product: product['name'], reverse=True
)

#################################################
# In a new list order the products by price (ASC)
#################################################

# order_by_price = copy.deepcopy(products)
# order_by_price.sort(key=lambda product: product['price'])

# Short version.

order_by_price = sorted(
    copy.deepcopy(products), key=lambda product: product['price']
)

#################
# Showing results
#################

print(*products, sep='\n', end='\n'*2)
print(*new_products, sep='\n', end='\n'*2)
print(*order_by_name, sep='\n', end='\n'*2)
print(*order_by_price, sep='\n', end='\n'*2)
