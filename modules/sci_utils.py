import math

def power(a, b):
    """Return a raised to the power of b"""
    return math.pow(a, b)

def square_root(a):
    """Return the square root of a"""
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def factorial(n):
    """Return the factorial of n"""
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number")
    return math.factorial(n)

def sine(x):
    """Return the sine of x (in radians)"""
    return math.sin(x)

def cosine(x):
    """Return the cosine of x (in radians)"""
    return math.cos(x)

def tangent(x):
    """Return the tangent of x (in radians)"""
    return math.tan(x)