# ISINSTANCE METHOD, FALSY values in Python, dir, hasattr and getattr
# Method to check the instance of argument, object, etc

regular_list = [ 1, 2, 'a', 'b', 'test', [ 1, 3, 4 ], { 'name': 'Fred' }, { 1, 5 } ]

# checking if item in list is instance of set
for item in regular_list:
    if isinstance(item, set):
        item.add(55)
        print(item, isinstance(item, set))

    # after the validation with isinstance, we can make use of methods of the validated instance
    if isinstance(item, str):
        item.upper()


########################
# FALSY values in Python
########################

r_list = []
r_dict = {}
r_set = set()
r_tuple = ()
r_string = ''
r_integer = 0
r_float = 0.0
r_nothing = None
r_false = False
r_inter = range(0)

def falsy(value):
    return 'Falsy' if not value else 'Truthy'

print(falsy(r_list))
print(falsy(r_dict))
print(falsy(r_set))
print(falsy(r_tuple))
print(falsy(r_string))
print(falsy(r_integer))
print(falsy(r_float))
print(falsy(r_nothing))
print(falsy(r_false))
print(falsy(r_inter))


############
# DIR METHOD
############
# dir() show all names definied to an objetc

name = 'Paulo Borges'
# print(dir(name))

############
# HASATTR METHOD
############
# check if an objetc has an attribute (method)

if hasattr(name, 'lower'):
    print('String name has method lower().')

################
# GETATTR METHOD
################
# to invoke an method

method = 'upper'

if hasattr(name, method):
    print('Name has Method Upper...')
    print('It work: ', name.upper())
    # this won't work --> print(name.method()) -- in order to invoke the method, use getattr (after being validated)
    print('It work too: ', getattr(name, method)())
