from brain_games.utils import generates_random_numbers, MIN_NUMBER, MAX_NUMBER

MAX_NUMBER_FOR_STEP: int = 5
MIN_ARRAY_LENGTH_NUMBER: int = 8
MAX_ARRAY_LENGTH_NUMBER: int = 10


def generate_round() -> tuple[str, str]:
    random_number: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
    length: int = generates_random_numbers(
        MIN_ARRAY_LENGTH_NUMBER,
        MAX_ARRAY_LENGTH_NUMBER)
    step: int = generates_random_numbers(2, MAX_NUMBER_FOR_STEP)

    arr_prg: list[int] = generate_sequence(random_number, length, step)
    progression_str: str = ""
    right_number_index: int = generates_random_numbers(
        MIN_NUMBER,
        len(arr_prg) - 1)
    hidden_number: int = arr_prg[right_number_index]

    for j in range(len(arr_prg)):
        if j == right_number_index:
            progression_str += '.. '
        else:
            progression_str += f'{arr_prg[j]} '

    return progression_str.strip(), str(hidden_number)



def generate_sequence(next_random_number: int,
                      number_of_array_length: int,
                      step_of_sub_sequence: int) -> list[int]:
    array_of_numbers = []
    for j in range(number_of_array_length):
        current_element: int = next_random_number + j * step_of_sub_sequence
        array_of_numbers.append(current_element)
    return array_of_numbers



