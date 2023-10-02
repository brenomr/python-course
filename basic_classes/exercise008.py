# Exercise Numbers Quiz

questions = [
    {
        'Question': '2 + 2 = ?',
        'Options': ['3', '4', '6'],
        'Correct Answer': '4'
    },
    {
        'Question': '4 * 5 = ?',
        'Options': ['12', '20', '25'],
        'Correct Answer': '20'
    },
    {
        'Question': '10 - 3 = ?',
        'Options': ['7', '8', '9'],
        'Correct Answer': '7'
    },
]

points = 0

#########################
# Simple exercise answer
#########################

# for question in questions:
#     print(question.get('Question'))
#     print(f"Options are: {question.get('Options')}")
#     answer = input(f"Your answer: ")

#     if answer == question.get('Answer'):
#         points += 1
#         print('Your answer is correct!')
#     else:
#         print('Your answer is incorrect.')

#########################
# Complex exercise answer
#########################

# for question in questions:
    # quest, opt, ans = list(question.items())

    # print(f"\n{quest[0]}: {quest[1]}")
    # print(f"{opt[0]} are: {opt[1]}")

    # answer = input('Your answer: ')

    # if answer == ans[1]:
    #     points += 1
    #     print('Your answer is correct!')
    # else:
    #     print('Your answer is incorrect!')

##################################################
# Even more complex with options based in index
##################################################

try:
    for question in questions:
        quest, opt, ans = list(question.items())

        print(f"\n{quest[0]}: {quest[1]}\nOptions are:")

        for index, option in enumerate(opt[1]):
            print(f"{index+1}) {option}")

        answer = int(input('Your answer: '))-1

        if opt[1][answer] == ans[1]:
            points += 1
            print('Your answer is correct!')
        else:
            print('Your answer is incorrect!')
except Exception as err:
    if type(err) == IndexError or type(err) == ValueError:
        print('You inserted an invalid option, try again!')
    else:
        print(err)

print(f'\nYou got {points} out of 3 questions right!')