#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Prints integers of lists in reverse order"""
    if my_list is None:
        return (None)
    my_list.reverse()
    for i in my_list:
        print('{:d}'.format(i))
