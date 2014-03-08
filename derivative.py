import numpy as np
import pylab as py
import math as m
import scipy.signal as sig

def arrayify(f, x_0, h, length):
    """ Converts a function f into a set of discrete values.  
        :param f: the function to calculate the derivatives for.
        :param x_0: the starting x value.
        :param h: the step size. 
        :param length: the number of steps to perform.
    """
    return np.array([f(x_0 + h * i) for i in range(0, length)])

def mse(f, f_golden):
    pass

class Derivative:
    def __init__(self, finite_difference_formula, finite_difference_args):
        """ The Derivative class
            :param f: the candidate formula to calculate the derivate for. 
            :param finite_difference_formula: Formula to calculate teh finite difference.
            :param finite_difference_args: The arguments to pass into the formula. 
        """
        self.f = finite_difference_formula
        self.f_args = finite_difference_args

    def derive(self, f, x_0, length):
        """ Calculates the derivatives of a function
            :param f: the function to calculate the derivatives for.
            :param x_0: the starting x value.
            :param h: the step size. 
            :param length: the number of steps to perform.
        """
        h = self.f_args[-1]
        y = arrayify(f, x_0, h[0], length)
        out = self.f(y, *self.f_args)
        return out

