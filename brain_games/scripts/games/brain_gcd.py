from brain_games.start_engine import start_engine
from brain_games.utils import generates_random_numbers

DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER: int = 1
MAX_NUMBER: int = 99
NUMBER_OF_ROUNDS: int = 3


def main():
    array_data = []

    for _ in range(NUMBER_OF_ROUNDS):
        number1: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
        number2: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
        question: str = f"{number1} {number2}"
        result = str(get_gcd(number1, number2))
        array_data.append((question, str(result)))

    start_engine(DESCRIPTION, array_data)


def get_gcd(number1: int, number2: int) -> int:
    if number2 == 0:
        return number1
    return get_gcd(number2, number1 % number2)


if __name__ == '__main__':
    main()
