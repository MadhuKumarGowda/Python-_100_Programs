"""
Armstrong Number Checker
========================
This program checks if a given number is an Armstrong number using two different approaches:
1. String-based approach: Convert number to string and process each digit
2. Digit extraction approach: Use mathematical operations to extract digits

An Armstrong number is a number that equals the sum of its digits raised to the power
of the number of digits.

The program also finds all Armstrong numbers within a given range.

Author: Programming Assistant
"""

def validate_armstrong_string(x: int) -> bool:
    """
    Check if a number is Armstrong using string conversion approach.
    
    Args:
        x (int): The number to check
        
    Returns:
        bool: True if the number is Armstrong, False otherwise
    """
    sum = 0
    digits = str(x)  # Convert number to string to easily access each digit
    n = len(digits)  # Get the number of digits
    
    # Iterate through each digit character in the string
    for i in range(n):
        sum += int(digits[i]) ** n  # Convert digit back to int and raise to power of total digits
    
    return True if sum == x else False

def validate_armstrong_digits(x: int) -> bool:
    """
    Check if a number is Armstrong using mathematical digit extraction.
    
    Args:
        x (int): The number to check
        
    Returns:
        bool: True if the number is Armstrong, False otherwise
    """
    sum = 0
    temp = x  # Create a copy to avoid modifying original number
    n = len(str(x))  # Get the number of digits by converting to string
    
    # Extract digits one by one using mathematical operations
    while temp > 0:
        digit = temp % 10  # Get the rightmost digit
        sum += digit ** n  # Add digit raised to power of total digits
        temp = temp // 10  # Remove the rightmost digit
    
    return True if sum == x else False

# Main program execution
# Get input number from user
num = int(input("Enter number: "))

# Test both validation methods on the input number
res = validate_armstrong_string(num)
res1 = validate_armstrong_digits(num)

# Display result for single number check (both methods should give same result)
if res is True and res1 is True:
    print(f"The given number {num} is armstrong")
else:
    print(f"The given number {num} is not armstrong")

# Get range from user to find all Armstrong numbers
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

# Find and display all Armstrong numbers in the given range
print(f"Armstrong numbers between {lower} and {upper}:")
for i in range(lower, upper + 1):
    res = validate_armstrong_digits(i)
    if res is True:
        print(i)