import random

RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(first, second):
    while second:
        first, second = second, first % second
    return first


def get_question_and_answer():
    first = random.randint(1, 100)
    second = random.randint(1, 100)

    question = f'{first} {second}'
    correct_answer = str(find_gcd(first, second))

    return question, correct_answer
