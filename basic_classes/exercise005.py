#########################
# Exercise Shopping List
#########################
"""
PT/BR: Criar uma lista de compra com listas, usuário deve
ter possiblidade de: Adicionar, apagar ou listar itens.
Inpedir que programa retorn erros de indices inexistentes.
"""

import os
os.system('clear')

shopping_list = ['avocado']

while True:
    try:
        print('\n--------------------\n'\
              '| Select an option |\n'\
              '--------------------'
        )
        option = input('[I]nsert [R]emove [L]ist [E]xit: ').lower()

        if len(option) > 1 or option not in 'irle':
            os.system('clear')
            print('Invalid Option:\n'\
                  'Options are: I, R or L and one letter at time.'
            )
            continue

        if option == 'e':
            break

        if option == 'i':
            os.system('clear')
            item_to_add = input('Insert the item you want to buy: ')
            shopping_list.append(item_to_add)

        elif option == 'r':
            if len(shopping_list) == 0:
                os.system('clear')
                print('Nothing to be removed.')
                continue
            else:
                item_to_remove = int(input('Insert the item ID to be removed: '))
                shopping_list.pop(item_to_remove)
                os.system('clear')
                print('Item sucessfully removed!')
                continue

        elif option == 'l':
            os.system('clear')

            if len(shopping_list) == 0:
                print('Nothing to be listed.')
                continue
            else:
                enum_shopping_list = enumerate(shopping_list)
                for item in enum_shopping_list:
                    print(item)
                continue
    except Exception as err:
        if type(err) == IndexError:
            os.system('clear')
            print('No item found with given ID.')
            continue
        print(type(err))