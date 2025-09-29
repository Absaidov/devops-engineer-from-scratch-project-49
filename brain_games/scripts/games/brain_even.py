import random

from brain_games.start_engine import start_engine

MAX_NUMBER_OF_NUMBERS = 99
description = "Answer 'yes' if the number is even, otherwise answer 'no'."


def main():
    array_data = [["", ""] for _ in range(3)]

    for j in range(len(array_data)):
        random_number = random.randint(1, MAX_NUMBER_OF_NUMBERS)
        array_data[j][0] = str(random_number)
        array_data[j][1] = "yes" if is_even(random_number) else "no"

    start_engine(description, array_data)


def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()
