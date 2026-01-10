"""
Random Number Generator Program
This program generates random numbers within a specified range and allows
the user to generate multiple random numbers interactively.

Author: Madhu Kumar K S
"""

import random

def generate_random_numbers(start: int, end: int):
    """
    Generate a random integer between start and end (inclusive).
    
    Args:
        start (int): The minimum value for the random number
        end (int): The maximum value for the random number
    
    Returns:
        int: A random integer between start and end
    """
    return random.randint(start, end)

# Generate and display the first random number
print(generate_random_numbers(1, 40))

# Interactive loop to generate more random numbers
while True:
    user_input = input("Would like to continue, press y else n \n")
    if user_input.lower() == "y":
        print(generate_random_numbers(1, 40))
    else:
        break