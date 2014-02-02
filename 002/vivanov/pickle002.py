class Calculator:
    def __init__(self):
        self.number_of_operations = 0

    @staticmethod
    def _is_number(number):
        return type(number) == int

    def add(self, number1, number2):
        self.number_of_operations += 1
        if not self._is_number(number1) or not self._is_number(number2):
            return 'error'

        return number1 + number2

    def subtract(self, number1, number2):
        self.number_of_operations += 1
        if not self._is_number(number1) or not self._is_number(number2):
            return 'error'

        return number1 - number2

    def multiply(self, number1, number2):
        self.number_of_operations += 1
        if not self._is_number(number1) or not self._is_number(number2):
            return 'error'

        return number1 * number2

    def divide(self, number1, number2):
        self.number_of_operations += 1
        if not self._is_number(number1) or not self._is_number(number2) or number2 is 0:
            return 'error'

        return number1 / number2