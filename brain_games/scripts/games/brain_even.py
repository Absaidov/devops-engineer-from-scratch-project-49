from brain_games.start_engine import start_engine
from brain_games.utils import generates_random_numbers

DESCRIPTION: str = "Answer 'yes' if the number is even, otherwise answer 'no'."
MAX_NUMBER: int = 99
MINIMUM_NUMBER: int = 1
NUMBER_OF_ROUNDS: int = 3

def main():
    array_data: list[list[str]] = [["", ""] for _ in range(NUMBER_OF_ROUNDS)]

    for j in range(len(array_data)):
        random_number = generates_random_numbers(MINIMUM_NUMBER, MAX_NUMBER)
        array_data[j][0] = str(random_number)
        array_data[j][1] = "yes" if is_even(random_number) else "no"

    start_engine(DESCRIPTION, array_data)


def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()