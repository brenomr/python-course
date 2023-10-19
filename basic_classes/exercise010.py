"""
Exercise 010
"""

import copy

# Base list
products = [
    { 'name': 'Screwdriver', 'price': 120.50 },
    { 'name': 'Intel i5 4500k', 'price': 85.50 },
    { 'name': 'RTX 4080ti', 'price': 400.00 },
    { 'name': 'Monitor AOC 25', 'price': 70.00 },
    { 'name': 'Mouse Logitech A600', 'price': 115.00 },
]

######################################################
# In a new list raise the price of all products in 10%
######################################################
# Personal option, doing without deepcopy

new_products = []

for product in products:
    new_products.append(product.copy())

for product in new_products:
    product['price'] = round((product['price'] * 1.1), 2)

#################################################
# In a new list order the products by name (DESC)
#################################################

order_by_name = copy.deepcopy(new_products)
order_by_name.sort(key=lambda product: product['name'], reverse=True)

#################################################
# In a new list order the products by price (ASC)
#################################################

order_by_price = copy.deepcopy(new_products)
order_by_price.sort(key=lambda product: product['price'])


#################
# Showing results
#################

print(*products, sep='\n', end='\n'*2)
print(*new_products, sep='\n', end='\n'*2)
print(*order_by_name, sep='\n', end='\n'*2)
print(*order_by_price, sep='\n', end='\n'*2)
