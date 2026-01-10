"""
Largest Numbers Program
Author: Madhu Kumar K S

This program finds the largest number among three given integers.
"""

def largest_three_numbers(a: int, b: int, c: int) -> int:
    """
    Find the largest number among three given integers.
    
    Args:
        a (int): First number
        b (int): Second number
        c (int): Third number
    
    Returns:
        int: The largest of the three numbers
    """
    # Check if 'a' is greater than both 'b' and 'c'
    if a > b and a > c:
        return a
    # If 'a' is not the largest, return the larger of 'b' and 'c'
    return b if b > c else c

def largest_number_max_method(a: int, b: int, c: int) -> int:
    """
    Find the largest number among three given integers using the built-in max function.
    
    Args:
        a (int): First number
        b (int): Second number
        c (int): Third number
    
    Returns:
        int: The largest of the three numbers
    """
    # Use Python's built-in max() function to find the largest value
    return max(a, b, c)

        
    
# Test the function with sample values
print("Largest of given 3 numbers is :", largest_three_numbers(10, 7, 11))
print("Largest of given 3 numbers is using max :", largest_number_max_method(10, 17, 11))