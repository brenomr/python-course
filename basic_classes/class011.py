# INPUT() METHOD, IF, ELSE AND ELIF
# Classes 014, 015, 016, 017, 018, 019 and 020

"""
Annotations:

Operator    Meaning         E.G.
>           greater than    5 > 3
>=          greater/equal   5 >=
<           less than       3 < 66
<=          less/equal      6 <= 20
==          equal           5 == 5
!=          different       12 != 7
"""


# simple input data
#
# while True:
#     name = input("Enter your name: ").strip()
#
#     if(len(name) == 0 or name == ' '):
#         print("You must enter at least one letter.")
#     else:
#         print(f'Your name is: {name}')
#         break


# input data with 3 tries

count = 3

while True:
    option = input("Do you want to login? (yes or no): ").strip().lower()

    if(option == 'yes'):
        print("Login...")
        break
    elif(option == 'no'):
        print("Closing terminal...")
        break
    else:
        if count > 1:
            print("You need to enter a valid option!")
            count -= 1
            print(f"Tries until process be terminate: {count}")
        else:
            print("Process terminated...")
            break