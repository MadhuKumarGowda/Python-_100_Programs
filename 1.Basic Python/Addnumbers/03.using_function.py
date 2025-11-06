"""
Program: Add Two Numbers using function
Description: This program demonstrates basic arithmetic operation by adding two numbers
Author: Madhu Kumar K S
Date: 2025-11-05
"""

def add_two_numbers(num1, num2):
    """Function to add two numbers and return the result"""
    # Perform addition operation and return the sum
    return num1 + num2

# Get input from user for first number and convert to float
num_1 = float(input("Enter first Number:"))

# Get input from user for second number and convert to float
num_2 = float(input("Enter the Second Number:"))

# Call the function to add the two numbers and store result
result = add_two_numbers(num_1, num_2)

# Display the result to the user
print("The sum of", num_1, "and", num_2, "is:", result)