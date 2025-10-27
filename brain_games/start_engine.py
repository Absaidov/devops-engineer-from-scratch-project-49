import prompt

NUMBER_OF_ROUNDS: int = 3


def start_engine(description: str, generate_round):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(description)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = generate_round()

        print(f'Question: {question}')
        answer_from_console = prompt.string('Your answer: ')

        if answer_from_console.lower() == correct_answer.lower():
            print('Correct!')
        else:
            print(f'\'{answer_from_console}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {player_name}!')
            return

    print(f"Congratulations, {player_name}!")
