#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Print the last digit of a number and return it."""
    if number < 0:
        number = -number
    last_digit = number % 10
    print('{}'.format(last_digit), end="")
    return (last_digit)
