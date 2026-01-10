"""
File: 07.Swap_numbers.py
Description: This program demonstrates three different methods to swap two numbers:
1. Using a temporary variable
2. Without using a temporary variable (arithmetic method)
3. Using Python's default tuple unpacking method

Author: Madhu Kumar K S
"""

def swap_numbers_temp(num1:int,num2:int):
    """
    Swap two numbers using a temporary variable
    Args:
        num1 (int): First number
        num2 (int): Second number
    Returns:
        tuple: Swapped numbers (num2, num1)
    """
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2

def swap_numbers_without_temp(num1:int,num2:int):
    """
    Swap two numbers without using a temporary variable (arithmetic method)
    Args:
        num1 (int): First number
        num2 (int): Second number
    Returns:
        tuple: Swapped numbers (num2, num1)
    """
    num1 = num1 + num2  # num1 now contains sum of both numbers
    num2 = num1 - num2  # num2 now contains original num1
    num1 = num1 - num2  # num1 now contains original num2
    return num1,num2

def swap_numbers_def_method(num1:int,num2:int):
    """
    Swap two numbers using Python's default tuple unpacking method
    Args:
        num1 (int): First number
        num2 (int): Second number
    Returns:
        tuple: Swapped numbers (num2, num1)
    """
    num1,num2 = num2, num1
    return num1,num2

# Test all three methods
print("swap 2 number using Temp", swap_numbers_temp(10,20))
print("swap 2 number without Temp", swap_numbers_without_temp(33,22))
print("swap 2 number with python default method", swap_numbers_def_method(40,21))