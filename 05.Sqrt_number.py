"""
Square Root Calculator
This file contains functions to calculate square roots using different methods.

Author: Madhu Kumar K S
"""

import math

def math_sqrt(x: int) -> int:
    """Calculate square root using math.sqrt() function"""
    return int(math.sqrt(x))

def expo_sqrt(x: int) -> int:
    """Calculate square root using exponentiation operator"""
    return int(x ** (1/2))

# Test the functions
print(math_sqrt(64))
print(expo_sqrt(121))