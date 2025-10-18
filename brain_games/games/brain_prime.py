from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER


def generate_round() -> tuple[str, str]:
    random_number: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
    answer: str = "yes" if is_simple(random_number) else "no"
    return str(random_number), answer


def is_simple(random_number: int) -> bool:
    if random_number < 2:
        return False

    for i in range(2, random_number):
        if random_number % i == 0:
            return False

    return True
