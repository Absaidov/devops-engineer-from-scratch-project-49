def prompt(message):
    return input(message)


def start_engine(description: str, array_data):
    print('Welcome to the Brain Games!')
    player_name = prompt('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(description)

    for question, answer in array_data:
        print(f'Question: {question}')
        answer_from_console = prompt('Your answer: ')

        if answer_from_console.lower() == answer:
            print('Correct!')
        else:
            print(f'\'{answer_from_console}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'.')
            print(f'Let\'s try again, {player_name}!')
            return

    print(f"Congratulations, {player_name}!")
