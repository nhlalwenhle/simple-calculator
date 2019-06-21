import re

def add(first_number=0, second_number=0):
    return first_number + second_number
    

class calculator():
    def add(*numbers):
        total = 0 
        for number in numbers: 
            total += number 
        return total


    def multiply(first_number, second_number):
        return first_number * second_number

