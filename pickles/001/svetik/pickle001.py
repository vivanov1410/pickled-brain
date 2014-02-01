def is_number(number):
    return type(number) == int


def add(number1, number2):
    if not is_number(number1) or not is_number(number2):
        return 'error'

    return number1 + number2


def subtract(number1, number2):
    if not is_number(number1) or not is_number(number2):
        return 'error'

    return number1 - number2


def multiply(number1, number2):
    if not is_number(number1) or not is_number(number2):
        return 'error'
    return number1 * number2


def divide(number1, number2):
    if not is_number(number1) or not is_number(number2):
        return 'error'

    if number2 == 0:
        return 'error'
    return number1 / number2