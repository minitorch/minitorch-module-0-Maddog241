"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    """Multiplies two numbers

    Args:
        a (float): number a 
        b (float): number b 

    Returns:
        float: product of a and b
        
    """
    return a * b

def id(a: float) -> float:
    """Return the input unchanged"""
    return a

def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

def neg(a: float) -> float:
    """Negates a number"""
    return -a

def lt(a: float, b: float) -> float:
    """Checks if one number is less than another"""
    return a < b

def eq(a: float, b: float) -> float:
    """Checks if two numbers are equal"""
    return a == b

def max(a: float, b: float) -> float:
    """Returns the larger of two numbers"""
    return a if a >= b else b

def is_close(a: float, b: float) -> float:
    """Checks if two numbers are close in value"""
    return abs(a - b) < 1e-2

def sigmoid(a: float) -> float:
    """Calculates the sigmoid function"""
    if a >= 0.0:
        return 1.0 / (1.0 + math.exp(-a))
    else:
        return math.exp(a) / (1.0 + math.exp(a))

def relu(a: float) -> float:
    """Applies the ReLU activation"""
    return a if a >= 0.0 else 0.0

def log(a: float) -> float:
    """Calculates the natural logarithm"""
    return math.log(a)

def exp(a: float) -> float:
    """Calculates the exponential function"""
    return math.exp(a)

def inv(a: float) -> float:
    """Calculates the reciprocal"""
    return 1.0 / a

def log_back(a: float, b: float) -> float:
    """Computes the derivative of log times a seoncd arg"""
    return inv(a) * b

def inv_back(a: float, b: float) -> float:
    """Computes the derivative of reciprocal times a second arg"""
    return -1.0 / a**2 * b

def relu_back(a: float, b: float) -> float:
    """Computes the derivative of ReLU times a second arg"""
    return b if a >= 0.0 else 0.0



# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
