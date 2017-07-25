"""
A small set of functions for doing math operations.
"""

def add(a, b):
    """
    Function that adds 2 arguements
    """
    return a + b

def mult(a, b):
    """
    Function that multiplies 2 arguements
    """
    return a * b

def div(a, b):
    """
    Function that divides 2 arguements
    """
    a = float(a)
    b = float(b)
    return a / b

def sub(a, b):
    """
    Function that subtracts 2 arguements
    """
    return a - b

def rem(a, b):
    """
    Function that gives remainder of 2 arguements
    """
    return a % b

def per(a):
    """
    Function that converts decimal to percent
    """
    return a * 100

def dec(a):
    """
    Function that converts percent to decimal
    """
    a = float(a)
    return a / 100
