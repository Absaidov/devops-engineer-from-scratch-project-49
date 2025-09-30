from brain_games.start_engine import start_engine
from brain_games.utils import generates_random_numbers

DESCRIPTION: str = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER: int = 99
MINIMUM_NUMBER: int = 1
NUMBER_OF_ROUNDS: int = 3


def main():
    array_data = [["", ""] for _ in range(NUMBER_OF_ROUNDS)]
    for j in range(NUMBER_OF_ROUNDS):
        number1 = generates_random_numbers(MINIMUM_NUMBER, MAX_NUMBER)
        number2 = generates_random_numbers(MINIMUM_NUMBER, MAX_NUMBER)
        question = f"{number1} {number2}"
        result = str(get_gcd(number1, number2))
        array_data[j][0] = question
        array_data[j][1] = result
    start_engine(DESCRIPTION, array_data)


def get_gcd(n1: int, n2: int) -> int:
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1


if __name__ == '__main__':
    main()
