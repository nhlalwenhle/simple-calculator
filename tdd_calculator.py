#import tdd_calculator
import re
#from tdd_calculator import add, multiply





class Calculator(object):

  def add(self, x, y):
    number_types = (int, float,  complex )
    if isinstance(x, number_types) and isinstance(y, number_types):
      return x - y
    else:
      raise ValueError


    def multiply(self):
        """Multiply parameters."""
        return self.num_x * self.num_y