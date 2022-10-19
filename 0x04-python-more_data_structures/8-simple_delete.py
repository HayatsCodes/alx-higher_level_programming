#!/usr/bin/python3
# 8-simple_delete.py

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary."""
    for i in a_dictionary:
        if i is key:
            del a_dictionary[key]
            break
    return (a_dictionary)
