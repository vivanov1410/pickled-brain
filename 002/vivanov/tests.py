import unittest

from pickle002 import Calculator


class AddTest(unittest.TestCase):
    """Test for add() function"""

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        self.assertEquals(self.calc.add(1, 2), 3)

    def test_add_positive_numbers2(self):
        self.assertEquals(self.calc.add(10, 25), 35)

    def test_add_zeros(self):
        self.assertEquals(self.calc.add(0, 0), 0)

    def test_add_positive_and_zero(self):
        self.assertEquals(self.calc.add(45, 0), 45)

    def test_add_zero_and_positive(self):
        self.assertEquals(self.calc.add(0, 45), 45)

    def test_add_negative_and_zero(self):
        self.assertEquals(self.calc.add(-33, 0), -33)

    def test_add_zero_and_negative(self):
        self.assertEquals(self.calc.add(0, -33), -33)

    def test_add_negative_numbers(self):
        self.assertEquals(self.calc.add(-3, -15), -18)

    def test_add_negative_numbers2(self):
        self.assertEquals(self.calc.add(-101, -19), -120)

    def test_add_positive_and_negative(self):
        self.assertEquals(self.calc.add(21, -7), 14)

    def test_add_negative_and_positive(self):
        self.assertEquals(self.calc.add(-7, 21), 14)

    def test_first_argument_not_number(self):
        self.assertEquals(self.calc.add('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(self.calc.add(3, 'asd'), 'error')

    def test_subtract_positive_numbers(self):
        self.assertEquals(self.calc.subtract(10, 6), 4)

    def test_subtract_positive_numbers2(self):
        self.assertEquals(self.calc.subtract(111, 11), 100)

    def test_subtract_zeros(self):
        self.assertEquals(self.calc.subtract(0, 0), 0)

    def test_subtract_positive_and_zero(self):
        self.assertEquals(self.calc.subtract(45, 0), 45)

    def test_subtract_zero_and_positive(self):
        self.assertEquals(self.calc.subtract(0, 45), -45)

    def test_subtract_negative_and_zero(self):
        self.assertEquals(self.calc.subtract(-33, 0), -33)

    def test_subtract_zero_and_negative(self):
        self.assertEquals(self.calc.subtract(0, -33), 33)

    def test_subtract_negative_numbers(self):
        self.assertEquals(self.calc.subtract(-3, -15), 12)

    def test_subtract_negative_numbers2(self):
        self.assertEquals(self.calc.subtract(-79, -19), -60)

    def test_subtract_positive_and_negative(self):
        self.assertEquals(self.calc.subtract(21, -7), 28)

    def test_subtract_negative_and_positive(self):
        self.assertEquals(self.calc.subtract(-7, 21), -28)

    def test_first_argument_not_number(self):
        self.assertEquals(self.calc.subtract('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(self.calc.subtract(3, 'asd'), 'error')

    def test_multiply_positive_numbers(self):
        self.assertEquals(self.calc.multiply(10, 6), 60)

    def test_multiply_positive_and_negative(self):
        self.assertEquals(self.calc.multiply(10, -6), -60)

    def test_multiply_negative_numbers(self):
        self.assertEquals(self.calc.multiply(-10, -6), 60)

    def test_multiply_zeros(self):
        self.assertEquals(self.calc.multiply(0, 0), 0)

    def test_multiply_positive_and_zero(self):
        self.assertEquals(self.calc.multiply(10, 0), 0)

    def test_multiply_negative_and_zero(self):
        self.assertEquals(self.calc.multiply(-10, 0), 0)

    def test_first_argument_not_number(self):
        self.assertEquals(self.calc.multiply('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(self.calc.multiply(3, 'asd'), 'error')

    def test_divide_positive_numbers(self):
        self.assertEquals(self.calc.divide(60, 6), 10)

    def test_divide_negative_numbers(self):
        self.assertEquals(self.calc.divide(-60, -6), 10)

    def test_divide_positive_and_negative(self):
        self.assertEquals(self.calc.divide(60, -6), -10)

    def test_divide_zero_by_number(self):
        self.assertEquals(self.calc.divide(0, 123), 0)

    def test_divide_number_by_zero(self):
        self.assertEquals(self.calc.divide(10, 0), 'error')

    def test_first_argument_not_number(self):
        self.assertEquals(self.calc.divide('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(self.calc.divide(3, 'asd'), 'error')

    def test_operations_start_with_zero(self):
        calc = Calculator()
        self.assertEquals(0, calc.number_of_operations)

    def test_operations_increase_when_add_called(self):
        calc = Calculator()
        calc.add(1, 1)
        calc.add(2, 2)
        self.assertEquals(2, calc.number_of_operations)

    def test_operations_increase_when_subtract_called(self):
        calc = Calculator()
        calc.subtract(1, 1)
        calc.subtract(2, 2)
        self.assertEquals(2, calc.number_of_operations)

    def test_operations_increase_when_multiply_called(self):
        calc = Calculator()
        calc.multiply(1, 1)
        calc.multiply(2, 2)
        self.assertEquals(2, calc.number_of_operations)

    def test_operations_increase_when_divide_called(self):
        calc = Calculator()
        calc.divide(1, 1)
        calc.divide(2, 2)
        self.assertEquals(2, calc.number_of_operations)


if __name__ == '__main__':
    unittest.main()