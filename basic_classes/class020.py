# Exercise
""""
Create a program to validate a CPF, rules:

-- VALIDANTING THE 10º DIGIT
- Multiply each of the first 9 digits by their position starting from 10, e.g.:
    0   9   3   .  2   6   7    .   3   3   0   (FIRST 9 DIGITS)
    10  9   8  --- 7   6   5   ---  4   3   2   (POSITIONS FROM 10)
    -----------------------------------------
    0   81  24      14  36  35      12  9   0
- Sum all results from the multiplication
- Multiply the new result by 10
- Get the REMAINDER from the last result divided by 11
- If the remainder is greater than 9, the 10º CPF digit will be zero, otherwise, it will be the remainder

-- VALIDATING THE 11º DIGIT
- Multiply each of the first 10 digits (this includes the first one already validated) by their position starting from 11, e.g.:
    0   9   3   .   2   6   7   .   3   3   0   -   9   (FIRST 10 DIGITS)
    11  10  9  ---  8   7   6  ---  5   4   3  ---  2   (POSITIONS FROM 10)
    --------------------------------------------------
    0   90  27      16  42  42      15  12  0       18
- SAME RULE FROM THE 10º DIGIT

CPF EXAMPLE: 093.267.330-92
"""

while True:
    try:
        parsed_cpf = ''
        valid_digits = '0123456789.-'
        valid_parsed_cpf = True

        print('\n|  CPF EXAMPLE:  |')
        cpf = input(' ----------------\n'\
                    '| 093.267.330-92 |\n'\
                    ' ----------------\n\n'\
                    'Inser your CPF: '
                    )
        
        if len(cpf) > 14:
            print('\nCPF must have a maximum of 14 digits.\n')
            continue
        
        for digit in cpf:
            if digit not in valid_digits:
                valid_parsed_cpf = False
                print('\nCPF must have only numbers, dots, and hífen.\n')
                break
            elif digit != '-' and digit != '.':
                parsed_cpf += digit
        
        if not valid_parsed_cpf:
            continue

        if len(parsed_cpf) != 11:
            print('\nCPF must have 11 numbers.\n')
            continue

        else:
            print('Your parsed CPF: ', parsed_cpf)
            break
    except:
        pass