import random

from brain_games.start_engine import start_engine

max_number_of_numbers = 99
description = "What is the result of the expression?"
minimum_number = 1
array_operators = [" - ", " * ", " + "]


def main():
    array_data = [["", ""] for _ in range(3)]

    for j in range(len(array_data)):
        random_operator = random.randint(0, len(array_operators) - 1)
        random_number1 = random.randint(minimum_number, max_number_of_numbers)
        random_number2 = random.randint(minimum_number, max_number_of_numbers)

        question = get_question(random_number1, array_operators[random_operator], random_number2)
        result = calculate_expression(random_number1, array_operators[random_operator], random_number2)

        array_data[j][0] = question
        array_data[j][1] = str(result)

    start_engine(description, array_data)


def get_question(number1, operator, number2):
    return str(number1) + operator + str(number2)


def calculate_expression(number1, operator, number2):
    match operator:
        case " - ": return number1 - number2
        case " * ": return number1 * number2
        case " + ": return number1 + number2


if __name__ == '__main__':
    main()