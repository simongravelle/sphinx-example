"""
A collection of python modules to be displayed by sphinx
"""
__autor__ = 'Simon Gravelle'


def add_number(a, b):
    """Add two numbers

    Description
    -----------

    add_number is a Python function returning the sum
    of two numbers.

    Arguments
    ---------
    a : float
        The first number
    b : float
        The second number

    Returns
    -------
    c : float
        The sum of the two input arguments
    """
    c = a + b
    return c


def divide_number(a, b):
    r"""Divide two numbers

    Description
    -----------

    divide_number is a Python function dividing one number
    by another, and returning the fraction c:

    .. math::

        c = \frac{a}{b}

    .. note::

        If :math:`b` is zero it will raise a ZeroDivisionError

    Arguments
    ---------
    a : float
        The numerator
    b : float
        The denominator

    Returns
    -------
    c : float
        The fraction
    """
    c = a / b
    return c

