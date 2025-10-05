from brain_games.start_engine import start_engine
from brain_games.utils import generates_random_numbers

DESCRIPTION: str = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER: int = 1
MAX_NUMBER: int = 99
NUMBER_OF_ROUNDS: int = 3


def main():
    array_data = []

    for _ in range(NUMBER_OF_ROUNDS):
        random_number: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
        answer: str = 'yes' if is_even(random_number) else 'no'
        array_data.append((str(random_number), answer))

    start_engine(DESCRIPTION, array_data)


def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()
