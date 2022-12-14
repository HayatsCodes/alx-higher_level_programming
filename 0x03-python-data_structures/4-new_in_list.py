#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replace element in a list at a specific position
    without modifying the original list
    """

    new_list = []
    for i in my_list:
        new_list.append(i)
    if idx < 0 or idx > (len(my_list) - 1):
        return new_list
    new_list[idx] = element
    return (new_list)
