from brain_games.scripts.start_engine import start_engine
from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER

DESCRIPTION: str = 'What is the result of the expression?'
NUMBER_OF_ROUNDS: int = 3
ARRAY_OPERATORS: list[str] = [' - ', ' * ', ' + ']


def main():
    array_data = []

    for _ in range(NUMBER_OF_ROUNDS):
        random_operator: int = generates_random_numbers(
            0,
            len(ARRAY_OPERATORS) - 1)
        random_number1: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
        random_number2: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)

        question: str = get_question(
            random_number1,
            ARRAY_OPERATORS[random_operator],
            random_number2)
        result: int = calculate_expression(
            random_number1,
            ARRAY_OPERATORS[random_operator],
            random_number2)

        array_data.append((question, str(result)))

    start_engine(DESCRIPTION, array_data)


def get_question(number1: int, operator: str, number2: int) -> str:
    return str(number1) + operator + str(number2)


def calculate_expression(number1: int, operator: str, number2: int) -> int:
    match operator:
        case " - ":
            return number1 - number2
        case " * ":
            return number1 * number2
        case " + ":
            return number1 + number2
        case _:
            return 0


if __name__ == '__main__':
    main()
