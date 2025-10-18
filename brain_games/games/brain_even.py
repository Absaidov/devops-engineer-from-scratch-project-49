from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER

DESCRIPTION: str = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round() -> tuple[str, str]:
    random_number: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
    answer: str = 'yes' if is_even(random_number) else 'no'
    return str(random_number), answer


def is_even(number):
    return number % 2 == 0
