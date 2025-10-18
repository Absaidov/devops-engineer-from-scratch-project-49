from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER


def generate_round() -> tuple[str, str]:
    number1: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
    number2: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)

    question: str = f"{number1} {number2}"
    result = str(get_gcd(number1, number2))

    return question, result

def get_gcd(number1: int, number2: int) -> int:
    if number2 == 0:
        return number1
    return get_gcd(number2, number1 % number2)
