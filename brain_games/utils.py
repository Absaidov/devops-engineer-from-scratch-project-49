import random

MIN_NUMBER: int = 1
MAX_NUMBER: int = 99


def generates_random_numbers(min_number: int, max_number: int):
    return random.randint(min_number, max_number)
