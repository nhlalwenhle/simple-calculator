import re
import pytest
#mport tdd_simple_calculator_part_1.py
from tdd_simple_calculator_part_1 import *

def test_add_two_numbers():
	"""test that adding two 0's results in 0"""
	assert add(0, 0) == 0

def test_add_negative_numbers():
	"""test that adding -1, -1 gives -2"""
	assert add(-1, -1) == -2

def test_add_positive_numbers():
	"""test adding positive numbers"""
	assert add(4, 5) == 9

def test_add_multiple_numbers():
	"""test that adding 1, 2, 3, 4 equals 10"""
	assert add(1, 2, 3, 4) == 10


def test_multiply():
	assert multiply (2, 2) == 4

def test_multiply_multiple_numbers():
	assert multiply(2, 2, 2, 2) == 16
	assert multiply(10, 10, 10, 10) == 10000

