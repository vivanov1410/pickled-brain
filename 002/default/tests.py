import unittest

from pickle002 import Calculator


class AddTest(unittest.TestCase):
    """Test for add() function"""

    def test_add_positive_numbers(self):
        self.assertEquals(add(1, 2), 3)

    def test_add_positive_numbers2(self):
        self.assertEquals(add(10, 25), 35)

    def test_add_zeros(self):
        self.assertEquals(add(0, 0), 0)

    def test_add_positive_and_zero(self):
        self.assertEquals(add(45, 0), 45)

    def test_add_zero_and_positive(self):
        self.assertEquals(add(0, 45), 45)

    def test_add_negative_and_zero(self):
        self.assertEquals(add(-33, 0), -33)

    def test_add_zero_and_negative(self):
        self.assertEquals(add(0, -33), -33)

    def test_add_negative_numbers(self):
        self.assertEquals(add(-3, -15), -18)

    def test_add_negative_numbers2(self):
        self.assertEquals(add(-101, -19), -120)

    def test_add_positive_and_negative(self):
        self.assertEquals(add(21, -7), 14)

    def test_add_negative_and_positive(self):
        self.assertEquals(add(-7, 21), 14)

    def test_first_argument_not_number(self):
        self.assertEquals(add('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(add(3, 'asd'), 'error')


class SubtractTest(unittest.TestCase):
    """Test for subtract() function"""

    def test_subtract_positive_numbers(self):
        self.assertEquals(subtract(10, 6), 4)

    def test_subtract_positive_numbers2(self):
        self.assertEquals(subtract(111, 11), 100)

    def test_subtract_zeros(self):
        self.assertEquals(subtract(0, 0), 0)

    def test_subtract_positive_and_zero(self):
        self.assertEquals(subtract(45, 0), 45)

    def test_subtract_zero_and_positive(self):
        self.assertEquals(subtract(0, 45), -45)

    def test_subtract_negative_and_zero(self):
        self.assertEquals(subtract(-33, 0), -33)

    def test_subtract_zero_and_negative(self):
        self.assertEquals(subtract(0, -33), 33)

    def test_subtract_negative_numbers(self):
        self.assertEquals(subtract(-3, -15), 12)

    def test_subtract_negative_numbers2(self):
        self.assertEquals(subtract(-79, -19), -60)

    def test_subtract_positive_and_negative(self):
        self.assertEquals(subtract(21, -7), 28)

    def test_subtract_negative_and_positive(self):
        self.assertEquals(subtract(-7, 21), -28)

    def test_first_argument_not_number(self):
        self.assertEquals(subtract('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(subtract(3, 'asd'), 'error')

class MultiplyTest(unittest.TestCase):
    """Test for multiply() function"""

    def test_multiply_positive_numbers(self):
        self.assertEquals(multiply(10, 6), 60)

    def test_multiply_positive_and_negative(self):
        self.assertEquals(multiply(10, -6), -60)

    def test_multiply_negative_numbers(self):
        self.assertEquals(multiply(-10, -6), 60)

    def test_multiply_zeros(self):
        self.assertEquals(multiply(0, 0), 0)

    def test_multiply_positive_and_zero(self):
        self.assertEquals(multiply(10, 0), 0)

    def test_multiply_negative_and_zero(self):
        self.assertEquals(multiply(-10, 0), 0)

    def test_first_argument_not_number(self):
        self.assertEquals(multiply('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(multiply(3, 'asd'), 'error')

class DivideTest(unittest.TestCase):
    """Test for divide() function"""

    def test_divide_positive_numbers(self):
        self.assertEquals(divide(60, 6), 10)

    def test_divide_negative_numbers(self):
        self.assertEquals(divide(-60, -6), 10)

    def test_divide_positive_and_negative(self):
        self.assertEquals(divide(60, -6), -10)

    def test_divide_zero_by_number(self):
        self.assertEquals(divide(0, 123), 0)

    def test_divide_number_by_zero(self):
        self.assertEquals(divide(10, 0), 'error')

    def test_first_argument_not_number(self):
        self.assertEquals(divide('asd', 2), 'error')

    def test_second_argument_not_number(self):
        self.assertEquals(divide(3, 'asd'), 'error')


if __name__ == '__main__':
    unittest.main()