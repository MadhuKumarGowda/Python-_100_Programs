"""
Simple Interest Calculator

This program calculates simple interest using the formula:
Simple Interest = (Principal * Rate * Time) / 100

Author: madhu gowda
Date: November 11, 2025
File: 01.SI.py
Description: A basic Python program to calculate simple interest given principal amount,
             rate of interest, and time period.
"""

# Simple Interest Calculation
def calculate_simple_interest_fun(_principal, rate, time):
    """
    Calculate simple interest
    
    Args:
        principal (float): Principal amount
        rate (float): Rate of interest per annum
        time (float): Time period in years
    
    Returns:
        float: Simple interest amount
    """
    return (_principal * time * rate) / 100

# Lambda function to calculate simple interest
si_lambda = lambda p,t,r: (p*t*r)/100

# Input values for calculation
principal, rate, time = 10000, 4, 3

# Calculate simple interest using the function
result = calculate_simple_interest_fun(principal,rate,time)

# Calculate simple interest using the lambda function
lambda_result = si_lambda(principal,rate,time)

# Display results from both methods
print(f"SI by function {result} and lambda {lambda_result}")