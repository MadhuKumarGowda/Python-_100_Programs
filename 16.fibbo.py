"""
Fibonacci Number Generator
This program generates Fibonacci sequence numbers up to a given count.

Author: Madhu Kumar K S
"""

def generate_fibonacci(x: int):
    """
    Generate and print Fibonacci sequence up to x numbers.
    
    Args:
        x (int): Number of Fibonacci numbers to generate
    """
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    print(a)     # Print first number (0)
    print(b)     # Print second number (1)
    
    # Generate remaining Fibonacci numbers
    for i in range(2, x):
        c = a + b    # Calculate next Fibonacci number
        a = b        # Move to next pair
        b = c        # Update second number
        print(f"{c}")  # Print current Fibonacci number

print(generate_fibonacci(5))
