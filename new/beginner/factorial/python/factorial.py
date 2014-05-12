#!/usr/bin/python

import sys

from library import factorial

number = int(sys.argv[1])
factorial = factorial(number)

print('{0}! = {1}'.format(number, factorial))