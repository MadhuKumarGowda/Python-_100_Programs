"""
Program: Add Two Numbers using built in methods
Description: This program demonstrates basic arithmetic operation by adding two numbers
Author: Madhu Kumar K S
Date: 2025-11-05
"""

import operator

def using_add_method(num1, num2):
    """
    Add two numbers using operator.add() method
    Args:
        num1: First number
        num2: Second number
    Returns:
        Sum of num1 and num2
    """
    return operator.add(num1, num2)

def using_sum_method(num1, num2):
    """
    Add two numbers using built-in sum() method
    Args:
        num1: First number
        num2: Second number
    Returns:
        Sum of num1 and num2
    """
    # sum() method accepts a list/iterable and returns the sum of all elements
    return sum([num1, num2])

# Define two numbers to add
num1 = 20
num2 = 40

# Test both methods and display results
print("Add method:" , using_add_method(num1, num2))  # Using operator.add()
print("Sum Method:", using_sum_method(num1, num2))   # Using built-in sum()