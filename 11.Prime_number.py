"""
Prime Number Checker
Author: Madhu Kumar K S

This program checks if a given number is prime or not.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def check_prime_number(x: int):
    """
    Check if a number is prime or not.
    
    Args:
        x (int): The number to check for primality
        
    Returns:
        str: "not a Prime Number" if x is 1, "Not a prime" if x is composite, "Prime Number" if x is prime
    """
    # 1 is neither prime nor composite
    if x <= 1:
        return False
    
    # Check for divisors from 2 to sqrt(x)
    for i in range(2, int(math.sqrt(x) + 1)):
        # If x is divisible by i, it's not prime
        if x % i == 0:
            return False
    return True
    
def print_all_prime_number_range(lower: int, upper: int):
    """
    Find all prime numbers within a given range.
    
    Args:
        lower (int): The lower bound of the range (inclusive)
        upper (int): The upper bound of the range (inclusive)
        
    Returns:
        list: A list of all prime numbers in the specified range
    """
    # Initialize empty list to store prime numbers
    prime_numbers = []
    
    # Iterate through each number in the range
    for num in range(lower, upper + 1):
        # Check if current number is prime using our helper function
        if check_prime_number(num):
            # Add prime number to our list
            prime_numbers.append(num)
    
    # Return the list of prime numbers found
    return prime_numbers
                    

# Test the function with number 37
print(check_prime_number(37))
# Find and print all prime numbers between 1 and 50
print(print_all_prime_number_range(1, 50))