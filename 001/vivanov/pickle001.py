def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


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
    if not is_number(number1) or not is_number(number2) or number2 is 0:
        return 'error'

    return number1 / number2
