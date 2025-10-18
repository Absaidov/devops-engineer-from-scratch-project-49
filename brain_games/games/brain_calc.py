from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER

ARRAY_OPERATORS: list[str] = [' - ', ' * ', ' + ']

def generate_round() -> tuple[str, str]:
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
    return question, str(result)


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
