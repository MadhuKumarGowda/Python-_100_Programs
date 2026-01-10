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
    if x == 1:
        return "not a Prime Number"
    
    # Check for divisors from 2 to sqrt(x)
    for i in range(2, int(math.sqrt(x) + 1)):
        # If x is divisible by i, it's not prime
        return "Not a prime" if x % i == 0 else "Prime Number"

# Test the function with number 37
print(check_prime_number(37))