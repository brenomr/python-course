# USING RANDOM()
# Class 064
# Exercise CPF GENERATOR

import random

try:
    cpf = ''
    i = 0

    while i < 9:
        cpf += str(random.randint(0,9))
        i += 1
    
    sum_first_nine_numbers = 0
    sum_first_ten_numbers = 0
    first_multiplier = 10
    second_multiplier = 11

    for number in cpf:
        sum_first_nine_numbers += int(number) * first_multiplier
        first_multiplier -= 1
    
    first_sum_multiply_ten = sum_first_nine_numbers * 10
    first_remainder = first_sum_multiply_ten % 11
    cpf += str(0 if first_remainder > 9 else first_remainder)

    for number in cpf:
        sum_first_ten_numbers += int(number) * second_multiplier
        second_multiplier -= 1
    
    second_sum_multiply_ten = sum_first_ten_numbers * 10
    second_remainder = second_sum_multiply_ten % 11
    cpf += str(0 if second_remainder > 9 else second_remainder)

    print(f'Generated CPF: {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
except Exception as err:
    print(err)