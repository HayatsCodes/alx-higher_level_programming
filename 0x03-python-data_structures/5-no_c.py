#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Remove all chars c and C from a string."""
    new_str = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(new_str))
