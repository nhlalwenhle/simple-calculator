import pytest
#import tdd_calculator
from tdd_calculator import*

#write a test to demonstrate that add(0,0) will return 0.
def test_add_two_zeros():
    result = add(0,0)
    assert result == 0

def test_add_negatives():
    result = add(-1,-1)
    assert result == -2

def test_add_positive_numbers():
    result = add(4,5)
    assert result == 9

def test_add_many_numbers():
    result = add(1,2,3,4)
    assert result == 10

def test_multiplication_of_two_numbers():
    result = multiply(1,2)
    assert result == 2

def test_multiplication_of_multiple_numbers():
    result = multiply(1,2,3,4)
    assert result == 24

    result = multiply(1,3,5,7,9)
    assert result == 945

    result = multiply(1,1,3,3,4,4)
    assert result == 144
