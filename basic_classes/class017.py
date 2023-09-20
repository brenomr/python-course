# Exercise
"""
PT/BR: Desenvolver um jogo onde o usuário deverá adivinhar uma palavra (aka forca), regras:
- O usuário poderá digitar uma letra por vez (validar);
- A cada acerto a letra da palavra deverá ser exibida;
- Contar o número de tentativas do usuário e exibí-las no final;

Sugestão pessoal de melhorias:
- Como na forca ao invés de exibir tentativas, gerar o boneco do usuário a cada erro e ao
completar o boneco o usuário perde o jogo.
- Adicionar algumas dicas.
- Trabalhar com lista ao invés de string pura (mais simples e performático)
- Modelo do boneco:
  _______
 |/     |
 |     (_)
 |     _|_
 |    / | |
 |     _|_
 |    |   |
 |
_|___
"""

# vars to setting up the game
secret_word = 'avocado'

hint_1 = 'Its a fruit'
hint_2 = 'Its green'

secret_word_result = []

for l in secret_word:
    secret_word_result.append(' _ ')

chances = 5

game_over = False

while chances > 0:
    try:
        if secret_word == ''.join(secret_word_result):
            break

        print('\nSecret Word: ' + ''.join(secret_word_result), end='\n'*2)
        letter = input('Insert a letter: ')
        
        if len(letter) > 1:
            print('One letter at time, try again...')
        
        elif letter in secret_word_result:
            print('You already choose this letter.')

        elif letter in secret_word:
            loop = 0

            for current_letter in secret_word:
                if current_letter == letter:
                    secret_word_result[loop] = letter
                loop += 1
        
        else:
            chances -= 1

            if chances > 0:
                print(f'Oops wrong letter. You have {chances} chance{"s" if chances > 1 else ""}.')
                if chances ==3:
                    print(f'Here a hint to help you: {hint_1}.')
                if chances == 1:
                    print(f'Another hint to help you: {hint_2}.')
            else:
                game_over = True
                print('Game over!')
            print(' _______',\
                    ' |/     |',\
                    ' |     (_)',\
                    ' |     'f'{"_|_" if chances < 4 else ""}',\
                    ' |    'f'{"/ | |" if chances < 3 else ""}',\
                    ' |    'f'{" _|_" if chances < 2 else ""}',\
                    ' |    'f'{"|   |" if chances < 1 else ""}',\
                    ' |',\
                    '_|____',\
                sep='\n'
            )
    except Exception as err:
        print(err)

print(f'\nThe secret word was: {secret_word}.')
if game_over:
    print("Don't worry, you can try again! ;)")
else:
    print("Congratulations! You rock! =)")