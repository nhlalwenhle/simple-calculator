import re

"""The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function."""

def add(*args): 
    """total = 0
    for i in args:
        total += i
    return total"""
    return float(sum(args))



def multiply(*args):
    total = 1
    for i in args:
        total *= i
    return total