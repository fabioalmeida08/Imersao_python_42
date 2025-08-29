from typing import Any


def add(a: int, b: int) -> int: 
    """a function that receives two ints and return the sum of the two"""
    return a + b


def subtract(a: int, b: int) -> int:
    """a function that receives two ints and return the subtraction of the two"""
    return a - b


def multiply(a: int, b: int) -> int:
    """a function that receives two ints and return the multiplication of the two"""
    return a * b


def divide(a: int, b: int) -> float:
    """ 
    a function that receives two ints and try to return the division of the two
    if second is zero raise a exception
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int, exponent: int) -> Any:
    """a function that receives two integers and returns the first raised to the power of the second."""
    return base**exponent
