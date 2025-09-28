import random
import prompt


def main():
    print(f'Welcome to the Brain Games!')
    player_name: str = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(0, 3):
        random_number: int = random.randint(0, 99)
        print(f'Question {random_number}')
        answer_from_console = prompt.string('Your answer: ')
        print(answer_from_console)
        is_even_or_not: str = 'yes' if is_even(random_number) else 'no'
        if answer_from_console.lower() == is_even_or_not:
            print(f'Correct!')
        else:
            print(f"""{answer_from_console} is wrong answer ;(. Correct answer was {is_even_or_not}.
Let's try again, {player_name}!""")
            return
    print(f'Congratulations, {player_name}!')


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == '__main__':
    main()
