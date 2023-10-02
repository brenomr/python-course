########################
# Multiple Exercises
########################
"""
1) Faça um programa que peça ao usuário para informar um número inteiro, informe se este número
é par ou ímpar. Caso o usuário não digite um número inteiro, informar que não é a informação
solicitada (original language).

2) Faça um programa que pergunte a hora ao usuário, baseado no horário informado exibir uma
saudação apropriada (bom dia/tarde, boa noite).

3) Programa que peça o nome do usuário, informar o cumprimento do nome baseado na seguinte regra:
curto: <5 letras, normal: 5~6 letras, grande >6.

4) Extra logic exercise Radar program

5) Extra exercise using while
"""

# 1)
# try:
#     num = input('Insert an integer number: ')
#     parsed_int = int(num)

#     if not parsed_int % 2:
#         print(f'The given number ({num}) is even.')
#     else:
#         print(f'The given number ({num}) is odd.')
# except Exception as err:
#     if type(err) == ValueError: print('ERROR: You need to insert an integer number!')
#     else: print(err)

# 2)
# try:
#     time = input('What time is it? (just integer hour from 0h to 23h): ')
#     parsed_time = int(time)
#     is_morning = parsed_time >= 0 and parsed_time < 12
#     is_afternoon = parsed_time >= 12 and parsed_time < 18

#     if is_morning: print('Good morning!')
#     elif is_afternoon: print('Good afternoon!')
#     else: print('Good evening!')

# except Exception as err:
#     if type(err) == ValueError: print('ERROR: You need to insert the hour as integer number!')
#     else: print(err)

# 3)
# try:
#     name = input('Insert your name: ')
#     name_length = len(name)

#     if name_length < 5: print('You have a short name.')
#     elif name_length == 5 or name_length == 6: print('You have a regular size name.')
#     else: print('You have a big name.')
# except Exception as err:
#     print(err)

# 4)
# car_velocity = 60
# car_local = 101

# VEL_LIMIT = 60
# LOCAL = 100
# RADAR_RANGE = 1

# if car_local >= LOCAL and car_local <= (LOCAL + RADAR_RANGE):
#     print("The car is on the spot where radar can read its velocity...")

#     if car_velocity > VEL_LIMIT: print('The car committed an infraction and it will be charged...')
#     else: print('The car is under the velocity limit...')

# 5) Enter a name and return it with * between all characters
# name = input('Enter your name: ')
# count = 0
# new_name = '*'

# while count < len(name):
#     new_name += name[count] + '*'
#     count += 1

# print(new_name)

# 6) Simple calculator with while (enter 2 numbers and 1 operator)

while True:
    try:
        # Parse input numbers
        parsed_num_a = float(input('Enter the FIRST NUMBER: '))
        parsed_num_b = float(input('Enter the SECOND NUMBER: '))

        # Input operator
        print(f'''
              ---------------------------
              |  Choose your operation  |
              ---------------------------
              | Addition       (type +) |
              | Subtraction    (type -) |
              | Division       (type /) |
              | Multiplication (type *) |
              ---------------------------
        ''')
        operator = input('Type your desired operation: ')

        # Check data and make operations
        if operator not in ['+','-','/','*']:
            print('Invalid choice, try again.')
            break
        elif operator == '+': result = parsed_num_a + parsed_num_b
        elif operator == '-': result = parsed_num_a - parsed_num_b
        elif operator == '/':
            if parsed_num_b == 0:
                print('Division by zero is undefined, try again.')
                break
            else: result = parsed_num_a / parsed_num_b
        else: result = parsed_num_a * parsed_num_b

        #generating bar to show result
        symbols = 10
        generate_bar = '-' * (len(f'{parsed_num_a:.2f}')+len(f'{parsed_num_b:.2f}')+len(f'{result:.2f}')+symbols)
        print(generate_bar)
        print(f'| {parsed_num_a:.2f} {operator} {parsed_num_b:.2f} = {result:.2f} |')
        print(generate_bar)
        break
    except Exception as err:
        print(f'ERROR: {err}')