"""
This module provides functions to convert temperatures
between Celsius, Fahrenheit, and Kelvin.
"""

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return c + 273.15
