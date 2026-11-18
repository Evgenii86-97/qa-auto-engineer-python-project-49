from brain_games.cli import welcome_user


def run_game(game):
    name = welcome_user()

    print(game.RULES)

    for _ in range(3):
        question, correct_answer = game.get_question_and_answer()

        print(f'Question: {question}')
        answer = input('Your answer: ').strip()

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
