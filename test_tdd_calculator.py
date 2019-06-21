import pytest
import tdd_calculator
from tdd_calculator import*


def test_add_two_single_numbers():
    assert calculator.add(2, 2) == 4

def test_add_mixed_numbers():
    assert calculator.add(50, 17) == 67

def test_adding_zeros_together():
    assert calculator.add(0, 0) == 0

def test_adding_three_numbers():
    assert calculator.add(1, 3, 5) == 9

    assert calculator.add(10, 30, 50) == 90

def test_with_5_arguments():
    assert calculator.add(1, 2, 3, 4, 5) == 15



def test_multiply_single_numbers():
    assert calculator.multiply (3, 2) == 6

def test_multiplying_double_digit_numbers():
	assert calculator.multiply (10, 20) == 200

def test_multiply_large_numbers():
	assert calculator.multiply (2000, 1000) == 2000000

def test_multiplication_with_zero():
	assert calculator.multiply (5,0) == 0

	assert calculator.multiply (10, 0) == 0


