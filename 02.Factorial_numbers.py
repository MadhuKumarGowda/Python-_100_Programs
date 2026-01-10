"""
Program: Factorial Number Calculator
Description: This program calculates the factorial of a number using both iterative (loop) and recursive methods.
             Factorial of n (n!) is the product of all positive integers less than or equal to n.
             For example: 5! = 5 × 4 × 3 × 2 × 1 = 120

Author: Madhu Gowda
Date: November 10, 2025 (MDT)

Methods implemented:
1. Iterative method using for loop
2. Recursive method using function recursion

Note: Factorial is only defined for non-negative integers.
      0! = 1 by definition
"""

# Factorial calculation using iterative method (for loop)def factorial_loop(number):


def factorial_loop(number):
            """
            Calculate factorial using iterative method (for loop).
            
            Args:
                  number (int): Non-negative integer to calculate factorial for
                  
            Returns:
                  int: Factorial of the given number
            """
            fact = 1  # Initialize factorial result to 1
            # Multiply all numbers from 1 to number (inclusive)
            for i in range(1, number + 1):
                  fact *= i  # Multiply current number with accumulated result
            return fact


def factorial_recursive(number):
            """
            Calculate factorial using recursive method.
            
            Args:
                  number (int): Non-negative integer to calculate factorial for
                  
            Returns:
                  int: Factorial of the given number
            """
            # Base case: 0! = 1 and 1! = 1
            return 1 if number == 0 or number == 1 else number * factorial_recursive(number - 1)


# Test the factorial functions
number = 6  # Input number to calculate factorial

# Calculate factorial using both methods
loop_res = factorial_loop(number)
recursive_res = factorial_recursive(number)

# Display results from both methods
print(f"Factorial number of {number} by loop {loop_res} and recursive is {recursive_res}")