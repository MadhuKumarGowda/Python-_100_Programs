"""
Compound Interest Calculator

Author: Madhu Gowda
Date: November 17, 2025
Description: A Python program to calculate compound interest
"""

# formula for CI is A = P * (1 + R/100) ** T

# Function to calculate compound interest using basic arithmetic
def calculate_CI(principle, rate, time):
    # Calculate final amount using the compound interest formula
    amount = principle * (1 + rate/100) ** time
    # Return compound interest (amount - principal)
    return amount - principle

# Function to calculate compound interest using built-in pow() function
def calculate_CI_built(principle, rate, time):
    # Calculate final amount using pow() function for exponentiation
    amount = principle * (pow((1 + rate/100), time))
    # Return compound interest (amount - principal)
    return amount - principle

# Set input values: principal amount, interest rate (%), and time period (years)
principle, rate, time = 50000, 12, 5

# Display results from both calculation methods
print("CI by function", calculate_CI(principle, rate, time))
print("CI by built in function", calculate_CI_built(principle, rate, time))