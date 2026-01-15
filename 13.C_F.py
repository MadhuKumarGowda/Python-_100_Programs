"""
Temperature Conversion Program
This program provides functions to convert between Celsius and Fahrenheit temperatures.

Author: Madhu Kumar K S
"""

def convert_C_F(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    F = (celsius * 1.8) + 32
    return F

def convert_F_C(F: float) -> float:
    """
    Convert Fahrenheit to Celsius
    
    Args:
        F (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    C = (F - 32) / 1.8
    return C

# Convert 40°C to Fahrenheit
F = convert_C_F(40)
print(f"The F of given C is {F}")

# Convert 89.6°F to Celsius
C = convert_F_C(89.6)
print(f"The C for given F is {C}")