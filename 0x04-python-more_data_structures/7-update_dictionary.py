#!/usr/bin/python3
# 7-update_dictionary.py


def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value pairs in a dictionary."""
    for i in a_dictionary:
        if i is key:
            a_dictionary[key] = value
            break
    else:
        a_dictionary[key] = value
    return (a_dictionary)
