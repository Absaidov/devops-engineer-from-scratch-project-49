from brain_games.start_engine import start_engine
from brain_games.utils import generates_random_numbers

DESCRIPTION: str = 'What number is missing in the progression?'
MIN_NUMBER: int = 1
MAX_NUMBER: int = 99
NUMBER_OF_ROUNDS: int = 3
MAX_NUMBER_FOR_STEP: int = 5
MIN_ARRAY_LENGTH_NUMBER: int = 8
MAX_ARRAY_LENGTH_NUMBER: int = 10


def main():
    array_data = []

    for _ in range(NUMBER_OF_ROUNDS):
        random_number: int = generates_random_numbers(MIN_NUMBER, MAX_NUMBER)
        length: int = generates_random_numbers(MIN_ARRAY_LENGTH_NUMBER, MAX_ARRAY_LENGTH_NUMBER)
        step: int = generates_random_numbers(2, MAX_NUMBER_FOR_STEP)

        arr_prg: list[int] = generate_sequence(random_number, length, step)
        progression_str: str = ""
        right_number_index: int = generates_random_numbers(MIN_NUMBER, len(arr_prg) - 1)
        hidden_number: int = arr_prg[right_number_index]

        for j in range(len(arr_prg)):
            if j == right_number_index:
                progression_str += '.. '
            else:
                progression_str += f'{arr_prg[j]} '

        array_data.append((progression_str.strip(), str(hidden_number)))

    start_engine(DESCRIPTION, array_data)


def generate_sequence(next_random_number: int, number_of_array_length: int, step_of_sub_sequence: int) -> list[int]:
    array_of_numbers = []
    for j in range(number_of_array_length):
        current_element: int = next_random_number + j * step_of_sub_sequence
        array_of_numbers.append(current_element)
    return array_of_numbers


if __name__ == '__main__':
    main()
