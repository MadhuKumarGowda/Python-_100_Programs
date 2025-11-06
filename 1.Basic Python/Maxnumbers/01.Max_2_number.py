"""
File: 01.Max_2_number.py
Author: madhugowda
Date: November 05, 2024
Description: Different methods to find the maximum of two numbers
"""

def using_max_method(num1, num2):
    """
    Find maximum using Python's built-in max() function
    """
    return max(num1, num2)

def using_ternary_method(num1, num2):
    """
    Find maximum using ternary operator (conditional expression)
    """
    return num1 if num1 > num2 else num2

def using_condition_method(num1, num2):
    """
    Find maximum using traditional if-else condition
    """
    if num1 > num2:
        return num1
    else:
        return num2

def using_sort_method(num1, num2):
    """
    Find maximum by sorting a list and getting the last element
    """
    params = [num1, num2]  # Create list with both numbers
    params.sort()          # Sort in ascending order
    return params[-1]      # Return last element (maximum)

# Test all methods with different number pairs
print("using max method 20 & 30:", using_max_method(20, 30))
print("using ternary method 10 & 50:", using_ternary_method(10, 50))
print("using condition method 43 & 22:", using_condition_method(43, 22))
print("using sort method 22 & 7:", using_sort_method(22, 7))

