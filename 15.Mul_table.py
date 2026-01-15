"""
Multiplication Table Generator
Author: Madhu Kumar K S
Description: This program generates and displays a multiplication table for a given number from 1 to 10.
"""

def generate_mul_table(x: int):
    """
    Generates and prints multiplication table for given number x.
    
    Args:
        x (int): The number for which multiplication table is to be generated
    """
    for i in range(1, 11):
        print(f"{x} X {i} = {x * i}")

def generate_mul_table_while(x: int):
    """
    Generates and prints multiplication table for given number x using while loop.
    
    Args:
        x (int): The number for which multiplication table is to be generated
    """
    i = 1  # Initialize counter variable
    while i < 11:  # Loop from 1 to 10
        print(f"{x} X {i} = {x * i}")  # Print multiplication result
        i += 1  # Increment counter

# Get input from user and generate multiplication table
num = int(input("Enter digit to display a table: "))
generate_mul_table(num)
generate_mul_table_while(num)