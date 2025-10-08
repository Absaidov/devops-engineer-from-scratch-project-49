from brain_games.scripts.start_engine import start_engine
from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER

DESCRIPTION: str = \
    'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_OF_ROUNDS: int = 3


def main():
    array_data = []

    for _ in range(NUMBER_OF_ROUNDS):
        random_number: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
        answer: str = "yes" if is_simple(random_number) else "no"
        array_data.append((str(random_number), answer))

    start_engine(DESCRIPTION, array_data)


def is_simple(random_number: int) -> bool:
    if random_number < 2:
        return False

    for i in range(2, random_number):
        if random_number % i == 0:
            return False

    return True


if __name__ == '__main__':
    main()
