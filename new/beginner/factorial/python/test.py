import unittest

from library import factorial

class FactorialTest(unittest.TestCase):
  '''Tests factorial function'''

  def test_factorial_of_1(self):
    self.assertEqual(1, factorial(1))

  def test_factorial_of_2(self):
    self.assertEqual(2, factorial(2))

  def test_factorial_of_3(self):
    self.assertEqual(6, factorial(3))

  def test_factorial_of_5(self):
    self.assertEqual(120, factorial(5))
