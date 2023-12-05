"""
Decorator ordering
"""

def decorator_parameters(name):
    def decorator(func):
        print(f"Decorator: {name}.")

        def new_function(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f'{result} {name}'

            return final

        return new_function
    
    return decorator

# All of them will be printed on the final
@decorator_parameters(name="Third Decorator")
@decorator_parameters(name="Second Decorator")
@decorator_parameters(name="First Decorator")
def own_sum(a, b):
    return a + b

print(own_sum(10, 10))
