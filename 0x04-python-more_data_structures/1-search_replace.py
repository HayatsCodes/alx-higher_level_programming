#!/usr/bin/python3
# 1-search_replace.py


def search_replace(my_list, search, replace):
    """Replacing occurrences of an element by another using a new list."""
    new_list = [x if x is not search else replace for x in my_list]
    return (new_list)
