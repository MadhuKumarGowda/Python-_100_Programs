"""
Numbers.py - Python program demonstrating number validation functions

This file contains functions to:
- Validate if a number is positive, negative, or zero
- Check if a number is even or odd
- Determine if a year is a leap year

Author: Madhu Kumar K S
"""

def validate_number(x: int):
    """
    Validates if a number is positive, negative, or zero
    
    Args:
        x (int): The number to validate
        
    Returns:
        str: "Positive Number", "Negative Number", or "Number is Zero"
    """
    if x > 0:
        return "Positive Number"
    elif x < 0:
        return "Negative Number"
    else:
        return "Number is Zero"
    
def validate_number_even_odd(x: int):
    """
    Checks if a number is even or odd
    
    Args:
        x (int): The number to check
        
    Returns:
        str: "Even Number" or "Odd Number"
    """
    return "Even Number" if x % 2 == 0 else "Odd Number"

def check_leap_year(year: int):
    """
    Determines if a year is a leap year
    Note: This is a simplified check (divisible by 4)
    
    Args:
        year (int): The year to check
        
    Returns:
        str: "Leap Year" or "Not a Leap Year"
    """
    return "Leap Year" if year % 4 == 0 else "Not a Leap Year"

# Test the functions
print(validate_number(10))
print(validate_number(-10))
print(validate_number(0))
print("***" * 15)
print(validate_number_even_odd(10))
print(validate_number_even_odd(11))
print("*" * 15)
year = int(input("Enter a year\n"))
print(check_leap_year(year))
