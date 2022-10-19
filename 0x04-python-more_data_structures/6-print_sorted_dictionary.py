#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    for k, v in sorted(a_dictionary.items()):
        print('{}: {}'.format(k, v))
