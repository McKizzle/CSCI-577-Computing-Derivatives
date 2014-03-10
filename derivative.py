import numpy as np
import pylab as py
import math as m
import scipy.signal as sig

def arrayify(f, x_0, x_max, h):
    """ Converts a function f into a set of discrete values.  
        :param f: the function to calculate the derivatives for.
        :param x_0: the starting x value.
        :param h: the step size. 
        :param length: the number of steps to perform.
    """
    X = np.arange(x_0, x_max, h)
    return np.array([f(x_0 + x) for x in X])

def rss(f, f_golden):
    """ Compares a function output to a expected output using the least sum squared error """
    f = np.array(f)
    f_golden = np.array(f_golden)
    return np.sum((f_golden - f)**2)

class Derivative:

    def __init__(self, finite_difference_formula, finite_difference_args):
        """ The Derivative class
            :param f: the candidate formula to calculate the derivate for. 
            :param finite_difference_formula: Formula to calculate teh finite difference.
            :param finite_difference_args: The arguments to pass into the formula. 
        """
        self.f = finite_difference_formula
        self.f_args = finite_difference_args
    
    def derive(self, f, x_0, x_max):
        """ Calculates the derivatives of a function
            :param f: the function to calculate the derivatives for.
            :param x_0: the starting x value.
            :param h: the step size. 
            :param length: the number of steps to perform.
        """
        h = self.f_args[-1]
        y = arrayify(f, x_0, x_max, h[0])
        return self.f(y, *self.f_args)


