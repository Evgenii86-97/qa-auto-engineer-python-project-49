import random

RULES = 'What is the result of the expression?'


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    operator = random.choice(['+', '-', '*'])

    question = f'{number1} {operator} {number2}'

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    return question, str(result)
