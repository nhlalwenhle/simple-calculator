import pytest
import tdd_calculator
from tdd_calculator import*


def test_add_two_single_numbers():
    assert add(2, 2) == 4
    assert add(3, 2) == 5

def test_add_mixed_numbers():
     assert add(50, 17) == 67

def test_adding_zeros_together():
    assert add(0, 0) == 0

def test_multiply_single_numbers():
    assert multiply(3, 2) == 6#

def test_multiplying_double_digit_numbers():
 	assert multiply (10, 20) == 200

def test_multiply_large_numbers():
 	assert multiply (2000, 1000) == 2000000

def test_multiplication_with_zero():
	assert multiply (5,0) == 0

def test_subtract():
	assert subtract (20, 12) == 8
	assert subtract (500, 250) == 250	
def test_divide():
 	assert divide (10, 2) == 5

def test_no_parameter():
    """ if no parameters are provided, return 0
    """


