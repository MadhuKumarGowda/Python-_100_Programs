"""
File: KM_Miles.py
Description: A simple program to convert between kilometers and miles
Author: Madhu Kumar K S
"""

def m_km_convert(miles: float):
    """Convert miles to kilometers"""
    km = miles * 1.60934
    return str(km) + " km"

def km_m_convert(km: float):
    """Convert kilometers to miles"""
    miles = km * 0.621371
    return str(miles) + " miles"

# Test the conversion functions
print("The KM of given miles is", m_km_convert(42))
print("The Miles of given KM is", km_m_convert(120))